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
  <input>Hard engineering, compliance, security, delivery, or accessibility constraints.</input>
  <rules>
    <rule>Keep non-negotiable rules separate from ordinary coding conventions.</rule>
    <rule>State enforcement or validation for each rule when known.</rule>
  </rules>
  <actions>Keep hard constraints distinct from ordinary coding conventions.</actions>
  <artifact>devspec/foundation/rules.md</artifact>
  <handoff>story</handoff>
</workflow>
