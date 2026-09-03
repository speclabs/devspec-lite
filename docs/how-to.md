# How to use Devspec Lite

This guide uses real developer situations to show which agent command to run, when to run it, and what happens next. Run `devspec-lite init` and `devspec-lite doctor` first; then invoke the listed `devspec.*` command from your configured agent host.

Git-tracked `devspec/` artifacts are the project record. Do not skip a command because the answer is present in chat: record the evidence or decision in the matching artifact.

> Commands validate their entry state. If a command says the work is blocked, use `devspec.clarify`; do not force the next route.

## Choose the scaffold and confirm source scope

The `devspec/` scaffold may live in the code repository or in a separate Git repository that records a multi-repository change. The directory open in the agent host is the scaffold location, not automatic permission to inspect source. Before every `devspec.*` command, confirm single-repository or multi-repository scope in two steps when current evidence is absent: first ask for one repository name or local path in a free-form text input with examples; after that path is confirmed, ask one interactive access question with examples, Custom Answer, and one recommendation. Repeat the two questions for each repository, recording its role and separate `read`, `edit`, and `validate` permissions. A new repository may explicitly confirm that no source exists yet. Current canonical evidence may replace a repeated confirmation only when it records the same facts.

Use the [beginner command examples](command-examples.md) to choose a scaffold layout, confirm one or more repository boundaries, and copy a safe first prompt for every command.

