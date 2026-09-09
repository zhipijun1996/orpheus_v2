from pathlib import Path
import yaml, sys, tomllib

root=Path(__file__).resolve().parents[1]
errors=[]
route_ids={"FLESH","ECHO","ORIGIN","BLINDSPOT","NOBODY","NULL"}
ordinary=route_ids-{"NULL"}

found={p.stem for p in (root/"project/state/routes").glob("*.yaml")}
if found!=route_ids: errors.append(f"Route set mismatch: expected={sorted(route_ids)} found={sorted(found)}")
iface_paths={p.stem:p for p in (root/"project/state/interfaces").glob("*.yaml")}
if set(iface_paths)!=ordinary: errors.append(f"Interface set mismatch: expected={sorted(ordinary)} found={sorted(iface_paths)}")

shared=yaml.safe_load((root/"project/state/shared.yaml").read_text(encoding="utf-8")); shared_text=yaml.safe_dump(shared,allow_unicode=True)
for phrase in ["未来程砚作为独立身体回到2036","成熟阿尔戈传递人格/神经状态而非新增肉身","NULL就是未来程砚"]:
    if phrase in shared_text: errors.append(f"Route-local truth leaked into shared state: {phrase}")
for phrase in ["未来人已确认","未来制造物已确认","客观证明来自未来","未来访客已确认"]:
    if phrase in shared_text: errors.append(f"NOBODY-killing future-origin assertion in shared state: {phrase}")
for old in ["BODY","ZERO","OBSERVATION","NO_SOURCE"]:
    if (root/f"project/state/routes/{old}.yaml").exists(): errors.append(f"Legacy active route file exists: {old}.yaml")

ch2=yaml.safe_load((root/"project/state/scenes/CH2.yaml").read_text(encoding="utf-8"))
unknown=" ".join(ch2["character_knowledge"]["does_not_know"])
if "未来是否成功发展出成熟阿尔戈" not in unknown: errors.append("CH2 missing future-success knowledge boundary")

contract_path=root/"project/state/STORY_CONTRACT.yaml"
if not contract_path.exists(): errors.append("Missing Project Story Contract")
else:
    contract=yaml.safe_load(contract_path.read_text(encoding="utf-8"))
    if contract.get("shared_story_anchor",{}).get("artifact_id")!="SCENE_CH2": errors.append("Story Contract must anchor ordinary Routes to SCENE_CH2")
    chapters=contract.get("chapter_architecture",{})
    if str(chapters.get("ch4",{}).get("time_anchor"))!="2054": errors.append("Story Contract Ch4 must anchor to 2054")
    if chapters.get("ch5",{}).get("time_anchor")!="2036_CAUSAL_LAYER": errors.append("Story Contract Ch5 must enter the 2036 causal layer")
    if chapters.get("ch5",{}).get("physical_future_return_required") is not False: errors.append("Story Contract must not require physical future return in every Route")

    core=contract.get("core_route_mysteries",{})
    required_core={"accident_causality","null_mystery","zhou_0317_role","lin_0317_role"}
    if not required_core.issubset(core): errors.append("Story Contract missing required core mystery dimensions")
    null=core.get("null_mystery",{})
    if null.get("route_engagement")!="REQUIRED" or null.get("route_resolution")!="LOCAL_COMMITMENT_REQUIRED": errors.append("NULL mystery must stay Shared-open but close locally in every ordinary Route")
    required_null={"ontology","agency","actions","motive","objective","causal_impact","apparent_contradiction"}
    if not required_null.issubset(set(null.get("required_answers",[]))): errors.append("NULL mystery answer contract incomplete")
    if null.get("identity_only_resolution")!="insufficient": errors.append("NULL identity-only reveal must be insufficient")

    fusion=contract.get("route_engine_fusion",{})
    if not fusion.get("diagnostics") or fusion.get("verdicts",{}).get("DETACHED") is None: errors.append("Story Contract missing Route Engine fusion diagnostics")
    if contract.get("truth_layers",{}).get("rule") is None: errors.append("Story Contract must distinguish Evidence from Truth/Story Engine")

    mech=contract.get("mechanism_discipline",{})
    if set(mech.get("classes",{}))!={"ENGINE","SUPPORT","PATCH"}: errors.append("Mechanism discipline must distinguish ENGINE/SUPPORT/PATCH")
    if not mech.get("explore") or not mech.get("synthesis_preference"): errors.append("Mechanism discipline must protect Explore novelty and rank by leverage")

