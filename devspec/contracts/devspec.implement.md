# devspec.implement

Implement pending ready tasks with focused checkpoints and validation.

Invocation: `/devspec.implement [work-item-id]`

<workflow command="devspec.implement">
  <purpose>Implement pending ready tasks with focused checkpoints and validation.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="current-work-item" />
    <protocol ref="work" />
    <protocol ref="repo-access" />
  </protocols>
  <input>An optional work-item ID with ready finalization and pending task records.</input>
  <rules>
    <rule>Confirm every task is in finalized scope, unblocked, and ordered before editing code.</rule>
    <rule>Checkpoint before edits and focused validation; stop for a material ambiguity instead of expanding scope.</rule>
    <rule>Before editing, apply the relevant finalization foundation trace: coding standards, owned code areas and boundaries, canonical rules, and applicable OWASP controls.</rule>
    <rule>Record changed areas, applied decision or canonical rule IDs, and validation evidence after each meaningful task.</rule>
    <rule>Express a business or validation decision through named code and tests. Add a developer comment only when its rationale is not evident from the code or test; reference the canonical rule ID, never an old work-item decision as the sole authority.</rule>
    <rule>Record project-native security evidence for every applicable OWASP control. A suspected false positive or not-applicable finding requires the agent to ask one material confirmation question of the implementing developer, then record the explicit confirmation, rationale, enforceable supporting evidence, and material-change revalidation trigger; it remains proposed until review.</rule>
    <rule>Do not classify a known unresolved vulnerability as not applicable merely because access is limited, authenticated, or internal-only.</rule>
  </rules>
  <entry>Active work item at implementation with current-revision ready finalization and ordered pending tasks; reject stale plans, blocked tasks, or changed scope.</entry>
  <outputs>
    <artifact path="devspec/work-items/&lt;id&gt;/implement.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/tasks.md" />
  </outputs>
  <transitions>
    <transition outcome="implementation-complete" stage="review" run="active" next="devspec.review" />
    <transition outcome="material-blocker" stage="implementation" run="blocked" next="devspec.clarify" />
  </transitions>
  <closure>Record the changed-work baseline and mark a task complete only after its recorded validation passes; preserve superseded revisions.</closure>
  <actions>Stay within finalized scope; checkpoint before edits and validation.</actions>
  <artifact>devspec/work-items/&lt;id&gt;/implement.md</artifact>
  <handoff>review</handoff>
</workflow>
