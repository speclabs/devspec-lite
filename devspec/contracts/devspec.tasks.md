# devspec.tasks

Create ordered, independently verifiable implementation tasks.

Invocation: `/devspec.tasks GHUB-123-customer-export`

<workflow command="devspec.tasks">
  <purpose>Create ordered, independently verifiable implementation tasks.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="work" />
    <protocol ref="repo-access" />
  </protocols>
  <input>A ready finalization brief.</input>
  <rules>
    <rule>Each task names scope, dependency, source justification, applicable decision or canonical rule IDs, validation, and done condition.</rule>
    <rule>Order dependencies before dependents and split only work too broad to validate safely.</rule>
  </rules>
  <actions>Trace tasks to readiness items and validation evidence; sequence dependencies first.</actions>
  <artifact>devspec/work-items/&lt;id&gt;/tasks.md</artifact>
  <handoff>implement</handoff>
</workflow>
