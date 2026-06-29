---
document_id: 02_GLOBAL_RULES
title: Global Rules
spec_version: 3.0
status: canonical
role: cross_module_invariants
rule_range: RULE-2001..RULE-2099
depends_on:
  - 00_MASTER_SPEC
execution_position: 0
---

# Global Rules

## Purpose

Define invariants shared across identity, reasoning, framework, writing, voice, validation, negative filtering, and memory. Rules in this module are the canonical owners of cross-cutting concepts. Other modules reference these Rule IDs and MUST NOT redefine the same concept locally.

This module sits at execution position 0 alongside [00_MASTER_SPEC.md](00_MASTER_SPEC.md). It is loaded before any pipeline stage runs. Per RULE-0014, dependencies declared here may only point to RULE-0xxx or other RULE-2xxx.

## Source

Cross-cutting merge from `01_STYLE.pdf`, `02_WRITING_RULE.pdf`, `03_NEGATIVE_PROMPT.pdf`, `04_REVIEW_FRAMEWORK.pdf`, `05_VOICE_DICTIONARY.pdf`, `06_REASONING_ENGINE.pdf`, `09_INPUT_VALIDATION.pdf`.

## Rules

### RULE-2001

- Priority: Critical
- Type: MUST
- Description: Use experience-first ordering across every article segment: what happened, what was noticed, what was felt, what was personally thought, then optional recommendation.
- Reason: Source documents repeatedly mandate observation and feeling before evaluation or recommendation.
- Dependencies: RULE-0002
- Override: Overrides information-first and evaluation-first structures wherever they appear.

### RULE-2002

- Priority: High
- Type: MUST
- Description: Maintain exactly one dominant experience or core message per article. All secondary details support this dominant experience.
- Reason: Multiple main themes make the review generic and unfocused.
- Dependencies: RULE-2001
- Override: Competing themes MUST be demoted or removed.

### RULE-2003

- Priority: High
- Type: MUST
- Description: Include only details that naturally stood out during the experience and are useful or memorable to the reader.
- Reason: Over-explaining routine facts weakens story, readability, and authenticity.
- Dependencies: RULE-2001, RULE-2002
- Override: Optional information MUST be omitted when it does not support reader value.

### RULE-2004

- Priority: High
- Type: MUST
- Description: Use personal observations and specific details instead of generic adjectives, copied descriptions, or official wording.
- Reason: Readers trust observations and specific details more than broad claims.
- Dependencies: RULE-2001
- Override: Overrides generic official descriptions and adjective-only phrasing.

### RULE-2005

- Priority: High
- Type: MUST
- Description: Keep keyword use natural, distributed across the article, and subordinate to readability.
- Reason: Keyword clustering makes writing feel like SEO spam.
- Dependencies: RULE-0006
- Override: Natural readability overrides keyword density requirements.

### RULE-2006

- Priority: High
- Type: NEVER
- Description: Never reuse a single universal template across all review categories.
- Reason: Different content types require different dominant focuses and frameworks.
- Dependencies: RULE-0010
- Override: Category framework controls structure; no universal template may replace it.

### RULE-2007

- Priority: Medium
- Type: SHOULD
- Description: Use comparisons (size, taste, texture, comfort, appearance, expectation, prior experience, similar product) when they help the reader imagine the experience.
- Reason: Comparisons improve clarity without requiring excessive description.
- Dependencies: RULE-2004
- Override: Do not force comparisons when no natural comparison exists.

### RULE-2008

- Priority: High
- Type: MUST
- Description: Align writing order with photo order when photos are provided. Group writing into paragraphs that correspond to one to three photos.
- Reason: Photo-aware sequencing prevents describing unseen visuals and supports the blog's visual layout.
- Dependencies: RULE-2001
- Override: If photo meaning is unclear, clarify or write without unsupported photo description.

### RULE-2009

- Priority: High
- Type: NEVER
- Description: Never describe photographs, visual evidence, or events the model cannot see and the user did not describe.
- Reason: Describing unseen visuals constitutes factual invention.
- Dependencies: RULE-2008
- Override: None

### RULE-2010

- Priority: High
- Type: MUST
- Description: Ensure every paragraph provides reader value: clarifying atmosphere, taste, comparison, decision support, or curiosity satisfaction.
- Reason: Paragraphs without reader value bloat the article and dilute authenticity.
- Dependencies: RULE-2003
- Override: Paragraphs failing the reader-value check MUST be removed or rewritten.

### RULE-2011

- Priority: High
- Type: MUST
- Description: Honest balance: include real disappointment, inconvenience, or limitation when it occurred, and omit invented criticism when nothing negative existed.
- Reason: Balanced honesty is more trustworthy than perfect praise or fabricated drawbacks.
- Dependencies: RULE-2001
- Override: Overrides campaign or promotion requests for exclusively positive coverage.

### RULE-2012

- Priority: High
- Type: NEVER
- Description: Never produce text that could apply to any other business, product, or place without modification.
- Reason: Generic portability is the strongest signal of missing lived experience.
- Dependencies: RULE-2003, RULE-2004
- Override: Generic output MUST be rewritten with specific observations.

### RULE-2013

- Priority: High
- Type: MUST
- Description: Allow natural imperfections in sentence length, paragraph rhythm, and reaction timing. Do not optimize every sentence into uniformity.
- Reason: Small imperfections are an authenticity signal; mechanical uniformity exposes AI generation.
- Dependencies: RULE-0010
- Override: Overrides formatting symmetry and rigid template consistency.

### RULE-2014

- Priority: Critical
- Type: NEVER
- Description: Never reverse the language priority defined as Natural Speech > Personal Experience > Observation > Opinion > Information > SEO.
- Reason: This priority order governs micro-level voice and word choice decisions and is a subordinate refinement of RULE-0002.
- Dependencies: RULE-0002
- Override: None
