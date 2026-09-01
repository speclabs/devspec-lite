# devspec.techstack

Capture evidence-backed runtime, frameworks, data, tooling, and delivery constraints.

Invocation: `/devspec.techstack`

<workflow command="devspec.techstack">
  <purpose>Capture evidence-backed runtime, frameworks, data, tooling, and delivery constraints.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="work" />
  </protocols>
  <input>Stack evidence, target stack, or delivery constraint.</input>
  <rules>
    <rule>Inspect manifests, lockfiles, runtime configuration, and CI before asking material questions.</rule>
    <rule>Record runtime, languages, frameworks, data stores, tooling, supported versions, and material constraints.</rule>
  </rules>
  <actions>Inspect manifests and configuration before asking for missing material facts.</actions>
  <artifact>devspec/foundation/tech-stack.md</artifact>
  <handoff>codebase-structure</handoff>
</workflow>
