# devspec.finalize

Produce a concise readiness brief and validation plan.

Invocation: `/devspec.finalize GHUB-123-customer-export`

<workflow command="devspec.finalize">
  <purpose>Produce a concise readiness brief and validation plan.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="work" />
  </protocols>
  <input>A groomed or otherwise complete draft work item.</input>
  <rules>
    <rule>Check only material readiness gaps: scope, criteria, behavior, data, integration, security, compliance, validation, and delivery constraints.</rule>
    <rule>Mark ready only when remaining gaps cannot materially change implementation or validation; otherwise create one blocker question.</rule>
    <rule>Write a concise implementation brief and validation plan, not implementation code.</rule>
  </rules>
  <actions>Scan only material readiness gaps; do not invent implementation detail.</actions>
  <artifact>devspec/work-items/&lt;id&gt;/finalize.md</artifact>
  <handoff>clarify-or-tasks</handoff>
</workflow>
