# devspec.changerequest

Append one related post-finalization requirement without rewriting history.

Invocation: `/devspec.changerequest GHUB-123 Add JSON export`

<workflow command="devspec.changerequest">
  <purpose>Append one related post-finalization requirement without rewriting history.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="work" />
  </protocols>
  <input>A finalized-or-later work item and one related missing requirement.</input>
  <rules>
    <rule>Append the next CR-### entry and CR-scoped criteria; never rewrite baseline evidence.</rule>
    <rule>Ask one material classification question when it is unclear whether the request is related or a new linked work item.</rule>
  </rules>
  <actions>Classify scope as related or independent; append the next CR identifier when related.</actions>
  <artifact>devspec/work-items/&lt;id&gt;/story.md</artifact>
  <handoff>finalize</handoff>
</workflow>
