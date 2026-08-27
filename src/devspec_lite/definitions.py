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
        "Record subject, type, evidence, format, status, and next in the queue; index completed output in the overview.",
        "Default to SVG with title and description and validate its XML; write Mermaid or HTML only when explicitly requested.",
        "Keep labels short and place explanations in supporting Markdown rather than the graphic.",
    )),
    "quickfix": ("One localized bug fix or small enhancement.", (
        "Select one primary scope: UI, internal API, function/job, library, configuration, tests, or Custom Answer.",
        "Create a QF record, implement, and run focused validation in the same command.",
        "Route public API contracts, database schema or migration, authentication or security work, breaking changes, unrelated concerns, and unresolved risk to story and suggested grooming without editing code.",
    )),
}
COMMAND_DETAILS["diagram"] = (COMMAND_DETAILS["diagram"][0], (COMMAND_DETAILS["diagram"][1][0], "Select the smallest type from diagram-types.md and load only that rendering pattern.", *COMMAND_DETAILS["diagram"][1][1:]))

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
    "overview.md": "# Architecture Overview\n\n## Confirmed boundaries\n\n## Diagram index\n\n| ID | Diagram | Scope | Evidence | Link |\n|---|---|---|---|---|\n",
    "artifact-queue.md": "# Architecture Artifact Queue\n\n| ID | Scope | Type | Subject | Output | Evidence | Status | Next |\n|---|---|---|---|---|---|---|---|\n",
}

