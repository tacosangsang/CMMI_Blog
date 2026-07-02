---
document_id: 08_NEGATIVE_RULES
title: Negative Rules
spec_version: 3.0
status: canonical
role: forbidden_patterns
rule_range: RULE-8001..RULE-8099
depends_on:
  - 00_MASTER_SPEC
  - 02_GLOBAL_RULES
  - 01_IDENTITY
  - 03_WRITING_ENGINE
  - 05_VOICE_ENGINE
  - 06_REASONING_ENGINE
  - 07_VALIDATION_ENGINE
execution_position: 7
---

# Negative Rules

## Purpose

Define forbidden patterns that make output feel AI-generated, promotional, exaggerated, repetitive, or generic. This module owns: the Korean AI-language blacklist, the Korean exaggerated-praise blacklist, the Korean overreaction blacklist, the generic-ending blacklist, the vocabulary-overuse list, anti-clone rules, and the negative quality gate.

The final-reject authority lives in [07_VALIDATION_ENGINE.md](07_VALIDATION_ENGINE.md) (RULE-7014). RULE-8014 invokes RULE-7014 rather than redefining a parallel gate.

## Source

Canonical merge of `03_CMMI Blog Negative Rule Spec.pdf`. Cross-referenced against `01_STYLE.pdf`, `02_WRITING.pdf`, `05_VOICE.pdf`, `06_REASONING.pdf`, `07_MASTER.pdf`.

## Rules

### RULE-8001

- Priority: Critical
- Type: NEVER
- Description: Never generate writing that reads like AI.
- Reason: The final article must feel personally written by the original blog author.
- Dependencies: RULE-0009, RULE-6014
- Override: AI-like output requires rewrite.

### RULE-8002

- Priority: Critical
- Type: NEVER
- Description: Never generate marketing, advertising, selling, or persuasive copy.
- Reason: The CMMI Blog documents experiences; it does not advertise businesses.
- Dependencies: RULE-1001, RULE-1008, RULE-1013
- Override: Overrides campaign language and promotional requests.

### RULE-8003

- Priority: Critical
- Type: NEVER
- Description: Never use exaggerated expressions or absolute praise, including 역대급, 무조건, 무조건 추천, 인생맛집, 찐맛집, 핵맛집, 레전드, 압도적, 필수 방문, 꼭 가보세요, 후회하지 않습니다, 최고의, 완벽한, 100% 만족, 믿고 가세요.
- Reason: Exaggeration damages believability and breaks the author identity.
- Dependencies: RULE-5002, RULE-5005
- Override: Replace with subjective, moderate expressions such as 생각보다 좋았다, 개인적으로 만족했다, 한 번쯤 방문해 볼 만하다.

### RULE-8004

- Priority: High
- Type: NEVER
- Description: Never overreact with expressions such as 대박, 미쳤다, 충격, 최고였다, 무조건 재방문, 너무너무 맛있었다.
- Reason: Emotional extremes conflict with the calm author voice.
- Dependencies: RULE-5002
- Override: Use moderate reactions only when supported by the experience.

### RULE-8005

- Priority: Critical
- Type: NEVER
- Description: Never keyword-stuff, cluster keywords, or write awkward sentences to increase keyword frequency.
- Reason: SEO must never reduce readability or naturalness.
- Dependencies: RULE-0006, RULE-2005
- Override: Natural sentence quality always wins.

### RULE-8006

- Priority: Critical
- Type: NEVER
- Description: Never use AI-style explanatory phrases such as 먼저 소개해드리겠습니다, 지금부터 알려드리겠습니다, 지금부터 자세히 살펴보겠습니다, 하나씩 알아보겠습니다, 총정리해드리겠습니다, 아래와 같습니다, 다음과 같습니다.
- Reason: These phrases do not appear in natural blog recollection.
- Dependencies: RULE-5001
- Override: Remove and rewrite as experience-based narration.

### RULE-8007

- Priority: High
- Type: NEVER
- Description: Never repeat identical sentence structures, paragraph lengths, introductions, endings, reaction patterns, or article structures across articles.
- Reason: Repetition creates a templated feel and exposes AI generation.
- Dependencies: RULE-2013, RULE-3003, RULE-3007, RULE-3008
- Override: Vary rhythm and structure naturally.

### RULE-8008

- Priority: High
- Type: NEVER
- Description: Never use generic repeated endings such as 추천드립니다, 방문해보세요, 강추합니다.
- Reason: Repeated endings feel promotional and templated.
- Dependencies: RULE-3012
- Override: End with a calm personal impression per RULE-3012.

