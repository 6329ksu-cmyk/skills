# Steering Signals

Use this file when the latest user message is short, corrective, frustrated, or directional.

## Interpretation

- "continue", "go on", "이어서해": continue the same loop from the last unresolved gaps; do not ask for a new plan.
- "wrong direction", "아냐 방향 이상함": re-infer the objective from the user's correction; explicitly drop the prior assumption that caused drift.
- "harder", "더 세게", "not enough": add skeptical and edge-case lenses; raise acceptance criteria; spend more effort on verification.
- "usability first", "사용성 위주": prioritize real workflows, empty states, navigation, copy, layout, and failure recovery over architecture elegance.
- "security only", "보안만": narrow to secrets, auth, authorization, injection, data exposure, dependency risk, logging, and operational abuse.
- "do not ask me", "묻지마", "알아서": proceed with reasonable assumptions; ask only for hard blockers.
- "I should not have to point that out": add an explicit unknown-unknown pass and report what was found beyond the user's examples.
- "brief me", "짧게": compress final output to decisions, changes, validation, and next direction.

## Response Behavior

Treat steering phrases as constraints for the next cycle. Do not defend the previous output unless the user asks for explanation.

When the user expresses lost trust, increase verification and show concrete evidence in the final briefing. Evidence means tests, screenshots, validators, diffs, reproduced failures, or exact files changed; not vague assurance.

When the user asks for "more experts", use perspectives as a coverage mechanism. The point is not theatrical role count; the point is finding gaps the main pass missed.
