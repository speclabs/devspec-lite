# Upstream Command Parity

Comparison baseline: [`speclabs/devspec` commit `b93275bb4cef4645bbeef72cb8357aa7a6f8adb7`](https://github.com/speclabs/devspec/blob/b93275bb4cef4645bbeef72cb8357aa7a6f8adb7/devspec/adapters/command-registry.md).

| Upstream command | Devspec Lite | Status |
|---|---|---|
| extract, projectcontext, techstack, codebase-structure, coding-standards, rules | Same name | Supported |
| story, clarify, changerequest, finalize, tasks, implement, review, diagram | Same name | Supported |

Lite additionally provides `devspec.grooming` and `devspec.quickfix`. Existing-system extraction remains deliberately comprehensive and routes directly to `devspec.story`; it does not repeat the upstream's five foundation commands.

This release adds constitution candidates and explicit promotion, work-item clarification ledgers, finalization architecture traces, explicit process-flow batch diagrams, and the `diff`/`sync` installer lifecycle. `sync` never deletes retained obsolete files.
