# devspec.extract

Build a complete evidence-backed baseline for one existing repository or an explicitly scoped multi-repository system.

Invocation: `/devspec.extract`

<workflow command="devspec.extract">
  <purpose>Inspect the approved existing system end-to-end and produce its technical, business, workflow, rule, and diagram baseline without requiring separate foundation or diagram commands.</purpose>
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
    <rule>Ask one clarification for every unresolved material question. Label all durable findings confirmed, observed, inferred, or blocked; do not invent roles, workflows, business rules, validation rules, integrations, or diagrams.</rule>
    <rule>Initialize and complete every listed foundation artifact from its template when missing: project context, technology stack, codebase structure, coding standards with local examples, rules, technical baseline, roles, workflows, workflow rules, extraction state, exploration state, and coverage.</rule>
    <rule>Populate the single OWASP Top 10:2025 baseline in rules.md from observed code, dependencies, configuration, deployment, and access evidence. Record controls, gaps, and unknowns; do not infer an internal-only or limited-access boundary without enforceable evidence.</rule>
    <rule>For every confirmed business workflow, record its business area, participating roles, trigger, outcome, business rules, validation rules, evidence, and applicable exceptions.</rule>
    <rule>Create the applicable evidence-backed SVG baseline diagrams directly: system architecture; application landscape; infrastructure topology; integration sequence or context; and a journey or process-flow diagram for every confirmed workflow. Add domain-model or state-lifecycle diagrams only when evidence supports them.</rule>
    <rule>Use the diagram queue and overview as the only diagram record. Validate every SVG XML file, record its evidence and status, and do not create duplicate diagrams.</rule>
    <rule>Keep one extraction coverage item active and write discovered facts to their destination artifact, not queue state. Reuse recorded discovery methods and do not repeat a failed method unless its condition changed.</rule>
  </rules>
  <entry>Existing system with confirmed source scope and no active incompatible extraction run; reject new-repository foundation authoring or an assumed workspace target.</entry>
  <transitions>
    <transition outcome="foundation-ready" stage="foundation" run="active" next="devspec.story" />
    <transition outcome="evidence-blocked" stage="foundation" run="blocked" next="devspec.clarify" />
  </transitions>
  <closure>Complete the listed baseline outputs before routing to story. Record every material evidence gap as blocked with a continuation condition.</closure>
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
  <actions>Confirm and record source scope before inspection, then complete the existing-system baseline, create applicable SVG diagrams, and record remaining gaps or blocked evidence.</actions>
  <artifact>devspec/foundation/extraction-coverage.md</artifact>
  <handoff>devspec.story-or-devspec.clarify</handoff>
</workflow>