# WinGet setup

Use this route on Windows only after the Devspec Lite package is published to WinGet. If the package is unavailable, use [manual copy from `main`](manual-copy.md); the [Python route](setup-python.md) needs the same release.

## Install

```powershell
winget install --id SpecLabs.Devspec --exact
devspec --version
```

## Initialize a repository

```powershell
# Existing repository
devspec init --target . --profile all --repo-state existing
devspec doctor --target . --profile all

# New repository
devspec init --target . --profile all --repo-state new
devspec doctor --target . --profile all
```

Choose a narrower profile such as `copilot`, `codex`, `claude`, `cursor`, `gemini`, or `antigravity` when only one agent is used.

## Next steps

For upgrades, safe synchronization, profile changes, and workflow routing, see the [CLI lifecycle guide](setup-lifecycle.md).