For provider-backed story intake, pass one GitHub, Azure DevOps, Jira, GitLab, or other provider work-item URL or identifier to `/devspec.story` only when an authenticated MCP connector is available. Intake reads the item, shows a summary, and asks for explicit structured confirmation before creating the work item; it never writes back to the provider. See [MCP provider intake](command-examples.md#intake-from-mcp-providers).

## Choose the first command

| Developer situation | Run | Then |
|---|---|---|
| Existing codebase with no trusted Devspec baseline | `devspec.extract` | Start a story after the baseline is ready. |
| Brand-new repository | `devspec.projectcontext` | Continue the new-foundation route. |
| New feature, API contract, migration, security change, or multiple concerns | `devspec.story` | Groom when needed, then finalize, plan, implement, and review. |
| One local, low-risk correction | `devspec.quickfix` | Complete directly or route to a story. |
| A recorded material decision blocks current work | `devspec.clarify` | Resume the exact saved command. |
| A related requirement arrives after finalization | `devspec.changerequest` | Re-finalize the new scope revision. |
| One evidence-backed architecture or workflow visual is needed | `devspec.diagram` | Return to the caller's workflow. |
| A known foundation artifact needs a narrow update | Its matching foundation command | Return to the caller after the update. |

## Continue current work without an ID

Say `continue` or run the next work-item command without an ID. Devspec resolves private per-worktree context, reads the selected `meta.md` next action, and resumes only that action. If context is missing or multiple active stories exist, it asks you to select one; use an ID only to switch stories explicitly.



## 1. Map an existing service before changing it

**Scenario.** You inherit an orders API and need to add an export, but its integrations, conventions, and security controls are not documented.

1. Initialize the repository as `existing` if it is not initialized yet.

```powershell
uvx devspec-lite init --target . --profile all --repo-state existing
uvx devspec-lite doctor --target . --profile all
```

2. Confirm source scope in order: first enter the repository path or name in the free-form prompt, then choose access after the path is confirmed. The current workspace is only a proposed target; current canonical evidence may replace these questions only when it records the same path, role, and permissions.
3. In your agent host, run a scoped request such as `/devspec.extract Source scope confirmed: orders API at D:\Code\orders-api (primary, read/edit/validate).`
4. It inspects only the confirmed source, tests, configuration, and documentation, then creates the evidence-backed foundation and applicable diagrams.
5. If material evidence or source scope is unavailable, answer the recorded question through `/devspec.clarify`. Otherwise, begin the requested change with `/devspec.story Add customer export`.

**What to expect.** `extract` is the existing-system baseline command. Do not run individual foundation or diagram commands afterward just to recreate its baseline; use a targeted update only when a known artifact needs one.

- Next command when ready: `/devspec.story <request>`.

## 2. Establish a new repository before the first feature

**Scenario.** Your team has created an empty service repository and wants a durable engineering baseline before accepting feature work.

1. Initialize it with `--repo-state new`.
2. Confirm the repository scope before the first command, for example: `Scope confirmed: scaffold and planned source at D:\Code\inventory; no source exists yet; read/edit/validate.`
3. Run these agent commands in order:

```text
/devspec.projectcontext
/devspec.techstack
/devspec.codebase-structure
/devspec.coding-standards
/devspec.rules
```

4. Use `/devspec.diagram <subject>` only when a specific evidence-backed visual is needed during this route.

**What to expect.** Each command records its artifact and advances to the next command. After `rules`, the foundation is ready for `/devspec.story`.

## 3. Deliver a feature from request to accepted review

**Scenario.** Product asks for a customer-export API with authorization, audit evidence, and automated validation.

1. Start one work item: `/devspec.story Add customer export API with authorization`.
2. Run `/devspec.grooming` when the code area, compatibility, risk, or acceptance criteria needs scoped analysis. Otherwise move directly to `/devspec.finalize`.
3. After finalization reports `ready`, run the delivery route:

```text
/devspec.tasks
/devspec.implement
/devspec.review
```

4. Follow the review outcome exactly:

   - `accepted`: the work item is complete; no next command is required.
   - `rework-required`: run `/devspec.implement` for the affected tasks.
   - `blocked`: run `/devspec.clarify`, then resume the saved command.

**What to expect.** Finalization, tasks, implementation, and review are stamped with the same scope revision. Review checks the recorded changed-work baseline and the validation evidence, not just the code diff.

## 4. Work across an API and a web application repository

**Scenario.** A checkout-flow change needs an API in `D:\Code\orders-api` and a web application in `D:\Code\orders-web`.

1. Choose one Git-tracked scaffold location for the change record: either the primary code repository or a dedicated Devspec repository. Keep the work-item artifacts in that one location.
2. Initialize the scaffold location with the appropriate profile and repository state. When it is a dedicated scaffold repository, open that directory in the agent host; do not assume it grants access to the code repositories.
3. Start the story from the primary repository and state the repository roles, local paths, and read, edit, and validation permissions in the request. For example:

```text
/devspec.story Add checkout address validation. Primary: orders-api at D:\Code\orders-api (read/edit/validate). Dependent UI: orders-web at D:\Code\orders-web (read/edit/validate).
```

4. When a command needs the second repository, it uses the `repo-access` protocol before reading, editing, or validating it. Record a repository as reference-only or validation-only when that is its real boundary.
5. Run `/devspec.extract` instead of the individual foundation commands when you need an evidence-backed baseline for an explicitly scoped multi-repository existing system.

**What to expect.** There is no separate multi-repository configuration command. The approved roles, paths, and access permissions are the configuration, recorded in canonical Devspec artifacts. Never infer edit access, and never validate a reference-only or unavailable repository.

- Next command for a new change: `/devspec.story <one request with repository scope>`.

## 5. Handle the common exceptions

### Correct one low-risk UI defect

**Scenario.** The Orders page has an incorrect empty-state label and no contract, data, security, or cross-cutting behavior changes are involved.

1. Run `/devspec.quickfix Fix Orders empty-state text` and select `UI` as the primary scope.
2. Record the changed area and focused validation in the generated quickfix record.

**What to expect.** A quickfix completes directly only when the risk stays local. If investigation exposes authentication, a public API, a migration, unresolved risk, or unrelated work, it routes to `/devspec.story` without editing code.

### Add a related requirement after implementation started

**Scenario.** After export implementation begins, product asks for a new JSON format in the same feature.

1. Run `/devspec.changerequest Add JSON export`.
2. Follow the route back through `/devspec.finalize`, `/devspec.tasks`, implementation, and review.

**What to expect.** This is the post-finalization route: the command increments `scope_revision`, retains previous records as superseded history, and prevents implementation against stale tasks.

### Resolve a material question without guessing

**Scenario.** Finalization is blocked because the required data-retention period is unknown.


1. Run `/devspec.clarify` and answer the one recorded decision.

**What to expect.** Clarification resumes the exact saved stage and next command. It does not add new scope or bypass a required review.
