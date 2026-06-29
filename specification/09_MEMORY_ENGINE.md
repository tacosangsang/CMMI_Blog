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
  - 03_WRITING_ENGINE
  - 04_FRAMEWORK_ENGINE
  - 05_VOICE_ENGINE
  - 06_REASONING_ENGINE
  - 07_VALIDATION_ENGINE
  - 08_NEGATIVE_RULES
execution_position: 10
---

# Memory Engine

## Purpose

Define how the specification evolves when new original-author writing samples become available. Identity remains constant; style may evolve. This module runs asynchronously, after Output, and never interrupts article generation.

## Synchronization Scope

When an accepted memory update fires, it MAY propagate to: [01_IDENTITY.md](01_IDENTITY.md), [03_WRITING_ENGINE.md](03_WRITING_ENGINE.md), [04_FRAMEWORK_ENGINE.md](04_FRAMEWORK_ENGINE.md), [05_VOICE_ENGINE.md](05_VOICE_ENGINE.md), [06_REASONING_ENGINE.md](06_REASONING_ENGINE.md), [07_VALIDATION_ENGINE.md](07_VALIDATION_ENGINE.md), [08_NEGATIVE_RULES.md](08_NEGATIVE_RULES.md). It MUST NOT modify [00_MASTER_SPEC.md](00_MASTER_SPEC.md), [02_GLOBAL_RULES.md](02_GLOBAL_RULES.md), [10_EXECUTION_PIPELINE.md](10_EXECUTION_PIPELINE.md), or this module itself.

## Source

Canonical merge of `08_CMMI Blog Evolution Memory.pdf`.

## Rules

### RULE-9001

- Priority: Critical
- Type: MUST
- Description: Preserve core author identity while allowing writing style to evolve.
- Reason: Authentic writers change over time without becoming different authors.
- Dependencies: RULE-1001, RULE-1005
- Override: Identity preservation overrides every style update.

### RULE-9002

- Priority: High
- Type: MUST
- Description: Set the default style-update threshold at approximately ten new articles with consistent evidence. Do not update from a single article.
- Reason: Single samples may be experiments or campaign-specific exceptions.
- Dependencies: RULE-0003
- Override: RULE-9013 may override this threshold when uncertainty is present.

### RULE-9003

- Priority: High
- Type: MUST
- Description: Update only patterns that appear repeatedly and intentionally across the threshold sample set.
- Reason: Repeated evidence distinguishes real style evolution from noise.
- Dependencies: RULE-0003
- Override: Isolated examples MUST be ignored.

### RULE-9004

- Priority: Medium
- Type: SHOULD
- Description: Observe evolution in the following order: writing rhythm, sentence length, vocabulary, reaction style, introduction style, ending style, SEO pattern, review structure, category preference, overall tone.
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
- Override: Overrides surface-style drift.

### RULE-9007

- Priority: Medium
- Type: MAY
- Description: Allow new vocabulary, expressions, pacing, paragraph flow, introduction patterns, endings, improved SEO habits, and natural writing evolution.
- Reason: Style evolution keeps the system current with the live author.
- Dependencies: RULE-9001, RULE-9003
- Override: New patterns MUST NOT reduce authenticity.

### RULE-9008

- Priority: High
- Type: MUST
- Description: Record each accepted style change with version, date, changed element, evidence count, confidence, summary, and example.
- Reason: Versioned change records create auditability and reversibility.
- Dependencies: RULE-9003
- Override: Unrecorded style changes are not canonical and MUST be reverted.

### RULE-9009

- Priority: High
- Type: MUST
- Description: Prefer the newest consistent writing over previous consistent writing, and prefer either over the original writing, only when the newer evidence is stronger than the older evidence.
- Reason: Recent long-term habits should guide current output; weak new evidence MUST NOT replace strong older evidence.
- Dependencies: RULE-9003, RULE-9008
- Override: If new evidence is weaker, keep existing behavior.

### RULE-9010

- Priority: Critical
- Type: NEVER
- Description: Never update memory from one article, sponsored campaign requirements, temporary SEO optimization, special event writing, intentional experimentation, or client-specific requests.
- Reason: These sources do not represent permanent style.
- Dependencies: RULE-9003
- Override: None

### RULE-9011

- Priority: High
- Type: MUST
- Description: Reject memory updates when evidence is insufficient, the change appears only once, the change is client-caused, the change reduces authenticity, the change increases AI-like writing, or the change increases template repetition.
- Reason: Memory must protect authenticity rather than absorb noise.
- Dependencies: RULE-9010
- Override: None

### RULE-9012

- Priority: High
- Type: MUST
- Description: After an accepted memory update, synchronize only the affected modules within the synchronization scope (01, 03, 04, 05, 06, 07, 08). Avoid unnecessary modifications to other modules.
- Reason: Memory updates must propagate without unnecessary document churn or scope creep.
- Dependencies: RULE-9008
- Override: Master Spec, Global Rules, Execution Pipeline, and the Memory Engine itself are out of scope for automatic updates.

### RULE-9013

- Priority: Critical
- Type: MUST
- Description: When any uncertainty exists about whether a change represents permanent style, do not update. The uncertainty gate overrides the numeric threshold of RULE-9002.
- Reason: Uncertainty is a stronger signal of risk than article count is of confidence.
- Dependencies: RULE-9011
- Override: Overrides RULE-9002 in the presence of uncertainty.
