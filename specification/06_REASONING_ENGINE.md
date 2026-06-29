---
document_id: 06_REASONING_ENGINE
title: Reasoning Engine
spec_version: 3.0
status: canonical
role: prewriting_reasoning
rule_range: RULE-6001..RULE-6099
depends_on:
  - 00_MASTER_SPEC
  - 07_VALIDATION_ENGINE
execution_position: 2
---

# Reasoning Engine

## Purpose

Define how the LLM must think before writing. This module creates memory-like understanding from verified user input.

## Rules

### RULE-6001

- Priority: Critical
- Type: MUST
- Description: Reason in this fixed order before writing: experience, observation, emotion, meaning, story, writing.
- Reason: Writing should begin only after the experience feels understood.
- Dependencies: RULE-7001
- Override: Never begin article generation before completing this reasoning order.

### RULE-6002

- Priority: High
- Type: MUST
- Description: Identify why the visit, purchase, stay, or experience happened.
- Reason: Motivation prevents generic openings and supports personal context.
- Dependencies: RULE-7005
- Override: Missing motivation may trigger clarification if critical.

### RULE-6003

- Priority: High
- Type: MUST
- Description: Identify one central experience that all secondary details support.
- Reason: One core experience creates coherence and prevents unfocused writing.
- Dependencies: RULE-2002
- Override: Competing themes must be demoted or clarified.

### RULE-6004

- Priority: High
- Type: MUST
- Description: Determine natural emotional flow from beginning, expectation, experience, reflection, to conclusion.
- Reason: Emotional progression makes writing feel lived rather than static.
- Dependencies: RULE-5002
- Override: Remove constant excitement.

### RULE-6005

- Priority: High
- Type: MUST
- Description: Select only memorable moments worth detailing and ignore routine actions unless needed for context.
- Reason: Detail should support story and reader value.
- Dependencies: RULE-2003
- Override: None

### RULE-6006

- Priority: Medium
- Type: SHOULD
- Description: Choose one story direction such as discovery, comparison, challenge, surprise, comfort, relaxation, or improvement.
- Reason: Story direction creates internal coherence.
- Dependencies: RULE-6003
- Override: Do not force a named direction if the experience is straightforward.

### RULE-6007

- Priority: High
- Type: MUST
- Description: Determine the dominant writing focus from category and experience instead of dividing focus equally.
- Reason: Equal coverage makes reviews generic and unfocused.
- Dependencies: RULE-4002, RULE-6003
- Override: Category priority controls default focus.

### RULE-6008

- Priority: High
- Type: MUST
- Description: Classify information as essential, useful, optional, or unnecessary before writing.
- Reason: Information filtering prevents bloated and official-description-like articles.
- Dependencies: RULE-7008, RULE-2003
- Override: Ignore unnecessary facts.

### RULE-6009

- Priority: Critical
- Type: MUST
- Description: Form personal opinion only after experience and observation have been reasoned through.
- Reason: Unsupported opinion feels generic and promotional.
- Dependencies: RULE-2001, RULE-3005
- Override: Rewrite opinion-first content.

### RULE-6010

- Priority: High
- Type: MUST
- Description: Treat recommendation as optional and as a result of experience, not a mandatory section.
- Reason: Forced recommendations sound like promotion.
- Dependencies: RULE-3011, RULE-3012
- Override: None

### RULE-6011

- Priority: High
- Type: MUST
- Description: Before every paragraph, check what happened, what was noticed, what surprised the author, what felt different, whether a friend would be told this, whether it sounds like marketing, and whether it uniquely describes this subject.
- Reason: Paragraph-level reasoning filters generic and AI-like content before generation.
- Dependencies: RULE-1009, RULE-8001
- Override: Failed paragraph checks require rewrite.

### RULE-6012

- Priority: High
- Type: MUST
- Description: Remove generic sentences, copied information, marketing language, empty praise, SEO-first writing, unnecessary explanations, and repeated structures before drafting.
- Reason: Pre-generation filtering reduces final validation failures.
- Dependencies: RULE-8001, RULE-8002, RULE-8005
- Override: None

### RULE-6013

- Priority: Critical
- Type: MUST
- Description: Think like a person remembering an experience, not like an AI assembling an article.
- Reason: The master reasoning objective is believable memory reconstruction.
- Dependencies: RULE-1002, RULE-5012
- Override: Overrides template-driven generation.

