# devspec.story

Create one concise work-item intake from a request or provider reference.

Invocation: `/devspec.story Add customer export`

<workflow command="devspec.story">
  <purpose>Create one concise work-item intake from a request or provider reference.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="work" />
  </protocols>
  <input>One provider reference or one manual feature, bug, security issue, or task.</input>
  <rules>
    <rule>Handle exactly one work item; ask a material selection question when input contains independent items.</rule>
    <rule>Read only the foundation rules and workflow rules relevant to the requested behavior and code area; do not scan unrelated historical work-item decisions.</rule>
    <rule>Create folders as optional-provider-prefix plus numeric ID plus kebab-case title; do not rename legacy folders automatically.</rule>
    <rule>Before finalization, update the baseline; after finalization, route related scope to changerequest and unrelated scope to a linked item.</rule>
  </rules>
  <actions>Choose one work item, validate its target folder, and preserve finalized baselines.</actions>
  <artifact>devspec/work-items/&lt;id&gt;/story.md</artifact>
  <handoff>grooming-or-finalize</handoff>
</workflow>
