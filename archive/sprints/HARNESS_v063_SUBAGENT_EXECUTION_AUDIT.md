# Harness v0.6.3 — Subagent Execution Audit

## OBSERVE
A single thread can follow role order but cannot honestly claim independent Cold Reader or reviewer evidence after authoring the same candidate.

## LOCALIZE
`ROUTER_ORCHESTRATOR` + execution adapter. No Core change required.

## PATCH
- fresh role threads for cognition-sensitive Formal Sprint work when subagents are available
- frozen artifact before Review
- reviewer allowlists exclude author rationale, rejected variants, and peer reviews
- model diversity preferred for at least one independent reviewer
- parallel read-heavy Review; single-writer active State
- audit records agent/model/effort/context provenance
- project Codex adapter maps roles to capability-appropriate models

## CALIBRATE / REGRESS
Calibration: `archive/calibration/CAL_EXECUTION_INDEPENDENCE.yaml`.
Static regression passed on main:
- Harness lint PASS
- Project lint PASS, including Codex agent/config invariants
- Registry validation PASS
- all six Route Context Pack smoke tests PASS

Controls preserve two important non-goals: mechanical tasks are not forced into unnecessary subagents, and reviewers do not write active State.

## DISTILL
No new Core rule and no new active Harness module. Model names remain outside generic Harness policy under `.codex/`.

## Remaining runtime proof
A real Codex Remote Formal Sprint must still verify that the client actually spawns the configured fresh role threads and reports the requested model/effort profiles. Until that pilot passes, v0.6.3 is structurally validated but runtime behavior remains unproven.
