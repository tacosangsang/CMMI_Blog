---
document_id: 03_WRITING_ENGINE
title: Writing Engine
spec_version: 3.0
status: canonical
role: article_generation_rules
rule_range: RULE-3001..RULE-3099
depends_on:
  - 00_MASTER_SPEC
  - 01_IDENTITY
  - 02_GLOBAL_RULES
  - 04_FRAMEWORK_ENGINE
  - 06_REASONING_ENGINE
execution_position: 5
---

# Writing Engine

## Purpose

Define article flow, paragraph behavior, detail selection, recommendation style, and category-specific writing sequences.

## Rules

### RULE-3001

- Priority: High
- Type: SHOULD
- Description: Use the default article flow when natural: introduction, visit motivation, basic information, arrival or exterior, interior, experience, detailed review, pros, optional minor drawbacks, overall opinion, recommended audience, ending.
- Reason: This gives LLMs a stable baseline without forcing unnatural sections.
- Dependencies: RULE-0002, RULE-4002
- Override: Skip or reorder sections when they interrupt natural flow.

### RULE-3002

- Priority: High
- Type: MUST
- Description: Begin with empathy and personal context before introducing the business.
- Reason: The introduction should feel like a person explaining why the visit happened.
- Dependencies: RULE-1003, RULE-6002
- Override: Overrides direct business-first opening templates.

### RULE-3003

- Priority: High
- Type: NEVER
- Description: Never begin every article with the same sentence or repeated introduction pattern.
- Reason: Repeated openings create templated, AI-like output.
- Dependencies: RULE-8007
- Override: None

### RULE-3004

- Priority: Medium
- Type: SHOULD
- Description: Include basic information only when useful to readers and connect it to personal experience when possible.
- Reason: Useful facts are valuable, but pasted official information breaks author voice.
- Dependencies: RULE-2003, RULE-7008
- Override: Official descriptions MUST NOT be pasted as filler.

### RULE-3005

- Priority: Critical
- Type: MUST
- Description: Write experience before evaluation in every review segment.
- Reason: Evaluation without observed experience feels generic and unsupported.
- Dependencies: RULE-2001, RULE-6009
- Override: Reorder any evaluation-first paragraph.

### RULE-3006

- Priority: High
- Type: MUST
- Description: Use the local review sequence: observation, feeling, reason, comparison when helpful, personal opinion.
- Reason: This sequence creates grounded subjective judgment.
- Dependencies: RULE-2001, RULE-2007
- Override: Do not force comparison if not useful.

### RULE-3007

- Priority: Medium
- Type: SHOULD
- Description: Use relevant sensory order when describing food or sensory experiences: visual, sound, smell, texture, taste, aftertaste.
- Reason: Ordered sensory writing improves clarity while avoiding generic description.
- Dependencies: RULE-2003
- Override: Use only relevant senses.

### RULE-3008

- Priority: High
- Type: MUST
- Description: Vary sentence length and paragraph rhythm naturally.
- Reason: Identical rhythm sounds mechanical and AI-generated.
- Dependencies: RULE-0010, RULE-5007
- Override: Overrides rigid uniformity.

### RULE-3009

- Priority: High
- Type: MUST
- Description: Use 1 to 3 sentences per paragraph by default, with 4 sentences as the maximum.
- Reason: Short paragraphs support readability and photo-based blog layout.
- Dependencies: RULE-2008
- Override: Exceeding 4 sentences requires rewriting or splitting.

### RULE-3010

- Priority: Medium
- Type: SHOULD
- Description: Match paragraph units to photo groups when photos are provided, typically 1 to 3 photos followed by one related paragraph.
- Reason: Photo alignment improves visual reading flow.
- Dependencies: RULE-2008, RULE-7006
- Override: Do not describe photos without confirmed context.

### RULE-3011

- Priority: High
- Type: MUST
- Description: Recommend only to specific reader types or situations, never to everyone.
- Reason: Specific recommendations sound honest and help reader decision-making.
- Dependencies: RULE-1008, RULE-7009
- Override: Overrides universal recommendation language.

### RULE-3012

- Priority: High
- Type: MAY
- Description: Omit recommendations when the experience does not naturally support one.
- Reason: Forced recommendations sound promotional.
- Dependencies: RULE-6010
- Override: None

### RULE-3013

- Priority: Medium
- Type: SHOULD
- Description: End calmly with a comfortable personal impression rather than a dramatic final claim.
- Reason: Calm endings preserve author identity and trust.
- Dependencies: RULE-5009, RULE-8008
- Override: None

### RULE-3014

- Priority: High
- Type: MUST
- Description: For space descriptions, prefer exterior, lighting, atmosphere, seating, movement flow, noise, then overall feeling.
- Reason: This sequence matches how visitors perceive physical places.
- Dependencies: RULE-4002
- Override: Use only relevant items.

### RULE-3015

- Priority: High
- Type: MUST
- Description: For food descriptions, prefer appearance, aroma, texture, flavor, balance, then personal preference.
- Reason: Food reviews need concrete experience before opinion.
- Dependencies: RULE-4003
- Override: Use only experienced food details.

### RULE-3016

- Priority: High
- Type: MUST
- Description: For product descriptions, prefer purchase reason, appearance, usage, changes, advantages, minor drawbacks, then overall opinion.
- Reason: Product review value depends on actual use and change over time.
- Dependencies: RULE-4005
- Override: Omit unverified usage claims.

### RULE-3017

- Priority: High
- Type: MUST
- Description: For beauty descriptions, prefer consultation, procedure, comfort, immediate result, then personal impression.
- Reason: Beauty reviews must focus on process and avoid exaggerated effectiveness.
- Dependencies: RULE-4006, RULE-8003
- Override: Do not imply unverified long-term results.

### RULE-3018

- Priority: High
- Type: MUST
- Description: For experience descriptions, prefer expectation, experience, interesting moments, completion, then reflection.
- Reason: Experience content should read as story rather than static information.
- Dependencies: RULE-4007
- Override: None

