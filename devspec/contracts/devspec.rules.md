# devspec.rules

Capture non-negotiable engineering, security, compliance, delivery, and accessibility rules.

Invocation: `/devspec.rules`

<workflow command="devspec.rules">
  <purpose>Capture non-negotiable engineering, security, compliance, delivery, and accessibility rules.</purpose>
  <protocols>
    <protocol ref="ask" />
    <protocol ref="run" />
    <protocol ref="work" />
  </protocols>
  <scope>Use for new-repository foundation authoring or an explicitly requested targeted update. Use devspec.extract, not this command, to establish an existing-system baseline.</scope>
  <input>Hard engineering, compliance, security, delivery, or accessibility constraints.</input>
  <rules>
    <rule>Keep non-negotiable rules separate from ordinary coding conventions.</rule>
    <rule>State enforcement or validation for each rule when known.</rule>
    <rule>Maintain one OWASP Top 10:2025 baseline in rules.md. For every category, record whether it is applicable, limited, out-of-scope, or unknown, plus the required project control and enforcement evidence.</rule>
    <rule>Record limited or internal-only exposure only when enforceable access, deployment, or network evidence supports it; otherwise treat the category as applicable with reduced exposure.</rule>
  </rules>
  <actions>Keep hard constraints distinct from ordinary coding conventions and establish the project OWASP baseline.</actions>
  <artifact>devspec/foundation/rules.md</artifact>
  <handoff>story</handoff>
</workflow>
