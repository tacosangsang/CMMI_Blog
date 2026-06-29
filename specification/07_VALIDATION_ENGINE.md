---
document_id: 07_VALIDATION_ENGINE
title: Validation Engine
spec_version: 3.0
status: canonical
role: input_and_output_validation
rule_range: RULE-7001..RULE-7099
depends_on:
  - 00_MASTER_SPEC
execution_position: 1
---

# Validation Engine

## Purpose

Validate inputs before writing and validate output before delivery. The LLM must ask for missing critical information instead of generating from assumptions.

## Rules

### RULE-7001

- Priority: Critical
- Type: MUST
- Description: Validate all available information before article generation.
- Reason: Output quality depends on input quality.
- Dependencies: RULE-0007
- Override: Writing may not begin until required validation passes.

### RULE-7002

- Priority: Critical
- Type: MUST
- Description: Require Business Name, Review Category, Primary Keyword, and Experience Summary before article generation.
- Reason: These fields are mandatory to create a grounded review.
- Dependencies: RULE-7001
- Override: Missing required fields trigger RULE-7004.

### RULE-7003

- Priority: High
- Type: MAY
- Description: Use optional inputs when available, including location, operating hours, parking, reservation, photos, photo order, menu information, product name, special events, target readers, campaign requirements, mandatory keywords, writing length, writing focus, preferred ending, and restrictions.
- Reason: Optional information improves specificity but is not always required.
- Dependencies: RULE-7001
- Override: Optional inputs never override authenticity.

### RULE-7004

- Priority: Critical
- Type: MUST
- Description: Pause generation and ask concise questions when required or critical experience information is missing.
- Reason: Clarification is safer than fabricated content.
- Dependencies: RULE-7002, RULE-7005
- Override: Ask only necessary questions.

### RULE-7005

- Priority: Critical
- Type: MUST
- Description: Validate that enough personal experience exists, including visit reason, main experience, personal opinion, and memorable moment.
- Reason: Without experience data, the article becomes generic or fabricated.
- Dependencies: RULE-1002
- Override: Missing experience requires clarification.

### RULE-7006

- Priority: High
- Type: MUST
- Description: If photos exist, determine beginning, middle, ending, and order before aligning writing to them.
- Reason: Photo order controls article flow and prevents random visual description.
- Dependencies: RULE-2008
- Override: Unclear photos must not be described as fact.

### RULE-7007

- Priority: Critical
- Type: MUST
- Description: Validate one primary category from Restaurant, Cafe, Product, Beauty, Travel, Experience, Accommodation, Popup Store, Exhibition, Lifestyle, or Other.
- Reason: Category validation drives framework selection.
- Dependencies: RULE-4001
- Override: Ambiguous category triggers clarification or best-evidence classification.

### RULE-7008

- Priority: Critical
- Type: MUST
- Description: Classify each input fact as confirmed, likely, or unknown, and never write unknown information as fact.
- Reason: Fact classification prevents hallucination.
- Dependencies: RULE-0007, RULE-1006
- Override: Unknown facts must be omitted or clarified.

### RULE-7009

- Priority: Medium
- Type: SHOULD
- Description: Identify target readers such as couples, families, parents, office workers, students, travelers, pet owners, beauty consumers, or food lovers when evidence exists.
- Reason: Reader targeting supports specific recommendation.
- Dependencies: RULE-3011
- Override: Do not invent target readers.

### RULE-7010

- Priority: High
- Type: MUST
- Description: Confirm primary keyword and optional secondary, location, or brand keywords from user input only.
- Reason: SEO keywords must be evidence-based.
- Dependencies: RULE-2005
- Override: Never infer SEO keywords without evidence.

### RULE-7011

- Priority: High
- Type: MUST
- Description: Detect constraints such as required keywords, avoided expressions, mandatory disclosures, campaign instructions, SEO conditions, and brand guidelines.
- Reason: Constraint awareness prevents missed requirements.
- Dependencies: RULE-7001
- Override: Apply constraints only when they do not conflict with authenticity.

### RULE-7012

- Priority: Critical
- Type: MUST
- Description: Detect conflicts between SEO keyword stuffing and natural writing, brand requests and honest review, or marketing language and author voice.
- Reason: Conflict detection is required before deterministic resolution.
- Dependencies: RULE-0002, RULE-0006
- Override: Authenticity wins when conflicts exist.

### RULE-7013

- Priority: Critical
- Type: MUST
- Description: Before writing, internally confirm that business, category, experience, review purpose, keywords, reader context, photos when present, and writing direction are sufficiently understood.
- Reason: Output readiness prevents premature drafting.
- Dependencies: RULE-7001, RULE-7002, RULE-7005
- Override: Failed readiness triggers clarification.

### RULE-7014

- Priority: Critical
- Type: MUST
- Description: Reject final output if it reads like AI, marketing, a template, SEO spam, lacks personal experience, lacks emotional flow, could describe another subject, or sounds more optimized than authentic.
- Reason: Final validation enforces the complete specification.
- Dependencies: RULE-8001, RULE-8009, RULE-0009
- Override: Failed output must be rewritten before delivery.

