# Glossary

- Work-item stages: intake, grooming, finalization, tasks, implementation, review, complete.
- Quickfix stages: triage, implementation, validation, complete, routed.
- Run states: active (eligible to continue), paused (user-paused), blocked (one active material decision), stopped (requires new direction), complete (terminal with `next: none`).
- Task statuses: pending, in-progress, blocked, complete, superseded.
- Scope revision: a monotonic work-item number. Finalization, tasks, implementation, and review operate only on the current revision; older records are retained as superseded history.
- Evidence: confirmed, observed, inferred, blocked.
- OWASP exception: a reviewer-confirmed false-positive or not-applicable finding supported by enforceable evidence; it is distinct from an unresolved vulnerability.
