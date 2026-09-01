# Homebrew setup

Use this route on macOS or Linux only after the Devspec Lite formula is published to a Homebrew tap. If the tap or formula is unavailable, choose [Python and uvx](setup-python.md) or [manual copy from `main`](manual-copy.md).

## Install

```bash
brew tap speclabs/devspec-lite
brew install devspec-lite
devspec-lite --version
```

## Initialize a repository

```bash
# Existing repository
devspec-lite init --target . --profile all --repo-state existing
devspec-lite doctor --target . --profile all

# New repository
devspec-lite init --target . --profile all --repo-state new
devspec-lite doctor --target . --profile all
```

Use a single-agent profile when the repository does not need every adapter wrapper.

## Next steps

For upgrades, safe synchronization, profile changes, and workflow routing, see the [CLI lifecycle guide](setup-lifecycle.md).