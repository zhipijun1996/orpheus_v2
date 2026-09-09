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

## Fresh-thread rule
Each subagent receives an allowlisted role slice, not the whole Sprint history.

- Forge receives target constraints and selected seeds, not later reviews.
- Cold Reader receives the frozen player-facing artifact plus only facts needed to understand it.
- Other Review roles receive the frozen artifact plus their required factual dependencies.
- Reviewers do not receive Forge rationale, rejected variants, or other reviewers' conclusions.
- Synthesizer receives frozen candidates and frozen review outputs, not exploratory process notes.

If the runtime cannot provide a fresh role thread, mark the review `SELF_REVIEW`; it cannot satisfy an independence-sensitive Gate.

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

## Calibration isolation
Calibration and regression artifacts are never part of ordinary creative context.
They are loaded only by Harness-maintenance Tasks.
A story-generation Task cannot request Calibration material as `may` context.
