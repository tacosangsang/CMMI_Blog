---
document_id: 11_RULE_INDEX
title: Rule Index
spec_version: 3.0
status: canonical
role: rule_lookup
rule_range: all
depends_on:
  - 00_MASTER_SPEC
  - 01_IDENTITY
  - 02_GLOBAL_RULES
  - 03_WRITING_ENGINE
  - 04_FRAMEWORK_ENGINE
  - 05_VOICE_ENGINE
  - 06_REASONING_ENGINE
  - 07_VALIDATION_ENGINE
  - 08_NEGATIVE_RULES
  - 09_MEMORY_ENGINE
  - 10_EXECUTION_PIPELINE
execution_position: 11
---

# Rule Index

## ID Ranges

| Range | Module | File |
|---|---|---|
| RULE-0001..RULE-0099 | Master | [00_MASTER_SPEC.md](00_MASTER_SPEC.md) |
| RULE-1001..RULE-1099 | Identity | [01_IDENTITY.md](01_IDENTITY.md) |
| RULE-2001..RULE-2099 | Global Rules | [02_GLOBAL_RULES.md](02_GLOBAL_RULES.md) |
| RULE-3001..RULE-3099 | Writing Engine | [03_WRITING_ENGINE.md](03_WRITING_ENGINE.md) |
| RULE-4001..RULE-4099 | Framework Engine | [04_FRAMEWORK_ENGINE.md](04_FRAMEWORK_ENGINE.md) |
| RULE-5001..RULE-5099 | Voice Engine | [05_VOICE_ENGINE.md](05_VOICE_ENGINE.md) |
| RULE-6001..RULE-6099 | Reasoning Engine | [06_REASONING_ENGINE.md](06_REASONING_ENGINE.md) |
| RULE-7001..RULE-7099 | Validation Engine | [07_VALIDATION_ENGINE.md](07_VALIDATION_ENGINE.md) |
| RULE-8001..RULE-8099 | Negative Rules | [08_NEGATIVE_RULES.md](08_NEGATIVE_RULES.md) |
| RULE-9001..RULE-9099 | Memory Engine | [09_MEMORY_ENGINE.md](09_MEMORY_ENGINE.md) |
| RULE-10001..RULE-10099 | Execution Pipeline | [10_EXECUTION_PIPELINE.md](10_EXECUTION_PIPELINE.md) |

## Module Execution Positions

| Position | Module |
|---|---|
| 0 | Master, Global Rules |
| 1 | Validation Engine |
| 2 | Reasoning Engine |
| 3 | Framework Engine |
| 4 | Identity |
| 5 | Writing Engine |
| 6 | Voice Engine |
| 7 | Negative Rules |
| 9 | Execution Pipeline |
| 10 | Memory Engine |
| 11 | Rule Index |

## Rule Lookup

### Master (00)

| Rule ID | Type | Short Name |
|---|---|---|
| RULE-0001 | MUST | Single source of truth |
| RULE-0002 | MUST | Global conflict hierarchy |
| RULE-0003 | MUST | Semantic merge |
| RULE-0004 | MUST | Stable Rule IDs |
| RULE-0005 | MUST | Module execution order |
| RULE-0006 | NEVER | Authenticity over optimization |
| RULE-0007 | MUST | Fact classification delegation |
| RULE-0008 | MUST | Module boundaries |
| RULE-0009 | MUST | Believable authorship gate |
| RULE-0010 | NEVER | Imperfection over uniformity |
| RULE-0011 | MUST | Source PDF immutability |
| RULE-0012 | NEVER | No invented rules |
| RULE-0013 | MUST | YAML front matter required |
| RULE-0014 | MUST | One-direction dependency graph |
| RULE-0015 | NEVER | Output gate enforcement |

### Identity (01)

| Rule ID | Type | Short Name |
|---|---|---|
| RULE-1001 | MUST | Exclusive author |
| RULE-1002 | MUST | Real experience feel |
| RULE-1003 | MUST | Experience before information |
| RULE-1004 | MUST | Neighbor relationship |
| RULE-1005 | MUST | Author personality |
| RULE-1006 | NEVER | No fabricated authority |
| RULE-1007 | MUST | Honest balance |
| RULE-1008 | MUST | Reader decision freedom |
| RULE-1009 | SHOULD | Subject-specific writing |
| RULE-1010 | MUST | Believable over perfect |
| RULE-1011 | MUST | Observe before evaluate |
| RULE-1012 | MUST | Friend-question decision rule |
| RULE-1013 | NEVER | No teaching or selling posture |

