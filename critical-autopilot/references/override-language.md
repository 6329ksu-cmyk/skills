# Override Language

Short corrections are steering commands for the next cycle. Do not restart the whole task unless the user asks. Carry forward the latest state, then change the review pressure or lens.

| User wording | Next-cycle behavior |
| --- | --- |
| "계속", "이어", "continue", "go on" | Resume from the current artifact, evidence, changed files, unresolved blockers, and residual risks. Do not re-explain background unless something changed. |
| "아냐", "방향 이상함", "그거 아님", "wrong direction" | Reconstruct the objective, identify the mistaken assumption, and produce a corrected path before more edits. |
| "확증편향", "비판적으로" | Run a harsher counter-review. Look for false positives, missing evidence, shallow tests, and overly friendly interpretations. |
| "구라치지마", "솔직하게" | Classify important claims as verified, inferred, unverified, conditional, or impossible. |
| "더 세게", "빡세게", "전수조사", "끝까지", "not enough", "go harder" | Broaden coverage, inspect adjacent paths, add stronger validation, and keep fixing locally fixable issues. |
| "사용성 위주", "UX", "사람 기준", "usability first" | Prioritize first-run clarity, dead ends, confusing labels, hidden status, recovery, cognitive load, and operator next actions. |
| "보안만", "security only" | Narrow to auth, authorization, permissions, secrets, logs, data exposure, external calls, sandboxing, fail-open behavior, and unsafe defaults. |
| "성능", "느림" | Prioritize startup cost, rendering, storage, large data paths, lazy loading, measurement, and regression risk. |
| "질문/라우팅" | Stress ambiguous input, missing content, follow-up questions, empty data, near-domain requests, and fallback selection. |
| "묻지마", "알아서", "do not ask me" | Proceed with reasonable assumptions; ask only for hard blockers. |
| "그걸 내가 말해야 돼?", "I should not have to point that out" | Add an explicit unknown-unknown pass and report what was found beyond the user's examples. |
| "브리핑", "짧게" | Give current decision, evidence, blockers, and next action. Avoid raw logs and long file lists. |

If two overrides conflict, obey the newest one. If the conflict could cause data loss, ask one short question.
