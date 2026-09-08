# Homebrew setup

Use this route on macOS or Linux only after the Devspec Lite formula is published to a Homebrew tap. If the tap or formula is unavailable, use [manual copy from `main`](manual-copy.md); the [Python route](setup-python.md) needs the same release.

## Install

```bash
brew tap speclabs/devspec-lite
brew install devspec
devspec --version
```

## Next steps

Initialize and validate the repository with the [CLI quick start](quickstart.md). For upgrades, synchronization, and profile changes, see the [CLI lifecycle guide](setup-lifecycle.md).
