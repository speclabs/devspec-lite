# Manual installation

Use this route when a developer does not want to install Python, UV, WinGet, Homebrew, or the Devspec Lite CLI. It uses a release-ready manual bundle or a checkout of a manual-ready branch or release tag that contains the same prebuilt files.

## 1. Get the release-ready files

Download the versioned manual bundle from the release, or check out the required release tag:

```powershell
git clone --depth 1 --branch <manual-ready-branch-or-release-tag> https://github.com/speclabs/devspec-lite.git
```

The bundle or checkout supplies the canonical `devspec/` directory and prebuilt agent-profile wrappers. No workflow content is generated during manual setup.

## 2. Copy one profile

Copy `devspec/` and the folder or file for the agent host into the target repository.

| Profile | Copy from the manual bundle or checkout | Copy into the target repository |
|---|---|---|
| Copilot | `devspec/`, `.github/` | `devspec/`, `.github/` |
| Codex | `devspec/`, `AGENTS.md` | `devspec/`, `AGENTS.md` |
| Claude | `devspec/`, `.claude/` | `devspec/`, `.claude/` |
| Cursor | `devspec/`, `.cursor/` | `devspec/`, `.cursor/` |
| Gemini | `devspec/`, `.gemini/` | `devspec/`, `.gemini/` |
| Antigravity | `devspec/`, `.agents/` | `devspec/`, `.agents/` |

Do not pre-copy individual foundation or work-item templates. When an agent needs a missing target artifact, the shared `work` protocol creates it from the matching `_template`; creating a work item initializes every file in `devspec/work-items/_template`, including `meta.md`.

## Manual-copy lifecycle

![Manual copy flow](assets/manual-copy-flow.svg)

## 3. Verify and commit

Verify that every path listed in `devspec/install-manifest.txt` exists and that the selected agent wrapper is present. Compare any same-named target wrapper before replacing it, then commit the copied files with the target repository.

## 4. Update manually

Get a newer release bundle or check out a newer release tag. Compare the incoming files with the target repository, copy the approved changes, preserve local customizations, and commit the update. The CLI `doctor`, `init`, and package-manager upgrade paths are optional alternatives; they are not prerequisites for manual setup.