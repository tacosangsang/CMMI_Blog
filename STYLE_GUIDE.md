---
document_id: STYLE_GUIDE
title: Specification Style Guide
spec_version: 3.0
status: compatibility
---

# STYLE_GUIDE.md

## Purpose

Define Markdown, prose, and metadata conventions for `/specification` modules and root meta files. Style only; for rule semantics see [RULE_AUTHORING_GUIDE.md](RULE_AUTHORING_GUIDE.md).

## File Conventions

- File names: `NN_NAME.md` under `/specification`. NN is two-digit, zero-padded.
- Root meta files: UPPERCASE, e.g. `AGENTS.md`, `CLAUDE.md`.
- One module per file. No nested directories under `/specification`.
- UTF-8 encoding. LF line endings. Trailing newline.

## YAML Front Matter

Every `/specification` module MUST start with:

```yaml
---
document_id: NN_NAME
title: <Human Title>
spec_version: 3.0
status: canonical | compatibility
role: <single_purpose_kebab_or_snake>
rule_range: RULE-NNNN..RULE-NNNN
depends_on:
  - <document_id>
execution_position: <integer>
---
```

Root meta files MAY use a shorter front matter without `rule_range` or `execution_position`.

## Section Order

1. Front matter
2. `# Title`
3. `## Purpose`
4. `## Source` (canonical modules only)
5. Optional informational sections (`## Categories`, `## Pipeline Stages`, `## Synchronization Scope`, etc.)
6. `## Rules`

## Rule Block Style

Each rule is rendered as:

```markdown
### RULE-NNNN

- Priority: Critical | High | Medium | Low
- Type: MUST | SHOULD | MAY | NEVER
- Description: <one sentence>
- Reason: <one sentence>
- Dependencies: <comma-separated Rule IDs, or `None`>
- Override: <one sentence, or `None`>
- Example: <optional>
```

## Prose Rules

- Active voice.
- Present tense.
- One idea per sentence.
- No filler ("really", "just", "actually", "basically").
- No marketing language.
- No hedging ("might consider", "perhaps").
- Standard tech acronyms allowed (LLM, SEO, API). Do not invent new acronyms.

## Markdown Rules

- ATX-style headings (`#`, `##`, `###`).
- One blank line between blocks.
- Tables use leading and trailing pipes.
- Inline code uses backticks. Block code uses triple backticks with language tag.
- Links use Markdown link syntax: `[label](path)`. Always link to `/specification` or root meta files when referencing them.

## Korean Content

- Korean expressions referenced inside Description or Reason fields are written verbatim, no transliteration.
- Korean vocabulary lists belong to RULE-5003 (preferred) or RULE-8003 / 8004 / 8006 / 8008 / 8012 (forbidden / cautionary). Do not duplicate.

## Cross-References

- Always reference rules by ID: `RULE-NNNN`.
- Always reference modules by file path: `[03_WRITING_ENGINE.md](specification/03_WRITING_ENGINE.md)`.
- Never duplicate rule text in another module; reference the canonical Rule ID instead.

## Forbidden Style

- No emoji (unless the source text already contains one).
- No HTML.
- No footnotes.
- No tables of contents in `/specification` modules; the [11_RULE_INDEX.md](specification/11_RULE_INDEX.md) is the index.
- No prose paragraphs longer than four sentences.

## Lint Targets

The following may be enforced by future tooling:

- Every front matter field present and typed.
- `rule_range` matches actual rule IDs in file.
- Every `Dependencies` ID exists in [11_RULE_INDEX.md](specification/11_RULE_INDEX.md).
- Every dependency points to a module with `execution_position` ≤ this module's.
- No duplicate rule IDs across modules.
