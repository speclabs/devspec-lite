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
  <entry>Completed codebase structure in the new foundation chain, or an explicit targeted update; reject an existing-system baseline request.</entry>
  <outputs>
    <artifact path="devspec/foundation/coding-standards.md" />
  </outputs>
  <transitions>
    <transition outcome="foundation-updated" stage="foundation" run="active" next="devspec.rules" />
    <transition outcome="targeted-update-complete" stage="foundation" run="active" next="return-to-caller" />
  </transitions>
  <closure>Record evidence-backed conventions and one registered next command; blocked evidence routes to devspec.clarify.</closure>
  <actions>Record only standards that change a developer action.</actions>
  <artifact>devspec/foundation/coding-standards.md</artifact>
  <handoff>rules</handoff>
</workflow>
