# Python and uvx setup

Use this route on Windows, macOS, or Linux when Python 3.10 or newer is available. Choose `uvx` for one-off use, or `pipx` for a persistent CLI installation.

The commands below need a published package. Until the first `v*` release is tagged, no CLI route resolves; use [manual copy from `main`](manual-copy.md), which never requires Python or a package manager.

## One-off use with uvx

Install [uv](https://docs.astral.sh/uv/) using your platform's supported method, then run Devspec Lite without a permanent installation:

```text
uvx devspec --version
```

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
pipx install devspec
devspec --version
```

Restart the terminal if `devspec` is not found after `ensurepath`.

## Next steps

Initialize and validate the repository with the [CLI quick start](quickstart.md). For upgrades, synchronization, and profile changes, see the [CLI lifecycle guide](setup-lifecycle.md).
