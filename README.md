---
architecture: Enterprise
spec_version: 3.0
system: CMMI Blog AI Specification
---

# CMMI Blog AI Specification

## Project Goal

This repository rebuilds the original CMMI Blog writing system into an enterprise-grade AI Specification optimized for Large Language Models.

This is NOT a blog writing guide.

This is NOT prompt engineering.

This repository defines a deterministic execution specification for AI.

---

## Objectives

- Remove duplicated rules.
- Create a Single Source of Truth.
- Improve LLM parsing accuracy.
- Standardize every rule.
- Separate Identity, Writing, Reasoning, Validation and Execution.
- Optimize for GPT, Claude, Gemini and Codex.

---

## Final Output

[00_MASTER_SPEC.md](specification/00_MASTER_SPEC.md)

[01_IDENTITY.md](specification/01_IDENTITY.md)

[02_GLOBAL_RULES.md](specification/02_GLOBAL_RULES.md)

[03_WRITING_ENGINE.md](specification/03_WRITING_ENGINE.md)

[04_FRAMEWORK_ENGINE.md](specification/04_FRAMEWORK_ENGINE.md)

[05_VOICE_ENGINE.md](specification/05_VOICE_ENGINE.md)

[06_REASONING_ENGINE.md](specification/06_REASONING_ENGINE.md)

[07_VALIDATION_ENGINE.md](specification/07_VALIDATION_ENGINE.md)

[08_NEGATIVE_RULES.md](specification/08_NEGATIVE_RULES.md)

[09_MEMORY_ENGINE.md](specification/09_MEMORY_ENGINE.md)

[10_EXECUTION_PIPELINE.md](specification/10_EXECUTION_PIPELINE.md)

[11_RULE_INDEX.md](specification/11_RULE_INDEX.md)

---

## Architecture

The specification is executed in the following order

Input Validation

↓

Category Classification

↓

Reasoning

↓

Framework Selection

↓

Identity Apply

↓

Draft

↓

Voice Tuning

↓

Negative Filter

↓

Final Validation

↓

Output

↓

Memory Maintenance (async)

---

## Rule Format

Every rule must include

Rule ID

Priority

Type

Description

Reason

Dependencies

Override

Example (optional)

---

## Conflict Hierarchy

Single authority: RULE-0002.

Naturalness > Authenticity > Verified Human Experience > Trust > Readability > SEO > Structure.

---

## Golden Rule

Naturalness always overrides optimization.

Authenticity always overrides SEO.

Experience always precedes information.

---

## Meta Documents

[AGENTS.md](AGENTS.md), [CLAUDE.md](CLAUDE.md), [GEMINI.md](GEMINI.md), [CODEX.md](CODEX.md), [CONTRIBUTING.md](CONTRIBUTING.md), [ARCHITECTURE.md](ARCHITECTURE.md), [STYLE_GUIDE.md](STYLE_GUIDE.md), [RULE_AUTHORING_GUIDE.md](RULE_AUTHORING_GUIDE.md), [CHANGELOG.md](CHANGELOG.md), [ROADMAP.md](ROADMAP.md).
