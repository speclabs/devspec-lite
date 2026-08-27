"""Small, canonical definitions used to render framework files."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Command:
    name: str
    purpose: str
    example: str
    protocols: tuple[str, ...]
    actions: str
    artifact: str
    handoff: str


COMMANDS: tuple[Command, ...] = (
    Command("extract", "Backfill concise foundation evidence from an existing repository.", "/devspec.extract", ("run", "work"), "Queue owned source areas; record evidence and reusable discovery outcomes.", "foundation/extraction-state.md", "projectcontext"),
    Command("projectcontext", "Capture product purpose, users, outcomes, and scope boundaries.", "/devspec.projectcontext", ("ask", "run", "work"), "Update only confirmed or observed product context.", "foundation/project-context.md", "techstack"),
    Command("techstack", "Capture evidence-backed runtime, frameworks, data, tooling, and delivery constraints.", "/devspec.techstack", ("ask", "run", "work"), "Inspect manifests and configuration before asking for missing material facts.", "foundation/tech-stack.md", "codebase-structure"),
    Command("codebase-structure", "Capture owned source roots, module boundaries, integrations, and repository access.", "/devspec.codebase-structure", ("ask", "run", "work", "repo-access"), "Map owned areas and use repo-access only when more than one repository is involved.", "foundation/codebase-structure.md", "coding-standards"),
    Command("coding-standards", "Capture short, evidence-backed conventions and anti-patterns.", "/devspec.coding-standards", ("ask", "run", "work"), "Record only standards that change a developer action.", "foundation/coding-standards.md", "rules"),
    Command("rules", "Capture non-negotiable engineering, security, compliance, delivery, and accessibility rules.", "/devspec.rules", ("ask", "run", "work"), "Keep hard constraints distinct from ordinary coding conventions.", "foundation/rules.md", "story"),
    Command("story", "Create one concise work-item intake from a request or provider reference.", "/devspec.story Add customer export", ("ask", "run", "work"), "Choose one work item, validate its target folder, and preserve finalized baselines.", "work-items/<id>/story.md", "grooming-or-finalize"),
    Command("grooming", "Make one draft story buildable through scoped review and targeted questions.", "/devspec.grooming GHUB-123-customer-export", ("ask", "run", "work"), "Improve draft story and decisions in place; suggest only material questions.", "work-items/<id>/story.md", "clarify-or-finalize"),
    Command("clarify", "Resolve one active blocker and resume its originating stage.", "/devspec.clarify GHUB-123-customer-export", ("ask", "run"), "Ask the recorded high-priority question, append the resolution, and return to the saved next action.", "work-items/<id>/decisions.md", "resume-origin"),
    Command("changerequest", "Append one related post-finalization requirement without rewriting history.", "/devspec.changerequest GHUB-123 Add JSON export", ("ask", "run", "work"), "Classify scope as related or independent; append the next CR identifier when related.", "work-items/<id>/story.md", "finalize"),
    Command("finalize", "Produce a concise readiness brief and validation plan.", "/devspec.finalize GHUB-123-customer-export", ("ask", "run", "work"), "Scan only material readiness gaps; do not invent implementation detail.", "work-items/<id>/finalize.md", "clarify-or-tasks"),
    Command("tasks", "Create ordered, independently verifiable implementation tasks.", "/devspec.tasks GHUB-123-customer-export", ("ask", "run", "work", "repo-access"), "Trace tasks to readiness items and validation evidence; sequence dependencies first.", "work-items/<id>/tasks.md", "implement"),
    Command("implement", "Implement pending ready tasks with focused checkpoints and validation.", "/devspec.implement GHUB-123-customer-export", ("ask", "run", "work", "repo-access"), "Stay within finalized scope; checkpoint before edits and validation.", "work-items/<id>/implement.md", "review"),
    Command("review", "Review changed work against readiness, tasks, and validation evidence.", "/devspec.review GHUB-123-customer-export", ("ask", "run", "work"), "Record actionable findings; do not silently change implementation code.", "work-items/<id>/review.md", "implement-or-close"),
    Command("diagram", "Create one evidence-backed diagram with duplicate checks and durable queue state.", "/devspec.diagram runtime architecture format=svg", ("ask", "run", "work"), "Use SVG by default; write Mermaid or HTML only when requested.", "architecture/artifact-queue.md", "continue-current-workflow"),
    Command("quickfix", "Implement and validate one localized, low-risk enhancement or bug fix.", "/devspec.quickfix Fix Orders empty-state text", ("ask", "run", "work"), "Select one primary scope, route risky work, then implement and validate directly.", "quickfixes/QF-###-slug.md", "complete-or-story"),
)

# Command-local rules deliberately stay with their command. They are not loaded by
# unrelated workflows and replace a broad shared-pattern document.
COMMAND_DETAILS: dict[str, tuple[str, tuple[str, ...]]] = {
    "extract": ("Optional source or current repository.", (
        "Use owned source, tests, manifests, configuration, and docs; exclude dependencies, caches, and generated output.",
        "Keep one extraction queue item active and write discovered facts to their destination artifact, not queue state.",
        "Reuse recorded working discovery methods and do not repeat a failed method unless its condition changed.",
    )),
    "projectcontext": ("Product context or a confirmed source.", (
        "Capture purpose, users, outcomes, boundaries, and delivery context only.",
        "Mark each material statement confirmed, observed, inferred, or blocked.",
    )),
    "techstack": ("Stack evidence, target stack, or delivery constraint.", (
        "Inspect manifests, lockfiles, runtime configuration, and CI before asking questions.",
        "Record runtime, languages, frameworks, data stores, tooling, supported versions, and material constraints.",
    )),
    "codebase-structure": ("Repository layout, work area, integration, or multi-repository context.", (
        "Map owned source roots, boundaries, integration points, and validation locations.",
        "Load repo-access only when work crosses repositories; never infer edit access.",
    )),
    "coding-standards": ("Observed conventions or approved standards.", (
        "Keep only conventions that change implementation or review behavior.",
        "Record a short local example and an anti-pattern when evidence supports both.",
    )),
    "rules": ("Hard engineering, compliance, security, delivery, or accessibility constraints.", (
        "Keep non-negotiable rules separate from ordinary coding conventions.",
        "State enforcement or validation for each rule when known.",
    )),
    "story": ("One provider reference or one manual feature, bug, security issue, or task.", (
        "Handle exactly one work item; ask a selection question when input contains independent items.",
        "Create folders as optional-provider-prefix plus numeric ID plus kebab-case title; do not rename legacy folders automatically.",
        "Before finalization, update the baseline; after finalization, route related scope to changerequest and unrelated scope to a linked item.",
    )),
    "grooming": ("One draft work-item identifier or clear current draft.", (
        "Read only the draft, relevant foundation artifacts, selected code area, and direct dependencies.",
        "Improve behavior, acceptance criteria, scope, technical constraints, edge cases, dependencies, compatibility risks, and blockers in place.",
        "Do not groom finalized scope; route new scope to changerequest.",
    )),
    "clarify": ("One work item with an active recorded blocker or question.", (
        "Resolve the highest-priority open decision only and append its answer to decisions.md.",
        "Do not accept scope changes after finalization; route them to changerequest.",
        "Return to the saved stage and next action after resolution.",
    )),
    "changerequest": ("A finalized-or-later work item and one related missing requirement.", (
        "Append the next CR-### entry and CR-scoped criteria; never rewrite baseline evidence.",
        "Ask whether an ambiguous request is related or a new linked work item.",
    )),
    "finalize": ("A groomed or otherwise complete draft work item.", (
        "Check only material readiness gaps: scope, criteria, behavior, data, integration, security, compliance, validation, and delivery constraints.",
        "Mark ready only when remaining gaps cannot materially change implementation or validation; otherwise create one blocker question.",
        "Write a concise implementation brief and validation plan, not implementation code.",
    )),
    "tasks": ("A ready finalization brief.", (
        "Each task names scope, dependency, source justification, validation, and done condition.",
        "Order dependencies before dependents and split only work too broad to validate safely.",
    )),
    "implement": ("Ready finalization and pending task records.", (
        "Confirm every task is in finalized scope, unblocked, and ordered before editing code.",
        "Checkpoint before edits and focused validation; stop for a material ambiguity instead of expanding scope.",
        "Record changed areas and validation evidence after each meaningful task.",
    )),
    "review": ("Finalization, tasks, implementation record, and changed work.", (
        "Compare changed work to approved scope, task source coverage, and validation evidence.",
        "Write findings only; do not silently edit implementation code.",
    )),
    "diagram": ("Diagram subject, work item, or format request.", (
        "Create only evidence-backed, non-duplicate diagrams and persist queue or overview state for recovery.",
        "Default to SVG; generate Mermaid or HTML only when explicitly requested.",
        "Keep labels short and place explanations in supporting Markdown rather than the graphic.",
    )),
    "quickfix": ("One localized bug fix or small enhancement.", (
        "Select one primary scope: UI, internal API, function/job, library, configuration, tests, or Custom Answer.",
        "Create a QF record, implement, and run focused validation in the same command.",
        "Route public API contracts, database schema or migration, authentication or security work, breaking changes, unrelated concerns, and unresolved risk to story and suggested grooming without editing code.",
    )),
}

PROTOCOLS = {
    "ask": """<protocol id=\"ask\">\n  <trigger>Ask only when repository evidence and durable artifacts cannot resolve a material fact.</trigger>\n  <checkpoint>Persist question ID, evidence, impact, choices, recommendation, and resume action before waiting.</checkpoint>\n  <interaction count=\"one\" mode=\"interactive\">\n    <choices>Offer two to five meaningful exclusive choices, each with a short example.</choices>\n    <recommendation required=\"true\" />\n    <custom-answer required=\"true\" />\n    <fallback>Render identical text choices only when the host lacks interactive controls.</fallback>\n  </interaction>\n  <resolution>Append the answer to decisions.md, update the affected artifact, then continue with one next action.</resolution>\n</protocol>""",
    "run": """<protocol id=\"run\">\n  <preflight>Validate required input, target artifact, stage, and access before output.</preflight>\n  <checkpoint>Save stage, run state, last action, resume reference, and next action before questions, edits, validation, retries, or handoff.</checkpoint>\n  <resume>Resume paused work when prerequisites hold; ask one interactive resume question for stopped or ambiguous work.</resume>\n  <blocked>Record blocker and continuation condition; retry only when that condition changes or the user directs it.</blocked>\n  <closure>Report artifact, outcome, blocker if any, and exactly one registered next action.</closure>\n</protocol>""",
    "work": """<protocol id=\"work\">\n  <scope>Select the smallest affected area and direct dependencies; exclude generated, dependency, cache, and unrelated source.</scope>\n  <evidence>Label durable facts as confirmed, observed, inferred, or blocked.</evidence>\n  <change>Prefer existing patterns and the smallest safe change; do not add speculative abstractions or dependencies.</change>\n  <artifacts>Update targeted sections only, link instead of duplicate, and preserve user-authored useful content.</artifacts>\n</protocol>""",
    "repo-access": """<protocol id=\"repo-access\">\n  <when>Load only when a task depends on more than one repository.</when>\n  <validate>Confirm repository role, local path, workspace availability, and access requirement before edits or validation.</validate>\n  <respect>Never edit or validate reference-only, validation-only, release-coordination, or unavailable repositories without explicit scope change.</respect>\n</protocol>""",
}

