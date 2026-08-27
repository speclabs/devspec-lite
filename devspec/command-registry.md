# Command Registry

| Command | Purpose | Next route |
|---|---|---|
| `devspec.extract` | Backfill concise foundation evidence from an existing repository. | `projectcontext` |
| `devspec.projectcontext` | Capture product purpose, users, outcomes, and scope boundaries. | `techstack` |
| `devspec.techstack` | Capture evidence-backed runtime, frameworks, data, tooling, and delivery constraints. | `codebase-structure` |
| `devspec.codebase-structure` | Capture owned source roots, module boundaries, integrations, and repository access. | `coding-standards` |
| `devspec.coding-standards` | Capture short, evidence-backed conventions and anti-patterns. | `rules` |
| `devspec.rules` | Capture non-negotiable engineering, security, compliance, delivery, and accessibility rules. | `story` |
| `devspec.story` | Create one concise work-item intake from a request or provider reference. | `grooming-or-finalize` |
| `devspec.grooming` | Make one draft story buildable through scoped review and targeted questions. | `clarify-or-finalize` |
| `devspec.clarify` | Resolve one active blocker and resume its originating stage. | `resume-origin` |
| `devspec.changerequest` | Append one related post-finalization requirement without rewriting history. | `finalize` |
| `devspec.finalize` | Produce a concise readiness brief and validation plan. | `clarify-or-tasks` |
| `devspec.tasks` | Create ordered, independently verifiable implementation tasks. | `implement` |
| `devspec.implement` | Implement pending ready tasks with focused checkpoints and validation. | `review` |
| `devspec.review` | Review changed work against readiness, tasks, and validation evidence. | `implement-or-close` |
| `devspec.diagram` | Create one evidence-backed diagram with duplicate checks and durable queue state. | `continue-current-workflow` |
| `devspec.quickfix` | Implement and validate one localized, low-risk enhancement or bug fix. | `complete-or-story` |
