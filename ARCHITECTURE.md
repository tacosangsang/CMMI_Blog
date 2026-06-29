---
document_id: ARCHITECTURE
title: System Architecture
spec_version: 3.0
status: compatibility
---

# ARCHITECTURE.md

## Purpose

Describe the high-level architecture of the CMMI Blog AI Specification: module layout, ownership, pipeline order, and dependency rules. Normative content lives under `/specification`. This document is descriptive.

## Module Layout

| Position | Module | File | Range |
|---|---|---|---|
| 0 | Master Spec | [00_MASTER_SPEC.md](specification/00_MASTER_SPEC.md) | RULE-0001..0099 |
| 0 | Global Rules | [02_GLOBAL_RULES.md](specification/02_GLOBAL_RULES.md) | RULE-2001..2099 |
| 1 | Validation Engine | [07_VALIDATION_ENGINE.md](specification/07_VALIDATION_ENGINE.md) | RULE-7001..7099 |
| 2 | Reasoning Engine | [06_REASONING_ENGINE.md](specification/06_REASONING_ENGINE.md) | RULE-6001..6099 |
| 3 | Framework Engine | [04_FRAMEWORK_ENGINE.md](specification/04_FRAMEWORK_ENGINE.md) | RULE-4001..4099 |
| 4 | Identity Engine | [01_IDENTITY.md](specification/01_IDENTITY.md) | RULE-1001..1099 |
| 5 | Writing Engine | [03_WRITING_ENGINE.md](specification/03_WRITING_ENGINE.md) | RULE-3001..3099 |
| 6 | Voice Engine | [05_VOICE_ENGINE.md](specification/05_VOICE_ENGINE.md) | RULE-5001..5099 |
| 7 | Negative Rules | [08_NEGATIVE_RULES.md](specification/08_NEGATIVE_RULES.md) | RULE-8001..8099 |
| 9 | Execution Pipeline | [10_EXECUTION_PIPELINE.md](specification/10_EXECUTION_PIPELINE.md) | RULE-10001..10099 |
| 10 | Memory Engine | [09_MEMORY_ENGINE.md](specification/09_MEMORY_ENGINE.md) | RULE-9001..9099 |
| 11 | Rule Index | [11_RULE_INDEX.md](specification/11_RULE_INDEX.md) | all |

Final Validation re-enters the Validation Engine at pipeline stage 8. The module's `execution_position` reflects its earliest entry.

## Pipeline

```
Input Validation (10001)
    ↓
Category Classification (10002)
    ↓
Reasoning (10003)
    ↓
Framework Selection (10004)
    ↓
Identity Apply (10005)
    ↓
Draft (10006)
    ↓
Voice Tuning (10007)
    ↓
Negative Filter (10008)
    ↓
Final Validation (10009)
    ↓
Output (10010)
    ↓
Memory Maintenance, async (10011)
```

## Single-Owner Concept Map

| Concept | Owner |
|---|---|
| Global conflict hierarchy | 00 (RULE-0002) |
| Fact classification | 07 (RULE-7008) |
| Category list (canonical) | 07 (RULE-7007) |
| Experience-first ordering | 02 (RULE-2001) |
| Photo alignment | 02 (RULE-2008) |
| Reader-value gate | 02 (RULE-2010) |
| Korean exaggerated-praise blacklist | 08 (RULE-8003) |
| Korean overreaction blacklist | 08 (RULE-8004) |
| Korean AI-style phrase blacklist | 08 (RULE-8006) |
| Korean generic-ending blacklist | 08 (RULE-8008) |
| Korean vocabulary overuse warning | 08 (RULE-8012) |
| Preferred vocabulary list | 05 (RULE-5003) |
| Default emotion ratio | 05 (RULE-5002) |
| Sentence rhythm | 03 (RULE-3007) |
| Paragraph length | 03 (RULE-3008) |
| Photo-paragraph rhythm | 03 (RULE-3009) |
| Calm ending | 03 (RULE-3012) |
| Category-specific writing sequences | 03 (3013–3017) |
| Category priority and ratios | 04 (4003–4011) |
| Required input fields | 07 (RULE-7002) |
| Final reject gate | 07 (RULE-7014) |
| Memory update threshold | 09 (RULE-9002) |
| Memory uncertainty override | 09 (RULE-9013) |
| Synchronization scope | 09 (RULE-9012) |
| Execution order | 10 |

## Dependency Graph

One-direction (RULE-0014). For any rule X with owning module at position p(X), every `Dependencies` entry MUST point to a rule whose owning module is at position ≤ p(X). Cycles are forbidden.

The Memory Engine sits at position 10 and may reference any earlier module. It is async and never blocks generation.

## Source Traceability

Each module's `Source` section lists the originating `/source/*.pdf` documents. Sources are immutable (RULE-0011).

| Module | Source PDF |
|---|---|
| 01 Identity | `01_CMMI Blog Style Specification.pdf` |
| 03 Writing | `02_CMMI Blog Writing Specification.pdf` |
| 04 Framework | `04_CMMI Blog Review Framework.pdf` |
| 05 Voice | `05_CMMI Blog Voice Dictionary.pdf` |
| 06 Reasoning | `06_CMMI Blog Reasoning Engine.pdf` |
| 07 Validation | `09_CMMI Blog Input Validation Spec.pdf` |
| 08 Negative | `03_CMMI Blog Negative Rule Spec.pdf` |
| 09 Memory | `08_CMMI Blog Evolution Memory.pdf` |
| 10 Execution Pipeline | `07_CMMI Blog Master System Prompt.pdf` |
| 00 Master, 02 Global | Cross-cutting merge of all sources |

## Determinism Guarantees

- Single source of truth (RULE-0001).
- Stable Rule IDs (RULE-0004).
- One owner per concept (RULE-0008).
- Single conflict hierarchy (RULE-0002).
- One-direction dependencies (RULE-0014).
- Required YAML metadata (RULE-0013).
- Output gate enforcement (RULE-0015, RULE-10010).
