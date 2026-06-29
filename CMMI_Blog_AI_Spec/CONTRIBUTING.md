---
document_id: CONTRIBUTING
title: Contribution Guide
spec_version: 3.0
status: compatibility
---

# CONTRIBUTING.md

## Contribution Workflow

1. Analyze before editing.
2. Never edit files in /source.
3. Update only /specification.
4. Preserve backward compatibility.
5. Keep Rule IDs stable.
6. Update RULE_INDEX when adding rules.
7. Validate dependencies before committing.

## Pull Request Checklist

- [ ] No duplicate rules
- [ ] No conflicting priorities
- [ ] Rule IDs unique
- [ ] YAML metadata valid
- [ ] Cross references updated
- [ ] Changelog updated

## Quality Gate

Changes are accepted only if they improve:
- Determinism
- Maintainability
- LLM parsing
- Consistency
