---
document_id: RULE_AUTHORING_GUIDE
title: Rule Authoring Guide
spec_version: 3.0
status: compatibility
---

# RULE_AUTHORING_GUIDE.md

## Purpose

Define semantics for authoring rules: ID assignment, ownership, type selection, dependencies, override clauses, and merge policy.

For Markdown style see [STYLE_GUIDE.md](STYLE_GUIDE.md).

## When to Add a Rule

Add a rule only when:

1. The behavior is present in `/source/*.pdf` or in an explicit user instruction.
2. No existing rule already captures the same meaning (RULE-0003).
3. The rule belongs to an existing module's ownership (see Module Boundaries in [00_MASTER_SPEC.md](specification/00_MASTER_SPEC.md)).
4. The rule is enforceable at one specific pipeline stage.

If any of the four conditions fails, do not add the rule (RULE-0012).

## Rule ID Assignment

- IDs are stable. Once assigned, never reused or renumbered (RULE-0004).
- Each module owns a fixed range. Pick the lowest unused integer in that range.
- Reserve gaps only when explicitly documented.
- Cross-reference any new ID in [11_RULE_INDEX.md](specification/11_RULE_INDEX.md).

## Required Fields

| Field | Required | Notes |
|---|---|---|
| Rule ID | Yes | `RULE-NNNN` |
| Priority | Yes | Critical, High, Medium, Low |
| Type | Yes | MUST, SHOULD, MAY, NEVER |
| Description | Yes | One sentence. Imperative or declarative. |
| Reason | Yes | One sentence explaining WHY, not WHAT. |
| Dependencies | Yes | Comma-separated Rule IDs, or `None`. |
| Override | Yes | Effect on other rules, or `None`. |
| Example | No | Add only when behavior is non-obvious. |

## Priority Selection

- **Critical** — failure invalidates output. Used for identity, authenticity, validation, final reject gates.
- **High** — failure significantly degrades quality. Used for structure, voice, reasoning.
- **Medium** — failure degrades quality moderately. Used for sequences, story direction, comparisons.
- **Low** — preference only. Rarely used.

## Type Selection

- **MUST** — required, no exception.
- **SHOULD** — required unless an explicit override applies.
- **MAY** — permitted, not required.
- **NEVER** — forbidden, no exception.

A rule MUST NOT mix types in one statement. Split if necessary.

## Dependencies

- Every Rule ID listed in Dependencies MUST exist.
- Every dependency MUST point to a rule whose owning module's `execution_position` is less than or equal to this module's (RULE-0014).
- Master Spec (00) and Global Rules (02) may be referenced from any module.
- Memory Engine (09) may reference any module; nothing references back.
- Self-references within the same module are allowed.

## Override Clause

State the effect explicitly. Examples:

- "Overrides all SEO and keyword requirements."
- "Failed validation triggers RULE-7004."
- "None" if the rule does not override or trigger other behavior.

## Merge Policy

When two rules express the same meaning:

1. Identify the canonical owner per ARCHITECTURE.md Single-Owner Concept Map.
2. Keep the rule in the owning module.
3. Delete the duplicate.
4. Update any references to the deleted rule.
5. Record the merge in [CHANGELOG.md](CHANGELOG.md).

Never silently rename or renumber. Use the changelog and the index.

## Korean Vocabulary Rules

- Preferred vocabulary: owned by RULE-5003.
- Softening words: owned by RULE-5004.
- Forbidden exaggeration: owned by RULE-8003.
- Forbidden overreaction: owned by RULE-8004.
- Forbidden AI-style phrases: owned by RULE-8006.
- Forbidden generic endings: owned by RULE-8008.
- Overuse warnings: owned by RULE-8012.

Do not duplicate Korean expression lists outside these rules.

## Anti-Patterns

Reject any rule that:

- Restates the conflict hierarchy (RULE-0002 is the sole authority).
- Defines a fact-classification scheme outside RULE-7008.
- Defines a category list outside RULE-7007.
- Adds a parallel final-reject gate (only RULE-7014 exists).
- Introduces a circular dependency.
- Contains marketing language, hedging, or filler.
- Has no source in `/source` or user instruction.

## Testing a New Rule

Before committing:

1. Verify Rule ID is unique.
2. Verify all Dependencies exist and point to ≤ execution position.
3. Verify the description is one sentence.
4. Verify the rule is not a duplicate.
5. Update [11_RULE_INDEX.md](specification/11_RULE_INDEX.md).
6. Update [CHANGELOG.md](CHANGELOG.md).
