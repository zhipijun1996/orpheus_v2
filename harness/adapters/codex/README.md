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
  --task ORIGIN_ROUTE_ENGINE_REBOOT \
  --target ROUTE_ORIGIN \
  --goal "Build a character-driven ORIGIN Story Engine"
```

The adapter:
1. generates `runtime/CONTEXT_PACK.yaml` with the existing Project tool;
2. starts multiple fresh Forge threads;
3. freezes their candidates;
4. starts fresh Cold/Drama/Mystery/Logic review threads in parallel;
5. starts a fresh Synthesizer thread after reviews freeze;
6. stores only the resulting artifacts and thread metadata under `runtime/FRESH_SESSIONS/<run_id>/`.

It does **not** mutate Project State. The primary Codex Orchestrator consumes the synthesis/audits, completes the four Formal Sprint outputs, applies `STATE_DELTA.yaml`, runs checks, and stops at the Harness terminal state.

## Model routing

Defaults live in `roles.json`. Override any role without editing policy:

```bash
HARNESS_MODEL_COLD_READER=gpt-5.6-terra \
HARNESS_MODEL_LOGIC_SCOUT=gpt-5.6-sol \
npm --prefix harness/adapters/codex run sprint -- ...
```

If a requested model is unavailable, the adapter retries that role with the runtime default and records `degraded_model: true` in `MANIFEST.json`.

## Independence meaning

`FRESH_SESSION` means a new SDK thread was created rather than resuming/forking the author thread. The adapter also embeds an explicit role allowlist and runs workers read-only with network/web search disabled. It does not claim OS-level read isolation from every file on the host.
