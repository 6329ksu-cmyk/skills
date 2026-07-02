# Reviewer Roles

Use reviewer roles to widen the pass without turning the cycle into a user interview.

## Output Format

Each reviewer should produce:

```text
Verdict: PASS | CONCERNS | FAIL
Top risks:
- ...
Concrete fixes:
- ...
Validation needed:
- ...
```

## Default Roles

**Security/Safety**
Looks for auth bypass, secret leakage, unsafe defaults, injection, MITM, external target abuse, destructive paths, and authorization gaps.

**Platform/Runtime**
Looks for Windows/Linux/macOS differences, service state assumptions, shell/encoding issues, dependency drift, background process behavior, and network binding problems.

**QA/Test**
Looks for missing tests, tests that hit real systems, brittle fixtures, missing failure-mode coverage, and insufficient artifact/UI validation.

**Submission/Artifact Integrity**
Looks for stale sample data, run mismatch, generated files that include wrong evidence, inconsistent exception handling, report injection, missing provenance, and incomplete status gates.

**Product/UX**
Looks for user confusion, too much text, missing state feedback, poor default choices, and unnecessary user decisions.

**Skill Design**
Looks for weak trigger descriptions, overlong instructions, excessive questioning, missing validation, vague cycle exit rules, and no evolution path.

## Role Selection

Use only the roles that match the task. For skill creation, use Skill Design plus Product/UX and QA/Test by default. For security-sensitive code, include Security/Safety.
