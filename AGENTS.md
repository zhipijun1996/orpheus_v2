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

## 5. Subagent execution
In local Codex runtimes that expose subagents, a Formal creative Sprint must delegate cognition-sensitive Harness roles instead of silently doing all roles in the primary thread.

The primary thread is the Orchestrator and only writer of active Project State.

Use project custom agents when applicable:
- `forge` for divergent generation
- `evidence_scout` for bounded extraction
- `cold_reader`, `drama_reviewer`, `mystery_reviewer`, `logic_scout` for independent review
- `synthesizer` for convergence after reviews freeze

Rules:
- freeze candidate artifacts before Review
- spawn review roles as fresh threads; run independent reviewers in parallel when possible
- do not give reviewers Forge rationale, rejected variants, or each other's conclusions
- main-thread self-critique does not count as independent Cold Reader evidence
- prefer a different model profile for at least one independent reviewer than the authoring role
- subagents return findings; the primary thread performs state/registry writes
- if a required fresh reviewer cannot be spawned, record the limitation and stop at `HUMAN_GATE` rather than claiming an independent PASS

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