FOUNDATION_TEMPLATES = {
    "project-context.md": "# Project Context\n\n- Purpose:\n- Users:\n- Outcomes:\n- Scope boundaries:\n- Delivery context:\n",
    "tech-stack.md": "# Technology Stack\n\n| Area | Confirmed stack | Evidence | Constraint |\n|---|---|---|---|\n",
    "codebase-structure.md": "# Codebase Structure\n\n| Area | Ownership | Boundary | Evidence |\n|---|---|---|---|\n\n## Repositories\n\n| Repository | Role | Access | Path |\n|---|---|---|---|\n",
    "coding-standards.md": "# Coding Standards\n\n| Convention | Evidence | Example | Avoid |\n|---|---|---|---|\n",
    "rules.md": "# Rules\n\n| Rule | Why | Enforcement |\n|---|---|---|\n",
    "extraction-state.md": "# Extraction State\n\n| Item | Status | Evidence | Next |\n|---|---|---|---|\n",
    "discovery-exclusions.md": "# Discovery Exclusions\n\n- Exclude dependencies, generated output, caches, coverage, VCS internals, and temporary files.\n- Include owned source, tests, manifests, configuration, infrastructure, scripts, and docs.\n",
    "exploration-state.md": "# Exploration State\n\n| Goal | Method | Outcome | Reuse or retry condition |\n|---|---|---|---|\n",
    "provider-integrations.md": "# Provider Integrations\n\n| Provider | Resolution method | Confirmation required |\n|---|---|---|\n",
}

