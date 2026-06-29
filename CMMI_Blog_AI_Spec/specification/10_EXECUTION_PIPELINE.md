---
document_id: 10_EXECUTION_PIPELINE
title: Execution Pipeline
spec_version: 3.0
status: canonical
role: deterministic_execution_order
rule_range: RULE-10001..RULE-10099
depends_on:
  - 00_MASTER_SPEC
execution_position: 10
---

# Execution Pipeline

## Purpose

Define explicit execution order for deterministic LLM article generation.

## Pipeline Rules

### RULE-10001

- Priority: Critical
- Type: MUST
- Description: Execute input validation before all other generation steps.
- Reason: No downstream module can operate safely on missing or unknown information.
- Dependencies: RULE-7001
- Override: Failed validation pauses generation.

### RULE-10002

- Priority: Critical
- Type: MUST
- Description: Classify category and review purpose after validation and before reasoning.
- Reason: Category and purpose guide framework and reasoning focus.
- Dependencies: RULE-7007, RULE-4001
- Override: Ambiguous classification triggers clarification or best-evidence classification.

### RULE-10003

- Priority: Critical
- Type: MUST
- Description: Execute reasoning before drafting.
- Reason: The system must understand experience before writing.
- Dependencies: RULE-6001
- Override: Drafting before reasoning is invalid.

### RULE-10004

- Priority: High
- Type: MUST
- Description: Select and apply one framework after reasoning focus is known.
- Reason: Framework selection converts validated category into structure guidance.
- Dependencies: RULE-4001, RULE-4002, RULE-6007
- Override: Naturalness may adjust structure.

### RULE-10005

- Priority: Critical
- Type: MUST
- Description: Apply identity before article drafting.
- Reason: Every sentence must originate from the correct author posture.
- Dependencies: RULE-1001
- Override: Identity overrides external style imitation.

### RULE-10006

- Priority: High
- Type: MUST
- Description: Draft using the Writing Engine after validation, reasoning, framework, and identity are established.
- Reason: Drafting needs stable inputs and author posture.
- Dependencies: RULE-3001, RULE-3005
- Override: None

### RULE-10007

- Priority: High
- Type: MUST
- Description: Apply Voice Engine after drafting to tune rhythm, tone, vocabulary, opinion style, and emotional intensity.
- Reason: Voice pass preserves natural author sound without replacing structure.
- Dependencies: RULE-5001
- Override: Voice tuning must not introduce repetition or forced vocabulary.

### RULE-10008

- Priority: Critical
- Type: MUST
- Description: Apply Negative Rules after voice tuning.
- Reason: Forbidden patterns must be removed before final validation.
- Dependencies: RULE-8001, RULE-8014
- Override: Any violation requires rewrite.

### RULE-10009

- Priority: Critical
- Type: MUST
- Description: Execute final validation after negative filtering.
- Reason: Final output must pass believability, specificity, authenticity, and conflict checks.
- Dependencies: RULE-7014
- Override: Failed validation returns to the earliest failed module.

### RULE-10010

- Priority: Critical
- Type: MUST
- Description: Output only after all prior pipeline stages pass.
- Reason: Deterministic execution requires gate-based approval.
- Dependencies: RULE-10001, RULE-10009
- Override: None

### RULE-10011

- Priority: High
- Type: MUST
- Description: For memory maintenance tasks, execute Memory Engine after output or after new original-author samples are reviewed.
- Reason: Style evolution should not interrupt article generation unless explicitly requested.
- Dependencies: RULE-9001
- Override: Memory update never applies without sufficient evidence.

## Execution Order

1. Validate inputs.
2. Classify category and objective.
3. Reason through experience.
4. Select one framework.
5. Apply identity.
6. Draft article.
7. Apply voice.
8. Apply negative rules.
9. Run final validation.
10. Output.
11. Update memory only when requested or evidence threshold is met.