ARCHITECTURE_SAMPLE_TEMPLATES = {
    "diagram-sample.md": "# Diagram Sample\n\nUse this short worked example as a pattern; replace every value with repository evidence. Queue status belongs only in `artifact-queue.md`.\n\n| Field | Example |\n|---|---|\n| ID | `DIA-001` |\n| Scope | `workflow` |\n| Type | `flowchart` |\n| Subject | `customer-request-routing` |\n| Output | `devspec/architecture/images/dia-001-customer-request-routing.svg` |\n| Evidence | `devspec/contracts/devspec.quickfix.md`, `devspec/contracts/devspec.story.md` |\n| Confidence | `observed` |\n\n## Queue row\n\n| ID | Scope | Type | Subject | Output | Evidence | Status | Next |\n|---|---|---|---|---|---|---|---|\n| DIA-001 | workflow | flowchart | customer-request-routing | `images/dia-001-customer-request-routing.svg` | contracts above | complete | index in overview |\n\n## Notes\n\nKeep the SVG standalone and concise. Link it from `overview.md`; record assumptions in the work item or supporting Markdown.\n",
    "diagram-sample.svg": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 760 180\" role=\"img\" aria-labelledby=\"title desc\">\n  <title id=\"title\">Sample request routing diagram</title>\n  <desc id=\"desc\">A request is classified as a localized quickfix or a work item.</desc>\n  <style>.t{font:600 15px system-ui,sans-serif;fill:#102a43}.n{fill:#e8f1fb;stroke:#3478c8;stroke-width:2}.a{fill:none;stroke:#3478c8;stroke-width:2;marker-end:url(#m)}</style>\n  <defs><marker id=\"m\" markerWidth=\"10\" markerHeight=\"10\" refX=\"8\" refY=\"3\" orient=\"auto\"><path d=\"M0,0 L0,6 L9,3 z\" fill=\"#3478c8\"/></marker></defs>\n  <rect x=\"24\" y=\"64\" width=\"140\" height=\"48\" rx=\"8\" class=\"n\"/><text x=\"94\" y=\"94\" text-anchor=\"middle\" class=\"t\">Request</text>\n  <rect x=\"280\" y=\"24\" width=\"160\" height=\"48\" rx=\"8\" class=\"n\"/><text x=\"360\" y=\"54\" text-anchor=\"middle\" class=\"t\">quickfix</text>\n  <rect x=\"280\" y=\"112\" width=\"160\" height=\"48\" rx=\"8\" class=\"n\"/><text x=\"360\" y=\"142\" text-anchor=\"middle\" class=\"t\">story</text>\n  <path d=\"M164 78H240V48H280M164 98H240V136H280\" class=\"a\"/><text x=\"196\" y=\"44\" class=\"t\">local</text><text x=\"196\" y=\"132\" class=\"t\">broader</text>\n</svg>\n",
}
_DIAGRAM_HTML_TEMPLATE = {
    "diagram-sample.html": """<!doctype html>\n<html lang="en">\n<head>\n  <meta charset="utf-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1">\n  <title>Sample request routing diagram</title>\n  <style>\n    :root{color-scheme:dark;--bg:#070b18;--panel:#101827;--text:#f8fafc;--muted:#aab8cf;--line:#263653;--grid:#14213a;--accent:#69d8ff}*{box-sizing:border-box}body{margin:0;background:linear-gradient(var(--grid) 1px,transparent 1px),linear-gradient(90deg,var(--grid) 1px,transparent 1px),var(--bg);background-size:32px 32px;color:var(--text);font-family:ui-monospace,SFMono-Regular,Consolas,monospace}main{min-height:100vh;display:grid;place-items:center;padding:28px}article{width:min(100%,1200px);padding:28px;background:var(--panel);border:1px solid var(--line);border-radius:20px;box-shadow:0 22px 44px #0008}header{padding-bottom:20px;margin-bottom:20px;border-bottom:1px solid var(--line)}.eyebrow{color:var(--accent);font-weight:800;font-size:12px;letter-spacing:.14em}h1{margin:8px 0;font-size:clamp(28px,4vw,40px)}p,footer{margin:0;color:var(--muted);line-height:1.5}.diagram{overflow:auto;border:1px solid var(--line);border-radius:14px;background:#070b18}.diagram svg{display:block;width:100%;height:auto}footer{margin-top:14px;font-size:12px}\n  </style>\n</head>\n<body>\n  <main><article><header><div class="eyebrow">DEVSPEC LITE / EXAMPLE</div><h1>Customer request routing</h1><p>Choose Quickfix for one local, low-risk change; otherwise create a work item.</p></header><section class="diagram" aria-label="Customer request routing diagram"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 180" role="img" aria-labelledby="title desc"><title id="title">Sample request routing diagram</title><desc id="desc">A request is classified as a localized quickfix or a work item.</desc><style>.t{font:600 15px system-ui,sans-serif;fill:#f8fafc}.n{fill:#16223a;stroke:#69d8ff;stroke-width:2}.a{fill:none;stroke:#69d8ff;stroke-width:2;marker-end:url(#m)}</style><defs><marker id="m" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#69d8ff"/></marker></defs><rect x="24" y="64" width="140" height="48" rx="8" class="n"/><text x="94" y="94" text-anchor="middle" class="t">Request</text><rect x="280" y="24" width="160" height="48" rx="8" class="n"/><text x="360" y="54" text-anchor="middle" class="t">quickfix</text><rect x="280" y="112" width="160" height="48" rx="8" class="n"/><text x="360" y="142" text-anchor="middle" class="t">story</text><path d="M164 78H240V48H280M164 98H240V136H280" class="a"/><text x="196" y="44" class="t">local</text><text x="196" y="132" class="t">broader</text></svg></section><footer>Example rendering • replace all labels with repository evidence</footer></article></main>\n</body>\n</html>\n""",
}
ARCHITECTURE_SAMPLE_TEMPLATES.update(_DIAGRAM_HTML_TEMPLATE)

