# AGENTS.md — Orpheus Autonomous Development Contract

## 1. Entry rule
Do not recursively read the repository.

For an ordinary creative task, start with:
1. `harness/00_CORE.md`
2. `project/PROJECT_BRIEF.md`
3. `runtime/ACTIVE_TASK.yaml`
4. the generated `runtime/CONTEXT_PACK.yaml`

Use `tools/build_context_pack.py` rather than choosing historical files by filename.

## 2. Authority
- `LOCKED`: Human commitment; ordinary agents cannot mutate it.
- `PROVISIONAL`: current working direction; material challenges escalate to Human Gate.
- `CANDIDATE`: task must explicitly target/select it.
- `RAW_SEED`: Forge/Seed-Collision only.
- `ARCHIVED`: provenance only.

A file existing in Git does not make it active.

## 3. Archive isolation
Ordinary story generation does not read:
- `archive/`
- Calibration cases
- superseded Harness versions
- old Sprint reports
- legacy G2 baselines

These may be loaded only by a Harness-maintenance, provenance, regression, or explicit recovery task.

## 4. Shared vs Route Truth
Do not promote Route-local mechanisms into Shared truth.

Shared story should preserve observation when viable Routes require incompatible explanations.

If a proposed Shared fact kills an active Route Interface:
- open an Integration Debt / collision,
- change Shared,
- change/merge/drop a Route through the proper Gate,
- or escalate to Human Gate.

## 5. Independent execution
The primary thread is the Orchestrator and only writer of active Project State.

For cognition-heavy Formal creative Sprints, prefer the Codex fresh-session adapter at `harness/adapters/codex/` over relying on native subagent history isolation. The adapter starts new SDK threads for Forge, Review, and Synthesis and records model/thread provenance.

Execution labels:
- `FRESH_SESSION`: new external Codex thread; qualifies for full context-independence claims.
- `SUBAGENT_THREAD`: native subagent; useful parallel worker, but parent-history isolation is not assumed.
- `SELF_REVIEW`: primary thread reviewing its own work; not independent.

Rules:
- freeze candidate artifacts before Review
- Cold Reader must use `FRESH_SESSION` to count as fully independent
- run independent Review roles in parallel from the same frozen artifact when possible
- reviewers do not receive Forge rationale, rejected variants, or each other's conclusions
- prefer a different model profile for at least one independent reviewer than the authoring role
- native subagents remain valid for bounded extraction, cheap exploration, or degraded review
- worker sessions return findings only; the primary thread performs all State/Registry writes
- if a required independent review cannot be produced, record the downgrade and stop at `HUMAN_GATE` rather than claiming an independent PASS

Purely mechanical tasks may stay on the primary thread.

## 6. Formal Sprint close
Follow `harness/06_OUTPUTS.md`.

Every formal Sprint must produce in `runtime/CURRENT_SPRINT/`:
- `SPRINT_REPORT.md`
- `PRIMARY_ARTIFACT` or `PRIMARY/`
- `AUDIT_REPORT.md`
- `STATE_DELTA.yaml`

Then apply the writeback described by `STATE_DELTA.yaml` to Project State, Route Interface, Open Questions / Closure Debt, Artifact Registry, and Archive as relevant.

A Sprint is not complete until writeback is applied and a final workflow state is set: `NEXT / HUMAN_GATE / ROLLBACK_PARENT`.

## 7. Human Gate
Stop for:
- aesthetic commitment among strong candidates
- Route kill/merge/split
- architecture mutation
- promotion to `LOCKED`
- material change to a Human Decision
- unresolved high-impact collision

Do not self-approve these.

## 8. Harness changes
All Harness changes follow `harness/08_HARNESS_CHANGE_POLICY.md`.

A creative failure is evidence, not permission to add a new Core/Module rule.
Repair the narrowest responsible layer, calibrate, regress, distill, then promote or revert.

## 9. Game implementation
`game/` implements approved Project State.
Do not treat Ren'Py script text as the authoritative source of narrative canon when it conflicts with `project/state/`.
