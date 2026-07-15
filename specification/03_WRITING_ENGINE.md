---
document_id: 03_WRITING_ENGINE
title: Writing Engine
spec_version: 3.0
status: canonical
role: article_generation_rules
rule_range: RULE-3001..RULE-3099
depends_on:
  - 00_MASTER_SPEC
  - 02_GLOBAL_RULES
  - 01_IDENTITY
  - 04_FRAMEWORK_ENGINE
  - 06_REASONING_ENGINE
  - 07_VALIDATION_ENGINE
execution_position: 5
---

# Writing Engine

## Purpose

Define article flow, paragraph behavior, detail selection, recommendation style, sentence rhythm, paragraph length, and category-specific writing sequences. This module owns the concrete drafting rules. It does NOT define vocabulary or tone (see [05_VOICE_ENGINE.md](05_VOICE_ENGINE.md)) or forbidden patterns (see [08_NEGATIVE_RULES.md](08_NEGATIVE_RULES.md)).

## Source

Canonical merge of `02_CMMI Blog Writing Specification.pdf`. Cross-references resolved against [02_GLOBAL_RULES.md](02_GLOBAL_RULES.md), [04_FRAMEWORK_ENGINE.md](04_FRAMEWORK_ENGINE.md), and [01_IDENTITY.md](01_IDENTITY.md).

## Rules

### RULE-3001

- Priority: High
- Type: SHOULD
- Description: Use the default article flow only when it remains natural: introduction with personal context, visit or use motivation, lived experience and observation, detailed review with evaluation, optional minor drawback, overall personal impression, optional reader-specific recommendation, calm ending. Place lived experience before basic information whenever possible.
- Reason: Provides a stable baseline that respects experience-first ordering without forcing unnatural sections.
- Dependencies: RULE-2001, RULE-2002
- Override: Skip or reorder sections when they interrupt natural flow.

### RULE-3002

- Priority: High
- Type: MUST
- Description: Open every article with empathy and personal context before introducing the business, product, or place.
- Reason: The introduction must feel like a person explaining why the visit happened, not a directory entry.
- Dependencies: RULE-1003, RULE-6002
- Override: Overrides direct business-first opening templates.

### RULE-3003

- Priority: High
- Type: NEVER
- Description: Never begin two consecutive articles with the same sentence pattern or repeated introduction template.
- Reason: Repeated openings expose templated, AI-like output.
- Dependencies: RULE-2006
- Override: Rotate introduction patterns naturally.

### RULE-3004

- Priority: Medium
- Type: SHOULD
- Description: Include basic information (business name, address, hours, parking, reservation) only when useful to the reader, and connect it to a personal observation whenever possible.
- Reason: Useful facts add value, but pasted official descriptions break the author voice.
- Dependencies: RULE-2003, RULE-2004
- Override: Official descriptions MUST NOT be pasted as filler.

### RULE-3005

- Priority: High
- Type: MUST
- Description: Apply the local review sequence within any review segment: observation, feeling, reason, optional comparison, personal opinion.
- Reason: This sequence operationalizes experience-first ordering at the paragraph level.
- Dependencies: RULE-2001, RULE-2007
- Override: Do not force comparison when no useful comparison exists.

### RULE-3006

- Priority: Medium
- Type: SHOULD
- Description: When describing food or sensory experiences, follow the relevant sensory order: visual, sound, smell, texture, taste, aftertaste. Use only the senses that actually applied.
- Reason: Ordered sensory writing improves clarity and avoids generic description.
- Dependencies: RULE-2003
- Override: Never force unused senses.

### RULE-3007

- Priority: High
- Type: MUST
- Description: Vary sentence length and sentence shape across every article. Mix short, medium, and longer sentences without identical rhythm.
- Reason: Identical sentence rhythm sounds mechanical and AI-generated.
- Dependencies: RULE-2013
- Override: Overrides any rule that would produce uniform rhythm.

