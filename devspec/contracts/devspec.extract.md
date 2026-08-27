# devspec.extract

Backfill concise foundation evidence from an existing repository.

Invocation: `/devspec.extract`

<workflow command="devspec.extract">
  <purpose>Backfill concise foundation evidence from an existing repository.</purpose>
  <protocols>
    <protocol ref="run" />
    <protocol ref="work" />
  </protocols>
  <input>Optional source or current repository.</input>
  <rules>
    <rule>Use owned source, tests, manifests, configuration, and docs; exclude dependencies, caches, and generated output.</rule>
    <rule>Keep one extraction queue item active and write discovered facts to their destination artifact, not queue state.</rule>
    <rule>Reuse recorded working discovery methods and do not repeat a failed method unless its condition changed.</rule>
  </rules>
  <actions>Queue owned source areas; record evidence and reusable discovery outcomes.</actions>
  <artifact>devspec/foundation/extraction-state.md</artifact>
  <handoff>projectcontext</handoff>
</workflow>
