# devspec.finalize

Produce a concise readiness brief and validation plan.

Invocation: `/devspec.finalize [work-item-id]`

<workflow command="devspec.finalize">
  <purpose>Produce a concise readiness brief and validation plan.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="state" />
    <protocol ref="current-work-item" />
    <protocol ref="revision" />
    <protocol ref="work" />
    <protocol ref="security" />
  </protocols>
  <scope>Use to decide whether the current scope revision is buildable and to record its brief and validation plan. This command plans readiness only; devspec.tasks sequences the work and devspec.implement changes code.</scope>
  <input>An optional work-item ID or a groomed current draft.</input>
  <rules>
    <rule>Read only the current-revision story and decisions, the finalization traces' direct sources in coding standards, codebase structure, rules, workflow rules, constitution, and the architecture queue or overview. Do not scan unrelated work items, unrelated code areas, or historical revisions beyond the superseded sections of this work item.</rule>
    <rule>Check only material readiness gaps: scope, criteria, behavior, data, integration, security, compliance, validation, and delivery constraints.</rule>
    <rule>Mark ready only when remaining gaps cannot materially change implementation or validation; otherwise create one material blocker question.</rule>
    <rule>Classify every accepted material decision as work-item-local or reusable. Promote a reusable business or validation decision to devspec/foundation/workflow-rules.md with a stable rule ID and source decision link; promote a reusable engineering constraint to devspec/foundation/rules.md. Record the resulting canonical rule link in decisions.md.</rule>
    <rule>Record one compact foundation trace for the relevant coding conventions, owned areas and boundaries, canonical rules, applicable active `CP-###` principles, and the OWASP categories the change touches. Record a separate architecture and diagram trace for relevant overview entries, completed diagrams, or queued candidates, including implementation and validation impact; no diagram is required.</rule>
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
</workflow>
