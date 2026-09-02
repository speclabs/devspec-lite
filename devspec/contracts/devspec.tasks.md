# devspec.tasks

Create ordered, independently verifiable implementation tasks.

Invocation: `/devspec.tasks [work-item-id]`

<workflow command="devspec.tasks">
  <purpose>Create ordered, independently verifiable implementation tasks.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="current-work-item" />
    <protocol ref="work" />
    <protocol ref="repo-access" />
  </protocols>
  <input>An optional work-item ID with a ready current finalization brief.</input>
  <rules>
    <rule>Each task names scope, dependency, source justification, applicable decision or canonical rule IDs, validation, and done condition. Cite the finalization foundation trace for coding standards, codebase boundaries, and OWASP controls instead of duplicating them per task.</rule>
    <rule>Order dependencies before dependents and split only work too broad to validate safely.</rule>
  </rules>
  <entry>Active work item at tasks with a ready finalization matching the current scope revision; reject blocked, stale, or superseded readiness evidence.</entry>
  <outputs>
    <artifact path="devspec/work-items/&lt;id&gt;/tasks.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/meta.md" />
  </outputs>
  <transitions>
    <transition outcome="tasks-planned" stage="implementation" run="active" next="devspec.implement" />
    <transition outcome="material-blocker" stage="tasks" run="blocked" next="devspec.clarify" />
  </transitions>
  <closure>Plan only the active revision. Each task has source justification, validation, done condition, and a controlled initial status.</closure>
  <actions>Trace tasks to readiness items and validation evidence; sequence dependencies first.</actions>
  <artifact>devspec/work-items/&lt;id&gt;/tasks.md</artifact>
  <handoff>implement</handoff>
</workflow>
