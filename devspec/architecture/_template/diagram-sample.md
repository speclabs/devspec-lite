# Diagram Sample

Use this short worked example as a pattern; replace every value with repository evidence. Queue status belongs only in `artifact-queue.md`.

| Field | Example |
|---|---|
| ID | `DIA-001` |
| Scope | `workflow` |
| Type | `flowchart` |
| Subject | `customer-request-routing` |
| Output | `devspec/architecture/images/dia-001-customer-request-routing.svg` |
| Evidence | `devspec/contracts/devspec.quickfix.md`, `devspec/contracts/devspec.story.md` |
| Confidence | `observed` |

## Queue row

| ID | Scope | Type | Subject | Output | Evidence | Status | Next |
|---|---|---|---|---|---|---|---|
| DIA-001 | workflow | flowchart | customer-request-routing | `images/dia-001-customer-request-routing.svg` | contracts above | complete | index in overview |

## Notes

Keep the SVG standalone and concise. Link it from `overview.md`; record assumptions in the work item or supporting Markdown.
