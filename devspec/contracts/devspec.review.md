# devspec.review

Review changed work against readiness, tasks, and validation evidence.

Invocation: `/devspec.review [work-item-id]`

<workflow command="devspec.review">
  <purpose>Review changed work against readiness, tasks, and validation evidence.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="current-work-item" />
    <protocol ref="work" />
  </protocols>
  <input>An optional work-item ID with finalization, tasks, implementation record, and changed work.</input>
  <rules>
    <rule>Compare changed work to approved scope, task source coverage, finalization foundation trace, validation evidence, and every applicable accepted material decision or canonical rule.</rule>
    <rule>Record each decision or rule verification as implemented-as-decided, intentionally-superseded with a recorded replacement, or not-verified. Treat an unrecorded contradiction as rework-required.</rule>
    <rule>Verify every applicable OWASP control and its project-native evidence. Confirm a proposed false positive or not-applicable finding only when the implementing developer confirmed it, enforceable evidence supports the rationale, and the reviewer records confirmation.</rule>
    <rule>Do not record accepted while an applicable OWASP control lacks evidence or an exception lacks either confirmation. Treat unsupported internal-only, authenticated-only, or limited-access reasoning as an applicable risk with reduced exposure. A known unresolved vulnerability cannot be closed as an exception.</rule>
    <rule>Record a material-change revalidation trigger for every confirmed exception covering related code, access control, deployment, integration, or exposure.</rule>
    <rule>Write findings only; do not silently edit implementation code.</rule>
    <rule>Record exactly one outcome: accepted, rework-required, or blocked; record exactly one next action.</rule>
  </rules>
  <entry>Active work item at review with complete implementation and matching finalization and task records for the current scope revision; reject an unknown changed-work baseline.</entry>
  <outputs>
    <artifact path="devspec/work-items/&lt;id&gt;/review.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/meta.md" />
  </outputs>
  <transitions>
    <transition outcome="accepted" stage="complete" run="complete" next="none" />
    <transition outcome="rework-required" stage="implementation" run="active" next="devspec.implement" />
    <transition outcome="blocked" stage="review" run="blocked" next="devspec.clarify" />
  </transitions>
  <closure>Verify the recorded changed-work baseline. Accepted is terminal; rework returns only affected tasks to implementation.</closure>
  <actions>Record the review outcome, one next action, and any actionable findings; do not silently change implementation code.</actions>
  <artifact>devspec/work-items/&lt;id&gt;/review.md</artifact>
  <handoff>devspec.implement-or-devspec.clarify-or-none</handoff>
</workflow>
