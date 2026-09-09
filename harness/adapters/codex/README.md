# Codex Fresh-Session Adapter

Purpose: run cognition-heavy Harness roles in separate Codex SDK threads so independent review does not inherit the authoring thread's conversation history.

## Setup

Requires Node.js 18+ and an authenticated local Codex CLI.

```bash
npm install --prefix harness/adapters/codex
```

## Run

```bash
npm --prefix harness/adapters/codex run sprint -- \
  --task <TASK_ID> \
  --target <REGISTRY_ID> \
  --mode <TASK_MODE> \
  --goal "<goal>"
```

`--mode` controls task-semantic Context Pack dependencies. Route Story Engine work uses `ROUTE_ENGINE`; matching Registry artifacts such as the Project Story Contract and its shared anchor are loaded automatically. If omitted, Route/Story Engine task IDs are inferred as `ROUTE_ENGINE`, otherwise `GENERAL`.

The adapter generates the Context Pack, runs fresh Forge sessions, freezes candidates, runs fresh Review sessions in parallel, then runs a fresh Synthesizer session. Results and thread metadata go to `runtime/FRESH_SESSIONS/<run_id>/`.

It does **not** mutate Project State. The primary Orchestrator consumes the synthesis/audits, completes the four Formal Sprint outputs, applies `STATE_DELTA.yaml`, runs checks, and stops at the Harness terminal state.

## Seed-aware Forge fanout

For `ROUTE_ENGINE`, the default Forge fanout is 4 fresh sessions, each returning 2 candidates (normally 8 raw candidates total):

1. one permanent **BLIND** control with no Idea Seed exposure;
2. one worker with one optional Seed;
3. one worker with a different-kind optional Seed;
4. one worker with two cross-kind optional Seeds.

Seeds come from `project/ideas/creative_seeds.yaml`, which is `default_load: false` and is never part of the ordinary Context Pack. Seeded workers may use, mutate, fuse, invert, or reject their Seeds. Reviewers and the Synthesizer receive only frozen candidate text; Seed provenance is withheld until after convergence and written separately to `SEED_PROVENANCE.json`.

Controls:

```bash
# cheaper run; still keeps Forge 1 blind
--forge-workers 2

# no Seed exposure at all
--seed-policy off

# controlled cross-kind scheduling (default for ROUTE_ENGINE)
--seed-policy controlled

# stochastic Seed scheduling
--seed-policy random

# restrict Seeded workers to specific Seeds; adversarial probes can be addressed only this way
--seed-ids CAUSE-06,REL-04
```

Meta Seeds are excluded from ordinary Route runs by default. `ROUTE_NULL` enables them automatically; `--include-meta-seeds` can opt in elsewhere.

## Anonymous human-baseline benchmark

A registered `kind: human_baseline` artifact can be added **after Forge generation** for an anonymous core-engine comparison:

```bash
--baseline-id BASELINE_ORIGIN_HUMAN
```

The baseline is never loaded into the Context Pack and is never shown to Forge. After Forge finishes, its text is mixed with the Forge candidate sets under anonymous `Candidate Set N` labels. Reviewers and Synthesis are told only that candidate sets may differ in development depth; they are not told which set is human-authored, blind, or Seed-exposed.

In benchmark mode, Review/Synthesis separates **core engine value** from **development debt**. It compares 30-second clarity, character/speculative/shared-mystery fusion, Route identity, central-mystery reinterpretation, and value conflict before rewarding present completeness. Candidate/source mapping is restored only after Synthesis in `CANDIDATE_PROVENANCE.json`.

Human baselines must be registered with `default_load: false` and no `load_for_modes`; the runner rejects any baseline that leaks into the normal Context Pack.

## Model routing

Defaults live in `roles.json`. Override a role without editing policy, for example:

```bash
HARNESS_MODEL_COLD_READER=gpt-5.6-terra \
npm --prefix harness/adapters/codex run sprint -- ...
```

If a requested model is unavailable, the adapter retries with the runtime default and records the degradation in `MANIFEST.json`.

## Independence meaning

`FRESH_SESSION` means a new SDK thread was created rather than resuming/forking the author thread. Workers receive embedded role allowlists and run read-only with network/web search disabled. This does not claim OS-level read isolation from every host file.