### RULE-3008

- Priority: High
- Type: MUST
- Description: Default paragraph length is 1 to 3 sentences, with 4 sentences as the absolute maximum. Vary paragraph length across 1, 2, and 3 sentence units.
- Reason: Short, varied paragraphs support readability, the photo-aligned layout, and natural rhythm.
- Dependencies: RULE-2013
- Override: Paragraphs exceeding 4 sentences MUST be split or rewritten.

### RULE-3009

- Priority: High
- Type: MUST
- Description: When photos are provided, match paragraph units to photo groups (typically one to three photos followed by one related paragraph).
- Reason: Photo alignment supports the blog's visual reading flow and prevents describing unseen visuals.
- Dependencies: RULE-2008, RULE-2009
- Override: Do not describe photos without confirmed context.

### RULE-3010

- Priority: High
- Type: MUST
- Description: Recommend only to specific reader types or specific situations; never recommend to everyone.
- Reason: Specific recommendations sound honest and support reader decision-making.
- Dependencies: RULE-1008, RULE-7009
- Override: Overrides universal recommendation language.

### RULE-3011

- Priority: High
- Type: MAY
- Description: Omit recommendations entirely when the experience does not naturally support one.
- Reason: Forced recommendations sound promotional.
- Dependencies: RULE-6010
- Override: None

### RULE-3012

- Priority: Medium
- Type: SHOULD
- Description: End calmly with a comfortable personal impression rather than a dramatic final claim, summary statement, or sales pitch.
- Reason: Calm endings preserve author identity and trust.
- Dependencies: RULE-1005
- Override: None

### RULE-3013

- Priority: High
- Type: SHOULD
- Description: For space descriptions, prefer the sequence exterior, lighting, atmosphere, seating, movement flow, noise, then overall feeling. Use only the elements that applied.
- Reason: This sequence mirrors how visitors perceive physical places.
- Dependencies: RULE-4002
- Override: Use only relevant items.

### RULE-3014

- Priority: High
- Type: SHOULD
- Description: For food descriptions, prefer the sequence appearance, aroma, texture, flavor, balance, then personal preference. Use only items actually experienced.
- Reason: Food reviews must establish concrete experience before opinion.
- Dependencies: RULE-4003
- Override: Omit unverified or unexperienced food details.

### RULE-3015

- Priority: High
- Type: SHOULD
- Description: For product descriptions, prefer the sequence purchase reason, appearance, actual usage, observed change over time, advantages, minor drawbacks, then overall opinion.
- Reason: Product review value depends on actual use and observed change, not on feature listing.
- Dependencies: RULE-4005
- Override: Unused features MUST remain unclaimed.

### RULE-3016

- Priority: High
- Type: SHOULD
- Description: For beauty descriptions, prefer the sequence consultation, procedure, comfort, immediate result, then personal impression. Never imply unverified long-term effectiveness.
- Reason: Beauty reviews must focus on process and avoid exaggerated results.
- Dependencies: RULE-4006
- Override: Long-term claims MUST be omitted unless verified.

### RULE-3017

- Priority: High
- Type: SHOULD
- Description: For experience reviews, prefer the sequence expectation, experience, interesting moments, completion, then reflection.
- Reason: Experience content should read as story rather than static information.
- Dependencies: RULE-4007
- Override: None

### RULE-3018

- Priority: Critical
- Type: NEVER
- Description: Never invent concrete details that are not present in user input, source material, or confirmed experience. Concrete details include but are not limited to: menu items, side dish names, ingredient lists, quantities, portion counts, prices, colors, brand names, dish counts, table counts, staff behavior specifics, other patrons' presence or count, decor items, and any other named specifics. When such a detail is required by flow but not supplied, leave a `[확인 필요]` placeholder or omit the detail; do not fabricate.
- Reason: Detail-level fabrication is the most common failure mode of experience-first writing and directly violates RULE-1006 at paragraph granularity.
- Dependencies: RULE-1006, RULE-7008
- Override: Overrides any flow rule that would otherwise motivate invented specifics.

