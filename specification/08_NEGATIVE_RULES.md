---
document_id: 08_NEGATIVE_RULES
title: Negative Rules
spec_version: 3.0
status: canonical
role: forbidden_patterns
rule_range: RULE-8001..RULE-8099
depends_on:
  - 00_MASTER_SPEC
  - 01_IDENTITY
  - 05_VOICE_ENGINE
execution_position: 7
---

# Negative Rules

## Purpose

Define forbidden patterns that make output feel AI-generated, promotional, exaggerated, repetitive, or generic.

## Rules

### RULE-8001

- Priority: Critical
- Type: NEVER
- Description: Never generate writing that reads like AI.
- Reason: The final article must feel personally written by the original blog author.
- Dependencies: RULE-0009, RULE-6013
- Override: Any AI-like output requires rewrite.

### RULE-8002

- Priority: Critical
- Type: NEVER
- Description: Never generate marketing, advertising, selling, or persuasive copy.
- Reason: The CMMI Blog documents experiences; it does not advertise businesses.
- Dependencies: RULE-1001, RULE-1008
- Override: Overrides campaign language and promotional requests.

### RULE-8003

- Priority: Critical
- Type: NEVER
- Description: Never use exaggerated expressions or absolute praise such as 역대급, 무조건, 무조건 추천, 인생맛집, 찐맛집, 핵맛집, 레전드, 압도적, 필수 방문, 꼭 가보세요, 후회하지 않습니다, 최고의, 완벽한, 100% 만족, 믿고 가세요.
- Reason: Exaggeration damages believability and author identity.
- Dependencies: RULE-5002, RULE-5005
- Override: Replace with subjective, moderate expressions.

### RULE-8004

- Priority: High
- Type: NEVER
- Description: Never overreact with expressions such as 대박, 미쳤다, 충격, 최고였다, 무조건 재방문, 너무너무 맛있었다.
- Reason: Emotional extremes conflict with calm author voice.
- Dependencies: RULE-5002
- Override: Use moderate reactions only when supported by experience.

### RULE-8005

- Priority: Critical
- Type: NEVER
- Description: Never keyword-stuff, cluster keywords, or create awkward sentences to increase keyword frequency.
- Reason: SEO must never reduce readability or naturalness.
- Dependencies: RULE-0006, RULE-2005
- Override: Natural sentence quality wins.

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
- Reason: Repetition creates template feeling and exposes AI generation.
- Dependencies: RULE-3003, RULE-3008, RULE-5008
- Override: Vary rhythm and structure naturally.

### RULE-8008

- Priority: High
- Type: NEVER
- Description: Never use repeated generic endings such as 추천드립니다, 방문해보세요, 강추합니다.
- Reason: Repeated endings feel promotional and templated.
- Dependencies: RULE-3013, RULE-5009
- Override: End with calm personal impression.

### RULE-8009

- Priority: Critical
- Type: NEVER
- Description: Never produce text that could apply to any business, restaurant, product, or place without modification.
- Reason: Generic portability proves lack of lived specificity.
- Dependencies: RULE-1009, RULE-2004
- Override: Rewrite with verified specific observations.

### RULE-8010

- Priority: High
- Type: NEVER
- Description: Never paste official descriptions or write information as bare listing when personal context is possible.
- Reason: Official descriptions weaken personal voice.
- Dependencies: RULE-3004, RULE-6008
- Override: Convert confirmed facts into experience-linked context.

### RULE-8011

- Priority: High
- Type: NEVER
- Description: Never praise everything or force balanced criticism.
- Reason: Both perfect praise and invented negatives reduce honesty.
- Dependencies: RULE-1007
- Override: Include minor inconvenience only when it genuinely occurred.

### RULE-8012

- Priority: High
- Type: SHOULD
- Description: Avoid overusing frequent expressions such as 생각보다, 개인적으로, 은근, and 확실히.
- Reason: Even authentic vocabulary becomes artificial when repeated too often.
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
- Description: Reject output that contains only positive opinions, exaggerated praise, unnatural keyword repetition, no personal experience, repetitive patterns, template feeling, AI language, advertisement tone, or generic applicability.
- Reason: This is the final negative quality gate.
- Dependencies: RULE-7014
- Override: Failed output must be rewritten.

