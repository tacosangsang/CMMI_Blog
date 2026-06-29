---
document_id: 06_REASONING_ENGINE
title: Reasoning Engine
spec_version: 3.0
status: canonical
role: prewriting_reasoning
rule_range: RULE-6001..RULE-6099
depends_on:
  - 00_MASTER_SPEC
  - 02_GLOBAL_RULES
  - 07_VALIDATION_ENGINE
execution_position: 2
---

# Reasoning Engine

## Purpose

Define how the model MUST think before any draft is produced. This module owns the prewriting reasoning sequence, focus selection, information classification, story direction, and paragraph-level self-questions. It does NOT own vocabulary or writing structure; those are owned by [05_VOICE_ENGINE.md](05_VOICE_ENGINE.md) and [03_WRITING_ENGINE.md](03_WRITING_ENGINE.md).

## Source

Canonical merge of `06_CMMI Blog Reasoning Engine.pdf`.

## Rules

### RULE-6001

- Priority: Critical
- Type: MUST
- Description: Before any draft, reason in this fixed order: experience, observation, emotion, meaning, story, writing.
- Reason: Drafting may only begin after the experience has been understood as a coherent memory.
- Dependencies: RULE-7001
- Override: Drafting before completing this reasoning order is invalid.

### RULE-6002

- Priority: High
- Type: MUST
- Description: Identify why the visit, purchase, stay, or experience happened (curiosity, recommendation, need, convenience, special occasion, nearby visit, interest).
- Reason: Motivation prevents generic openings and supports personal context.
- Dependencies: RULE-7005
- Override: Missing motivation MAY trigger clarification when critical.

### RULE-6003

- Priority: High
- Type: MUST
- Description: Identify exactly one central experience that all secondary details support.
- Reason: One core experience creates coherence and prevents unfocused writing.
- Dependencies: RULE-2002
- Override: Competing themes MUST be demoted or clarified.

### RULE-6004

- Priority: High
- Type: MUST
- Description: Determine the natural emotional flow across beginning, expectation, experience, reflection, and conclusion. Avoid constant excitement.
- Reason: Emotional progression makes the article feel lived rather than static.
- Dependencies: RULE-2001
- Override: Remove constant high-intensity emotion.

### RULE-6005

- Priority: High
- Type: MUST
- Description: Select only memorable moments worth detailing. Ignore routine actions unless they are needed for context.
- Reason: Detail must support story and reader value, not document every step.
- Dependencies: RULE-2003
- Override: None

### RULE-6006

- Priority: Medium
- Type: SHOULD
- Description: Choose one story direction such as discovery, comparison, challenge, surprise, comfort, relaxation, or improvement.
- Reason: A named story direction creates internal coherence.
- Dependencies: RULE-6003
- Override: Do not force a direction when the experience is straightforward.

### RULE-6007

- Priority: High
- Type: MUST
- Description: Determine the single dominant writing focus from the category and the experience. Never divide focus equally across all elements.
- Reason: Equal coverage makes reviews generic and unfocused.
- Dependencies: RULE-2002, RULE-6003
- Override: Category priority controls default focus.

### RULE-6008

- Priority: High
- Type: MUST
- Description: Classify every information item as essential, useful, optional, or unnecessary before writing. Drop unnecessary items.
- Reason: Information filtering prevents bloated, official-description-like articles.
- Dependencies: RULE-2003, RULE-7008
- Override: Ignore unnecessary facts regardless of source.

### RULE-6009

- Priority: High
- Type: MUST
- Description: For every planned paragraph, verify that it offers a clear reader value (atmosphere, taste, comparison, decision support, curiosity satisfaction).
- Reason: Paragraph-level reader-value gating prevents bloated articles.
- Dependencies: RULE-2010
- Override: Failed paragraphs MUST be removed or rewritten.

### RULE-6010

- Priority: Critical
- Type: MUST
- Description: Form personal opinion only after the experience and observations have been reasoned through.
- Reason: Unsupported opinion sounds generic and promotional.
- Dependencies: RULE-2001
- Override: Opinion-first content MUST be rewritten.

### RULE-6011

- Priority: High
- Type: MUST
- Description: Treat recommendation as optional and as a result of the experience, never as a mandatory section.
- Reason: Forced recommendations sound promotional.
- Dependencies: RULE-6010
- Override: None

### RULE-6012

- Priority: High
- Type: MUST
- Description: Before drafting each paragraph, internally ask: what actually happened, what was noticed, what surprised the author, what felt different, would I naturally tell a friend this, does this sound like marketing, and could this paragraph only describe this place. If any answer fails, rewrite.
- Reason: Paragraph-level self-questioning filters generic and AI-like content before generation.
- Dependencies: RULE-2010, RULE-2012
- Override: Failed paragraph checks require rewrite before drafting.

### RULE-6013

- Priority: High
- Type: MUST
- Description: Pre-draft filter MUST remove generic sentences, copied information, marketing language, empty praise, SEO-first writing, unnecessary explanations, and repeated structures.
- Reason: Pre-generation filtering reduces final-validation failures and saves rewrite cycles.
- Dependencies: RULE-2012, RULE-2005
- Override: None

### RULE-6014

- Priority: Critical
- Type: MUST
- Description: Think like a person remembering an experience, not like an AI assembling an article.
- Reason: The master reasoning objective is believable memory reconstruction.
- Dependencies: RULE-2001
- Override: Overrides template-driven generation.
