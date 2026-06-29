---
document_id: ROADMAP
title: Specification Roadmap
spec_version: 3.0
status: compatibility
---

# ROADMAP.md

## Purpose

Track planned work on the CMMI Blog AI Specification. Items are not commitments; priorities may shift.

## v3.1 — Tooling & Validation

- Add a lint script that verifies front matter shape on every `/specification/*.md`.
- Add a dependency-graph validator that fails CI on any cycle or forward dependency.
- Add a duplicate-rule scanner that flags semantically equivalent rule pairs.
- Add a Rule ID uniqueness checker across the entire `/specification` tree.
- Generate [11_RULE_INDEX.md](specification/11_RULE_INDEX.md) automatically from module front matter and rule headings.

## v3.2 — Source Traceability

- Add `source_pdf` and `source_page` fields to every canonical rule's optional metadata block.
- Add a back-link from each rule to its originating `/source/*.pdf` page range.
- Add a coverage report: every normative statement in `/source` MUST map to at least one Rule ID.

## v3.3 — Memory Evolution Tooling

- Implement RULE-9008 change record format as a structured `memory/` directory with one file per accepted change.
- Add a synchronization runner that propagates accepted memory updates to the modules listed in RULE-9012.
- Add an uncertainty-gate prompt template enforcing RULE-9013.

## v3.4 — Multi-Platform Compatibility Tests

- Add compatibility test fixtures for Claude, Gemini, and Codex entry points.
- Verify each platform produces identical pipeline behavior given the same input.
- Document any platform-specific entry-point quirks in the respective root meta file ([CLAUDE.md](CLAUDE.md), [GEMINI.md](GEMINI.md), [CODEX.md](CODEX.md)).

## v3.5 — Output Format Hardening

- Define canonical output schema (article object) with required fields.
- Add a final-output JSON schema validator after RULE-10010.
- Reject any output that fails schema validation in addition to RULE-7014.

## v4.0 — Breaking Pipeline Refactor (tentative)

- Promote Validation re-entry to a separate module file rather than reusing 07 at two pipeline stages.
- Split Global Rules into thematic sub-modules if the count exceeds ~30.
- Introduce explicit module-level pre/post-condition rules.
- Backward-incompatible changes to `depends_on` semantics MAY be considered.

## Out of Scope

- Editing `/source/*.pdf` (RULE-0011).
- Inventing rules without source justification (RULE-0012).
- Redefining the Global Conflict Hierarchy outside RULE-0002.
- Adding a parallel final-reject gate.

## How to Propose a Roadmap Item

1. Open a PR that edits this file under the next planned version section.
2. Reference any prerequisite Rule IDs.
3. Cross-link to a CHANGELOG draft entry if the change is concrete.
