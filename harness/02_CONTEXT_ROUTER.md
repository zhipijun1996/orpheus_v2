# Context Router

Default context:
`Core + Task Manifest + Target Artifact + direct dependencies`

## Layers
- L0: Core / task
- L1: target state
- L2: direct truth, character, ledger, or interface dependencies
- L3: explicit comparison material
- L4: provenance and archive

## Load policy
- `PROVISIONAL` and `LOCKED` state may load by dependency.
- `CANDIDATE` loads only when named by the Task.
- `RAW_SEED` loads only for Forge or Seed Collision.
- `ARCHIVED` process material loads only for provenance, audit, or explicit recovery.
- Cross-route work reads Route Interfaces before full Route artifacts.

## Role isolation
A role receives an allowlisted slice, not the whole Sprint history.

Isolation labels:
- `FRESH_SESSION` — new external Codex thread; parent conversation is not resumed or forked.
- `SUBAGENT_THREAD` — native subagent thread; treat parent-history isolation as partial/unknown.
- `SELF_REVIEW` — same thread; no independence claim.

Rules:
- Forge receives target constraints and selected seeds, not later reviews.
- Cold Reader receives the frozen player-facing artifact plus only minimum comprehension facts.
- Other Review roles receive the frozen artifact plus their required factual dependencies.
- Reviewers do not receive Forge rationale, rejected variants, or other reviewers' conclusions.
- Synthesizer receives frozen candidates and frozen review outputs, not exploratory process notes.
- Full Cold Reader independence requires `FRESH_SESSION`; a native subagent alone is not proof of context isolation.

The Codex fresh-session adapter embeds the allowlisted context directly into each new SDK thread and runs the worker read-only with network/web search disabled. This is conversation isolation plus process discipline; it is not claimed as OS-level denial of every host file.

## Role slices

### Forge
Reads target, basic character facts, hard constraints, and selected seeds.

### Stage
Reads selected spine, character relations, and necessary facts.

### Cold Reader
Reads only frozen player-facing story material and minimum comprehension facts.

### Drama / Mystery Review
Reads the frozen work plus required factual dependencies.

### Logic Scout
Reads the frozen spine, reveal, and hard constraints; returns `CLEAR / RISK / DEAD`.

### Closure
Reads full Truth / Knowledge / Physical / Information ledgers.

### Cross-route Synthesis
Reads active Route Interfaces and only opens full Route artifacts to resolve a named collision.

## Budget
Default must-read set: 3–5 short artifacts.
Worker results return distilled findings; long intermediate reasoning stays outside the primary thread.

## Calibration isolation
Calibration and regression artifacts are never part of ordinary creative context.
They are loaded only by Harness-maintenance Tasks.
A story-generation Task cannot request Calibration material as `may` context.
