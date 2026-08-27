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
  <input>Product context or a confirmed source.</input>
  <rules>
    <rule>Capture purpose, users, outcomes, boundaries, and delivery context only.</rule>
    <rule>Mark each material statement confirmed, observed, inferred, or blocked.</rule>
  </rules>
  <actions>Update only confirmed or observed product context.</actions>
  <artifact>devspec/foundation/project-context.md</artifact>
  <handoff>techstack</handoff>
</workflow>
