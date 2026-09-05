# devspec.changerequest

Append one related post-finalization requirement without rewriting history.

Invocation: `/devspec.changerequest [work-item-id] Add JSON export`

<workflow command="devspec.changerequest">
  <purpose>Append one related post-finalization requirement without rewriting history.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="state" />
    <protocol ref="current-work-item" />
    <protocol ref="revision" />
    <protocol ref="work" />
  </protocols>
  <scope>Use only for a requirement related to a work item that is already finalized. Use devspec.story for independent scope, and edit the story directly while it is still before finalization.</scope>
  <input>An optional work-item ID and one related missing requirement.</input>
  <rules>
    <rule>Append the next CR-### entry and CR-scoped criteria; never rewrite baseline evidence.</rule>
    <rule>Ask one material classification question when it is unclear whether the request is related or a new linked work item.</rule>
  </rules>
  <entry>Related requirement for a finalized-or-later work item with an active current scope revision; reject independent, blocked, or pre-finalization requests.</entry>
  <outputs>
    <artifact path="devspec/work-items/&lt;id&gt;/story.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/meta.md" />
  </outputs>
  <transitions>
    <transition outcome="related-change-accepted" stage="finalization" run="active" next="devspec.finalize" />
    <transition outcome="classification-blocked" stage="finalization" run="blocked" next="devspec.clarify" />
  </transitions>
  <closure>Append the CR, increment scope_revision, mark downstream records superseded, and preserve their historical evidence.</closure>
</workflow>
