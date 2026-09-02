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
    <rule>Compare changed work to approved scope, task source coverage, validation evidence, and every applicable accepted material decision or canonical rule.</rule>
    <rule>Record each decision or rule verification as implemented-as-decided, intentionally-superseded with a recorded replacement, or not-verified. Treat an unrecorded contradiction as rework-required.</rule>
    <rule>Write findings only; do not silently edit implementation code.</rule>
    <rule>Record exactly one outcome: accepted, rework-required, or blocked; record exactly one next action.</rule>
  </rules>
  <actions>Record the review outcome, one next action, and any actionable findings; do not silently change implementation code.</actions>
  <artifact>devspec/work-items/&lt;id&gt;/review.md</artifact>
  <handoff>implement-or-close</handoff>
</workflow>