_DIAGRAM_GUIDE_TEMPLATE = {
    "diagram-types.md": """# Diagram Types\n\nUse the smallest diagram that makes a confirmed relationship easier to understand. SVG is the default; HTML is an optional presentation shell.\n\n## Shared visual grammar\n\n- Use a dark canvas, subtle grid, framed surface, short eyebrow, title, and evidence-backed subtitle.\n- Draw connectors behind cards. Use restrained accents only to distinguish meaning, not decoration.\n- Keep labels short; use supporting Markdown for details. Every SVG needs a title and description.\n- Include a small legend only when color, line style, or notation is not self-evident.\n\n## Select by question\n\n| Type | Use when the reader asks | Minimum evidence | Show |\n|---|---|---|---|\n| Architecture | What owns or connects to what? | source roots, integration points | boundaries, components, integrations |\n| Domain model | What data concepts relate? | types/schema/contracts | entities, fields only when useful, cardinality |\n| Journey map | What happens to an actor over time? | observed user/system flow | stages, actor actions, system touchpoints, outcome |\n| Mind map | What belongs in this problem space? | scoped discovery | central concern, grouped branches, open risks |\n| Process flow | What steps and gates decide the result? | command contract or observed process | steps, decisions, success and exception paths |\n| Quadrant | How should options be compared? | stated axes and rationale | axes, four meanings, evidence-backed placement |\n| Sequence | Who calls whom, and in what order? | call path/contracts | participants, ordered messages, returns when relevant |\n| State lifecycle | Which states and transitions are allowed? | persisted state/transition rules | start, states, transition labels, terminal or exception states |\n| Timeline | What depends on what, and when? | milestones/dependencies | phases, milestones, dependency or risk links |\n\n## Guardrails\n\nDo not infer entities, callers, timelines, ownership, user sentiment, or priorities. Record uncertain information in the work item or decisions file, not as a factual diagram label.\n\nFor every completed diagram: save the output, update artifact-queue.md, and index the link in overview.md.\n""",
}
ARCHITECTURE_SAMPLE_TEMPLATES.update(_DIAGRAM_GUIDE_TEMPLATE)
_REGENERATED_DIAGRAM_SAMPLES = {
    "diagram-sample.md": """# Diagram Sample\n\nUse this compact worked example as a pattern. Replace every value with repository evidence; queue state belongs only in artifact-queue.md.\n\n## Brief\n\n| Field | Example |\n|---|---|\n| ID | DIA-001 |\n| Type | Process flow |\n| Subject | Customer request routing |\n| Outputs | SVG by default; HTML only when a presentation shell is requested |\n| Evidence | quickfix and story contracts; observed routing rule |\n| Confidence | observed |\n\n## Why this type\n\nA process flow makes the one routing decision, its two outcomes, and the durable record visible without inventing system behavior.\n\n## Queue row\n\n| ID | Scope | Type | Subject | Output | Evidence | Status | Next |\n|---|---|---|---|---|---|---|---|\n| DIA-001 | workflow | process flow | customer-request-routing | images/dia-001-customer-request-routing.svg | contracts above | complete | index in overview |\n\n## Completion\n\nValidate SVG XML, link the completed output in overview.md, and keep uncertainty in the work item or decisions file.\n""",
    "diagram-sample.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 400" role="img" aria-labelledby="title desc"><title id="title">Customer request routing sample</title><desc id="desc">A confirmed request is routed to a localized quickfix or to a traceable work item based on scope and risk.</desc><style>.bg{fill:#070b18}.surface{fill:#101827;stroke:#263653}.lane{fill:#0c1323;stroke:#263653;stroke-dasharray:6 7}.eyebrow{font:700 11px system-ui,sans-serif;letter-spacing:1.8px;fill:#69d8ff}.title{font:700 24px system-ui,sans-serif;fill:#f8fafc}.sub{font:13px system-ui,sans-serif;fill:#aab8cf}.card{fill:#16223a;stroke:#35517c;stroke-width:1.5}.quick{fill:#3a2b10;stroke:#ffc857}.start{fill:#123745;stroke:#39c9d9}.decision{fill:#1d3450;stroke:#69d8ff;stroke-width:2}.node{font:700 14px system-ui,sans-serif;fill:#f8fafc}.meta{font:11px system-ui,sans-serif;fill:#aab8cf}.flow{fill:none;stroke:#69d8ff;stroke-width:2.4;marker-end:url(#a)}.gold{fill:none;stroke:#ffc857;stroke-width:2.4;marker-end:url(#g)}.label{font:700 11px system-ui,sans-serif;fill:#ffd978}.foot{font:600 10px system-ui,sans-serif;letter-spacing:1px;fill:#6f86a8}</style><defs><pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse"><path d="M28 0H0V28" fill="none" stroke="#14213a"/></pattern><marker id="a" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3z" fill="#69d8ff"/></marker><marker id="g" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3z" fill="#ffc857"/></marker></defs><rect class="bg" width="960" height="400"/><rect fill="url(#grid)" width="960" height="400"/><rect class="surface" x="22" y="22" width="916" height="356" rx="18"/><text x="52" y="57" class="eyebrow">DEVSPEC LITE / PROCESS FLOW SAMPLE</text><text x="52" y="88" class="title">Customer request routing</text><text x="52" y="111" class="sub">Use confirmed scope and risk to select one durable route.</text><rect class="lane" x="52" y="138" width="856" height="168" rx="12"/><rect class="card start" x="86" y="205" width="142" height="54" rx="9"/><text x="106" y="228" class="node">Request</text><text x="106" y="247" class="meta">confirmed need</text><polygon class="decision" points="338,190 396,232 338,274 280,232"/><text x="338" y="228" text-anchor="middle" class="node">Local +</text><text x="338" y="246" text-anchor="middle" class="node">low risk?</text><rect class="card quick" x="500" y="164" width="166" height="54" rx="9"/><text x="520" y="187" class="node">quickfix</text><text x="520" y="206" class="meta">focused validation</text><rect class="card" x="500" y="250" width="166" height="54" rx="9"/><text x="520" y="273" class="node">work item</text><text x="520" y="292" class="meta">story to review</text><rect class="card" x="740" y="205" width="130" height="54" rx="9"/><text x="760" y="228" class="node">Record</text><text x="760" y="247" class="meta">evidence + next</text><path class="flow" d="M228 232H280"/><path class="gold" d="M396 211H450V191H500M666 191H705V232H740"/><path class="flow" d="M396 253H450V277H500M666 277H705V232H740"/><text x="420" y="199" class="label">YES</text><text x="416" y="270" class="label">NO / RISK</text><text x="52" y="345" class="foot">EVIDENCE: QUICKFIX + STORY CONTRACTS • TYPE: PROCESS FLOW • STATUS: COMPLETE</text></svg>\n""",
    "diagram-sample.html": """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Customer request routing sample</title><style>:root{color-scheme:dark;--bg:#070b18;--panel:#101827;--text:#f8fafc;--muted:#aab8cf;--line:#263653;--grid:#14213a;--accent:#69d8ff}*{box-sizing:border-box}body{margin:0;background:linear-gradient(var(--grid) 1px,transparent 1px),linear-gradient(90deg,var(--grid) 1px,transparent 1px),var(--bg);background-size:32px 32px;color:var(--text);font-family:ui-monospace,SFMono-Regular,Consolas,monospace}main{min-height:100vh;display:grid;place-items:center;padding:28px}article{width:min(100%,1200px);padding:28px;background:var(--panel);border:1px solid var(--line);border-radius:20px;box-shadow:0 22px 44px #0008}header{padding-bottom:20px;margin-bottom:20px;border-bottom:1px solid var(--line)}.eyebrow{color:var(--accent);font-weight:800;font-size:12px;letter-spacing:.14em}h1{margin:8px 0;font-size:clamp(28px,4vw,40px)}p,footer{margin:0;color:var(--muted);line-height:1.5}.diagram{overflow:auto;border:1px solid var(--line);border-radius:14px;background:#070b18}.diagram img{display:block;width:100%;height:auto}footer{margin-top:14px;font-size:12px}</style></head><body><main><article><header><div class="eyebrow">DEVSPEC LITE / PROCESS FLOW SAMPLE</div><h1>Customer request routing</h1><p>HTML adds a responsive presentation shell around the standalone, evidence-backed SVG.</p></header><section class="diagram" aria-label="Customer request routing diagram"><img src="diagram-sample.svg" alt="Customer request routing: choose Quickfix for one local low-risk request, otherwise create a work item."></section><footer>Example rendering • replace all labels with repository evidence</footer></article></main></body></html>\n""",
}
ARCHITECTURE_SAMPLE_TEMPLATES.update(_REGENERATED_DIAGRAM_SAMPLES)
WORK_ITEM_TEMPLATES = {
    "meta.md": "---\nid: <id>\ntype: feature\nstage: intake\nrun: active\nscope: []\nlast: none\nresume: none\nnext: complete intake\nupdated: <yyyy-mm-dd>\n---\n",
    "story.md": "# Story\n\n## Summary\n\n## Acceptance Criteria\n\n| ID | Observable outcome | Scope |\n|---|---|---|\n\n## Risks and Blockers\n\n## Change Requests\n\n| ID | Request | Status |\n|---|---|---|\n",
    "decisions.md": "# Decisions\n\n| ID | Question | Choices | Recommended | Answer | Status |\n|---|---|---|---|---|---|\n",
    "finalize.md": "# Finalization\n\n## Readiness\n\n## Implementation Brief\n\n## Validation Plan\n\n## Blockers\n",
    "tasks.md": "# Tasks\n\n| ID | Task | Scope | Depends on | Validation | Status |\n|---|---|---|---|---|---|\n",
    "implement.md": "# Implementation\n\n| Task | Changed areas | Validation | Outcome |\n|---|---|---|---|\n",
    "review.md": "# Review\n\n| Finding | Severity | Evidence | Required action |\n|---|---|---|---|\n",
}
