# CLI quick start

Use this guide after choosing a CLI installation route. For a no-installer workflow, use [manual copy from `main`](manual-copy.md) instead.

## 1. Initialize and validate

Choose the repository state that matches the target:

```powershell
# New repository: no source code to inspect
uvx --from devspec-lite devspec init --target . --profile all --repo-state new
uvx --from devspec-lite devspec doctor --target . --profile all

# Existing repository: source code is already present
uvx --from devspec-lite devspec init --target . --profile all --repo-state existing
uvx --from devspec-lite devspec doctor --target . --profile all
```

Use a narrower profile such as `copilot`, `codex`, `claude`, `cursor`, `gemini`, or `antigravity` when the target uses one agent host. `all` installs every supported wrapper.

## 2. Start the right workflow

Every `devspec.*` command begins by confirming repository scope: it asks for each repository path, then one named access requirement per repository. Answer those before the command inspects any source. The route itself comes from `devspec/foundation/repository-state.md`, which `init` writes from `--repo-state`.

- New repository: author the foundation intentionally with `devspec.projectcontext → devspec.techstack → devspec.codebase-structure → devspec.coding-standards → devspec.rules`.
- Existing repository: run `devspec.extract` once. It creates the evidence-backed technical, business, workflow, and rule baseline, prepares the possible-diagram list, then asks one question with four answers: generate all, prepare the list only, choose specific diagrams, or a custom answer. Choosing to prepare the list only keeps the candidates without generating them; later generate a static SVG with `/devspec.diagram DIA-002`, or request an evidence-backed animated explanation with `/devspec.diagram DIA-002 motion=explain`.

Work route: `devspec.story → devspec.grooming` when needed `→ devspec.finalize → devspec.tasks → devspec.implement → devspec.review`.

When a command reports a blocker, run `devspec.clarify`: it resolves the one recorded decision and resumes the exact saved command. When a related requirement arrives after finalization, run `devspec.changerequest` to append it and re-finalize the new scope revision.

Use `devspec.quickfix` only for one localized, low-risk change. It routes API contracts, migrations, authentication/security, and breaking changes to the full route.

## Workflow routes

![Foundation route](assets/foundation-routes.svg)

![Delivery route](assets/delivery-routes.svg)

For scenarios and examples, see the [developer workflow guide](workflows.md).

## Setup routes

- [Manual copy from `main`](manual-copy.md)
- [Python and uvx](setup-python.md)
- [WinGet](setup-winget.md)
- [Homebrew](setup-homebrew.md)
- [CLI lifecycle](setup-lifecycle.md)