### Global Rules (02)

| Rule ID | Type | Short Name |
|---|---|---|
| RULE-2001 | MUST | Experience-first order |
| RULE-2002 | MUST | One dominant experience |
| RULE-2003 | MUST | Useful memorable details |
| RULE-2004 | MUST | Specific observations |
| RULE-2005 | MUST | Natural keyword distribution |
| RULE-2006 | NEVER | No universal template |
| RULE-2007 | SHOULD | Helpful comparisons |
| RULE-2008 | MUST | Photo order alignment |
| RULE-2009 | NEVER | No unseen photo description |
| RULE-2010 | MUST | Reader value gate |
| RULE-2011 | MUST | Honest balance |
| RULE-2012 | NEVER | No generic portability |
| RULE-2013 | MUST | Allow natural imperfections |
| RULE-2014 | NEVER | Sub-language priority |

### Writing Engine (03)

| Rule ID | Type | Short Name |
|---|---|---|
| RULE-3001 | SHOULD | Default article flow |
| RULE-3002 | MUST | Empathy before business |
| RULE-3003 | NEVER | No repeated introductions |
| RULE-3004 | SHOULD | Useful basic information |
| RULE-3005 | MUST | Local review sequence |
| RULE-3006 | SHOULD | Sensory sequence |
| RULE-3007 | MUST | Sentence rhythm variation |
| RULE-3008 | MUST | Paragraph length |
| RULE-3009 | MUST | Photo-paragraph rhythm |
| RULE-3010 | MUST | Specific recommendations |
| RULE-3011 | MAY | Optional recommendation |
| RULE-3012 | SHOULD | Calm ending |
| RULE-3013 | SHOULD | Space sequence |
| RULE-3014 | SHOULD | Food sequence |
| RULE-3015 | SHOULD | Product sequence |
| RULE-3016 | SHOULD | Beauty sequence |
| RULE-3017 | SHOULD | Experience sequence |
| RULE-3018 | NEVER | No invented concrete details |
| RULE-3019 | MUST | Naver mobile line breaks |

### Framework Engine (04)

| Rule ID | Type | Short Name |
|---|---|---|
| RULE-4001 | MUST | One primary category |
| RULE-4002 | MUST | Framework as guidance |
| RULE-4003 | MUST | Restaurant framework |
| RULE-4004 | MUST | Cafe framework |
| RULE-4005 | MUST | Product framework |
| RULE-4006 | MUST | Beauty framework |
| RULE-4007 | MUST | Experience framework |
| RULE-4008 | MUST | Travel framework |
| RULE-4009 | MUST | Accommodation framework |
| RULE-4010 | SHOULD | Popup framework |
| RULE-4011 | SHOULD | Exhibition framework |
| RULE-4012 | MAY | Lifestyle or Other |
| RULE-4013 | NEVER | No mixed frameworks |

### Voice Engine (05)

| Rule ID | Type | Short Name |
|---|---|---|
| RULE-5001 | MUST | Conversational voice |
| RULE-5002 | MUST | Calm emotion ratio |
| RULE-5003 | SHOULD | Preferred vocabulary |
| RULE-5004 | SHOULD | Softening words |
| RULE-5005 | MUST | Subjective opinion |
| RULE-5006 | SHOULD | Comparison phrasing |
| RULE-5007 | MAY | Light reader questions |
| RULE-5008 | MAY | Light humor |
| RULE-5009 | SHOULD | Natural reactions |
| RULE-5010 | MUST | Voice-level observe first |
| RULE-5011 | SHOULD | Soft recommendation phrasing |
| RULE-5012 | MUST | Thinking over word mimicry |
| RULE-5013 | MUST | Positive skew under campaign |

### Reasoning Engine (06)

| Rule ID | Type | Short Name |
|---|---|---|
| RULE-6001 | MUST | Reasoning order |
| RULE-6002 | MUST | Visit motivation |
| RULE-6003 | MUST | Central experience |
| RULE-6004 | MUST | Emotional flow |
| RULE-6005 | MUST | Memorable moments |
| RULE-6006 | SHOULD | Story direction |
| RULE-6007 | MUST | Dominant focus |
| RULE-6008 | MUST | Information classification |
| RULE-6009 | MUST | Paragraph reader value |
| RULE-6010 | MUST | Opinion after experience |
| RULE-6011 | MUST | Recommendation as result |
| RULE-6012 | MUST | Paragraph self-questions |
| RULE-6013 | MUST | Pre-draft filter |
| RULE-6014 | MUST | Memory-like thinking |

