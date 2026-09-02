# devspec.projectcontext

Capture product purpose, users, outcomes, and scope boundaries.

Invocation: `/devspec.projectcontext`

<workflow command="devspec.projectcontext">
  <purpose>Capture product purpose, users, outcomes, and scope boundaries.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="work" />
  </protocols>
  <scope>Use for new-repository foundation authoring or an explicitly requested targeted update. Use devspec.extract, not this command, to establish an existing-system baseline.</scope>
  <input>Product context or a confirmed source.</input>
  <rules>
    <rule>Capture purpose, users, outcomes, boundaries, and delivery context only.</rule>
    <rule>Mark each material statement confirmed, observed, inferred, or blocked.</rule>
  </rules>
  <entry>New foundation chain with project context absent, or an explicit targeted update; reject an existing-system baseline request.</entry>
  <outputs>
    <artifact path="devspec/foundation/project-context.md" />
  </outputs>
  <transitions>
    <transition outcome="foundation-updated" stage="foundation" run="active" next="devspec.techstack" />
    <transition outcome="targeted-update-complete" stage="foundation" run="active" next="return-to-caller" />
  </transitions>
  <closure>Record the foundation state and one registered next command; blocked evidence routes to devspec.clarify.</closure>
  <actions>Update product context with clearly labeled confirmed, observed, inferred, or blocked statements.</actions>
  <artifact>devspec/foundation/project-context.md</artifact>
  <handoff>techstack</handoff>
</workflow>
