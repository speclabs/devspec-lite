# WinGet setup

Use this route on Windows only after the Devspec Lite package is published to WinGet. If the package is unavailable, use [manual copy from `main`](manual-copy.md); the [Python route](setup-python.md) needs the same release.

## Install

```powershell
winget install --id SpecLabs.Devspec --exact
devspec --version
```

## Next steps

Initialize and validate the repository with the [CLI quick start](quickstart.md). For upgrades, synchronization, and profile changes, see the [CLI lifecycle guide](setup-lifecycle.md).
