---
name: self-steering-cycle
description: Compatibility alias for critical-autopilot. Use only when the user explicitly invokes self-steering-cycle or asks about this legacy skill name. For implicit autonomous improvement, terse steering, "continue", "wrong direction", "make it stricter", "security only", or "usability first" requests, prefer critical-autopilot as the canonical skill.
---

# Self-Steering Cycle

## Compatibility Alias

This skill name is preserved for old prompts. It is no longer the canonical autonomous loop.

When triggered, route the work to [critical-autopilot](../critical-autopilot/SKILL.md) and use Critical Autopilot's loop, evidence discipline, validation ladder, and briefing style.

## Preserved Emphasis

Carry these priorities into the Critical Autopilot cycle:

- Treat terse user feedback as steering, not as a request for debate.
- On "continue" or "계속", resume from unresolved blockers and residual risks.
- On "wrong direction" or "아냐", reopen the objective before editing more.
- Treat "I only fixed what the user explicitly named" as a failed cycle.
- Attempt at least one unknown-unknown pass unless the artifact is too small for that to be meaningful.

For detailed behavior, use `critical-autopilot/references/override-language.md`, `critical-autopilot/references/gap-lenses.md`, and `critical-autopilot/references/evidence-and-validation.md`.
