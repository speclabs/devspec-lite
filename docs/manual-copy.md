# Manual installation

If package installation is unavailable, run `devspec-lite init` once on a machine with Python, then copy the generated `devspec/` folder and the selected adapter wrapper folder into the target repository.

Use one of these profiles: `copilot`, `codex`, `claude`, `cursor`, `gemini`, or `antigravity`. Run `devspec-lite doctor --target <repository> --profile <profile>` after copying.

Do not copy another profile's wrapper folder unless that agent is used in the repository.
