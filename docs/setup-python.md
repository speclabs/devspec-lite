# Python and uvx setup

Use this route on Windows, macOS, or Linux when Python 3.10 or newer is available. Choose `uvx` for one-off use, or `pipx` for a persistent CLI installation. To avoid installing Python or any CLI, use [manual copy from `main`](manual-copy.md).

## One-off use with uvx

Install [uv](https://docs.astral.sh/uv/) using your platform's supported method, then run Devspec Lite without a permanent installation:

```powershell
uvx devspec-lite init --target . --profile all --repo-state existing
uvx devspec-lite doctor --target . --profile all
uvx devspec-lite --version
```

Use `--repo-state new` for a new repository.

## Persistent installation with pipx

```powershell
python -m pip install --user pipx
python -m pipx ensurepath
pipx install devspec-lite
devspec-lite --version
devspec-lite init --target . --profile all --repo-state existing
devspec-lite doctor --target . --profile all
```

Restart the terminal if `devspec-lite` is not found after `ensurepath`. Use `--repo-state new` for a new repository.

## Next steps

For upgrades, safe synchronization, profile changes, and workflow routing, see the [CLI lifecycle guide](setup-lifecycle.md).