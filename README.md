# Devspec Lite

Devspec Lite is a compact, resumable spec-driven workflow for AI coding agents. Git-tracked `devspec/` artifacts are the canonical project state.

## Choose a setup route

| Your situation | Use this guide |
|---|---|
| No installer, Python, package manager, or CLI | [Manual copy from `main`](docs/manual-copy.md) |
| Python is available; one-off or persistent CLI use | [Python and uvx](docs/setup-python.md) |
| Windows package-manager installation | [WinGet](docs/setup-winget.md) |
| macOS/Linux package-manager installation | [Homebrew](docs/setup-homebrew.md) |
| Already installed the CLI; need init, upgrade, or profile changes | [CLI lifecycle](docs/setup-lifecycle.md) |

Manual copying and CLI installation produce the same canonical `devspec/` content and agent wrappers. Choose one setup route; the CLI is optional.

## CLI quick start

After choosing a CLI route, initialize and validate the repository:

```powershell
# Existing repository
uvx devspec-lite init --target . --profile all --repo-state existing
uvx devspec-lite doctor --target . --profile all

# New repository
uvx devspec-lite init --target . --profile all --repo-state new
uvx devspec-lite doctor --target . --profile all
```

`init` copies canonical Markdown + XML contracts, concise templates, and the wrappers for the selected agent profile. Use the `devspec.*` commands exposed by your agent host.

## Choose a workflow route

![Foundation route for new and existing repositories](docs/assets/foundation-routes.svg)

![Delivery route for quickfix and work items](docs/assets/delivery-routes.svg)

Use the [developer workflow guide](docs/workflows.md) for concrete quickfix, grooming, clarification, and change-request examples.

## How to

Follow the scenario-based [how-to guide](docs/how-to.md) to choose the right command, establish an existing or new repository baseline, start and deliver a story, work across multiple repositories, or route a small fix safely.
