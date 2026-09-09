# Context Router

Default:
`Core + Task + Target + direct dependencies + task-semantic dependencies`

## Layers
- L0 Core/task
- L1 target state
- L2 direct truth/character/interface/task-contract dependencies
- L3 explicit comparison
- L4 provenance/archive

## Load policy
- `PROVISIONAL` / `LOCKED`: dependency-loadable.
- `CANDIDATE`: named or task-activated only.
- `RAW_SEED`: Forge / Seed Collision only.
- `ARCHIVED`: provenance, audit, or recovery only.
- Cross-route work reads Interfaces before full Routes.

## Task semantics
Task mode activates Registry artifacts tagged `load_for_modes`; their dependencies load normally. Use this for required story/chapter contracts or anchor material instead of repeating them in prompts or default context.

## Role isolation
Role slices are allowlists, not Sprint history. Forge gets task constraints; Review gets frozen work plus only required dependencies; Synthesis gets frozen candidates/reviews plus task constraints. Reviewers do not receive Forge rationale, rejected variants, or each other's conclusions.

Isolation: `FRESH_SESSION` = new external thread; `SUBAGENT_THREAD` = native subagent with unknown/partial parent-history isolation; `SELF_REVIEW` = same thread. Full Cold Reader independence requires `FRESH_SESSION`.

## Budget
Default must-read: 3–5 short artifacts. Return distilled findings; keep long intermediate reasoning outside the primary thread. Calibration/regression never enters ordinary creative context.
