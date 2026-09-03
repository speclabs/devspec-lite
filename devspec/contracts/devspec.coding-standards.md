# devspec.coding-standards

Capture concise, reusable coding conventions, examples, and anti-patterns.

Invocation: `/devspec.coding-standards`

<workflow command="devspec.coding-standards">
  <purpose>Capture concise, reusable coding conventions, followable examples, and anti-patterns from source evidence or developer-defined standards.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="work" />
  </protocols>
  <scope>Use for new-repository foundation authoring or an explicitly requested targeted update. Use devspec.extract, not this command, to establish an existing-system baseline.</scope>
  <input>Observed conventions, approved standards, or developer-defined custom standards with examples to follow.</input>
  <rules>
    <rule>Keep only conventions that change implementation or review behavior.</rule>
    <rule>For an observed convention, cite its local source evidence and record a concise code or test example developers can follow. Record an anti-pattern when repository evidence supports one.</rule>
    <rule>Accept a custom standard explicitly supplied or approved by a developer even when no local source example exists. Mark it developer-defined rather than observed, record its approval or request as evidence, and include a concise illustrative example for future implementations.</rule>
  </rules>
  <entry>Completed codebase structure in the new foundation chain, or an explicit targeted update; reject an existing-system baseline request.</entry>
  <outputs>
    <artifact path="devspec/foundation/coding-standards.md" />
  </outputs>
  <transitions>
    <transition outcome="foundation-updated" stage="foundation" run="active" next="devspec.rules" />
    <transition outcome="targeted-update-complete" stage="foundation" run="active" next="return-to-caller" />
  </transitions>
  <closure>Record each retained standard with its origin, a followable example, and an anti-pattern when applicable, then register one next command; blocked evidence routes to devspec.clarify.</closure>
  <actions>Record only standards that change a developer action, preserving developer-defined examples as reusable implementation guidance.</actions>
  <artifact>devspec/foundation/coding-standards.md</artifact>
  <handoff>rules</handoff>
</workflow>
