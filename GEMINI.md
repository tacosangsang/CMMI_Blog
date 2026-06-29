---
document_id: GEMINI
title: Gemini Compatibility Instructions
spec_version: 3.0
status: compatibility
---

# GEMINI.md

## Purpose

Maintain compatibility with Google Gemini while executing the CMMI Blog AI Specification. Architecture is identical to [AGENTS.md](AGENTS.md); only the platform-specific entry differs.

## Loading Order

1. Read [AGENTS.md](AGENTS.md).
2. Read [00_MASTER_SPEC.md](specification/00_MASTER_SPEC.md).
3. Read [11_RULE_INDEX.md](specification/11_RULE_INDEX.md).
4. Resolve any required module by Rule ID range (see Rule Index).

## Execution

Follow [10_EXECUTION_PIPELINE.md](specification/10_EXECUTION_PIPELINE.md). Pipeline stages 0–10 are mandatory; no stage may be skipped (RULE-10010).

## Conflict Resolution

Single authority: RULE-0002.

Naturalness > Authenticity > Verified Human Experience > Trust > Readability > SEO > Structure.

## Source Immutability

`/source/*.pdf` is read-only (RULE-0011). Never modify.

## Rule Format

Identical to [AGENTS.md](AGENTS.md) Rule Format section. See [RULE_AUTHORING_GUIDE.md](RULE_AUTHORING_GUIDE.md).

## Output Standard

- YAML front matter on every module (RULE-0013).
- Stable Rule IDs (RULE-0004).
- Cross-references by Rule ID only.
- One-direction dependency graph (RULE-0014).
- Machine-readable Markdown.

## Quality Gate

Final reject authority is RULE-7014. Failure rewinds to earliest failed module (RULE-7015).
