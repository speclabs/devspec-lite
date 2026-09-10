# devspec.finalize

Produce a concise readiness brief and validation plan.

Invocation: `/devspec.finalize [work-item-id]`

<workflow command="devspec.finalize">
  <purpose>Produce a concise readiness brief and validation plan.</purpose>
  <protocols>
    <protocol ref="ask" queue="single-blocker" />
    <protocol ref="run" />
    <protocol ref="state" />
    <protocol ref="current-work-item" />
    <protocol ref="revision" />
    <protocol ref="work" />
    <protocol ref="security" />
  </protocols>
  <scope>Use to decide whether the current scope revision is buildable and to record its brief and validation plan. This command plans readiness only; devspec.tasks sequences the work and devspec.implement changes code.</scope>
  <input>An optional work-item ID or a refined current draft.</input>
  <rules>
    <rule>Read only the current-revision story and decisions, the current-revision task statuses when a correction is requested from the tasks stage, the finalization traces' direct sources in coding standards, codebase structure, rules, workflow rules, constitution, and the architecture queue or overview. Do not scan unrelated work items, unrelated code areas, or historical revisions beyond the superseded sections of this work item.</rule>
    <rule>devspec.refine owns the requirement questions. Ask nothing whose answer it should already have recorded; when a requirement is still missing, record one blocker and route it rather than re-opening refinement's queue.</rule>
    <rule>Check only material readiness gaps, judging buildability and verifiability rather than re-deriving requirements: whether the recorded scope and criteria can be built and validated as written, and the data, integration, security, compliance, validation, and delivery constraints that decide it. Those last are this command's own, and the security protocol's gate applies here rather than in refinement.</rule>
    <rule>Reject the work item when story.md's Open Requirement Gaps table still holds an entry that is neither resolved nor explicitly skipped with its reason; record one blocker naming the open entries and route back through devspec.clarify to refinement.</rule>
    <rule>Mark ready only when the remaining gaps cannot materially change implementation or validation; a gap that can becomes one material blocker question. Record every gap judged immaterial in the brief's Assumptions and Open Items section with its basis, impact if wrong, and status, rather than discarding it.</rule>
    <rule>Accept a correction request re-entered from the tasks stage only while `implemented_revision` is behind `scope_revision` and no task is in-progress or complete. Rewrite the brief in place at the same scope revision, set its Status to revised, record what changed and why in decisions.md, mark the superseded task list `superseded`, and reset `planned_revision` to none so devspec.tasks re-plans against the corrected brief. This is a correction, not a change request: reject a new or widened requirement and route it to devspec.changerequest, which increments the revision instead.</rule>
    <rule>Classify every accepted material decision as work-item-local or reusable. Promote a reusable business or validation decision to devspec/foundation/workflow-rules.md with a stable rule ID and source decision link; promote a reusable engineering constraint to devspec/foundation/rules.md. Record the resulting canonical rule link in decisions.md.</rule>
    <rule>Record one compact foundation trace for the relevant coding conventions, owned areas and boundaries, canonical rules, applicable active `CP-###` principles, and the OWASP categories the change touches. Record a separate architecture and diagram trace for relevant overview entries, completed diagrams, or queued candidates, including implementation and validation impact; no diagram is required.</rule>
    <rule>Write a concise implementation brief and validation plan, not implementation code. Write the brief under its template sections so a developer can review the plan section by section, recording a section as not applicable with its reason rather than omitting it, and name the concrete components, interfaces, contracts, schemas, and migrations the work will touch instead of describing them in general terms.</rule>
  </rules>
  <entry>Active work item at finalization with a complete current-revision story, or at tasks when the developer asks to correct the current-revision brief before implementation has begun; reject stale finalization, blocked work, incomplete draft scope, and a correction request once any task for the current revision is in-progress or complete.</entry>
  <outputs>
    <artifact path="devspec/work-items/&lt;id&gt;/finalize.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/meta.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/decisions.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/tasks.md" />
    <artifact path="devspec/foundation/workflow-rules.md" />
    <artifact path="devspec/foundation/rules.md" />
  </outputs>
  <transitions>
    <transition outcome="ready" stage="tasks" run="active" next="devspec.tasks" />
    <transition outcome="material-blocker" stage="finalization" run="blocked" next="devspec.clarify" />
  </transitions>
  <closure>Stamp the readiness brief with the current scope revision. Preserve earlier revision sections as superseded history.</closure>
</workflow>
