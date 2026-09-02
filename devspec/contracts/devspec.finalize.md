# devspec.finalize

Produce a concise readiness brief and validation plan.

Invocation: `/devspec.finalize [work-item-id]`

<workflow command="devspec.finalize">
  <purpose>Produce a concise readiness brief and validation plan.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="current-work-item" />
    <protocol ref="work" />
  </protocols>
  <input>An optional work-item ID or a groomed current draft.</input>
  <rules>
    <rule>Check only material readiness gaps: scope, criteria, behavior, data, integration, security, compliance, validation, and delivery constraints.</rule>
    <rule>Mark ready only when remaining gaps cannot materially change implementation or validation; otherwise create one material blocker question.</rule>
    <rule>Classify every accepted material decision as work-item-local or reusable. Promote a reusable business or validation decision to devspec/foundation/workflow-rules.md with a stable rule ID and source decision link; promote a reusable engineering constraint to devspec/foundation/rules.md. Record the resulting canonical rule link in decisions.md.</rule>
    <rule>Record one compact foundation trace for the relevant coding conventions, owned areas and boundaries, canonical rules, and OWASP categories. For every relevant OWASP category, state applicability, required control, and planned project-native evidence.</rule>
    <rule>Do not mark ready while a relevant OWASP category, required control, or security-validation plan is unresolved.</rule>
    <rule>Write a concise implementation brief and validation plan, not implementation code.</rule>
  </rules>
  <entry>Active work item at finalization with a complete current-revision story; reject stale finalization, blocked work, or incomplete draft scope.</entry>
  <outputs>
    <artifact path="devspec/work-items/&lt;id&gt;/finalize.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/meta.md" />
  </outputs>
  <transitions>
    <transition outcome="ready" stage="tasks" run="active" next="devspec.tasks" />
    <transition outcome="material-blocker" stage="finalization" run="blocked" next="devspec.clarify" />
  </transitions>
  <closure>Stamp the readiness brief with the current scope revision. Preserve earlier revision sections as superseded history.</closure>
  <actions>Scan only material readiness gaps; do not invent implementation detail.</actions>
  <artifact>devspec/work-items/&lt;id&gt;/finalize.md</artifact>
  <handoff>devspec.clarify-or-devspec.tasks</handoff>
</workflow>
