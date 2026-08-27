# Manual installation

Use manual copy when package installation is blocked in the target repository. Generate the selected profile in a temporary folder on any machine that can run Python 3.10+ and then copy only its generated framework files.

## Generate a profile

```powershell
mkdir C:\Temp\devspec-lite-profile
devspec-lite init --target C:\Temp\devspec-lite-profile --profile copilot --repo-state existing
```

For a new project, replace `existing` with `new`. The generated `devspec/` directory is required for every profile; the adapter wrapper is profile-specific.

## Copy the required files

| Profile | Copy into the target repository | Example |
|---|---|---|
| Copilot | `devspec/`, `.github/prompts/`, `.github/agents/` | `Copy-Item C:\Temp\devspec-lite-profile\devspec, C:\Temp\devspec-lite-profile\.github -Destination D:\Code\orders -Recurse` |
| Codex | `devspec/`, `AGENTS.md` | `Copy-Item C:\Temp\devspec-lite-profile\devspec -Destination D:\Code\orders -Recurse; Copy-Item C:\Temp\devspec-lite-profile\AGENTS.md D:\Code\orders` |
| Claude | `devspec/`, `.claude/skills/` | `Copy-Item C:\Temp\devspec-lite-profile\devspec, C:\Temp\devspec-lite-profile\.claude -Destination D:\Code\orders -Recurse` |
| Cursor | `devspec/`, `.cursor/rules/` | `Copy-Item C:\Temp\devspec-lite-profile\devspec, C:\Temp\devspec-lite-profile\.cursor -Destination D:\Code\orders -Recurse` |
| Gemini | `devspec/`, `.gemini/commands/` | `Copy-Item C:\Temp\devspec-lite-profile\devspec, C:\Temp\devspec-lite-profile\.gemini -Destination D:\Code\orders -Recurse` |
| Antigravity | `devspec/`, `.agents/skills/` | `Copy-Item C:\Temp\devspec-lite-profile\devspec, C:\Temp\devspec-lite-profile\.agents -Destination D:\Code\orders -Recurse` |


## Manual-copy lifecycle

![Install and maintenance flow](assets/maintenance-flow.svg)

Generate one profile, copy only its listed files, then run Doctor when Python is available. After validation, use the [developer workflow guide](workflows.md) to choose the foundation or delivery route.

Replace `D:\Code\orders` with the target repository. If the target already contains a same-named wrapper file, compare it first; do not overwrite user-managed instructions accidentally.

## Validate after copying

If Python is available on the target machine:

```powershell
devspec-lite doctor --target D:\Code\orders --profile copilot
```

Otherwise, verify that `devspec/contracts/`, `devspec/protocols/`, and the profile-specific wrapper path from the table are all present.
