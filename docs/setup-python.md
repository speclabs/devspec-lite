# Python and uvx setup

Use this route on Windows, macOS, or Linux when Python 3.10 or newer is available.

## One-off use with uvx

Install [uv](https://docs.astral.sh/uv/) using your platform's supported method, then initialize a repository without a permanent Devspec Lite installation:

```powershell
uvx devspec-lite init --target . --profile all --repo-state existing
uvx devspec-lite doctor --target . --profile all
uvx devspec-lite --version
```

For a new repository, use `--repo-state new`.

## Persistent installation with pipx

```powershell
python -m pip install --user pipx
python -m pipx ensurepath
pipx install devspec-lite
devspec-lite init --target . --profile all --repo-state existing
devspec-lite --version

## Next steps

For upgrade, safe synchronization, profile changes, and agent workflow examples, see the [installer lifecycle guide](setup-lifecycle.md).
```

Restart the terminal if `devspec-lite` is not found after `ensurepath`.

## Validation

```powershell
devspec-lite doctor --target . --profile all
```

The command verifies contracts, XML protocols, and the selected adapter wrappers. It never changes application code.
