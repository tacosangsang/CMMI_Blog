#!/usr/bin/env python3
"""네이버 블로그 임시저장 도우미.

사용법:
    python3 tools/naver_draft.py
    → 브라우저에서 http://localhost:8787 열기
    → 원고 통째로 붙여넣기 (첫 줄 = 제목, 나머지 = 본문) → [임시저장 실행]
    → Playwright 브라우저 창이 뜨면, 로그인 화면일 경우 직접 로그인 (최대 3분 대기)
    → 로그인 세션은 ~/.naver_draft_profile 에 유지되어 다음부터는 자동
    → 저장 후에도 브라우저 창은 열려 있음. 닫아도 다음 실행 때 다시 뜸.

주의: 네이버 공식 글쓰기 API는 종료되어 브라우저 자동화로 동작.
      에디터 UI가 바뀌면 셀렉터 수정 필요.
"""
import html
import re
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs

PORT = 8787
PROFILE = Path.home() / ".naver_draft_profile"
WRITE_URL = "https://blog.naver.com/GoBlogWrite.naver"
LOGIN_WAIT_SEC = 180

PAGE = """<!doctype html><meta charset="utf-8">
<title>네이버 블로그 임시저장</title>
<style>
 body{{font-family:-apple-system,sans-serif;max-width:720px;margin:40px auto;padding:0 16px}}
 textarea{{width:100%;box-sizing:border-box;font-size:15px;padding:8px;margin:4px 0 16px;height:420px}}
 button{{font-size:16px;padding:10px 24px;cursor:pointer}}
 pre{{background:#f4f4f4;padding:12px;white-space:pre-wrap}}
</style>
<h2>네이버 블로그 임시저장</h2>
<form method="post" action="/draft">
 <label>원고 전체 붙여넣기</label>
 <textarea name="manuscript" required placeholder="첫 줄 = 제목&#10;&#10;본문 시작...&#10;&#10;---&#10;&#10;주제 바뀌면 위처럼 --- 넣기 → 구분선 자동 삽입&#10;&#10;#태그1 #태그2 #태그3"></textarea>
 <button>임시저장 실행</button>
</form>
<p style="color:#888">
 규칙: <b>첫 줄=제목</b>, 단독 줄 <code>---</code>=구분선, 맨 끝 해시태그 줄=태그(작게 좌측정렬).<br>
 서식: 제목 24pt(SmartEditor 미지원으로 26→24), 본문 16pt 중앙정렬, 태그 11pt 좌측정렬.<br>
 브라우저 창은 저장 후에도 열려 있습니다.
</p>
{result}
"""

# 브라우저를 서버 프로세스가 계속 소유 — 저장 후에도 창 유지, 재사용
_pw = None
_ctx = None


SEPARATOR_MARKER = re.compile(r"^\s*-{3,}\s*$")
TAG_LINE_RE = re.compile(r"^\s*(#\S+\s*)+$")
# SmartEditor 본문 지원 폰트: 11 13 14 15 16 19 24 28 30 34 38 50
BODY_FONT_SIZE = 16
TAG_FONT_SIZE = 11
TITLE_FONT_SIZE = 24  # 26 요청했으나 SmartEditor 미지원 → 24


def parse_manuscript(text: str) -> tuple[str, list[list[str]], str]:
    """(제목, 본문 청크들, 태그줄) 반환.

    - 첫 줄 = 제목
    - `---` 단독 줄 = 청크 분리 (구분선 삽입 지점)
    - 마지막 비어있지 않은 줄이 해시태그 전용이면 태그로 분리
    - 각 청크는 문단(줄) 리스트
    """
    lines = text.lstrip().split("\n")
    title = lines[0].strip()
    rest = lines[1:]
    while rest and not rest[0].strip():
        rest.pop(0)

    tag = ""
    for i in range(len(rest) - 1, -1, -1):
        s = rest[i].strip()
        if not s:
            continue
        if TAG_LINE_RE.match(rest[i]):
            tag = s
            rest = rest[:i]
            while rest and not rest[-1].strip():
                rest.pop()
        break

    chunks: list[list[str]] = [[]]
    for ln in rest:
        if SEPARATOR_MARKER.match(ln):
            if any(l.strip() for l in chunks[-1]):
                chunks.append([])
        else:
            chunks[-1].append(ln)
    # 각 청크 앞뒤 빈 줄 제거 + 완전 빈 청크 제거
    trimmed = []
    for c in chunks:
        while c and not c[0].strip():
            c.pop(0)
        while c and not c[-1].strip():
            c.pop()
        if c:
            trimmed.append(c)
    return title, trimmed, tag


