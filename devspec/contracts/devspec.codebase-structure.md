# devspec.codebase-structure

Capture owned source roots, module boundaries, integrations, and repository access.

Invocation: `/devspec.codebase-structure`

<workflow command="devspec.codebase-structure">
  <purpose>Capture owned source roots, module boundaries, integrations, and repository access.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="work" />
    <protocol ref="repo-access" />
  </protocols>
  <scope>Use for new-repository foundation authoring or an explicitly requested targeted update. Use devspec.extract, not this command, to establish an existing-system baseline.</scope>
  <input>Repository layout, work area, integration, or multi-repository context.</input>
  <rules>
    <rule>Map owned source roots, boundaries, integration points, and validation locations.</rule>
    <rule>Load repo-access only when work crosses repositories; never infer edit access.</rule>
  </rules>
  <actions>Map owned areas and use repo-access only when more than one repository is involved.</actions>
  <artifact>devspec/foundation/codebase-structure.md</artifact>
  <handoff>coding-standards</handoff>
</workflow>