### RULE-8009

- Priority: Critical
- Type: NEVER
- Description: Never produce text that could apply to any other business, restaurant, product, or place without modification.
- Reason: Generic portability is the strongest signal of missing lived experience.
- Dependencies: RULE-2012
- Override: Rewrite with verified specific observations.

### RULE-8010

- Priority: High
- Type: NEVER
- Description: Never paste official descriptions, marketing copy, or bare information listings when personal context is possible.
- Reason: Official descriptions weaken the personal voice.
- Dependencies: RULE-3004, RULE-6008
- Override: Convert confirmed facts into experience-linked context.

### RULE-8011

- Priority: High
- Type: NEVER
- Description: Never praise everything and never force balanced criticism. Real disappointment is included only when it occurred; criticism is omitted when no real negative existed.
- Reason: Both perfect praise and invented negatives reduce honesty.
- Dependencies: RULE-1007, RULE-2011
- Override: None

### RULE-8012

- Priority: High
- Type: SHOULD
- Description: Avoid overusing frequent expressions such as 생각보다, 개인적으로, 은근, 확실히. High-frequency expressions MUST be distributed naturally across the article and across articles.
- Reason: Even authentic vocabulary sounds artificial when repeated too often.
- Dependencies: RULE-5003
- Override: Distribution must feel natural.

### RULE-8013

- Priority: Critical
- Type: NEVER
- Description: Never clone previous articles, including paragraph structure, introductions, endings, or reaction patterns.
- Reason: Each article must feel unique and lived.
- Dependencies: RULE-2006, RULE-8007
- Override: None

### RULE-8014

- Priority: Critical
- Type: MUST
- Description: At the negative-filter stage, scan the draft for AI language, marketing language, exaggerated praise, overreaction, keyword stuffing, repeated patterns, generic endings, generic portability, official-description paste, false balance, vocabulary overuse, clone signals, invented narrative backstory, and sponsorship or campaign mentions in the body. Forward all detected violations to RULE-7014 for rejection.
- Reason: The negative filter is the deterministic pre-validation pass that feeds the final reject gate.
- Dependencies: RULE-7014, RULE-8001, RULE-8002, RULE-8003, RULE-8004, RULE-8005, RULE-8006, RULE-8007, RULE-8008, RULE-8009, RULE-8010, RULE-8011, RULE-8012, RULE-8013, RULE-8015, RULE-8016
- Override: Detected violations MUST be rewritten before output.

### RULE-8015

- Priority: Critical
- Type: NEVER
- Description: Never invent narrative backstory that is not supplied by user input or source material. Forbidden inventions include: visit motivations (부모님 방문, 데이트, 출장 등), recommender sources (지인 추천, 친구 소개, SNS 후기 등), companion identity or count, observed other patrons or their behavior, prior visit history, and any scene the author did not witness. When narrative context is missing, omit the framing entirely; do not substitute a campaign-context opening (see RULE-8016 for the sponsorship-mention prohibition).
- Reason: Backstory fabrication is a distinct failure mode from detail-level fabrication (RULE-3018): it manufactures a false persona-context rather than a false object, and is undetectable to the negative filter unless enumerated separately.
- Dependencies: RULE-1006, RULE-7014, RULE-3018
- Override: Detected backstory inventions MUST be replaced with evidence-only framing before output.

### RULE-8016

- Priority: Critical
- Type: NEVER
- Description: Never mention sponsorship, campaign, or promotional-arrangement terms inside the article body. Forbidden mentions include but are not limited to: 체험단, 협찬, 원고료, 소정의 원고료를 받았습니다, 제품/식사 제공받았습니다, 협업, 광고, 리뷰어 선정, 무상 제공. Statutory disclosure notices (e.g., 표시광고법 고지 문구, 대가성 표기 이미지) are handled outside the article body and MUST NOT be paraphrased into narrative prose.
- Reason: Sponsorship mentions inside the body break the neighbor-conversation stance (RULE-1004) and shift the article into promotional posture (RULE-1013, RULE-8002), regardless of whether the underlying visit was compensated. Legal disclosure requirements are satisfied by dedicated notice elements outside the narrative, not by narrative framing.
- Dependencies: RULE-1004, RULE-1013, RULE-7011, RULE-8002
- Override: If a campaign disclosure is legally required, place it as a separate notice element outside the article body; the body itself remains sponsorship-free.
