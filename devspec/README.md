# Devspec Lite

New repository foundation: `projectcontext → techstack → codebase-structure → coding-standards → rules`. Existing repository baseline: `extract` completes the foundation, prepares the applicable diagram list, and asks whether to generate all or selected diagrams. Rare durable cross-work-item principles live in `constitution.md`; `projectcontext` promotes or retires them only on explicit input.

Work item: `story → grooming` when needed `→ finalize → tasks → implement → review`. Story intake accepts one manual request or, when an authenticated MCP connector is available, one read-only provider work-item reference.
After `story` selects a work item, use the normal work-item commands without repeating its ID. Per-worktree private context resolves the selected story and its recorded `next` action; use an ID only to switch or disambiguate stories.

Use `clarify` only for an active blocker and `quickfix` only for localized, low-risk changes. See `lifecycle.md` for all command transitions.
