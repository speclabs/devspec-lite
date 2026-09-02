# devspec.story

Create one concise work-item intake from a request or provider reference.

Invocation: `/devspec.story Add customer export`

<workflow command="devspec.story">
  <purpose>Create one concise work-item intake from a request or provider reference.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="current-work-item" />
    <protocol ref="work" />
  </protocols>
  <input>One provider reference or one manual feature, bug, security issue, or task.</input>
  <rules>
    <rule>Handle exactly one work item; ask a material selection question when input contains independent items.</rule>
    <rule>Read only the coding standards, codebase structure, foundation rules, and workflow rules relevant to the requested behavior and code area; do not scan unrelated historical work-item decisions.</rule>
    <rule>Create folders as optional-provider-prefix plus numeric ID plus kebab-case title; do not rename legacy folders automatically.</rule>
    <rule>Before finalization, update the baseline; after finalization, route related scope to changerequest and unrelated scope to a linked item.</rule>
    <rule>Treat an explicit story request as new-work intent unless it is clearly related finalized scope, which routes to changerequest.</rule>
    <rule>When creating a story or accepting a validated explicit ID, set current-work-item context for the current branch; preserve meta.md as the canonical state record.</rule>
    <rule>For an ordinary request with current context, resume clearly related pre-finalization work; ask one classification question before switching stories or accepting independent scope.</rule>
  </rules>
  <entry>One selected request with a valid work-item folder at intake and an active scope revision; reject finalized scope changes and independent bundled requests.</entry>
  <outputs>
    <artifact path="devspec/work-items/&lt;id&gt;/story.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/meta.md" />
  </outputs>
  <transitions>
    <transition outcome="grooming-required" stage="grooming" run="active" next="devspec.grooming" />
    <transition outcome="ready-for-finalization" stage="finalization" run="active" next="devspec.finalize" />
  </transitions>
  <closure>Record the selected route. Use grooming when code-area evidence, compatibility, risk, or acceptance criteria needs scoped analysis.</closure>
  <actions>Choose one work item, validate its target folder, and preserve finalized baselines.</actions>
  <artifact>devspec/work-items/&lt;id&gt;/story.md</artifact>
  <handoff>devspec.grooming-or-devspec.finalize</handoff>
</workflow>
