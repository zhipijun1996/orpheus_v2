# Harness v0.6.4 — Fresh Session Execution Audit

## Failure localized
v0.6.3 treated a native subagent thread as if it guaranteed clean parent-history isolation. That guarantee is not part of the execution contract.

## Patch
- independence labels split into `FRESH_SESSION / SUBAGENT_THREAD / SELF_REVIEW`;
- full Cold Reader independence requires a new external Codex thread;
- added `harness/adapters/codex/` using the official TypeScript Codex SDK;
- fresh workers receive embedded role allowlists, run read-only/offline, and return artifacts only;
- active Project State remains single-writer in the primary Orchestrator.

## Regression intent
- fresh external thread: independence claim valid;
- native subagent: useful but partial/unknown parent-history isolation;
- mechanical task: no forced multi-session overhead;
- unavailable preferred model: record degradation rather than falsify model diversity.

## Status
Policy/config lint must pass before use. Runtime behavior still requires a real Remote pilot.
