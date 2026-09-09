# orpheus_v2

正式 Project State Bootstrap v0.1。

## Repository layers
- `harness/` — 通用叙事创作OS，不包含奥菲斯具体剧情案例
- `project/` — 《奥菲斯计划：03:17》当前有效状态
- `runtime/` — 当前Task/Context Pack/Sprint临时区
- `archive/` — 历史过程与校准证据，默认不读
- `game/` — Ren'Py正式工程
- `tools/` — 奥菲斯项目级状态/上下文检查
- `.github/workflows/` — GitHub CI

## Current Routes
FLESH / ECHO / ORIGIN / BLINDSPOT / NOBODY / NULL(meta)

## Bootstrap rule
旧G2文档保留在Archive，但不再拥有全局Canon权威。
当前工作状态以 `project/state/` + `project/decisions/` 为准。

## Local checks
```bash
pip install pyyaml
python harness/tools/lint_harness.py
python tools/lint_project.py
python tools/validate_registry.py
python tools/build_context_pack.py ROUTE_NOBODY NOBODY_LEDGER
```
