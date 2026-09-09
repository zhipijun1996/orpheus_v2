# Orchestrator

## State machine
`EXPLORE -> BUILD -> REVIEW -> SYNTHESIZE`

Exits: `NEXT / INTEGRATION_CHECK / HUMAN_GATE / ROLLBACK_PARENT`.

## Execution
The primary thread is Orchestrator + sole active-State writer.

Independence labels:
- `FRESH_SESSION` — new external thread; full independence claim allowed.
- `SUBAGENT_THREAD` — native subagent; useful, but parent-history isolation is not assumed.
- `SELF_REVIEW` — same thread; never independent.

Formal creative Sprints SHOULD use the Codex fresh-session adapter for Cold Reader and other independence-sensitive reviews. Native subagents remain valid for bounded extraction, cheap divergence, and degraded review.

At least one independent reviewer SHOULD differ from the authoring model profile. Model diversity does not replace context freshness.

## Concurrency
- EXPLORE: 2–3 Forge workers when useful.
- REVIEW: independent read-heavy reviewers may run in parallel on the same frozen artifact.
- SYNTHESIZE: waits for required reviews.
- State / Registry writes: primary thread only.

## Sprint budget
- max 4 Formal Tasks per Sprint
- max 2 divergence rounds per problem
- Explore: 6–10 short candidates

## Triggers
`ROLLBACK_PARENT` when distinct child solutions repeat the same parent-caused failure.

`INTEGRATION_CHECK` when a Route gains a provisional Story Engine, a Route changes topology, shared observations harden, or 2+ active Interfaces changed.

`DISTILL_CHECK` after 5 Formal Tasks, context-budget overflow, 3+ duplicate active facts, or a Sprint closes with a new provisional decision.

Harness changes follow `08_HARNESS_CHANGE_POLICY.md`; Core promotion requires Human approval.

Run `HARNESS_SIMPLIFY` when active policy grows without capability gain, duplicate concepts accumulate, or default context expands without need.

## Autonomous ceiling
Autonomous work may advance to `READY_FOR_HUMAN`.
