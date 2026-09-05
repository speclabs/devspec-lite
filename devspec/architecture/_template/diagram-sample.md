# Diagram Sample

Use this compact worked example as a pattern. Replace every value with repository evidence; queue state belongs only in artifact-queue.md.

## Brief

| Field | Example |
|---|---|
| ID | DIA-001 |
| Type | Process flow |
| Subject | Customer request routing |
| Outputs | SVG by default; HTML only when a presentation shell is requested |
| Evidence | quickfix and story contracts; observed routing rule |
| Confidence | observed |

## Why this type

A process flow makes the one routing decision, its two outcomes, and the durable record visible without inventing system behavior.

## Queue row

| ID | Scope | Type | Subject | Output | Evidence | Duplicate check | Status | Next |
|---|---|---|---|---|---|---|---|---|
| DIA-001 | workflow | Process flow | customer-request-routing | `devspec/architecture/diagrams/dia-001-customer-request-routing.svg` | contracts above | no existing diagram covers this subject | complete | index in overview |

## Completion

Validate SVG XML, link the completed output in overview.md, and keep uncertainty in the work item or decisions file.
