# Orchestrator

## State machine
`EXPLORE -> BUILD -> REVIEW -> SYNTHESIZE`

Possible exits:
- `NEXT`
- `INTEGRATION_CHECK`
- `HUMAN_GATE`
- `ROLLBACK_PARENT`

## Execution contract
The primary thread is the Orchestrator and final State Writer.

When the runtime supports subagents, a formal creative Sprint MUST use fresh role threads for cognition that benefits from independence:
- Forge / divergent exploration
- applicable Review roles
- Synthesis when multiple candidates or material review conflict exist

The primary thread may coordinate, freeze artifacts, and write state, but its own critique does not count as an independent review.

At least one independent reviewer SHOULD use a different model profile from the authoring role when the execution adapter supports model routing. If required role/model independence cannot be provided, record the degradation and do not claim an independent `PASS`; use `HUMAN_GATE` when that review is required for advancement.

Purely mechanical tasks may remain on the primary thread.

## Concurrency
Parallelize independent read-heavy work:
- EXPLORE: 2–3 Forge workers when genuine divergence is useful
- REVIEW: applicable reviewers run concurrently from the same frozen artifact
- SYNTHESIZE: starts only after required reviews freeze
- Project State / Registry writeback: primary thread only

Avoid parallel writes to active Project State.

## Sprint budget
- maximum 4 formal Tasks per Sprint
- maximum 2 divergence rounds on one problem
- Explore produces 6–10 short candidates
- every Sprint ends with a readable artifact and a state delta

## Repeated failure
When distinct child solutions repeat the same root failure, inspect the nearest shared parent assumption.
If the parent causes the failure, return `ROLLBACK_PARENT`.

## Integration trigger
Run `INTEGRATION_CHECK` when:
- a Route reaches a new provisional Story Engine
- a Route is merged, split, or dropped
- shared observations are proposed or hardened
- two or more active Route Interfaces have changed since the last check

## Distill trigger
Run `DISTILL_CHECK` when:
- 5 formal Tasks have completed
- active context exceeds budget
- the same information appears in 3+ active artifacts
- a Sprint closes with a new provisional decision

## Harness-change trigger
Creative Sprints record process failures but do not directly mutate active policy.

Any proposed Harness change must run the fixed protocol in `08_HARNESS_CHANGE_POLICY.md`:
`OBSERVE -> LOCALIZE -> PATCH -> CALIBRATE -> REGRESS -> DISTILL`.

The default repair target is the narrowest responsible Module.
Core promotion is exceptional and requires Human approval.

## Harness simplify trigger
Run `HARNESS_SIMPLIFY` when:
- active policy grows for 2 consecutive versions without a demonstrated capability gain
- a Module exceeds 6 primary audit dimensions without demonstrated regression benefit
- duplicate concepts appear in multiple active files
- default task context grows without an explicit new task requirement

`HARNESS_SIMPLIFY` may only:
`DELETE / MERGE / REPLACE / MOVE_TO_CALIBRATION`

## Autonomous ceiling
Autonomous work may advance to `READY_FOR_HUMAN`.
