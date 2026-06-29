---
document_id: 04_FRAMEWORK_ENGINE
title: Framework Engine
spec_version: 3.0
status: canonical
role: review_classification_and_structure
rule_range: RULE-4001..RULE-4099
depends_on:
  - 00_MASTER_SPEC
  - 07_VALIDATION_ENGINE
execution_position: 3
---

# Framework Engine

## Purpose

Classify the review category and select one dominant framework before writing.

## Rules

### RULE-4001

- Priority: Critical
- Type: MUST
- Description: Select exactly one primary review category before writing.
- Reason: One primary category prevents mixed frameworks and generic structure.
- Dependencies: RULE-7007
- Override: Use secondary categories only as supporting context.

### RULE-4002

- Priority: High
- Type: MUST
- Description: Apply the category framework as structure guidance, not as a rigid template.
- Reason: Frameworks improve determinism, but naturalness remains higher priority.
- Dependencies: RULE-0002, RULE-4001
- Override: Natural flow may modify section order.

### RULE-4003

- Priority: High
- Type: MUST
- Description: For Restaurant, focus on food experience with priority Food > Experience > Space and ratio guidance Food 50%, Space 20%, Service 10%, Personal Story 20%.
- Reason: Restaurant reader value primarily comes from food experience.
- Dependencies: RULE-4001, RULE-3015
- Override: Specific user-provided core experience may shift emphasis without changing primary category.

### RULE-4004

- Priority: High
- Type: MUST
- Description: For Cafe, focus on atmosphere with priority Atmosphere > Experience > Beverage and ratio guidance Atmosphere 40%, Drink 25%, Dessert 15%, Personal Story 20%.
- Reason: Cafe reader value often depends on mood and time spent.
- Dependencies: RULE-4001, RULE-3014
- Override: Specific user-provided core experience may shift emphasis.

### RULE-4005

- Priority: High
- Type: MUST
- Description: For Product, focus on usage with priority Usage > Change > Opinion and ratio guidance Usage 60%, Features 20%, Opinion 20%.
- Reason: Product reviews are useful when based on actual use rather than features alone.
- Dependencies: RULE-4001, RULE-3016
- Override: Unused product features must remain unclaimed.

### RULE-4006

- Priority: High
- Type: MUST
- Description: For Beauty, focus on process with priority Experience > Process > Result and ratio guidance Process 45%, Result 35%, Opinion 20%.
- Reason: Beauty reviews must balance procedure experience with cautious result claims.
- Dependencies: RULE-4001, RULE-3017
- Override: Never exaggerate effectiveness.

### RULE-4007

- Priority: High
- Type: MUST
- Description: For Experience, focus on story with priority Story > Emotion > Information and ratio guidance Story 60%, Information 20%, Opinion 20%.
- Reason: Experience reviews succeed through lived sequence and reflection.
- Dependencies: RULE-4001, RULE-3018
- Override: None

### RULE-4008

- Priority: High
- Type: MUST
- Description: For Travel, focus on journey with priority Journey > Place > Information and ratio guidance Story 40%, Scenery 30%, Information 30%.
- Reason: Travel reviews require movement, place, and practical reader value.
- Dependencies: RULE-4001
- Override: None

### RULE-4009

- Priority: High
- Type: MUST
- Description: For Accommodation, focus on stay experience with sequence reservation, check-in, room, facilities, breakfast, check-out, overall satisfaction.
- Reason: Accommodation readers need a stay timeline.
- Dependencies: RULE-4001
- Override: Omit unavailable stay elements.

### RULE-4010

- Priority: Medium
- Type: SHOULD
- Description: For Popup Store, focus on limited experience with sequence reason for visit, waiting, entrance, space, products, experience, purchase, opinion.
- Reason: Limited-time spaces require time-sensitive experiential structure.
- Dependencies: RULE-4001
- Override: Omit steps that did not occur.

### RULE-4011

- Priority: Medium
- Type: SHOULD
- Description: For Exhibition, focus on emotion with sequence reason, theme, space, favorite section, experience, reflection.
- Reason: Exhibition reviews depend on emotional and spatial response.
- Dependencies: RULE-4001
- Override: None

### RULE-4012

- Priority: Medium
- Type: MAY
- Description: Use Lifestyle or Other only when no defined category accurately fits the input.
- Reason: Broad categories prevent false classification while preserving flexibility.
- Dependencies: RULE-4001, RULE-7007
- Override: Prefer a specific category when evidence supports it.

### RULE-4013

- Priority: Critical
- Type: NEVER
- Description: Never combine unrelated frameworks into one universal article structure.
- Reason: Framework mixing creates bloated and non-deterministic output.
- Dependencies: RULE-2006, RULE-4001
- Override: None

