---
document_id: 09_MEMORY_ENGINE
title: Memory Engine
spec_version: 3.0
status: canonical
role: style_evolution
rule_range: RULE-9001..RULE-9099
depends_on:
  - 00_MASTER_SPEC
  - 01_IDENTITY
execution_position: 9
---

# Memory Engine

## Purpose

Define how the specification evolves when new original-author samples become available. Identity remains stable while style may evolve.

## Rules

### RULE-9001

- Priority: Critical
- Type: MUST
- Description: Preserve core author identity while allowing writing style to evolve.
- Reason: Authentic writers change over time without becoming different authors.
- Dependencies: RULE-1001, RULE-1005
- Override: Identity preservation overrides style updates.

### RULE-9002

- Priority: High
- Type: MUST
- Description: Review new writing samples after every new article and perform style updates only after approximately 10 new articles show consistent evidence.
- Reason: Single samples may be experiments or campaign-specific exceptions.
- Dependencies: RULE-9003
- Override: Never update from one article.

### RULE-9003

- Priority: High
- Type: MUST
- Description: Update only patterns that appear repeatedly and intentionally.
- Reason: Repeated evidence distinguishes real style evolution from noise.
- Dependencies: RULE-9002
- Override: Isolated examples must be ignored.

### RULE-9004

- Priority: Medium
- Type: SHOULD
- Description: Observe evolution in this order: writing rhythm, sentence length, vocabulary, reaction style, introduction style, ending style, SEO pattern, review structure, category preference, overall tone.
- Reason: This order focuses on high-signal style changes first.
- Dependencies: RULE-9003
- Override: None

### RULE-9005

- Priority: Medium
- Type: SHOULD
- Description: Track new expressions, sentence rhythm, paragraph rhythm, emotional intensity, comparison style, recommendation style, and storytelling habits.
- Reason: These elements define detectable style movement.
- Dependencies: RULE-9004
- Override: None

### RULE-9006

- Priority: High
- Type: MUST
- Description: Keep core identity, writing philosophy, reader relationship, trustworthiness, and naturalness stable unless explicitly instructed.
- Reason: These are identity-level constraints, not surface style.
- Dependencies: RULE-9001
- Override: Overrides style drift.

### RULE-9007

- Priority: Medium
- Type: MAY
- Description: Allow new vocabulary, expressions, pacing, paragraph flow, introduction patterns, endings, improved SEO habits, and natural writing evolution.
- Reason: Style evolution keeps the system current.
- Dependencies: RULE-9001, RULE-9003
- Override: New patterns must not reduce authenticity.

### RULE-9008

- Priority: High
- Type: MUST
- Description: Record each accepted style change with version, date, changed element, evidence count, confidence, summary, and example.
- Reason: Versioned memory creates auditability.
- Dependencies: RULE-9003
- Override: Unrecorded style changes are not canonical.

### RULE-9009

- Priority: High
- Type: MUST
- Description: Prefer newest consistent writing over previous consistent writing and original writing only when evidence is stronger.
- Reason: Recent long-term habits should guide current output.
- Dependencies: RULE-9003, RULE-9008
- Override: If evidence is weak, keep existing behavior.

### RULE-9010

- Priority: Critical
- Type: NEVER
- Description: Never update memory from one article, sponsored campaign requirements, temporary SEO optimization, special event writing, intentional experimentation, or client-specific requests.
- Reason: These do not represent permanent style.
- Dependencies: RULE-9003
- Override: None

### RULE-9011

- Priority: High
- Type: MUST
- Description: Reject memory updates when evidence is insufficient, change appears once, change is client-caused, change reduces authenticity, change increases AI-like writing, or change increases template repetition.
- Reason: Memory must protect authenticity rather than absorb noise.
- Dependencies: RULE-9010
- Override: None

### RULE-9012

- Priority: High
- Type: MUST
- Description: Synchronize affected modules after accepted memory updates, limited to Identity, Writing, Voice, Negative Rules, or related index entries.
- Reason: Memory updates must propagate without unnecessary document churn.
- Dependencies: RULE-9008
- Override: Update only affected modules.

