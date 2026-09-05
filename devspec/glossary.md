# Glossary

Run states, work-item and quickfix stages, task statuses, evidence labels, the changed-work baseline, and resume semantics are defined once in `devspec/protocols/state.xml`. `devspec/lifecycle.md` owns the route graph. This file covers the remaining terms.

- Scope revision: a monotonic work-item number. Finalization, tasks, implementation, and review operate only on the current revision; older records are retained as superseded history. `devspec/protocols/revision.xml` owns its rules.
- Current work-item context: a private, per-worktree Git-metadata selection used to resolve an omitted work-item ID. It is never a Git-tracked artifact and never replaces `meta.md` as canonical state.
- Material question: a question whose answer can change implementation, validation, or scope. Only material questions enter the ask queue.
- OWASP exception: a reviewer-confirmed false-positive or not-applicable finding supported by enforceable evidence; it is distinct from an unresolved vulnerability. `devspec/protocols/security.xml` owns its confirmation rules.

## Repository access requirements

| Value | Meaning |
|---|---|
| `reference-only` | Read repository content as evidence only; do not edit or validate it. |
| `edit` | Read and edit approved repository files; do not run validation there. |
| `edit-and-test` | Read and edit approved repository files and run approved validations. |
| `validation-only` | Read required files and run approved validations; do not edit repository files. |
| `release-coordination` | Coordinate release information only; do not inspect, edit, or validate repository contents. |
| `unavailable` | The repository cannot currently be accessed; record the impact as a blocker. |

Record these values in `foundation/codebase-structure.md`. Select the least privilege that satisfies the current command; the repository location alone never grants access. `devspec/protocols/repo-access.xml` owns how they are collected and enforced.