for rid,p in iface_paths.items():
    data=yaml.safe_load(p.read_text(encoding="utf-8"))
    if "must_remain_open" in data.get("shared_inputs",{}): errors.append(f"{rid} still uses must_remain_open; use dimension-only shared_open_dimensions")
    dims=data.get("shared_open_dimensions")
    if not isinstance(dims,list) or any(not isinstance(x,str) for x in dims): errors.append(f"{rid} shared_open_dimensions must be string dimension ids")
    for x in dims or []:
        if any(token in x for token in ["是否","就是","不规定","必须不是"]): errors.append(f"{rid} shared openness enumerates solution language: {x}")
    rd=data.get("route_dimensions",{})
    if not isinstance(rd,dict): errors.append(f"{rid} route_dimensions must be a mapping")
    for dim,policy in (rd or {}).items():
        if policy.get("engagement") not in {"REQUIRED","OPTIONAL"}: errors.append(f"{rid}:{dim} invalid engagement")
        if policy.get("resolution") not in {"LOCAL_COMMITMENT_REQUIRED","FUNCTION_REQUIRED","PARTIAL_ALLOWED","MAY_REMAIN_OPEN"}: errors.append(f"{rid}:{dim} invalid resolution")

origin_iface=yaml.safe_load((root/"project/state/interfaces/ORIGIN.yaml").read_text(encoding="utf-8"))
for dim in ["daughter_temporal_role","parent_child_temporal_causality"]:
    p=origin_iface.get("route_dimensions",{}).get(dim,{})
    if p.get("engagement")!="REQUIRED" or p.get("resolution")!="LOCAL_COMMITMENT_REQUIRED": errors.append(f"ORIGIN must locally commit required dimension: {dim}")

origin=yaml.safe_load((root/"project/state/routes/ORIGIN.yaml").read_text(encoding="utf-8"))
if "2054成年" in yaml.safe_dump(origin,allow_unicode=True): errors.append("ORIGIN route state still hard-seeds an adult-at-2054 daughter")
daughter=yaml.safe_load((root/"project/state/characters/DAUGHTER.yaml").read_text(encoding="utf-8"))
if daughter.get("working_label")=="成年养女": errors.append("Daughter working label still fixes adulthood")
if "age_at_2054" not in daughter.get("open_dimensions",[]): errors.append("Daughter age_at_2054 should remain an open dimension")

registry=yaml.safe_load((root/"project/registry/ARTIFACT_REGISTRY.yaml").read_text(encoding="utf-8"))["entries"]
story_entry=next((e for e in registry if e.get("id")=="STORY_CONTRACT"),None)
if not story_entry or "ROUTE_ENGINE" not in story_entry.get("load_for_modes",[]): errors.append("STORY_CONTRACT must load for ROUTE_ENGINE mode")

for p in (root/"harness").rglob("*"):
    if not p.is_file() or p.name=="CHANGELOG.md": continue
    txt=p.read_text(encoding="utf-8",errors="ignore")
    for term in ["程砚","林岚","周启明","FLESH","ECHO","ORIGIN","BLINDSPOT","NOBODY","奥菲斯计划"]:
        if term in txt: errors.append(f"Project-specific term leaked into active Harness: {term} in {p.relative_to(root)}")

cfg_path=root/".codex/config.toml"
if not cfg_path.exists(): errors.append("Missing .codex/config.toml")
else:
    cfg=tomllib.loads(cfg_path.read_text(encoding="utf-8")); agents_cfg=cfg.get("agents",{})
    if agents_cfg.get("enabled") is not True: errors.append("Codex subagents must be enabled")
    if agents_cfg.get("max_concurrent_threads_per_session",0)<4: errors.append("Codex subagent concurrency cap must allow at least 4 review threads")

required={"forge":"forge.toml","evidence_scout":"evidence-scout.toml","cold_reader":"cold-reader.toml","drama_reviewer":"drama-reviewer.toml","mystery_reviewer":"mystery-reviewer.toml","logic_scout":"logic-scout.toml","synthesizer":"synthesizer.toml"}
loaded={}
for role,filename in required.items():
    p=root/".codex/agents"/filename
    if not p.exists(): errors.append(f"Missing Codex custom agent: {filename}"); continue
    data=tomllib.loads(p.read_text(encoding="utf-8")); loaded[role]=data
    if data.get("name")!=role: errors.append(f"Agent name mismatch in {filename}: {data.get('name')} != {role}")
    if not data.get("model") or not data.get("model_reasoning_effort"): errors.append(f"Agent must pin model and reasoning effort: {filename}")
    if data.get("sandbox_mode")!="read-only": errors.append(f"Subagent must be read-only; primary thread owns writes: {role}")
if "forge" in loaded and "cold_reader" in loaded and loaded["forge"].get("model")==loaded["cold_reader"].get("model"): errors.append("Cold Reader model must differ from Forge model")

print("PROJECT LINT:","PASS" if not errors else "FAIL")
for e in errors: print("ERROR:",e)
sys.exit(1 if errors else 0)
