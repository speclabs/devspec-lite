# WinGet setup

Use this route on Windows only after the Devspec Lite package is published to WinGet. If the package is unavailable, choose [Python and uvx](setup-python.md) or [manual copy from `main`](manual-copy.md).

## Install

```powershell
winget install --id SpecLabs.DevspecLite --exact
devspec-lite --version
```

## Initialize a repository

```powershell
# Existing repository
devspec-lite init --target . --profile all --repo-state existing
devspec-lite doctor --target . --profile all

# New repository
devspec-lite init --target . --profile all --repo-state new
devspec-lite doctor --target . --profile all
```

Choose a narrower profile such as `copilot`, `codex`, `claude`, `cursor`, `gemini`, or `antigravity` when only one agent is used.

## Next steps

For upgrades, safe synchronization, profile changes, and workflow routing, see the [CLI lifecycle guide](setup-lifecycle.md).