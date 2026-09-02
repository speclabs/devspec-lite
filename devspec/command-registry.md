# Command Registry

| Command | Purpose | Next route |
|---|---|---|
| `devspec.extract` | Build the complete evidence-backed baseline for an existing scoped system. | `devspec.story` or `devspec.clarify` |
| `devspec.projectcontext` | Capture product purpose, users, outcomes, and scope boundaries. | `techstack` |
| `devspec.techstack` | Capture evidence-backed runtime, frameworks, data, tooling, and delivery constraints. | `codebase-structure` |
| `devspec.codebase-structure` | Capture owned source roots, module boundaries, integrations, and repository access. | `coding-standards` |
| `devspec.coding-standards` | Capture short, evidence-backed conventions and anti-patterns. | `rules` |
| `devspec.rules` | Capture non-negotiable engineering, security, compliance, delivery, and accessibility rules. | `story` |
| `devspec.story` | Create one concise work-item intake from a request or provider reference. | `devspec.grooming` or `devspec.finalize` |
| `devspec.grooming` | Make one draft story buildable through scoped review and material questions. | `devspec.clarify` or `devspec.finalize` |
| `devspec.clarify` | Resolve one active blocker and resume its originating command. | `resume-origin` |
| `devspec.changerequest` | Append one related post-finalization requirement without rewriting history. | `finalize` |
| `devspec.finalize` | Produce a concise readiness brief and validation plan. | `devspec.clarify` or `devspec.tasks` |
| `devspec.tasks` | Create ordered, independently verifiable implementation tasks. | `implement` |
| `devspec.implement` | Implement pending ready tasks with focused checkpoints and validation. | `review` |
| `devspec.review` | Review changed work, record an outcome, and set one next action. | `devspec.implement`, `devspec.clarify`, or terminal |
| `devspec.diagram` | Create one targeted evidence-backed diagram with duplicate checks and durable queue state. | return to caller |
| `devspec.quickfix` | Implement and validate one localized, low-risk enhancement or bug fix. | terminal, `devspec.clarify`, or `devspec.story` |

Work-item IDs are optional for `grooming`, `finalize`, `tasks`, `implement`, `review`, `clarify`, and `changerequest`. Without an ID, resolve the private per-worktree current context and run only the work item's recorded `next` action. Use an explicit ID to switch stories; when several eligible stories exist, ask the user to choose.