ARCHITECTURE_TEMPLATES = {
    "overview.md": "# Architecture Overview\n\n## Confirmed boundaries\n\n## Diagram index\n\n| Diagram | Scope | Evidence | Status |\n|---|---|---|---|\n",
    "artifact-queue.md": "# Architecture Artifact Queue\n\n| ID | Subject | Type | Evidence | Format | Status | Next |\n|---|---|---|---|---|---|---|\n",
}

WORK_ITEM_TEMPLATES = {
    "meta.md": "---\nid: <id>\ntype: feature\nstage: intake\nrun: active\nscope: []\nlast: none\nresume: none\nnext: complete intake\nupdated: <yyyy-mm-dd>\n---\n",
    "story.md": "# Story\n\n## Summary\n\n## Acceptance Criteria\n\n| ID | Observable outcome | Scope |\n|---|---|---|\n\n## Risks and Blockers\n\n## Change Requests\n\n| ID | Request | Status |\n|---|---|---|\n",
    "decisions.md": "# Decisions\n\n| ID | Question | Choices | Recommended | Answer | Status |\n|---|---|---|---|---|---|\n",
    "finalize.md": "# Finalization\n\n## Readiness\n\n## Implementation Brief\n\n## Validation Plan\n\n## Blockers\n",
    "tasks.md": "# Tasks\n\n| ID | Task | Scope | Depends on | Validation | Status |\n|---|---|---|---|---|---|\n",
    "implement.md": "# Implementation\n\n| Task | Changed areas | Validation | Outcome |\n|---|---|---|---|\n",
    "review.md": "# Review\n\n| Finding | Severity | Evidence | Required action |\n|---|---|---|---|\n",
}
