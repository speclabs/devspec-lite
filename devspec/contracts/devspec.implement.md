# devspec.implement

Implement pending ready tasks with focused checkpoints and validation.

Invocation: `/devspec.implement GHUB-123-customer-export`

<workflow command="devspec.implement">
  <purpose>Implement pending ready tasks with focused checkpoints and validation.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="work" />
    <protocol ref="repo-access" />
  </protocols>
  <input>Ready finalization and pending task records.</input>
  <rules>
    <rule>Confirm every task is in finalized scope, unblocked, and ordered before editing code.</rule>
    <rule>Checkpoint before edits and focused validation; stop for a material ambiguity instead of expanding scope.</rule>
    <rule>Record changed areas, applied decision or canonical rule IDs, and validation evidence after each meaningful task.</rule>
    <rule>Express a business or validation decision through named code and tests. Add a developer comment only when its rationale is not evident from the code or test; reference the canonical rule ID, never an old work-item decision as the sole authority.</rule>
  </rules>
  <actions>Stay within finalized scope; checkpoint before edits and validation.</actions>
  <artifact>devspec/work-items/&lt;id&gt;/implement.md</artifact>
  <handoff>review</handoff>
</workflow>
