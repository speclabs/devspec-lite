# devspec.diagram

Create one evidence-backed diagram with duplicate checks and durable queue state.

Invocation: `/devspec.diagram runtime architecture format=svg`

<workflow command="devspec.diagram">
  <purpose>Create one evidence-backed diagram with duplicate checks and durable queue state.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="work" />
  </protocols>
  <input>Diagram subject, work item, or format request.</input>
  <rules>
    <rule>Create only evidence-backed, non-duplicate diagrams and persist queue or overview state for recovery.</rule>
    <rule>Default to SVG; generate Mermaid or HTML only when explicitly requested.</rule>
    <rule>Keep labels short and place explanations in supporting Markdown rather than the graphic.</rule>
  </rules>
  <actions>Use SVG by default; write Mermaid or HTML only when requested.</actions>
  <artifact>devspec/architecture/artifact-queue.md</artifact>
  <handoff>continue-current-workflow</handoff>
</workflow>
