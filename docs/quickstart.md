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
