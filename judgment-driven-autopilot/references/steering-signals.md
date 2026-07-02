# Steering Signals

Use terse user replies as control input for the next cycle.

| User signal | Next-cycle behavior |
| --- | --- |
| `계속`, `이어`, `continue` | Resume from the last evidence and unresolved blockers. Do not re-explain from scratch. |
| `아냐`, `방향 이상함`, `wrong direction` | Reopen the objective, identify the mistaken assumption, and run a harsher counter-pass. |
| `더 세게`, `빡세게`, `전수조사`, `끝까지` | Increase adversarial coverage and verification depth. Separate impossible, conditional, and risky claims. |
| `사용성 위주`, `UX`, `사람 기준` | Prioritize first-run flow, dead controls, unclear state, feedback ambiguity, recovery, and cognitive load. |
| `보안만`, `security only` | Prioritize secrets, auth, sandboxing, injection, external calls, logs, permissions, and fail-open states. |
| `성능`, `느림` | Prioritize startup cost, rendering, storage, large data paths, lazy loading, and measurement. |
| `브리핑` | Stop expanding unless needed; summarize status, evidence, blockers, and next action. |
| `구라치지마`, `솔직하게` | Classify claims as verified, inferred, unverified, impossible, or conditional. |

If a signal conflicts with older instructions, the newest signal steers the next cycle.
