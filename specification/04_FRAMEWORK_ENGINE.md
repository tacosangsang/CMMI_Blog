---
document_id: 04_FRAMEWORK_ENGINE
title: Framework Engine
spec_version: 3.0
status: canonical
role: category_classification_and_priority
rule_range: RULE-4001..RULE-4099
depends_on:
  - 00_MASTER_SPEC
  - 02_GLOBAL_RULES
  - 07_VALIDATION_ENGINE
execution_position: 3
---

# Framework Engine

## Purpose

Classify the review into exactly one primary category and select the matching framework before drafting. This module owns category definitions, category-level priority orders, and category-level writing-ratio guidance. It does NOT own paragraph-level sensory or feature sequences (see [03_WRITING_ENGINE.md](03_WRITING_ENGINE.md)).

## Categories

Restaurant, Cafe, Product, Beauty, Travel, Experience, Accommodation, Popup Store, Exhibition, Lifestyle, Other.

The category list is canonical here. Other modules MUST reference RULE-4001 rather than redefining the list.

## Source

Canonical merge of `04_CMMI Blog Review Framework.pdf`. Category naming aligned with [07_VALIDATION_ENGINE.md](07_VALIDATION_ENGINE.md) (RULE-7007).

## Rules

### RULE-4001

- Priority: Critical
- Type: MUST
- Description: Select exactly one primary review category from Restaurant, Cafe, Product, Beauty, Travel, Experience, Accommodation, Popup Store, Exhibition, Lifestyle, or Other before drafting begins.
- Reason: One primary category prevents mixed frameworks and generic structure.
- Dependencies: RULE-7007
- Override: Secondary categories may be used only as supporting context.

### RULE-4002

- Priority: High
- Type: MUST
- Description: Apply the selected category framework as structural guidance, not as a rigid template. Naturalness MAY adjust the section order.
- Reason: Frameworks improve determinism, but naturalness remains the higher-priority concern per RULE-0002.
- Dependencies: RULE-0002, RULE-4001
- Override: Natural flow may modify section order when the original order would break authenticity.

### RULE-4003

- Priority: High
- Type: MUST
- Description: For Restaurant, the writing focus is food experience. Priority order: Food > Experience > Space. Ratio guidance: Food 50%, Space 20%, Service 10%, Personal Story 20%.
- Reason: Restaurant reader value primarily comes from food experience.
- Dependencies: RULE-4001
- Override: A user-provided dominant experience MAY shift emphasis without changing the primary category.

### RULE-4004

- Priority: High
- Type: MUST
- Description: For Cafe, the writing focus is atmosphere. Priority order: Atmosphere > Experience > Beverage. Ratio guidance: Atmosphere 40%, Drink 25%, Dessert 15%, Personal Story 20%.
- Reason: Cafe reader value depends primarily on mood and time spent.
- Dependencies: RULE-4001
- Override: A user-provided dominant experience MAY shift emphasis.

### RULE-4005

- Priority: High
- Type: MUST
- Description: For Product, the writing focus is actual usage. Priority order: Usage > Change > Opinion. Ratio guidance: Usage 60%, Features 20%, Opinion 20%.
- Reason: Product reviews are useful only when grounded in actual use, not in feature listing.
- Dependencies: RULE-4001
- Override: Unused product features MUST remain unclaimed.

### RULE-4006

- Priority: High
- Type: MUST
- Description: For Beauty, the writing focus is process. Priority order: Experience > Process > Result. Ratio guidance: Process 45%, Result 35%, Opinion 20%.
- Reason: Beauty reviews must balance procedure experience with cautious result claims.
- Dependencies: RULE-4001
- Override: Never exaggerate effectiveness or claim unverified long-term results.

### RULE-4007

- Priority: High
- Type: MUST
- Description: For Experience, the writing focus is story. Priority order: Story > Emotion > Information. Ratio guidance: Story 60%, Information 20%, Opinion 20%.
- Reason: Experience reviews succeed through lived sequence and reflection.
- Dependencies: RULE-4001
- Override: None

### RULE-4008

- Priority: High
- Type: MUST
- Description: For Travel, the writing focus is journey. Priority order: Journey > Place > Information. Ratio guidance: Story 40%, Scenery 30%, Information 30%.
- Reason: Travel reviews require movement, place, and practical reader value.
- Dependencies: RULE-4001
- Override: None

### RULE-4009

- Priority: High
- Type: MUST
- Description: For Accommodation, the writing focus is stay experience. Priority order: Experience > Room > Service. Macro sequence: reservation, check-in, room, facilities, breakfast, check-out, overall satisfaction.
- Reason: Accommodation readers need a coherent stay timeline.
- Dependencies: RULE-4001
- Override: Omit unavailable stay elements.

### RULE-4010

- Priority: Medium
- Type: SHOULD
- Description: For Popup Store, the writing focus is the limited-time experience. Priority order: Experience > Products. Macro sequence: reason for visit, waiting, entrance, space, products, experience, purchase, opinion.
- Reason: Limited-time spaces require time-sensitive experiential structure.
- Dependencies: RULE-4001
- Override: Omit steps that did not occur.

### RULE-4011

- Priority: Medium
- Type: SHOULD
- Description: For Exhibition, the writing focus is emotion. Priority order: Emotion > Story. Macro sequence: reason, theme, space, favorite section, experience, reflection.
- Reason: Exhibition reviews depend on emotional and spatial response.
- Dependencies: RULE-4001
- Override: None

### RULE-4012

- Priority: Medium
- Type: MAY
- Description: Use Lifestyle or Other only when no defined category accurately fits the input. Prefer a specific category when evidence supports it.
- Reason: Broad categories preserve flexibility while preventing false classification.
- Dependencies: RULE-4001, RULE-7007
- Override: Specific evidence overrides broad classification.

### RULE-4013

- Priority: Critical
- Type: NEVER
- Description: Never combine unrelated category frameworks into one universal article structure.
- Reason: Framework mixing creates bloated and non-deterministic output.
- Dependencies: RULE-2006, RULE-4001
- Override: None
