---
document_id: 00_MASTER_SPEC
title: CMMI Blog Enterprise AI Specification
spec_version: 3.0
status: canonical
role: single_source_of_truth
rule_range: RULE-0001..RULE-0099
depends_on: []
execution_position: 0
---

# CMMI Blog Enterprise AI Specification

## Purpose

Defines deterministic LLM behavior for generating CMMI Blog articles. Merges all source documents (`/source/*.pdf`) into one canonical Rule ID architecture. No duplicated logic. Every execution is driven by Rule IDs.

This document is the **Single Source of Truth**. Every other module derives from, or refers back to, the rules defined here.

## Canonical Architecture

| Position | Module | File |
|---|---|---|
| 0 | Master Spec | [00_MASTER_SPEC.md](00_MASTER_SPEC.md) |
| 1 | Validation Engine | [07_VALIDATION_ENGINE.md](07_VALIDATION_ENGINE.md) |
| 2 | Reasoning Engine | [06_REASONING_ENGINE.md](06_REASONING_ENGINE.md) |
| 3 | Framework Engine | [04_FRAMEWORK_ENGINE.md](04_FRAMEWORK_ENGINE.md) |
| 4 | Identity Engine | [01_IDENTITY.md](01_IDENTITY.md) |
| 5 | Writing Engine | [03_WRITING_ENGINE.md](03_WRITING_ENGINE.md) |
| 6 | Voice Engine | [05_VOICE_ENGINE.md](05_VOICE_ENGINE.md) |
| 7 | Negative Rules | [08_NEGATIVE_RULES.md](08_NEGATIVE_RULES.md) |
| 8 | Final Validation | [07_VALIDATION_ENGINE.md](07_VALIDATION_ENGINE.md) |
| 9 | Execution Pipeline | [10_EXECUTION_PIPELINE.md](10_EXECUTION_PIPELINE.md) |
| 10 | Memory Engine | [09_MEMORY_ENGINE.md](09_MEMORY_ENGINE.md) |
| — | Global Rules | [02_GLOBAL_RULES.md](02_GLOBAL_RULES.md) |
| — | Rule Index | [11_RULE_INDEX.md](11_RULE_INDEX.md) |

## Global Conflict Hierarchy

When two rules conflict, apply this hierarchy in descending priority. Higher rank always overrides lower rank.

1. Naturalness
2. Authenticity
3. Verified Human Experience
4. Trust
5. Readability
6. SEO
7. Structure

This hierarchy is the **only** conflict-resolution authority in the specification. No other module may redefine or re-order it.

## Rule ID Policy

- Every normative rule MUST have a globally unique Rule ID of the form `RULE-NNNN`.
- Rule IDs are stable. Once assigned, never reused or renumbered.
- Each module owns a fixed numeric range (see [11_RULE_INDEX.md](11_RULE_INDEX.md)).
- Cross-references between modules use Rule IDs only.
- Root meta documents (`AGENTS.md`, `README.md`, `CLAUDE.md`, `CONTRIBUTING.md`) MUST NOT contain Rule IDs; they reference Rule IDs only.

## Rule Format

Every rule MUST include the following fields:

- Rule ID
- Priority (Critical | High | Medium | Low)
- Type (MUST | SHOULD | MAY | NEVER)
- Description
- Reason
- Dependencies (list of Rule IDs, or `None`)
- Override (effect on other rules, or `None`)
- Example (optional)

## Module Boundaries

Each concept has exactly one owner module. Other modules reference the owner via Rule ID. No duplicated logic.

| Concept | Owner |
|---|---|
| Conflict hierarchy | 00 (RULE-0002) |
| Fact classification (confirmed/likely/unknown) | 07 (RULE-7008) |
| Experience-first ordering | 02 (RULE-2001) |
| Photo alignment | 02 (RULE-2008) |
| Korean AI-language blacklist | 08 |
| Exaggerated-praise blacklist | 08 |
| Preferred vocabulary list | 05 |
| Vocabulary overuse warnings | 08 (cross-ref 05) |
| Sentence and paragraph rhythm | 03 |
| Category definitions | 04 |
| Category-specific sequences | 03 (04 owns priority ratios only) |
| Calm ending | 03 |
| Anti-clone, anti-repetition | 08 |
| Input required fields | 07 |
| Final reject gate | 07 (RULE-7014) |
| Memory threshold and synchronization | 09 |
| Execution order | 10 |

## Rules

### RULE-0001

- Priority: Critical
- Type: MUST
- Description: Treat this specification as the single source of truth for all CMMI Blog LLM execution.
- Reason: A single canonical specification prevents document drift and duplicated instructions.
- Dependencies: None
- Override: None

