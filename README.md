# Devspec Lite

Devspec Lite is a compact, resumable spec-driven workflow for AI coding agents.

```powershell
uvx devspec-lite init --target . --profile all --repo-state existing
uvx devspec-lite doctor --target . --profile all
```

`init` installs canonical Markdown + XML contracts, concise templates, and only the wrappers for the selected agent profile. Use the `/devspec.*` commands exposed by your agent host.

The framework is intentionally clean-room: it keeps its own small contracts and does not copy any upstream framework files.

## Setup guides

## Workflow routes

![Foundation route for new and existing repositories](docs/assets/foundation-routes.svg)

![Delivery route for quickfix and work items](docs/assets/delivery-routes.svg)

Choose a route with the [developer workflow guide](docs/workflows.md), including concrete quickfix, grooming, clarification, and change-request examples.

- [WinGet](docs/setup-winget.md)
- [Python and uvx](docs/setup-python.md)
- [Homebrew](docs/setup-homebrew.md)
- [Installer lifecycle: init, upgrade, sync, profiles](docs/setup-lifecycle.md)
- [Manual copy](docs/manual-copy.md)
