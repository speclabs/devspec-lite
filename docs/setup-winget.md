# WinGet setup

Use this route on Windows after the Devspec Lite package is published to WinGet.

## Install

```powershell
winget install --id SpecLabs.DevspecLite --exact
devspec-lite --help
devspec-lite --version
```

## Initialize a repository

```powershell
devspec-lite init --target . --profile all --repo-state existing

## Next steps

For upgrade, safe synchronization, profile changes, and agent workflow examples, see the [installer lifecycle guide](setup-lifecycle.md).
devspec-lite doctor --target . --profile all
```

Use `--repo-state new` for a new repository. Choose a narrower profile such as `copilot`, `codex`, `claude`, `cursor`, `gemini`, or `antigravity` when only one agent is used.

## If WinGet is not available

Use the [Python and uvx setup](setup-python.md) or the [manual-copy guide](manual-copy.md).
