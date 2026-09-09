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

## 5. Formal Sprint close
A formal Sprint must produce:
- contracted primary artifact
- Project State delta
- Route Interface delta if assumptions changed
- Open Question / Closure Debt delta if relevant
- Artifact Registry update
- process artifact moved to `archive/sprints/` after distillation
- final workflow state (`NEXT / HUMAN_GATE / ROLLBACK_PARENT`)

## 6. Human Gate
Stop for:
- aesthetic commitment among strong candidates
- Route kill/merge/split
- architecture mutation
- promotion to `LOCKED`
- material change to a Human Decision
- unresolved high-impact collision

Do not self-approve these.

## 7. Harness changes
All Harness changes follow `harness/08_HARNESS_CHANGE_POLICY.md`.

A creative failure is evidence, not permission to add a new Core/Module rule.
Repair the narrowest responsible layer, calibrate, regress, distill, then promote or revert.

## 8. Game implementation
`game/` implements approved Project State.
Do not treat Ren'Py script text as the authoritative source of narrative canon when it conflicts with `project/state/`.
