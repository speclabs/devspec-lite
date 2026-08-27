# Installer lifecycle

This guide covers the normal life of a Devspec Lite installation: install the CLI, initialize a repository, validate it, upgrade safely, synchronize generated files, and add another agent profile.

## 1. Install Devspec Lite

Choose one supported path:

| Platform or preference | Example |
|---|---|
| One-off, any OS | `uvx devspec-lite --help` |
| Persistent Python install | `pipx install devspec-lite` |
| Windows package manager | `winget install --id SpecLabs.DevspecLite --exact` |
| Homebrew tap | `brew tap speclabs/devspec-lite && brew install devspec-lite` |

See the platform guides for prerequisites and fallback options.

## Check the installed version

Before upgrading or troubleshooting, verify the CLI version:

```powershell
devspec-lite --version
```

Example output: `devspec-lite 0.1.0`.

## 2. Initialize a repository

Use `existing` when source code already exists:

```powershell
devspec-lite init --target D:\Code\orders --profile all --repo-state existing
devspec-lite doctor --target D:\Code\orders --profile all
```

Use `new` before the first foundation workflow in a blank repository:

```powershell
devspec-lite init --target D:\Code\orders --profile copilot --repo-state new
devspec-lite doctor --target D:\Code\orders --profile copilot
```

`all` installs every supported wrapper. Use one of `copilot`, `codex`, `claude`, `cursor`, `gemini`, or `antigravity` when the repository uses only that agent.

## 3. Validate the installation

Run Doctor after installation, after a manual copy, and before reporting a setup problem:

```powershell
devspec-lite doctor --target D:\Code\orders --profile all
```

Doctor checks that each canonical contract, XML protocol, and selected adapter wrapper exists and that wrappers point to their matching contract. It does not modify repository code.

## 4. Upgrade the CLI

Upgrade using the same installation method:

```powershell
# uvx: use the latest package for the next command
uvx devspec-lite@latest --help

# pipx
pipx upgrade devspec-lite

# WinGet
winget upgrade --id SpecLabs.DevspecLite --exact

# Homebrew

## Lifecycle at a glance

![Install and maintenance flow](assets/maintenance-flow.svg)

After setup, choose a foundation or delivery route from the [developer workflow guide](workflows.md).

For a manual installation, follow the same validation steps in the [manual-copy guide](manual-copy.md).
brew upgrade devspec-lite
```

After upgrading, synchronize and validate the target repository.

## 5. Synchronize generated framework files

There is intentionally no separate `sync` command. Run Doctor first, then rerun `init` with the same profile:

```powershell
devspec-lite doctor --target D:\Code\orders --profile all
devspec-lite init --target D:\Code\orders --profile all --repo-state existing
devspec-lite doctor --target D:\Code\orders --profile all
```

`init` is safe for unchanged managed files and adds missing generated files. It refuses to overwrite a changed managed file. Example: if `devspec/contracts/devspec.story.md` was customized locally, preserve the customization and merge the desired update manually instead of forcing an overwrite.

## 6. Change or add a profile

To add Codex to a repository that already has the Copilot profile:

```powershell
devspec-lite init --target D:\Code\orders --profile codex --repo-state existing
devspec-lite doctor --target D:\Code\orders --profile codex
```

To add every remaining wrapper, use `all`:

```powershell
devspec-lite init --target D:\Code\orders --profile all --repo-state existing
devspec-lite doctor --target D:\Code\orders --profile all
```

Changing to a narrower profile does not delete wrappers from other agents. Review and remove obsolete wrapper folders manually only after confirming no team member needs them.

## 7. Start using the workflow

For a new repository, start with `devspec.projectcontext`. For an existing repository, start with `devspec.extract`. Then follow the route in `devspec/README.md`. Use `devspec.quickfix` only for one localized, low-risk change.
