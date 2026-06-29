---
document_id: CLAUDE
title: Claude Project Instructions
spec_version: 3.0
status: compatibility
---

# CLAUDE.md

## Purpose

Maintain compatibility with Claude while following the same architecture as [AGENTS.md](AGENTS.md). Claude executes the CMMI Blog AI Specification by reading the canonical modules under `/specification` and the immutable source PDFs under `/source`.

## Workflow

1. Read [AGENTS.md](AGENTS.md).
2. Read [00_MASTER_SPEC.md](specification/00_MASTER_SPEC.md) for the Global Conflict Hierarchy (RULE-0002) and Rule ID policy (RULE-0004).
3. Read [11_RULE_INDEX.md](specification/11_RULE_INDEX.md) for the full Rule lookup.
4. Analyze `/source/*.pdf` only as immutable reference. Never modify (RULE-0011).
5. Detect duplicates and conflicts before any change.
6. Refactor only inside `/specification`.
7. Preserve rule meaning (RULE-0003). Never invent rules (RULE-0012).
8. Produce deterministic, machine-readable Markdown.

## Execution Pipeline

Defined canonically in [10_EXECUTION_PIPELINE.md](specification/10_EXECUTION_PIPELINE.md). Summary:

1. Input Validation (RULE-10001)
2. Category Classification (RULE-10002)
3. Reasoning (RULE-10003)
4. Framework Selection (RULE-10004)
5. Identity Apply (RULE-10005)
6. Draft (RULE-10006)
7. Voice Tuning (RULE-10007)
8. Negative Filter (RULE-10008)
9. Final Validation (RULE-10009)
10. Output (RULE-10010)
11. Memory Maintenance, async (RULE-10011)

## Conflict Resolution

Single authority: RULE-0002.

Naturalness > Authenticity > Verified Human Experience > Trust > Readability > SEO > Structure.

Never redefine this hierarchy locally.

## Output Standard

- YAML front matter on every module (RULE-0013).
- Stable Rule IDs (RULE-0004).
- Cross-references by Rule ID only.
- No duplicated logic; single owner per concept (RULE-0008).
- One-direction dependency graph (RULE-0014): every Dependencies entry points to a Rule whose owning module has equal or earlier `execution_position`.
- Machine-readable Markdown.

## Rule Format

Every rule MUST include:

- Rule ID
- Priority (Critical | High | Medium | Low)
- Type (MUST | SHOULD | MAY | NEVER)
- Description
- Reason
- Dependencies
- Override
- Example (optional)

## Source Immutability

`/source/*.pdf` is read-only. All canonical merging happens in `/specification`. See RULE-0011 and RULE-0012.

## Memory and Synchronization

Memory updates run async after Output (RULE-10011). Synchronization scope is defined in RULE-9012: 01, 03, 04, 05, 06, 07, 08. Master (00), Global (02), Pipeline (10), and Memory (09) itself are out of scope for automatic updates.

## Quality Gate

Final approval gate is RULE-7014 in [07_VALIDATION_ENGINE.md](specification/07_VALIDATION_ENGINE.md). Failure rewinds to the earliest failed module per RULE-7015.
