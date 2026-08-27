# Quick start

For a new repository:

```powershell
uvx devspec-lite init --target . --profile all --repo-state new
```

For an existing repository:

```powershell
uvx devspec-lite init --target . --profile all --repo-state existing
uvx devspec-lite doctor --target . --profile all
```

Foundation route: `projectcontext → techstack → codebase-structure → coding-standards → rules`.

Work route: `story → grooming` when needed `→ finalize → tasks → implement → review`.

Use `quickfix` only for one localized, low-risk change. It routes API contracts, migrations, authentication/security, and breaking changes to the full route.

## Choose a workflow route

![Foundation route](assets/foundation-routes.svg)

![Delivery route](assets/delivery-routes.svg)

For scenarios and examples, see the [developer workflow guide](workflows.md).

## Platform setup

- [WinGet](setup-winget.md)
- [Python and uvx](setup-python.md)
- [Homebrew](setup-homebrew.md)
- [Installer lifecycle](setup-lifecycle.md)
- [Manual copy](manual-copy.md)