### Validation Engine (07)

| Rule ID | Type | Short Name |
|---|---|---|
| RULE-7001 | MUST | Validate first |
| RULE-7002 | MUST | Required fields |
| RULE-7003 | MAY | Optional fields |
| RULE-7004 | MUST | Clarification gate |
| RULE-7005 | MUST | Experience sufficiency |
| RULE-7006 | MUST | Photo validation |
| RULE-7007 | MUST | Category validation (canonical list) |
| RULE-7008 | MUST | Fact classification |
| RULE-7009 | SHOULD | Target reader |
| RULE-7010 | MUST | Keyword confirmation |
| RULE-7011 | MUST | Constraint detection |
| RULE-7012 | MUST | Conflict detection |
| RULE-7013 | MUST | Output readiness |
| RULE-7014 | MUST | Final reject gate |
| RULE-7015 | MUST | Rewind to failed module |
| RULE-7016 | MUST | Traceability scan for fabrication |

### Negative Rules (08)

| Rule ID | Type | Short Name |
|---|---|---|
| RULE-8001 | NEVER | No AI writing |
| RULE-8002 | NEVER | No marketing |
| RULE-8003 | NEVER | No exaggerated praise |
| RULE-8004 | NEVER | No overreaction |
| RULE-8005 | NEVER | No keyword stuffing |
| RULE-8006 | NEVER | No AI-style phrases |
| RULE-8007 | NEVER | No repeated patterns |
| RULE-8008 | NEVER | No generic endings |
| RULE-8009 | NEVER | No generic portability |
| RULE-8010 | NEVER | No official-description paste |
| RULE-8011 | NEVER | No false balance |
| RULE-8012 | SHOULD | Avoid expression overuse |
| RULE-8013 | NEVER | No cloned articles |
| RULE-8014 | MUST | Negative quality gate |
| RULE-8015 | NEVER | No invented backstory |
| RULE-8016 | NEVER | No sponsorship mention in body |

### Memory Engine (09)

| Rule ID | Type | Short Name |
|---|---|---|
| RULE-9001 | MUST | Identity stable, style evolves |
| RULE-9002 | MUST | Update threshold |
| RULE-9003 | MUST | Repeated evidence |
| RULE-9004 | SHOULD | Evolution observation order |
| RULE-9005 | SHOULD | Style tracking targets |
| RULE-9006 | MUST | Stable identity elements |
| RULE-9007 | MAY | Allowed style evolution |
| RULE-9008 | MUST | Change record format |
| RULE-9009 | MUST | Newest consistent style |
| RULE-9010 | NEVER | Rejected memory sources |
| RULE-9011 | MUST | Memory rejection gate |
| RULE-9012 | MUST | Synchronization scope |
| RULE-9013 | MUST | Uncertainty override |

### Execution Pipeline (10)

| Rule ID | Type | Short Name |
|---|---|---|
| RULE-10001 | MUST | Validate inputs |
| RULE-10002 | MUST | Classify category |
| RULE-10003 | MUST | Reason before drafting |
| RULE-10004 | MUST | Apply framework |
| RULE-10005 | MUST | Apply identity |
| RULE-10006 | MUST | Draft article |
| RULE-10007 | MUST | Apply voice |
| RULE-10008 | MUST | Apply negative filter |
| RULE-10009 | MUST | Final validation |
| RULE-10010 | MUST | Output gate |
| RULE-10011 | MUST | Memory maintenance |

## Counts

| Module | Rules |
|---|---|
| 00 Master | 15 |
| 01 Identity | 13 |
| 02 Global Rules | 14 |
| 03 Writing Engine | 19 |
| 04 Framework Engine | 13 |
| 05 Voice Engine | 13 |
| 06 Reasoning Engine | 14 |
| 07 Validation Engine | 16 |
| 08 Negative Rules | 16 |
| 09 Memory Engine | 13 |
| 10 Execution Pipeline | 11 |
| **Total** | **157** |
