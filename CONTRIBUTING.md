---
document_id: CONTRIBUTING
title: Contribution Guide
spec_version: 3.0
status: compatibility
---

# CONTRIBUTING.md

## Contribution Workflow

1. Analyze the current state before editing. Read [00_MASTER_SPEC.md](specification/00_MASTER_SPEC.md) and [11_RULE_INDEX.md](specification/11_RULE_INDEX.md) first.
2. Never edit files under `/source` (RULE-0011).
3. Update only under `/specification` or root meta files (`AGENTS.md`, `README.md`, `CLAUDE.md`, `CODEX.md`, `GEMINI.md`, this file).
4. Preserve backward compatibility: never reuse retired Rule IDs (RULE-0004).
5. Keep Rule IDs stable.
6. Update [11_RULE_INDEX.md](specification/11_RULE_INDEX.md) for every added, removed, or renamed rule.
7. Update [CHANGELOG.md](CHANGELOG.md) for every accepted change.
8. Validate dependencies before committing: every `Dependencies` entry MUST point to a Rule whose owning module has equal or earlier `execution_position` (RULE-0014).
9. Never invent rules without source justification (RULE-0012).

## Adding a Rule

1. Locate the correct owning module (see Module Boundaries in [00_MASTER_SPEC.md](specification/00_MASTER_SPEC.md)).
2. Pick the next unused ID in the module's range.
3. Fill all required fields: Rule ID, Priority, Type, Description, Reason, Dependencies, Override, optional Example. See [RULE_AUTHORING_GUIDE.md](RULE_AUTHORING_GUIDE.md).
4. Verify the rule does not duplicate an existing one (RULE-0003).
5. Add the entry to [11_RULE_INDEX.md](specification/11_RULE_INDEX.md).
6. Update the affected module's `rule_range` only if extended.

## Removing a Rule

A rule MAY be removed only when another rule already represents the same meaning. Remove from the owning module, remove from [11_RULE_INDEX.md](specification/11_RULE_INDEX.md), and record in [CHANGELOG.md](CHANGELOG.md).

## Pull Request Checklist

- [ ] No duplicate rules introduced
- [ ] No conflicting priorities introduced
- [ ] Rule IDs unique across the spec
- [ ] YAML front matter valid (`document_id`, `spec_version`, `status`, `role`, `rule_range`, `depends_on`, `execution_position`)
- [ ] All `Dependencies` point to equal or earlier `execution_position` (no cycles)
- [ ] Cross-references updated
- [ ] [11_RULE_INDEX.md](specification/11_RULE_INDEX.md) updated
- [ ] [CHANGELOG.md](CHANGELOG.md) updated
- [ ] Source PDFs unchanged

## Quality Gate

Changes are accepted only if they improve at least one of:

- Determinism
- Maintainability
- LLM parsing accuracy
- Internal consistency
- Source traceability

Changes are rejected if they degrade any of the above without compensating improvement.

## Architecture Reference

For module boundaries, ownership, and pipeline order, see [ARCHITECTURE.md](ARCHITECTURE.md).