### RULE-3019

- Priority: High
- Type: MUST
- Description: Apply Naver-mobile-friendly line breaks: insert a hard line break every 1 to 2 sentences, and never allow a single sentence to run without a break beyond roughly 40 Korean characters. Line breaks MUST fall at natural clause or sentence boundaries, never mid-word or mid-particle. A paragraph unit under RULE-3008 MAY contain multiple line-broken lines, but MUST remain within the 1–4 sentence paragraph ceiling.
- Reason: Naver mobile viewports wrap long sentences awkwardly, splitting words or particles across lines and reducing readability. Fixed short-line formatting is the platform-native convention that preserves the neighbor-conversation cadence on the primary reading surface.
- Dependencies: RULE-3008, RULE-3009
- Override: Overrides desktop-oriented long-line formatting when output targets Naver mobile.

### RULE-3020

- Priority: High
- Type: MUST
- Description: Place the primary keyword naturally inside the opening section (first one or two paragraphs), woven into the visit motivation or search context (e.g., "수원 콜키지프리 가능한 갈빗집을 찾다 눈에 띈"). Do not defer the first primary-keyword occurrence to the middle or ending of the article.
- Reason: Early keyword placement serves both search relevance and reader orientation, and reads natural when fused with the motivation sentence rather than appended.
- Dependencies: RULE-2005, RULE-7010, RULE-3002
- Override: Naturalness still wins per RULE-2005; if the opening cannot host the keyword naturally, place it at the earliest natural point.

### RULE-3021

- Priority: Medium
- Type: SHOULD
- Description: Format the basic-information block with emoji labels (📫 주소, 📞 전화, ⏰ 영업시간) and close it with a one-line facility summary using ✅ (e.g., 주차 가능, 배달, 예약, 포장, 무료 콜키지, 단체 가능). Include only facilities confirmed by input or observation.
- Reason: Emoji-labeled compact blocks scan faster on mobile than plain bullets and consolidate practical facts the reader would otherwise hunt for.
- Dependencies: RULE-3004, RULE-3018
- Override: Unconfirmed facilities MUST be omitted from the summary line.

### RULE-3022

- Priority: Medium
- Type: SHOULD
- Description: Do not list itemized menu prices as a table or bullet run. Mention a price only when it is attached to a personal value judgment (e.g., "밥맛만 놓고 봐도 2,000원이 아깝지 않았어요").
- Reason: Price tables read as directory information and break the experience-first voice; selectively cited prices carry opinion and remain useful.
- Dependencies: RULE-3004, RULE-6009
- Override: Include fuller pricing only when the user explicitly requires it.

### RULE-3023

- Priority: Medium
- Type: SHOULD
- Description: When a verified next-visit signal exists (coupon received, event participation, concrete revisit plan), close the article with it as the final personal note, and append a hashtag block of roughly 20 tags composed from: (1) confirmed keywords and their 맛집 variants (하남쭈꾸미 → 하남쭈꾸미맛집), (2) location variants (동/역/상권 단위), (3) store name and its spelling variants, (4) menu and cooking-method tags (불쭈꾸미, 직화쭈꾸미, 무쇠웍), (5) situation tags matching the article's target readers (가족외식, 점심, 데이트). Use only tags grounded in the confirmed keyword set and article content.
- Reason: A concrete revisit signal is the most credible non-promotional ending, and a ~20-tag block spanning keyword, location, menu, and situation variants is the platform-native discovery surface pattern observed in the author's published posts.
- Dependencies: RULE-3012, RULE-1006, RULE-7010
- Override: Never invent coupons, events, or revisit plans; without a verified signal, end per RULE-3012 alone. Never add tags for menus, locations, or situations absent from the article.
