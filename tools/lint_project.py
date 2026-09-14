from pathlib import Path
import json, yaml, sys, tomllib

root=Path(__file__).resolve().parents[1]
errors=[]
route_ids={"FLESH","ECHO","ORIGIN","BLINDSPOT","NOBODY","NULL"}
ordinary=route_ids-{"NULL"}

found={p.stem for p in (root/"project/state/routes").glob("*.yaml")}
if found!=route_ids: errors.append(f"Route set mismatch: expected={sorted(route_ids)} found={sorted(found)}")
iface_paths={p.stem:p for p in (root/"project/state/interfaces").glob("*.yaml")}
if set(iface_paths)!=ordinary: errors.append(f"Interface set mismatch: expected={sorted(ordinary)} found={sorted(iface_paths)}")

shared=yaml.safe_load((root/"project/state/shared.yaml").read_text(encoding="utf-8"))
if "must_remain_open" in shared: errors.append("Shared state must omit answer-menu must_remain_open lists")

ch2=yaml.safe_load((root/"project/state/scenes/CH2.yaml").read_text(encoding="utf-8"))
if not ch2.get("fixed_observations"): errors.append("CH2 missing fixed_observations")
if not ch2.get("route_obligations"): errors.append("CH2 missing route_obligations")
if not ch2.get("shared_rule") or not ch2.get("shared_delta"): errors.append("CH2 missing Shared scope/delta rule")
for legacy in ["preserve_open","route_hooks","character_knowledge"]:
    if legacy in ch2: errors.append(f"CH2 still carries legacy answer-menu field: {legacy}")

contract=yaml.safe_load((root/"project/state/STORY_CONTRACT.yaml").read_text(encoding="utf-8"))
if contract.get("shared_story_anchor",{}).get("artifact_id")!="SCENE_CH2": errors.append("Story Contract must anchor SCENE_CH2")
core=contract.get("core_route_mysteries",{})
if not {"accident_causality","null_mystery","zhou_0317_role","lin_0317_role"}.issubset(core): errors.append("Story Contract core mystery set incomplete")
if contract.get("route_engine_fusion",{}).get("verdicts",{}).get("DETACHED") is None: errors.append("Story Contract missing fusion verdicts")
if set(contract.get("mechanism_discipline",{}).get("classes",{}))!={"ENGINE","SUPPORT","PATCH"}: errors.append("Mechanism discipline incomplete")

for rid,p in iface_paths.items():
    data=yaml.safe_load(p.read_text(encoding="utf-8"))
    dims=data.get("shared_open_dimensions")
    if not isinstance(dims,list) or any(not isinstance(x,str) for x in dims): errors.append(f"{rid} shared_open_dimensions invalid")
    if not isinstance(data.get("route_dimensions",{}),dict): errors.append(f"{rid} route_dimensions invalid")

registry=yaml.safe_load((root/"project/registry/ARTIFACT_REGISTRY.yaml").read_text(encoding="utf-8"))["entries"]
byid={e.get("id"):e for e in registry}
required_author=["AUTHOR_SHARED","AUTHOR_FLESH","AUTHOR_ECHO","AUTHOR_ORIGIN","AUTHOR_BLINDSPOT","AUTHOR_NOBODY","AUTHOR_EXPERIENCE_MAP","AUTHOR_PREFLIGHT_PROTOCOL"]
for aid in required_author:
    e=byid.get(aid)
    if not e or e.get("kind")!="human_constraint" or e.get("default_load") is not False: errors.append(f"Invalid human constraint registration: {aid}")
meta=byid.get("META_RESERVATIONS")
if not meta or meta.get("default_load") is not False: errors.append("Meta reservations must stay non-default")
seed=byid.get("IDEAS_CREATIVE_SEEDS")
if not seed or seed.get("default_load") is not False: errors.append("Creative Seed pool must stay non-default")
baseline=byid.get("BASELINE_ORIGIN_HUMAN")
if not baseline or baseline.get("default_load") is not False: errors.append("Human baseline must stay non-default")

