# devspec.diagram

Create one evidence-backed diagram with duplicate checks and durable queue state.

Invocation: `/devspec.diagram runtime architecture format=svg motion=none|explain`

<workflow command="devspec.diagram">
  <purpose>Create one evidence-backed diagram with duplicate checks and durable queue state.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="work" />
    <protocol ref="repo-access" />
  </protocols>
  <scope>Use for one targeted diagram in the current approved context. An explicit process-flow batch request may generate every queued, non-duplicate process-flow candidate; devspec.extract otherwise owns existing-system diagram discovery, candidate listing, and all-or-selected generation approval.</scope>
  <input>Diagram queue ID, subject, work item, explicit process-flow batch request, format request, or optional `motion=none|explain` in the current repository or an explicitly scoped multi-repository system.</input>
  <rules>
    <rule>Select the diagram type from devspec/architecture/_template/diagram-types.md; load only the needed pattern.</rule>
    <rule>Start each SVG from the matching family-specific template: `architecture-diagram.svg` for system architecture, application landscape, and infrastructure topology; `process-flow-diagram.svg` for process flows; `sequence-diagram.svg` for interactions; `state-lifecycle-diagram.svg` for state behavior; `domain-model-diagram.svg` for domain models; `journey-map-diagram.svg` for journeys; `timeline-plan-diagram.svg` for timelines; `quadrant-analysis-diagram.svg` for quadrants; and `mindmap-diagram.svg` for mind maps.</rule>
    <rule>Create only evidence-backed, non-duplicate diagrams and persist queue or overview state for recovery.</rule>
    <rule>For a multi-repository diagram, use repo-access before reading or validating another repository.</rule>
    <rule>Accept a stable queued `DIA-###` ID or diagram subject, record subject, type, evidence, format, status, and next in the queue, and index completed output in the overview. On an explicit process-flow batch request, generate every queued non-duplicate process-flow candidate, validate each output, update each queue row independently, and leave the caller lifecycle state unchanged.</rule>
    <rule>Default to SVG with title and description and validate its XML; write Mermaid or HTML only when explicitly requested.</rule>
    <rule>Default to `motion=none`. Treat an explicit request for an animated diagram without a motion value as `motion=explain`; reject unsupported motion values.</rule>
    <rule>For `motion=explain`, animate only an evidence-backed sequence, flow, or state transition and follow the opt-in motion guidance in diagram-types.md. Keep the complete meaning visible in the static final frame, provide a reduced-motion result with no information loss, and do not add decorative motion or imply unsupported behavior.</rule>
    <rule>Record animated SVG output in the queue's existing Output field as `svg; motion=explain`. When HTML is also requested, inline the same SVG so its motion and reduced-motion behavior remain intact.</rule>
    <rule>Preserve the template's standalone dark visual contract: 1600 by 900 canvas, subtle grid, framed surface, monospace typography, semantic role colors, connectors behind cards, short labels, and a legend only when its notation needs explanation. Replace every placeholder before completion and do not use external assets, scripts, iframes, foreign objects, remote fonts, unresolved placeholders, or unsupported diagram families.</rule>
    <rule>Keep labels short and place explanations in supporting Markdown rather than the graphic. Keep flowcharts to one primary concern and split an overloaded diagram at a confirmed responsibility boundary; use `sequence` for ordered interactions and the process-flow template for end-to-end operational behavior.</rule>
    <rule>For process flows, make the happy path visually obvious; distinguish start or end, manual, automated, integration, decision, exception, and artifact steps; label loop-backs; and draw exception paths as labeled dashed rose arrows that terminate or reconnect to a named step.</rule>
  </rules>
  <entry>One approved diagram subject in the caller's current scope with duplicate check and queue access; reject requests that would alter caller lifecycle state.</entry>
  <outputs>
    <artifact path="devspec/architecture/artifact-queue.md" />
    <artifact path="devspec/architecture/overview.md" />
  </outputs>
  <transitions>
    <transition outcome="diagram-complete" stage="caller" run="active" next="return-to-caller" />
    <transition outcome="evidence-blocked" stage="caller" run="blocked" next="devspec.clarify" />
  </transitions>
  <closure>Validate the queued output, including finite animation and final-frame and reduced-motion completeness when motion is requested; index only completed diagrams, and leave the caller's saved stage unchanged.</closure>
  <actions>Use static SVG by default; add explanatory motion, Mermaid, or HTML only when requested.</actions>
  <artifact>devspec/architecture/artifact-queue.md</artifact>
  <handoff>return-to-caller</handoff>
</workflow>
