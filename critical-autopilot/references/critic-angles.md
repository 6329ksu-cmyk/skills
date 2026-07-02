# Critic Angles

Use these as independent lenses. Spawn subagents only when the user explicitly asks for or permits delegation/subagents/workflows and the environment provides an appropriate tool. Otherwise, run the lenses locally and keep the synthesis concise.

## Minimal Critical Panel

- **Readiness and truthfulness:** Does the artifact claim readiness without real data, real tests, or usable runtime state?
- **User experience:** Can a tired operator understand the state, failure reason, and next action without reading logs?
- **Security and privacy:** Are auth boundaries, secrets, logs, generated answers, exports, and source links safe by default?
- **Routing and edge cases:** Do short, ambiguous, missing, follow-up, off-topic, or near-domain inputs land in the right behavior?
- **Operations:** Can an admin configure, retry, recover, and inspect the system without babysitting every step?
- **Regression proof:** Is there a test, validator, prompt guard, fixture, or checklist that makes the fixed issue harder to reintroduce?
- **Data quality:** Are empty indexes, stale caches, duplicate sources, partial migrations, or malformed documents visible and handled honestly?
- **Product judgment:** Does the work match the user's stated taste: autonomous, practical, concise, and final-evaluator oriented?
- **Cost and dependency:** Are paid calls, network services, model choices, background jobs, and time-heavy operations explicit and bounded?

## Synthesis Rule

Do not average the panel into vague consensus. Keep any P0/P1 issue that one credible lens finds unless direct evidence disproves it. Prefer a small patch plus verification over a long unresolved risk list.
