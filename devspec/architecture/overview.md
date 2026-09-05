# Architecture Overview

## Confirmed boundaries
- Scope: developer workflow and setup guidance, not product runtime architecture.
- Sources: command contracts, protocols, CLI behavior, and setup documentation.
- Constraint: diagrams show confirmed routes only; they do not infer application dependencies.

## Diagram index

| ID | Diagram | Scope | Evidence | Link |
|---|---|---|---|---|
| DIA-001 | Foundation route | workflow | command registry, repository state | `docs/assets/foundation-routes.svg` |
| DIA-002 | Delivery route | workflow | command contracts, protocols | `docs/assets/delivery-routes.svg` |
| DIA-003 | Install lifecycle | workflow | CLI, doctor, setup guides | `docs/assets/maintenance-flow.svg` |
| DIA-004 | Manual copy route | workflow | manual copy guide, install manifest | `docs/assets/manual-copy-flow.svg` |