builder=(root/"tools/build_context_pack.py").read_text(encoding="utf-8")
for marker in ["ARCHITECTURE_PREFLIGHT","AUTHOR_SHARED","AUTHOR_EXPERIENCE_MAP","AUTHOR_PREFLIGHT_PROTOCOL","META_PLANNING"]:
    if marker not in builder: errors.append(f"Context builder missing marker: {marker}")

roles=json.loads((root/"harness/adapters/codex/roles.json").read_text(encoding="utf-8"))
for name in ["forge","cold_reader","drama_reviewer","mystery_reviewer","logic_scout","synthesizer"]:
    role=roles.get(name,{})
    if role.get("model")!="gpt-6-astra": errors.append(f"Fresh-session role is not GPT-6 Astra: {name}")
    if role.get("reasoning_effort") not in {"low","medium","high","xhigh"}: errors.append(f"Invalid reasoning effort: {name}")
if roles.get("forge",{}).get("reasoning_effort")==roles.get("cold_reader",{}).get("reasoning_effort"): errors.append("Forge and Cold Reader need different reasoning profiles")

runner=(root/"harness/adapters/codex/runner.mjs").read_text(encoding="utf-8")
for marker in ["baseline_id","human_baseline","ANONYMOUS_CORE_ENGINE_BENCHMARK","CANDIDATE_PROVENANCE.json"]:
    if marker not in runner: errors.append(f"Fresh-session runner missing invariant: {marker}")

for p in (root/"harness").rglob("*"):
    if not p.is_file() or p.name=="CHANGELOG.md": continue
    txt=p.read_text(encoding="utf-8",errors="ignore")
    for term in ["程砚","林岚","周启明","FLESH","ECHO","ORIGIN","BLINDSPOT","NOBODY","奥菲斯计划"]:
        if term in txt: errors.append(f"Project-specific term leaked into active Harness: {term} in {p.relative_to(root)}")

cfg=tomllib.loads((root/".codex/config.toml").read_text(encoding="utf-8"))
agents_cfg=cfg.get("agents",{})
if agents_cfg.get("enabled") is not True: errors.append("Codex subagents must be enabled")
if agents_cfg.get("default_subagent_model")!="gpt-6-astra": errors.append("Default subagent model must be GPT-6 Astra")
if agents_cfg.get("max_concurrent_threads_per_session",0)<4: errors.append("Codex subagent concurrency cap too low")

required_agents={"forge":"forge.toml","evidence_scout":"evidence-scout.toml","cold_reader":"cold-reader.toml","drama_reviewer":"drama-reviewer.toml","mystery_reviewer":"mystery-reviewer.toml","logic_scout":"logic-scout.toml","synthesizer":"synthesizer.toml"}
loaded={}
for role,filename in required_agents.items():
    p=root/".codex/agents"/filename
    if not p.exists(): errors.append(f"Missing Codex custom agent: {filename}"); continue
    data=tomllib.loads(p.read_text(encoding="utf-8")); loaded[role]=data
    if data.get("name")!=role: errors.append(f"Agent name mismatch: {filename}")
    if data.get("model")!="gpt-6-astra": errors.append(f"Native agent is not GPT-6 Astra: {role}")
    if not data.get("model_reasoning_effort"): errors.append(f"Native agent missing reasoning effort: {role}")
    if data.get("sandbox_mode")!="read-only": errors.append(f"Native agent must be read-only: {role}")
if "forge" in loaded and "cold_reader" in loaded and loaded["forge"].get("model_reasoning_effort")==loaded["cold_reader"].get("model_reasoning_effort"): errors.append("Native Forge and Cold Reader need different reasoning profiles")

print("PROJECT LINT:","PASS" if not errors else "FAIL")
for e in errors: print("ERROR:",e)
sys.exit(1 if errors else 0)
