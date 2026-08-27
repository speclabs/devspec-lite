# Developer workflow routes

Use the smallest route that preserves a durable, reviewable record. Generated `devspec/` files are the source of truth; chat history is only supporting context.

## 1. Establish project foundation

![Foundation routes](assets/foundation-routes.svg)

- New repository: start with `devspec.projectcontext`.
- Existing repository: run `devspec.extract` first so later foundation artifacts use observed evidence.
- Continue with `techstack`, `codebase-structure`, `coding-standards`, and `rules`.

## 2. Deliver a change

![Delivery routes](assets/delivery-routes.svg)

Use `devspec.quickfix` only when the request is one localized enhancement or bug fix with one primary scope. Examples: a UI copy correction, focused test adjustment, or local configuration fix.

Use the work-item route for public contracts, data migrations, authentication/security work, breaking changes, unresolved risk, or multiple concerns. Grooming is optional; use it when the story has material ambiguity, risk, or incomplete acceptance criteria. `clarify` asks one interactive blocker question, records the decision, and resumes the originating stage.

## 3. Install and maintain the framework

![Install and maintenance flow](assets/maintenance-flow.svg)

`init` is idempotent for unchanged managed files. It will not overwrite a changed contract or wrapper. Use `doctor` before and after an upgrade, manual copy, or profile addition. There is no separate `sync` command: validate, rerun `init` with the same profile, then validate again.

## Examples

| Situation | Route |
|---|---|
| New service repository | `projectcontext → techstack → codebase-structure → coding-standards → rules` |
| Existing service with unknown conventions | `extract → foundation route` |
| Correct a known empty-state label | `quickfix` with `UI` scope |
| Add a customer-export API and authorization | `story → grooming → finalize → tasks → implement → review` |
| A requirement is blocked by a data-retention decision | `clarify`, then resume the saved stage |
| Add a related requirement after finalization | `changerequest → finalize → tasks → implement → review` |