# clipboard_paste 제거 — SmartEditor가 반복 붙여넣기 차단


def get_page(log):
    global _pw, _ctx
    from playwright.sync_api import sync_playwright

    if _pw is None:
        _pw = sync_playwright().start()
    try:
        if _ctx:
            return _ctx.pages[-1] if _ctx.pages else _ctx.new_page()
    except Exception:
        _ctx = None
    _ctx = _pw.chromium.launch_persistent_context(
        str(PROFILE), headless=False,
        viewport={"width": 1280, "height": 900},
    )
    log.append("브라우저 실행")
    return _ctx.pages[0] if _ctx.pages else _ctx.new_page()


def find_editor(page, log):
    """에디터가 있는 frame 반환. 로그인 대기 포함."""
    deadline = time.time() + LOGIN_WAIT_SEC
    while time.time() < deadline:
        for f in page.frames:
            try:
                if f.locator(".se-section-documentTitle").count():
                    return f
            except Exception:
                pass
        if "nid.naver.com" in page.url:
            log.append("로그인 대기 중... 열린 창에서 직접 로그인하세요.")
        time.sleep(2)
    raise RuntimeError(f"{LOGIN_WAIT_SEC}초 안에 에디터를 찾지 못함 (로그인 미완료?)")


def set_align(page, direction: str):
    """SmartEditor 정렬 단축키. Cmd+Shift+E(중앙) / L(좌) / R(우) / J(양쪽)."""
    key = {"center": "e", "left": "l", "right": "r", "justify": "j"}[direction]
    page.keyboard.press(f"Meta+Shift+{key}")


def set_font_size(ed, size: int, log: list[str]):
    """툴바 폰트 크기 드롭다운 조작. 셀렉터 실패 시 로그만 남기고 계속."""
    try:
        # SmartEditor ONE 툴바 폰트 크기 버튼 — 클래스 부분일치
        for sel in ('button.se-font-size-code',
                    'button[class*="font-size"][class*="code"]',
                    'button.se-toolbar-item-font-size'):
            b = ed.locator(sel)
            if b.count():
                b.first.click()
                break
        else:
            log.append(f"경고: 폰트 크기 버튼 못 찾음 ({size}pt 스킵)")
            return
        # 드롭다운 항목 — data-value 또는 텍스트
        item = ed.locator(f'li[data-value="{size}"], button[data-value="{size}"]')
        if not item.count():
            item = ed.get_by_text(re.compile(rf"^{size}\s*$"))
        item.first.click(timeout=2000)
        log.append(f"폰트 {size}pt 적용")
    except Exception as e:
        log.append(f"경고: 폰트 {size}pt 실패 ({e.__class__.__name__})")


def insert_separator(ed, log: list[str]):
    """구분선 삽입. 툴바/사이드바의 '구분선' 버튼 클릭."""
    try:
        # 사이드바 라인 컴포넌트 버튼
        for sel in ('button.se-horizontalLine-toolbar-button',
                    'button[data-type="horizontalLine"]',
                    'button[data-name="horizontalLine"]'):
            b = ed.locator(sel)
            if b.count():
                b.first.click()
                log.append("구분선 삽입")
                return
        b = ed.get_by_role("button", name=re.compile("구분선"))
        if b.count():
            b.first.click()
            log.append("구분선 삽입")
            return
        log.append("경고: 구분선 버튼 못 찾음")
    except Exception as e:
        log.append(f"경고: 구분선 실패 ({e.__class__.__name__})")


def type_lines(page, lines: list[str]):
    """줄바꿈 Enter로, 각 줄 타이핑."""
    for i, line in enumerate(lines):
        if i:
            page.keyboard.press("Enter")
        s = line.strip()
        if s:
            page.keyboard.type(s, delay=5)


