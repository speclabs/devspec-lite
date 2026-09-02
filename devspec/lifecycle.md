# Devspec Lifecycle

Canonical contracts in `devspec/contracts/` own command behavior. This document defines the shared state vocabulary and the legal route graph those contracts use.

## State records

- A foundation command records its command, stage, run state, last action, resume reference, next action, and update date in `devspec/foundation/decisions.md`.
- A work item records the same state in `meta.md`. Its `scope_revision` starts at `1` and increases only when `devspec.changerequest` accepts a related requirement.
- A quickfix records its state in front matter. A diagram records queue status and returns to its invoking workflow without changing that workflow's state.
- `active` means the registered next command may run. `blocked` means exactly one active material decision is recorded and the next command is `devspec.clarify`. `paused` is an explicit user pause. `stopped` requires a new user direction before resuming. `complete` is terminal and must use `next: none`.

## Work-item states and revisions

| Stage | Required next command or terminal outcome |
|---|---|
| `intake` | `devspec.story` |
| `grooming` | `devspec.grooming` or `devspec.clarify` |
| `finalization` | `devspec.finalize` or `devspec.clarify` |
| `tasks` | `devspec.tasks` |
| `implementation` | `devspec.implement` or `devspec.clarify` |
| `review` | `devspec.review` or `devspec.clarify` |
| `complete` | terminal (`next: none`) |

Task status is one of `pending`, `in-progress`, `blocked`, `complete`, or `superseded`. A task becomes `complete` only after its recorded validation passes. Finalization, task, implementation, and review records carry the active scope revision. A change request increments that revision, preserves earlier revision sections as `superseded`, and requires fresh finalization before planning or implementation continues.

## Route graph

- Existing repository: `devspec.extract → devspec.story`; an evidence gap that can materially affect later work is `blocked → devspec.clarify`.
- New repository: `devspec.projectcontext → devspec.techstack → devspec.codebase-structure → devspec.coding-standards → devspec.rules → devspec.story`. A targeted foundation update returns to its caller after completing its declared artifact.
- Work item: `devspec.story → devspec.grooming|devspec.finalize → devspec.tasks → devspec.implement → devspec.review`. Review results are `accepted → complete`, `rework-required → devspec.implement`, or `blocked → devspec.clarify`.
