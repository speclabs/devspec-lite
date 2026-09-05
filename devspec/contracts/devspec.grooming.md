# devspec.grooming

Make one draft story buildable through scoped review and material questions.

Invocation: `/devspec.grooming [work-item-id]`

<workflow command="devspec.grooming">
  <purpose>Make one draft story buildable through scoped review and material questions.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="state" />
    <protocol ref="current-work-item" />
    <protocol ref="revision" />
    <protocol ref="work" />
    <protocol ref="repo-access" />
  </protocols>
  <scope>Use only when a draft story needs scoped analysis before it can be built. Skip it and run devspec.finalize directly when behavior, acceptance criteria, and the affected code area are already clear.</scope>
  <input>An optional work-item ID or clear current draft.</input>
  <rules>
    <rule>Read only the draft, relevant coding standards, codebase structure, foundation rules and workflow rules, selected code area, and direct dependencies; do not scan unrelated historical work-item decisions.</rule>
    <rule>Improve behavior, acceptance criteria, scope, technical constraints, edge cases, dependencies, compatibility risks, and blockers in place.</rule>
    <rule>Do not groom finalized scope; route new scope to changerequest.</rule>
  </rules>
  <entry>Active work item at grooming for the current scope revision; reject finalized, blocked, stale, or unrelated scope.</entry>
  <outputs>
    <artifact path="devspec/work-items/&lt;id&gt;/story.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/decisions.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/meta.md" />
  </outputs>
  <transitions>
    <transition outcome="ready-for-finalization" stage="finalization" run="active" next="devspec.finalize" />
    <transition outcome="material-blocker" stage="grooming" run="blocked" next="devspec.clarify" />
  </transitions>
  <closure>Do not advance while a material question remains unanswered; record the one blocker and resume reference.</closure>
</workflow>