### RULE-0002

- Priority: Critical
- Type: MUST
- Description: Apply the Global Conflict Hierarchy in this fixed order: Naturalness > Authenticity > Verified Human Experience > Trust > Readability > SEO > Structure.
- Reason: Source documents repeatedly establish natural, believable writing as more important than optimization or rigid structure.
- Dependencies: RULE-0001
- Override: Overrides every lower-priority module rule when conflict exists.

### RULE-0003

- Priority: Critical
- Type: MUST
- Description: Merge semantically identical rules into one canonical rule under a single owning module.
- Reason: Duplicate instructions reduce deterministic execution and increase conflict risk.
- Dependencies: RULE-0001
- Override: None

### RULE-0004

- Priority: Critical
- Type: MUST
- Description: Use each Rule ID as the stable reference for dependencies, validation, indexing, and conflict resolution.
- Reason: Stable IDs make the specification machine-readable and auditable.
- Dependencies: RULE-0001
- Override: None

### RULE-0005

- Priority: Critical
- Type: MUST
- Description: Execute modules in the order defined by RULE-10001 through RULE-10011.
- Reason: Deterministic execution requires fixed sequencing from validation to output.
- Dependencies: RULE-0001
- Override: None

### RULE-0006

- Priority: Critical
- Type: NEVER
- Description: Never satisfy SEO, campaign, structure, or keyword requirements by reducing authenticity, naturalness, or verified human experience.
- Reason: The blog must feel personally written after a real experience, not optimized or sponsored.
- Dependencies: RULE-0002
- Override: Overrides all SEO, keyword, and campaign requirements.

### RULE-0007

- Priority: Critical
- Type: MUST
- Description: Defer fact classification to RULE-7008. Every input fact MUST be classified as confirmed, likely, or unknown before use.
- Reason: Fact classification is owned by the Validation Engine. Master Spec only enforces the requirement.
- Dependencies: RULE-0001
- Override: Unknown information MUST be omitted or clarified per RULE-7004.

### RULE-0008

- Priority: High
- Type: MUST
- Description: Maintain strict module boundaries. Identity, validation, reasoning, framework, writing, voice, negative rules, memory, and pipeline each own a disjoint concern.
- Reason: Module boundaries prevent duplicated rules and make rule ownership explicit.
- Dependencies: RULE-0001, RULE-0003
- Override: None

### RULE-0009

- Priority: Critical
- Type: MUST
- Description: Approve final output only when it feels believable, personally observed, and recognizably written by the CMMI Blog author. Enforcement is delegated to RULE-7014.
- Reason: The final objective is believable authorship, not impressive or perfect prose.
- Dependencies: RULE-0001
- Override: Failed believability requires rewrite before output.

### RULE-0010

- Priority: High
- Type: NEVER
- Description: Never optimize every sentence, paragraph, or structure into perfect uniformity.
- Reason: Small natural imperfections increase authenticity and reduce AI-like output.
- Dependencies: RULE-0002
- Override: Overrides formatting symmetry and rigid template consistency.

### RULE-0011

- Priority: High
- Type: MUST
- Description: Source PDFs under `/source` are immutable. Refactor and merge only inside `/specification`.
- Reason: Source preservation guarantees traceability between canonical rules and their original normative text.
- Dependencies: RULE-0001
- Override: None

### RULE-0012

- Priority: High
- Type: NEVER
- Description: Never invent rules that have no source in `/source/*.pdf` or no explicit user instruction.
- Reason: Invented rules pollute the specification and reduce determinism.
- Dependencies: RULE-0001, RULE-0011
- Override: None

### RULE-0013

- Priority: High
- Type: MUST
- Description: Every module file MUST begin with the standard YAML front matter declaring `document_id`, `spec_version`, `status`, `role`, `rule_range`, `depends_on`, and `execution_position`.
- Reason: Machine-readable metadata enables deterministic loading and dependency validation.
- Dependencies: RULE-0001
- Override: None

### RULE-0014

- Priority: High
- Type: MUST
- Description: Dependencies declared in any rule MUST point to existing Rule IDs in modules with equal or earlier `execution_position`.
- Reason: One-direction dependency graph prevents circular reasoning and guarantees deterministic resolution order.
- Dependencies: RULE-0004, RULE-0013
- Override: None

### RULE-0015

- Priority: Critical
- Type: NEVER
- Description: Never produce output before all pipeline stages defined in [10_EXECUTION_PIPELINE.md](10_EXECUTION_PIPELINE.md) have passed. Enforcement is delegated to RULE-10010.
- Reason: Output is the terminal stage of the deterministic pipeline; skipping any stage invalidates the result.
- Dependencies: RULE-0005
- Override: None
