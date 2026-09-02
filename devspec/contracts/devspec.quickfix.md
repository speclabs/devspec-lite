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
    <rule>Select one primary scope: UI, internal API, function/job, library, configuration, tests, or a user-defined bounded scope.</rule>
    <rule>A user-defined scope is allowed only when it is documented as localized and low risk; otherwise route it to story before editing code.</rule>
    <rule>Create a QF record, implement, and run focused validation in the same command.</rule>
    <rule>Route public API contracts, database schema or migration, authentication or security work, breaking changes, unrelated concerns, and unresolved risk to story and suggested grooming without editing code.</rule>
  </rules>
  <entry>One documented localized low-risk request at triage with one primary scope; reject contracts, migrations, security work, breaking changes, unrelated concerns, and unresolved risk.</entry>
  <outputs>
    <artifact path="devspec/quickfixes/QF-###-slug.md" />
  </outputs>
  <transitions>
    <transition outcome="complete" stage="complete" run="complete" next="none" />
    <transition outcome="material-blocker" stage="triage" run="blocked" next="devspec.clarify" />
    <transition outcome="routed" stage="routed" run="complete" next="devspec.story" />
  </transitions>
  <closure>Record the selected route, validation evidence, and terminal next action. Direct implementation is allowed only for the declared low-risk scope.</closure>
  <actions>Select one primary scope, route risky work, then implement and validate directly.</actions>
  <artifact>devspec/quickfixes/QF-###-slug.md</artifact>
  <handoff>none-or-devspec.clarify-or-devspec.story</handoff>
</workflow>
