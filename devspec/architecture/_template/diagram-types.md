# Diagram Types

Use the smallest diagram that makes a confirmed relationship easier to understand. SVG is the default; HTML is an optional presentation shell.

## Shared visual grammar

- Use a dark canvas, subtle grid, framed surface, short eyebrow, title, and evidence-backed subtitle.
- Draw connectors behind cards. Use restrained accents only to distinguish meaning, not decoration.
- Keep labels short; use supporting Markdown for details. Every SVG needs a title and description.
- Include a small legend only when color, line style, or notation is not self-evident.

## Select by question

| Type | Use when the reader asks | Minimum evidence | Show |
|---|---|---|---|
| Architecture | What owns or connects to what? | source roots, integration points | boundaries, components, integrations |
| Domain model | What data concepts relate? | types/schema/contracts | entities, fields only when useful, cardinality |
| Journey map | What happens to an actor over time? | observed user/system flow | stages, actor actions, system touchpoints, outcome |
| Mind map | What belongs in this problem space? | scoped discovery | central concern, grouped branches, open risks |
| Process flow | What steps and gates decide the result? | command contract or observed process | steps, decisions, success and exception paths |
| Quadrant | How should options be compared? | stated axes and rationale | axes, four meanings, evidence-backed placement |
| Sequence | Who calls whom, and in what order? | call path/contracts | participants, ordered messages, returns when relevant |
| State lifecycle | Which states and transitions are allowed? | persisted state/transition rules | start, states, transition labels, terminal or exception states |
| Timeline | What depends on what, and when? | milestones/dependencies | phases, milestones, dependency or risk links |

## Guardrails

Do not infer entities, callers, timelines, ownership, user sentiment, or priorities. Record uncertain information in the work item or decisions file, not as a factual diagram label.

For every completed diagram: save the output, update artifact-queue.md, and index the link in overview.md.
