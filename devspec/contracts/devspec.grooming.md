# devspec.grooming

Make one draft story buildable through scoped review and material questions.

Invocation: `/devspec.grooming GHUB-123-customer-export`

<workflow command="devspec.grooming">
  <purpose>Make one draft story buildable through scoped review and material questions.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="work" />
  </protocols>
  <input>One draft work-item identifier or clear current draft.</input>
  <rules>
    <rule>Read only the draft, relevant coding standards, codebase structure, foundation rules and workflow rules, selected code area, and direct dependencies; do not scan unrelated historical work-item decisions.</rule>
    <rule>Improve behavior, acceptance criteria, scope, technical constraints, edge cases, dependencies, compatibility risks, and blockers in place.</rule>
    <rule>Do not groom finalized scope; route new scope to changerequest.</rule>
  </rules>
  <entry>Active work item at grooming for the current scope revision; reject finalized, blocked, stale, or unrelated scope.</entry>
  <outputs>
    <artifact path="devspec/work-items/&lt;id&gt;/story.md" />
    <artifact path="devspec/work-items/&lt;id&gt;/decisions.md" />
  </outputs>
  <transitions>
    <transition outcome="ready-for-finalization" stage="finalization" run="active" next="devspec.finalize" />
    <transition outcome="material-blocker" stage="grooming" run="blocked" next="devspec.clarify" />
  </transitions>
  <closure>Do not advance while a material question remains unanswered; record the one blocker and resume reference.</closure>
  <actions>Improve draft story and decisions in place; suggest only material questions.</actions>
  <artifact>devspec/work-items/&lt;id&gt;/story.md</artifact>
  <handoff>devspec.clarify-or-devspec.finalize</handoff>
</workflow>
