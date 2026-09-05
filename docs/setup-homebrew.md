# Homebrew setup

Use this route on macOS or Linux only after the Devspec Lite formula is published to a Homebrew tap. If the tap or formula is unavailable, use [manual copy from `main`](manual-copy.md); the [Python route](setup-python.md) needs the same release.

## Install

```bash
brew tap speclabs/devspec-lite
brew install devspec-lite
devspec --version
```

## Initialize a repository

```bash
# Existing repository
devspec init --target . --profile all --repo-state existing
devspec doctor --target . --profile all

# New repository
devspec init --target . --profile all --repo-state new
devspec doctor --target . --profile all
```

Use a single-agent profile when the repository does not need every adapter wrapper: `copilot`, `codex`, `claude`, `cursor`, `gemini`, or `antigravity`.

## Next steps

For upgrades, safe synchronization, profile changes, and workflow routing, see the [CLI lifecycle guide](setup-lifecycle.md).