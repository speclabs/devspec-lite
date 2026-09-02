# devspec.clarify

Resolve one active blocker and resume its originating stage.

Invocation: `/devspec.clarify GHUB-123-customer-export`

<workflow command="devspec.clarify">
  <purpose>Resolve one active blocker and resume its originating stage.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
  </protocols>
  <input>One foundation, work item, or quickfix record with one active material blocker question.</input>
  <rules>
    <rule>Resolve the one highest-priority material decision in its active queue and append its answer to decisions.md.</rule>
    <rule>Do not accept scope changes after finalization; route them to changerequest.</rule>
    <rule>Return to the saved stage and next action after resolution.</rule>
  </rules>
  <entry>Exactly one active material blocker in a foundation, work-item, or quickfix decision record with a saved originating command; reject unblocked or ambiguous records.</entry>
  <outputs>
    <artifact path="devspec/foundation/decisions.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/decisions.md" />
    <artifact path="devspec/quickfixes/QF-###-slug.md" />
  </outputs>
  <transitions>
    <transition outcome="decision-resolved" stage="origin" run="active" next="resume-origin" />
  </transitions>
  <closure>Append the resolution, restore the exact saved stage and next command, and do not change scope while resolving a blocker.</closure>
  <actions>Ask the recorded high-priority material question, append the resolution, and return to the saved next action.</actions>
  <artifact>devspec/work-items/&lt;id&gt;/decisions.md</artifact>
  <handoff>resume-origin</handoff>
</workflow>
