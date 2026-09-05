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

Manual copying and CLI installation produce the same canonical `devspec/` content and agent wrappers, once the manual route resets the project records listed in its guide. In either route, set the target repository's `repository-state.md` to `new` or `existing`. Choose one setup route; the CLI is optional.

## CLI quick start

The [CLI quick start](docs/quickstart.md) walks through initializing, validating, and choosing the first command.

After choosing a CLI route, initialize and validate the repository:

```powershell
# Existing repository
uvx --from devspec-lite devspec init --target . --profile all --repo-state existing
uvx --from devspec-lite devspec doctor --target . --profile all

# New repository
uvx --from devspec-lite devspec init --target . --profile all --repo-state new
uvx --from devspec-lite devspec doctor --target . --profile all
```

`init` copies canonical Markdown + XML contracts, concise templates, and the wrappers for the selected agent profile. It generates `devspec/foundation/repository-state.md` from `--repo-state` and seeds empty `devspec/architecture/overview.md` and `artifact-queue.md` from their templates. Those two, plus `devspec/constitution.md`, are project-owned: `init` and `sync` never overwrite them, even with `--force`. Use the `devspec.*` commands exposed by your agent host. Use `devspec diff --target .` to inspect installed-framework drift and `devspec sync --target . --profile all --dry-run` before applying a framework upgrade.

## Choose a workflow route

![Foundation route for new and existing repositories](docs/assets/foundation-routes.svg)

![Delivery route for quickfix and work items](docs/assets/delivery-routes.svg)

Use the [developer workflow guide](docs/workflows.md) for concrete quickfix, grooming, clarification, and change-request examples.

## How to

Follow the scenario-based [how-to guide](docs/how-to.md) to choose the right command, establish an existing or new repository baseline, start and deliver a story, work across multiple repositories, or route a small fix safely.
Before every `devspec.*` command, confirm the single-repository or multi-repository scope, unless current canonical evidence records it. After starting a story, use the normal work-item commands or `continue` without repeating its ID; private per-worktree context resumes only the recorded next action. See the [beginner command examples](docs/command-examples.md) for scaffold layouts, source-scope confirmation, multi-repository boundaries, and a first prompt for every command.
