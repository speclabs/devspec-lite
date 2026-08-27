# Homebrew setup

Use this route on macOS or Linux after the Devspec Lite formula is published to a Homebrew tap.

## Install

```bash
brew tap speclabs/devspec-lite
brew install devspec-lite
devspec-lite --help
devspec-lite --version
```

## Initialize a repository

```bash
devspec-lite init --target . --profile all --repo-state existing

## Next steps

For upgrade, safe synchronization, profile changes, and agent workflow examples, see the [installer lifecycle guide](setup-lifecycle.md).
devspec-lite doctor --target . --profile all
```

Use `--repo-state new` for a new repository. Use a single-agent profile when the repository does not need all adapter wrappers.

## If the tap is not yet published

Use the [Python and uvx setup](setup-python.md) instead.
