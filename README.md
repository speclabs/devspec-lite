# Devspec Lite

Devspec Lite is a compact, resumable spec-driven workflow for AI coding agents.

```powershell
uvx devspec-lite init --target . --profile all --repo-state existing
uvx devspec-lite doctor --target . --profile all
```

`init` installs canonical Markdown + XML contracts, concise templates, and only the wrappers for the selected agent profile. Use the `/devspec.*` commands exposed by your agent host.

The framework is intentionally clean-room: it keeps its own small contracts and does not copy any upstream framework files.
