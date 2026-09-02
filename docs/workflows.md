# Developer workflow routes

Use the smallest route that preserves a durable, reviewable record. Git-tracked canonical `devspec/` artifacts are the source of truth; chat history is only supporting context.

## 1. Establish project foundation

![Foundation routes](assets/foundation-routes.svg)

- New repository: start with `devspec.projectcontext`.
- Existing repository: run `devspec.extract` once. It completes the evidence-backed technical, workflow, rule, and SVG diagram baseline; do not rerun individual foundation or diagram commands afterward.
- New repository: use `projectcontext`, `techstack`, `codebase-structure`, `coding-standards`, `rules`, and `diagram` as input-driven authoring commands.

## 2. Deliver a change

![Delivery routes](assets/delivery-routes.svg)

Use `devspec.quickfix` only when the request is one localized enhancement or bug fix with one primary scope. Examples: a UI copy correction, focused test adjustment, or local configuration fix.

Use the work-item route for public contracts, data migrations, authentication/security work, breaking changes, unresolved risk, or multiple concerns. Grooming is optional; use it when the story has material ambiguity, risk, or incomplete acceptance criteria. `clarify` asks one interactive material blocker question, records the decision, and resumes the originating stage.

A material decision is work-item-local unless it applies beyond that story. At finalization, promote a reusable business or validation decision to `foundation/workflow-rules.md` with a stable rule ID; promote a reusable engineering constraint to `foundation/rules.md`. New stories read only relevant foundation rules and the affected code area, not every historic decision file. Code and tests are the primary enforcement; add a developer comment only for non-obvious rationale and cite the canonical rule ID.

## 3. Install and maintain the framework

![Install and maintenance flow](assets/maintenance-flow.svg)

## Diagram sample

For an evidence-backed architecture or workflow visual, choose a pattern from the [diagram type guide](../devspec/architecture/_template/diagram-types.md), then use the compact [diagram record sample](../devspec/architecture/_template/diagram-sample.md), its standalone [SVG sample](../devspec/architecture/_template/diagram-sample.svg), or its optional [HTML presentation sample](../devspec/architecture/_template/diagram-sample.html).

Assign a stable `DIA-###` ID, keep status in the queue, and add only completed diagram links to the overview index.


`init` is idempotent for unchanged managed files. It will not overwrite a changed contract or wrapper. For CLI-managed repositories, use `doctor` before and after an upgrade or profile addition. Manual-copy updates follow the [manual-copy guide](manual-copy.md). There is no separate `sync` command: validate, rerun `init` with the same profile, then validate again.

## Examples

| Situation | Route |
|---|---|
| New service repository | `projectcontext → techstack → codebase-structure → coding-standards → rules` |
| Existing service with unknown conventions | `extract` — complete baseline extraction |
| Correct a known empty-state label | `quickfix` with `UI` scope |
| Add a customer-export API and authorization | `story → grooming → finalize → tasks → implement → review` |
| A requirement is blocked by a data-retention decision | `clarify`, then resume the saved stage |
| Add a related requirement after finalization | `changerequest → finalize → tasks → implement → review` |
