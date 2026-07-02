# Expert Lenses

Use lenses to expose blind spots. Pick only the lenses relevant to the artifact.

## Core Lenses

- **Product truth:** Does the artifact match the user's actual goal, or only a convenient substitute?
- **User workflow:** Can the intended user complete the flow without reading code or logs?
- **QA/regression:** What would silently break while tests stay green?
- **Security/privacy:** What untrusted input, credential, export, log, or external call can escape its boundary?
- **Data model/persistence:** Is the state replayable, migrated, indexed, and recoverable?
- **Performance/scale:** What fails when the catalog, data, or traffic grows?
- **Accessibility/readability:** Can keyboard, screen-reader, reduced-motion, contrast, and text fit survive changes?
- **Operations:** Can the workflow restart, retry, fail clearly, and leave evidence?
- **Legal/copy risk:** Are external sources, assets, text, screenshots, and licenses safely separated?
- **Taste/quality:** Is it merely different, or actually coherent, useful, and domain-fit?
- **Skeptical final auditor:** What claim is still too strong?

## Subagent Use

Use subagents only when permitted by the user and useful for independent passes. Give each subagent a bounded role and ask for:

- 5-pass goal reapplication when the user demands depth
- `HARD IMPOSSIBLE / CONDITIONALLY SOLVABLE / ENGINEERING RISK`
- concrete gates or fixes
- no file edits unless explicitly assigned

If subagent parallelism fails, say so. Sequential work is acceptable; pretending parallel debate occurred is not.
