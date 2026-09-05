# Devspec Lifecycle

Canonical contracts in `devspec/contracts/` own command behavior. This document owns the state-record locations and the legal route graph those contracts use. The shared state vocabulary — run states, stages, task statuses, evidence labels, the changed-work baseline, and resume semantics — lives in `devspec/protocols/state.xml`.

## State records

- A foundation command records its command, stage, run state, last action, resume reference, next action, and update date in `devspec/foundation/decisions.md`.
- A work item records the same state in `meta.md`, together with its scope revision.
- A quickfix records its state in front matter. A diagram records queue status and returns to its invoking workflow without changing that workflow's state.
- The selected current work item is private convenience state, not workflow evidence. Store it only at the per-worktree path returned by `git rev-parse --git-path devspec/current-work-item.json`. Never commit a current-story file. `devspec/protocols/current-work-item.xml` owns its selection, validation, and recovery rules.

## Work-item stages

| Stage | Required next command or terminal outcome |
|---|---|
| `intake` | `devspec.story` or `devspec.clarify` |
| `grooming` | `devspec.grooming` or `devspec.clarify` |
| `finalization` | `devspec.finalize` or `devspec.clarify` |
| `tasks` | `devspec.tasks` or `devspec.clarify` |
| `implementation` | `devspec.implement` or `devspec.clarify` |
| `review` | `devspec.review` or `devspec.clarify` |
| `complete` | terminal (`next: none`) |

Every non-terminal stage may route to `devspec.clarify`, and only to `devspec.clarify`, when it records a material blocker. `devspec/protocols/revision.xml` owns which revision each stage may read and write.

## Route graph

- Existing repository: `devspec.extract → devspec.story`.
- New repository: `devspec.projectcontext → devspec.techstack → devspec.codebase-structure → devspec.coding-standards → devspec.rules → devspec.story`. A targeted foundation update returns to its caller after completing its declared artifact.
- Work item: `devspec.story → devspec.grooming|devspec.finalize → devspec.tasks → devspec.implement → devspec.review`. Review results are `accepted → complete`, `rework-required → devspec.implement`, or `blocked → devspec.clarify`.
- Work-item IDs are optional selectors for switching or resolving ambiguity. After a story is selected, normal commands and `continue` use its per-worktree context and never skip the recorded `next` command.
- `devspec.clarify` resolves one decision and resumes its saved originating command. `devspec.changerequest` is allowed only after finalization and always returns to `devspec.finalize` with a new revision. `devspec.quickfix` is `complete`, `blocked`, or `routed → devspec.story`. `devspec.diagram` returns to its caller.
