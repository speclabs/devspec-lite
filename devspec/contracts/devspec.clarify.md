# devspec.clarify

Resolve one active blocker and resume its originating stage.

Invocation: `/devspec.clarify GHUB-123-customer-export`

<workflow command="devspec.clarify">
  <purpose>Resolve one active blocker and resume its originating stage.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
  </protocols>
  <input>One work item with an active recorded blocker or question.</input>
  <rules>
    <rule>Resolve the highest-priority open decision only and append its answer to decisions.md.</rule>
    <rule>Do not accept scope changes after finalization; route them to changerequest.</rule>
    <rule>Return to the saved stage and next action after resolution.</rule>
  </rules>
  <actions>Ask the recorded high-priority question, append the resolution, and return to the saved next action.</actions>
  <artifact>devspec/work-items/&lt;id&gt;/decisions.md</artifact>
  <handoff>resume-origin</handoff>
</workflow>