def save_draft(title: str, chunks: list[list[str]], tag: str, log: list[str]):
    page = get_page(log)
    try:
        page.goto(WRITE_URL, wait_until="domcontentloaded")
        log.append("글쓰기 페이지 이동")

        ed = find_editor(page, log)
        log.append("에디터 감지")

        # 이어쓰기 팝업 취소, 도움말 패널 닫기
        for sel in (".se-popup-button-cancel", ".se-help-panel-close-button"):
            try:
                ed.locator(sel).first.click(timeout=2000)
                log.append(f"팝업 닫음: {sel}")
            except Exception:
                pass

        # ---- 제목 ----
        ed.locator(".se-section-documentTitle .se-text-paragraph").first.click()
        set_font_size(ed, TITLE_FONT_SIZE, log)  # 26 요청 → 24 (미지원)
        page.keyboard.type(title, delay=8)
        log.append(f"제목 입력 (요청 26pt → SmartEditor 미지원, {TITLE_FONT_SIZE}pt 적용)")

        # ---- 본문: 청크마다 구분선 삽입 ----
        ed.locator(".se-component.se-text .se-text-paragraph").last.click()
        set_align(page, "center")
        set_font_size(ed, BODY_FONT_SIZE, log)
        for ci, chunk in enumerate(chunks):
            if ci:
                insert_separator(ed, log)
                # 구분선 뒤에 새 문단 확보
                page.keyboard.press("Enter")
                set_align(page, "center")
                set_font_size(ed, BODY_FONT_SIZE, log)
            type_lines(page, chunk)
            if ci < len(chunks) - 1:
                page.keyboard.press("Enter")
        log.append(f"본문 입력 (청크 {len(chunks)}개, 중앙정렬 + {BODY_FONT_SIZE}pt)")

        # ---- 태그 줄 ----
        if tag:
            page.keyboard.press("Enter")
            set_align(page, "left")
            set_font_size(ed, TAG_FONT_SIZE, log)
            page.keyboard.type(tag, delay=5)
            log.append(f"태그 입력 (좌측정렬 + {TAG_FONT_SIZE}pt)")

        page.wait_for_timeout(500)

        # ponytail: 클래스명 해시가 빌드마다 바뀌어서 부분일치 + 텍스트 폴백
        btn = ed.locator('button[class*="save_btn"]')
        if not btn.count():
            btn = ed.get_by_role("button", name=re.compile("^저장"))
        btn.first.click()
        log.append("저장 버튼 클릭")

        try:
            ed.get_by_text(re.compile("저장.*(되었|했)")).first.wait_for(timeout=8000)
            log.append("임시저장 확인됨")
        except Exception:
            log.append("경고: 저장 확인 토스트 못 찾음 — 열린 창에서 직접 확인")
    except Exception:
        shot = str(Path.home() / "naver_draft_error.png")
        try:
            page.screenshot(path=shot)
            log.append(f"오류 스크린샷: {shot}")
        except Exception:
            pass
        raise
    # 창은 닫지 않음 — 사용자가 직접 확인/수정/닫기


class Handler(BaseHTTPRequestHandler):
    def _send(self, body: str, code: int = 200):
        data = body.encode()
        self.send_response(code)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        self._send(PAGE.format(result=""))

    def do_POST(self):
        raw = self.rfile.read(int(self.headers["Content-Length"])).decode()
        form = parse_qs(raw)
        title, chunks, tag = parse_manuscript(form.get("manuscript", [""])[0])
        log: list[str] = []
        try:
            if not title or not chunks:
                raise ValueError("첫 줄(제목)과 본문이 모두 필요함")
            save_draft(title, chunks, tag, log)
            result = "<h3>완료</h3><pre>" + html.escape("\n".join(log)) + "</pre>"
        except Exception as e:
            result = ("<h3>실패</h3><pre>"
                      + html.escape("\n".join(log) + f"\n\n오류: {e}")
                      + "</pre>")
        self._send(PAGE.format(result=result))

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    t, cs, tg = parse_manuscript(
        "제목줄\n\n첫청크1\n첫청크2\n\n---\n\n둘째청크\n\n#태그1 #태그2"
    )
    assert t == "제목줄"
    assert cs == [["첫청크1", "첫청크2"], ["둘째청크"]]
    assert tg == "#태그1 #태그2"
    # 태그·구분선 없는 경우
    t2, cs2, tg2 = parse_manuscript("T\n\nA\nB")
    assert t2 == "T" and cs2 == [["A", "B"]] and tg2 == ""
    print(f"http://localhost:{PORT} 에서 사용하세요. 종료: Ctrl+C")
    # 단일 스레드 필수 — playwright sync API는 생성 스레드에서만 사용 가능
    HTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
