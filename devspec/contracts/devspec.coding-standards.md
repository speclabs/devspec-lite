# devspec.coding-standards

Capture short, evidence-backed conventions and anti-patterns.

Invocation: `/devspec.coding-standards`

<workflow command="devspec.coding-standards">
  <purpose>Capture short, evidence-backed conventions and anti-patterns.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="work" />
  </protocols>
  <scope>Use for new-repository foundation authoring or an explicitly requested targeted update. Use devspec.extract, not this command, to establish an existing-system baseline.</scope>
  <input>Observed conventions or approved standards.</input>
  <rules>
    <rule>Keep only conventions that change implementation or review behavior.</rule>
    <rule>Record a short local example and an anti-pattern when evidence supports both.</rule>
  </rules>
  <actions>Record only standards that change a developer action.</actions>
  <artifact>devspec/foundation/coding-standards.md</artifact>
  <handoff>rules</handoff>
</workflow>
