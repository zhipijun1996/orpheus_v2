# Harness Change Policy

Purpose: let the Harness learn without turning local failures into global creative bias or growing default context.

## A. Self-modification protocol

Every change follows:
`OBSERVE -> LOCALIZE -> PATCH -> CALIBRATE -> REGRESS -> DISTILL -> STABLE | REVERT`

- **OBSERVE:** record the failure as evidence, not a rule.
- **LOCALIZE:** assign the narrowest responsible layer: `PROJECT_DATA / TEMPLATE / MODULE / ROUTER_ORCHESTRATOR / CORE`.
- **PATCH:** prefer `REPLACE -> MERGE -> DELETE -> ADD`; keep one authoritative home and state a quality/process test rather than a preferred story solution.
- **CALIBRATE:** keep the motivating concrete case outside ordinary creative context.
- **REGRESS:** test the motivating case plus at least two meaningfully different cases; verify the repair, false-positive rate, dramatic-shape neutrality, and context cost.
- **DISTILL:** replace superseded wording, merge overlap, remove residue, archive evidence.
- **STABLE / REVERT:** Core changes additionally require Human approval.

## B. Module evolution

Most learning belongs to the responsible Module, not Core. Modules may change audit dimensions, Gate criteria, required inputs, output schema, and failure classification.

Dimension decisions:
- `REFINE` when an existing concept can absorb the failure.
- `SPLIT` when one dimension combines independent judgments and regression shows the split helps.
- `ADD` only when the issue is orthogonal, recurs across meaningfully different cases, and changes a Gate, verdict, or ranking.
- `MERGE / DELETE` when dimensions overlap or rarely affect decisions.

3–6 primary dimensions is a normal range, not a cap. Exceeding it triggers consolidation review; net growth requires measurable regression benefit.

## C. Core discipline

Core is the last promotion layer. A Core rule must recur across Modules, remain solution-neutral, fit one sentence, and lack a cleaner narrower owner.

Core limits: maximum 10 rules; no project examples, anecdotes, rejected ideas, or solution catalogs.

## D. Negative-prior hygiene

Failed ideas remain evidence rather than active creative constraints. Active policy should express the general quality test. Solution-specific exclusions belong only to genuine hard boundaries or explicit architectural contracts.

## E. Context conservation

Stable patches replace old wording. Calibration and superseded versions stay non-default. One concept has one active owner. A permanent increase in default creative context requires explicit benefit and Human approval.

After stable Harness changes, check Core count, active policy size, duplicate concepts, default context size, Module dimension count, and regression status. If active policy grows across consecutive versions without demonstrated capability gain, run `HARNESS_SIMPLIFY` before adding features.
