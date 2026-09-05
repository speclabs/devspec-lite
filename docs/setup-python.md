# Python and uvx setup

Use this route on Windows, macOS, or Linux when Python 3.10 or newer is available. Choose `uvx` for one-off use, or `pipx` for a persistent CLI installation.

The commands below need a published package. Until the first `v*` release is tagged, no CLI route resolves; use [manual copy from `main`](manual-copy.md), which never requires Python or a package manager.

## One-off use with uvx

Install [uv](https://docs.astral.sh/uv/) using your platform's supported method, then run Devspec Lite without a permanent installation:

```text
uvx devspec-lite init --target . --profile all --repo-state existing
uvx devspec-lite doctor --target . --profile all
uvx devspec-lite --version
```

Use `--repo-state new` for a new repository.

## Persistent installation with pipx

On Windows:

```powershell
python -m pip install --user pipx
python -m pipx ensurepath
```

On macOS or Linux:

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

Then, in a new terminal on any platform:

```text
pipx install devspec-lite
devspec-lite --version
devspec-lite init --target . --profile all --repo-state existing
devspec-lite doctor --target . --profile all
```

Restart the terminal if `devspec-lite` is not found after `ensurepath`. Use `--repo-state new` for a new repository.

## Next steps

For upgrades, safe synchronization, profile changes, and workflow routing, see the [CLI lifecycle guide](setup-lifecycle.md).