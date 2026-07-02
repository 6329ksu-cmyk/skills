# Override Language

Short corrections are steering commands for the next cycle. Do not restart the whole task unless the user asks. Carry forward the latest state, then change the review pressure or lens.

| User wording | Next-cycle behavior |
| --- | --- |
| "아냐", "방향 이상함", "그거 아님" | Reconstruct the objective from scratch, identify the wrong assumption, and produce a corrected path before more edits. |
| "확증편향", "비판적으로" | Run a harsher counter-review. Look for false positives, missing evidence, shallow tests, and overly friendly interpretations. |
| "더 세게", "전수조사", "끝까지" | Broaden coverage, inspect adjacent paths, add stronger validation, and keep fixing locally fixable issues. |
| "사용성 위주" | Prioritize first-run clarity, dead ends, confusing labels, hidden status, stale reports, and operator next actions. |
| "보안만" | Narrow to auth, permissions, secrets, logs, data exposure, external calls, fail-open behavior, and unsafe defaults. |
| "질문/라우팅" | Stress ambiguous input, missing content, follow-up questions, empty data, near-domain requests, and fallback selection. |
| "계속" | Continue from the current artifact and evidence. Do not re-explain background unless something changed. |
| "브리핑" | Give current decision, evidence, blockers, and next action. Avoid raw logs and long file lists. |

If two overrides conflict, obey the newest one. If the conflict could cause data loss, ask one short question.
