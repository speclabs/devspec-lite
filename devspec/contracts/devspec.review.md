# devspec.review

Review changed work against readiness, tasks, and validation evidence.

Invocation: `/devspec.review GHUB-123-customer-export`

<workflow command="devspec.review">
  <purpose>Review changed work against readiness, tasks, and validation evidence.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="work" />
  </protocols>
  <input>Finalization, tasks, implementation record, and changed work.</input>
  <rules>
    <rule>Compare changed work to approved scope, task source coverage, and validation evidence.</rule>
    <rule>Write findings only; do not silently edit implementation code.</rule>
  </rules>
  <actions>Record actionable findings; do not silently change implementation code.</actions>
  <artifact>devspec/work-items/&lt;id&gt;/review.md</artifact>
  <handoff>implement-or-close</handoff>
</workflow>
