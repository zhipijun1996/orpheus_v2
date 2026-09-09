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

## Model routing

Defaults live in `roles.json`. Override a role without editing policy, for example:

```bash
HARNESS_MODEL_COLD_READER=gpt-5.6-terra \
npm --prefix harness/adapters/codex run sprint -- ...
```

If a requested model is unavailable, the adapter retries with the runtime default and records the degradation in `MANIFEST.json`.

## Independence meaning

`FRESH_SESSION` means a new SDK thread was created rather than resuming/forking the author thread. Workers receive embedded role allowlists and run read-only with network/web search disabled. This does not claim OS-level read isolation from every host file.
