# Context Router

Default context:
`Core + Task Manifest + Target Artifact + direct dependencies + task-semantic dependencies`

## Layers
- L0: Core / task
- L1: target state
- L2: direct truth, character, ledger, interface, or task-contract dependencies
- L3: explicit comparison material
- L4: provenance / archive

## Load policy
- `PROVISIONAL` / `LOCKED`: dependency-loadable.
- `CANDIDATE`: only when named or activated by task semantics.
- `RAW_SEED`: Forge / Seed Collision only.
- `ARCHIVED`: provenance, audit, or recovery only.
- Cross-route work reads Interfaces before full Route artifacts.

## Task-semantic routing
Task mode may activate Registry artifacts tagged `load_for_modes`; their declared dependencies then load normally. This is how a task receives required story/chapter contracts or anchor material without repeating them in the user prompt or making them default context for unrelated work.

## Role isolation
Use allowlisted role slices, not Sprint history.

- Forge: target + task contract + hard constraints + selected seeds.
- Cold Reader: frozen player-facing artifact + minimum comprehension facts.
- Drama / Mystery: frozen work + required factual/task dependencies.
- Logic Scout: frozen spine/reveal + hard constraints.
- Closure: full Truth / Knowledge / Physical / Information ledgers.
- Cross-route Synthesis: active Interfaces; open full Routes only for named collisions.
- Synthesizer: frozen candidates + frozen reviews + required task constraints.

Reviewers do not receive Forge rationale, rejected variants, or each other's conclusions.

Isolation labels:
`FRESH_SESSION` = new external thread; `SUBAGENT_THREAD` = native subagent with partial/unknown parent-history isolation; `SELF_REVIEW` = same thread.

Full Cold Reader independence requires `FRESH_SESSION`.

## Budget
Default must-read: 3–5 short artifacts. Worker results return distilled findings; long intermediate reasoning stays outside the primary thread.

Calibration/regression artifacts never enter ordinary creative context.
