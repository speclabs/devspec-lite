# Devspec Lifecycle

Canonical contracts in `devspec/contracts/` own command behavior. This document defines the shared state vocabulary and the legal route graph those contracts use.

## State records

- A foundation command records its command, stage, run state, last action, resume reference, next action, and update date in `devspec/foundation/decisions.md`.
- A work item records the same state in `meta.md`. Its `scope_revision` starts at `1` and increases only when `devspec.changerequest` accepts a related requirement.
- The selected current work item is private convenience state, not workflow evidence. Store it only at the per-worktree path returned by `git rev-parse --git-path devspec/current-work-item.json`; it identifies the work item, branch, selection source, and timestamp. Never commit a current-story file.
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

Before an ID-free work-item command, resolve current context in this order: a validated supplied ID, a valid branch-matched local selection, then exactly one eligible non-terminal work item on the current branch. Clear a selection that has a changed branch, a missing work-item folder or `meta.md`, terminal work, or a stage/next-action mismatch. If several items remain, ask the user to choose. A clear continuation request dispatches only the selected `next` action; blocked work goes through `devspec.clarify`, and terminal work does not resume.

## Route graph

- Existing repository: `devspec.extract → devspec.story`; an evidence gap that can materially affect later work is `blocked → devspec.clarify`.
- New repository: `devspec.projectcontext → devspec.techstack → devspec.codebase-structure → devspec.coding-standards → devspec.rules → devspec.story`. A targeted foundation update returns to its caller after completing its declared artifact.
- Work item: `devspec.story → devspec.grooming|devspec.finalize → devspec.tasks → devspec.implement → devspec.review`. Review results are `accepted → complete`, `rework-required → devspec.implement`, or `blocked → devspec.clarify`.
- Work-item IDs are optional selectors for switching or resolving ambiguity. After a story is selected, normal commands and `continue` use its per-worktree context and never skip the recorded `next` command.
- `devspec.clarify` resolves one decision and resumes its saved originating command. `devspec.changerequest` is allowed only after finalization and always returns to `devspec.finalize` with a new revision. `devspec.quickfix` is `complete`, `blocked`, or `routed -> devspec.story`. `devspec.diagram` returns to its caller.
