---
document_id: CHANGELOG
title: Specification Changelog
spec_version: 3.0
status: compatibility
---

# CHANGELOG.md

All notable changes to the CMMI Blog AI Specification.

Format follows [Keep a Changelog](https://keepachangelog.com/) conventions. Versions follow `spec_version` semantics: major for breaking pipeline change, minor for canonical rule changes, patch for non-semantic edits.

## [3.0.0] — 2026-06-29

### Added

- `00_MASTER_SPEC` RULE-0011 (source PDF immutability).
- `00_MASTER_SPEC` RULE-0012 (no invented rules).
- `00_MASTER_SPEC` RULE-0013 (YAML front matter required).
- `00_MASTER_SPEC` RULE-0014 (one-direction dependency graph).
- `00_MASTER_SPEC` RULE-0015 (output gate enforcement).
- `01_IDENTITY` RULE-1011 (observe before evaluate, identity-level stance).
- `01_IDENTITY` RULE-1012 (friend-question decision rule).
- `01_IDENTITY` RULE-1013 (no teaching or selling posture).
- `02_GLOBAL_RULES` RULE-2010 (reader-value gate).
- `02_GLOBAL_RULES` RULE-2011 (honest balance, cross-module).
- `02_GLOBAL_RULES` RULE-2012 (no generic portability, canonical owner).
- `02_GLOBAL_RULES` RULE-2013 (allow natural imperfections).
- `02_GLOBAL_RULES` RULE-2014 (sub-language priority).
- `05_VOICE_ENGINE` RULE-5009 (natural reactions).
- `05_VOICE_ENGINE` RULE-5010 (voice-level observe-before-evaluate).
- `06_REASONING_ENGINE` RULE-6014 (memory-like thinking).
- `07_VALIDATION_ENGINE` RULE-7015 (rewind to earliest failed module on rejection).
- `09_MEMORY_ENGINE` RULE-9013 (uncertainty override of update threshold).
- Root meta files: `ARCHITECTURE.md`, `STYLE_GUIDE.md`, `RULE_AUTHORING_GUIDE.md`, `CHANGELOG.md`, `ROADMAP.md`, `GEMINI.md`, `CODEX.md`.

### Changed

- Global Conflict Hierarchy now explicitly includes "Verified Human Experience" (RULE-0002). Reconciled across `AGENTS.md`, `README.md`, `CLAUDE.md`, `GEMINI.md`, `CODEX.md`.
- Category list canonical owner moved to RULE-7007. Framework Engine references it.
- Category-specific writing sequences (3013–3017) reclassified from MUST to SHOULD to align with RULE-4002 (framework as guidance, not template).
- Default article flow (RULE-3001) reordered to experience-first.
- Emotional intensity ratio standardized to calm 70 / excitement 20 / surprise 10 (RULE-5002). Conflicting 40 / 60 ratio removed.
- Category name `HOTEL` renamed to `Accommodation` across all modules.
- Final reject gate consolidated under RULE-7014. RULE-8014 now invokes RULE-7014 instead of defining a parallel gate.
- Memory synchronization scope expanded to include modules 04, 06, 07 (in addition to 01, 03, 05, 08).
- All Rule `Dependencies` re-resolved to enforce one-direction dependency graph (RULE-0014). All 27 prior bidirectional pairs broken.
- Identity rule deps no longer point forward to Voice, Negative, or Writing.
- Validation module now owns the canonical category list (RULE-7007).
- `02_WRITING_RULE` Basic Information section converted to RULE-3004 (useful + experience-linked) plus RULE-8010 (no official-description paste).
- `08_NEGATIVE_RULES` 8014 reformulated as a forward-to-7014 scan rather than a duplicate gate.
- `09_MEMORY_ENGINE` 9002 vs 9003 mutual dependency broken; 9003 now depends on 0003 only.
- `README.md` regenerated to reflect new pipeline and architecture.
- `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md` updated to the v3.0 architecture.

### Removed

- `01_IDENTITY` RULE-1001..1010 prior dependency cycles to 5xxx, 8xxx removed.
- `03_WRITING_ENGINE` RULE-3005 (experience-before-evaluation) removed as duplicate of RULE-2001.
- `02_GLOBAL_RULES` Dependencies pointing to forward modules removed.
- `04_FRAMEWORK_ENGINE` Dependencies pointing to forward sequences removed.
- `05_VOICE_ENGINE` RULE-5007 (sentence rhythm) and RULE-5008 (paragraph rhythm) moved into 03 ownership.
- `07_MASTER_PROMPT` document-priority list deprecated; replaced by RULE-0002 conflict hierarchy.

### Fixed

- CF1 — Conflict hierarchy mismatch across 5 documents. Single source: RULE-0002.
- CF2 — Emotional intensity duplicate ratios reconciled.
- CF3 — Default article flow now experience-first.
- CF4 — Framework rigidity tension resolved: 4002 MUST guidance + 3013–3017 SHOULD.
- CF5 — `Accommodation` naming unified.
- CF6 — Document priority vs pipeline order separated cleanly.
- CF7 — Identity stage added to pipeline diagram explicitly.
- CF8 — Food sequence single-owner = RULE-3014.
- CF9 — Recommendation rules unified to SHOULD / MAY.
- CF10 — Basic Information vs no-official-paste tension resolved by ownership split.
- CF11 — Required input fields canonical: RULE-7002.
- CF12 — Memory update threshold + uncertainty override reconciled via RULE-9013.
- CF13 — Memory synchronization scope expanded.
- CF14 — Pipeline RULE-10001 now explicitly depends on RULE-7001.
- CF15 — Pipeline diagram labels Input Validation vs Final Validation distinctly.

### Counts

| Module | Rules |
|---|---|
| 00 Master | 15 |
| 01 Identity | 13 |
| 02 Global Rules | 14 |
| 03 Writing Engine | 17 |
| 04 Framework Engine | 13 |
| 05 Voice Engine | 12 |
| 06 Reasoning Engine | 14 |
| 07 Validation Engine | 15 |
| 08 Negative Rules | 14 |
| 09 Memory Engine | 13 |
| 10 Execution Pipeline | 11 |
| **Total** | **151** |

## [2.0.0] — pre-3.0 baseline

Initial canonical merge of `/source/*.pdf` into `/specification`. 138 rules across 11 modules. Bidirectional dependencies and duplicate clusters present (see `ARCHITECTURE.md` retrospective).
