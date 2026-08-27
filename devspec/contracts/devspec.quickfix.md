# devspec.quickfix

Implement and validate one localized, low-risk enhancement or bug fix.

Invocation: `/devspec.quickfix Fix Orders empty-state text`

<workflow command="devspec.quickfix">
  <purpose>Implement and validate one localized, low-risk enhancement or bug fix.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="work" />
  </protocols>
  <input>One localized bug fix or small enhancement.</input>
  <rules>
    <rule>Select one primary scope: UI, internal API, function/job, library, configuration, tests, or Custom Answer.</rule>
    <rule>Create a QF record, implement, and run focused validation in the same command.</rule>
    <rule>Route public API contracts, database schema or migration, authentication or security work, breaking changes, unrelated concerns, and unresolved risk to story and suggested grooming without editing code.</rule>
  </rules>
  <actions>Select one primary scope, route risky work, then implement and validate directly.</actions>
  <artifact>devspec/quickfixes/QF-###-slug.md</artifact>
  <handoff>complete-or-story</handoff>
</workflow>
