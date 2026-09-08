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
  <scope>Use to make a draft story buildable through scoped analysis and material questions; this is the default route out of intake. Skip it and run devspec.finalize directly only when the intake source itself carried explicit acceptance criteria recorded as confirmed evidence and story.md lists no open requirement gap.</scope>
  <input>An optional work-item ID or clear current draft.</input>
  <rules>
    <rule>Read only the draft, relevant coding standards, codebase structure, foundation rules and workflow rules, selected code area, and direct dependencies; do not scan unrelated historical work-item decisions.</rule>
    <rule>Run the ask protocol's discovery across every grooming dimension before advancing: behavior, acceptance criteria, scope boundaries, technical constraints, edge cases, dependencies, compatibility risks, data and integration impact, and validation gaps. Queue every open requirement gap devspec.story recorded in story.md as a material question, add every gap the scoped reading exposes, and re-run discovery after each answer. This command owns the requirement questions intake is forbidden to ask.</rule>
    <rule>Do not re-ask intake identity questions. The work-item number, provider reference, and type are settled in story.md and meta.md; correct type in meta.md from better evidence without asking.</rule>
    <rule>Improve behavior, acceptance criteria, scope, technical constraints, edge cases, dependencies, compatibility risks, and blockers in place, and resolve each answered question into the artifact it affects rather than leaving it only in decisions.md.</rule>
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
  <closure>Do not advance while any applicable material question remains unanswered or explicitly skipped with its reason, and do not treat an empty queue as completeness without re-running discovery. Record the one blocker and resume reference.</closure>
</workflow>
