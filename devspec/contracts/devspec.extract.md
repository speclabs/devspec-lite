# devspec.extract

Build a complete evidence-backed baseline for one existing repository or an explicitly scoped multi-repository system.

Invocation: `/devspec.extract`

<workflow command="devspec.extract">
  <purpose>Inspect the approved existing system end-to-end, produce its technical, business, workflow, and rule baseline, and prepare an evidence-backed diagram candidate list for explicit generation approval.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="work" />
    <protocol ref="repo-access" />
  </protocols>
  <input>Explicitly confirmed source repository scope, or current canonical evidence that names each repository's role, local path, and allowed access.</input>
  <rules>
    <rule>Treat the agent's current workspace or scaffolding directory as a proposed source target, never proof. Before inspecting source, obtain either an explicit user confirmation that names every source repository, role, path, and read, edit, and validation permission, or current canonical evidence that records those facts. If neither exists, first collect one repository path at a time, then ask one access question after each confirmed path; record the accepted source scope in `devspec/foundation/codebase-structure.md` before reading source. Later commands may use that current record as scope evidence.</rule>
    <rule>Inspect owned source, tests, manifests, configuration, infrastructure, scripts, and docs; exclude dependencies, caches, generated output, and repositories outside approved scope.</rule>
    <rule>For multi-repository work, record every repository role, path, access boundary, and evidence before reading, editing, or validating it.</rule>
    <rule>For every approved repository, record an observed repository layout in `devspec/foundation/codebase-structure.md`: a readable `text` tree rooted at its confirmed local path that includes solution or manifest files, owned source and test roots, meaningful modules, configuration, and integration or migration locations. Keep the tree representative rather than exhaustive; exclude dependencies, caches, generated output, and secrets.</rule>
    <rule>Ask one clarification for every unresolved material question. Label all durable findings confirmed, observed, inferred, or blocked; do not invent roles, workflows, business rules, validation rules, integrations, or diagrams.</rule>
    <rule>Initialize and complete every listed foundation artifact from its template when missing: project context, technology stack, codebase structure, coding standards with followable local examples, rules, technical baseline, roles, workflows, workflow rules, extraction state, exploration state, and coverage.</rule>
    <rule>For each observed coding convention that changes implementation or review behavior, assign a stable `CS-###` ID and capture one or more concise, concrete local code or test snippets as `EX-###` entries under `## Standards Examples`. Each entry names the applicable standard IDs, source location, and fenced language-appropriate code; one example may apply to multiple standards. Record a relevant anti-pattern when repository evidence supports one.</rule>
    <rule>Populate the single OWASP Top 10:2025 baseline in rules.md from observed code, dependencies, configuration, deployment, and access evidence. Record controls, gaps, and unknowns; do not infer an internal-only or limited-access boundary without enforceable evidence.</rule>
    <rule>For every confirmed business workflow, record its business area, participating roles, trigger, outcome, business rules, validation rules, evidence, and applicable exceptions.</rule>
    <rule>Identify applicable evidence-backed diagram candidates: system architecture, application landscape, infrastructure topology, integration sequence or context, and a journey or process-flow diagram for every confirmed workflow. Add domain-model or state-lifecycle candidates only when evidence supports them.</rule>
    <rule>Record every candidate in the diagram queue with its stable ID, type, subject, evidence, output format, duplicate-check result, status, and next action. Keep the overview limited to completed diagram links; do not generate an SVG or add an overview entry during extraction before the user answers the post-extraction diagram question.</rule>
    <rule>After all foundation extraction outputs are complete, show the user or developer the complete candidate list. When one or more candidates exist, ask exactly one interactive confirmation: "Do you want me generate all the possible diagrams?" Offer: `Yes — generate all listed diagrams`, `No — prepare the list only`, `Choose diagrams — enter the IDs or subjects to generate`, and `Custom Answer`. Recommend `No — prepare the list only` when no generation preference is already confirmed. Each choice must include a concise example.</rule>
    <rule>If the user or developer chooses `Yes`, generate every listed non-duplicate candidate, validate each SVG XML file, update its queue status, and index completed durable output in the overview. If they choose `No`, leave the evidence-backed candidate list prepared in the queue without generating diagrams. If they choose `Choose diagrams`, generate only the entered non-duplicate IDs or subjects and leave the remainder listed in the queue.</rule>
    <rule>Whenever the candidate list is shown, tell the user or developer that any listed diagram can be generated later with `/devspec.diagram &lt;DIA-ID-or-subject&gt;`; include one concrete example such as `/devspec.diagram DIA-002`.</rule>
    <rule>Keep one extraction coverage item active and write discovered facts to their destination artifact, not queue state. Reuse recorded discovery methods and do not repeat a failed method unless its condition changed.</rule>
  </rules>
  <entry>Existing system with confirmed source scope and no active incompatible extraction run; reject new-repository foundation authoring or an assumed workspace target.</entry>
  <transitions>
    <transition outcome="foundation-ready" stage="foundation" run="active" next="devspec.story" />
    <transition outcome="evidence-blocked" stage="foundation" run="blocked" next="devspec.clarify" />
  </transitions>
  <closure>Complete the listed baseline outputs and present the diagram candidate list before routing to story. Record every material evidence gap as blocked with a continuation condition, and preserve ungenerated candidates for `/devspec.diagram`.</closure>
  <outputs>
    <artifact path="devspec/foundation/project-context.md" />
    <artifact path="devspec/foundation/tech-stack.md" />
    <artifact path="devspec/foundation/codebase-structure.md" />
    <artifact path="devspec/foundation/coding-standards.md" />
    <artifact path="devspec/foundation/rules.md" />
    <artifact path="devspec/foundation/technical-baseline.md" />
    <artifact path="devspec/foundation/roles.md" />
    <artifact path="devspec/foundation/workflows.md" />
    <artifact path="devspec/foundation/workflow-rules.md" />
    <artifact path="devspec/foundation/extraction-state.md" />
    <artifact path="devspec/foundation/exploration-state.md" />
    <artifact path="devspec/foundation/extraction-coverage.md" />
    <artifact path="devspec/architecture/artifact-queue.md" />
    <artifact path="devspec/architecture/overview.md" />
  </outputs>
  <actions>Confirm and record source scope before inspection, then complete the existing-system baseline, prepare and present the applicable diagram list, obtain the one diagram-generation confirmation, and record remaining gaps or blocked evidence.</actions>
  <artifact>devspec/foundation/extraction-coverage.md</artifact>
  <handoff>devspec.story-or-devspec.clarify</handoff>
</workflow>
