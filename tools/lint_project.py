from pathlib import Path
import yaml, sys, tomllib

root = Path(__file__).resolve().parents[1]
errors=[]
route_ids={"FLESH","ECHO","ORIGIN","BLINDSPOT","NOBODY","NULL"}
ordinary=route_ids-{"NULL"}

found={p.stem for p in (root/"project/state/routes").glob("*.yaml")}
if found != route_ids:
    errors.append(f"Route set mismatch: expected={sorted(route_ids)} found={sorted(found)}")

iface={p.stem for p in (root/"project/state/interfaces").glob("*.yaml")}
if iface != ordinary:
    errors.append(f"Interface set mismatch: expected={sorted(ordinary)} found={sorted(iface)}")

shared=yaml.safe_load((root/"project/state/shared.yaml").read_text(encoding="utf-8"))
shared_text=yaml.safe_dump(shared,allow_unicode=True)
for phrase in ["未来程砚作为独立身体回到2036","成熟阿尔戈传递人格/神经状态而非新增肉身","NULL就是未来程砚"]:
    if phrase in shared_text:
        errors.append(f"Route-local truth leaked into shared state: {phrase}")
for phrase in ["未来人已确认","未来制造物已确认","客观证明来自未来","未来访客已确认"]:
    if phrase in shared_text:
        errors.append(f"NOBODY-killing future-origin assertion in shared state: {phrase}")

for old in ["BODY","ZERO","OBSERVATION","NO_SOURCE"]:
    if (root/f"project/state/routes/{old}.yaml").exists():
        errors.append(f"Legacy active route file exists: {old}.yaml")

ch2=yaml.safe_load((root/"project/state/scenes/CH2.yaml").read_text(encoding="utf-8"))
unknown=" ".join(ch2["character_knowledge"]["does_not_know"])
if "未来是否成功发展出成熟阿尔戈" not in unknown:
    errors.append("CH2 missing future-success knowledge boundary")

for p in (root/"harness").rglob("*"):
    if not p.is_file() or p.name == "CHANGELOG.md":
        continue
    txt=p.read_text(encoding="utf-8",errors="ignore")
    for term in ["程砚","林岚","周启明","FLESH","ECHO","ORIGIN","BLINDSPOT","NOBODY","奥菲斯计划"]:
        if term in txt:
            errors.append(f"Project-specific term leaked into active Harness: {term} in {p.relative_to(root)}")

# Codex execution adapter: enforce independence/capability invariants without freezing one future model map.
cfg_path=root/".codex/config.toml"
if not cfg_path.exists():
    errors.append("Missing .codex/config.toml")
else:
    cfg=tomllib.loads(cfg_path.read_text(encoding="utf-8"))
    agents_cfg=cfg.get("agents",{})
    if agents_cfg.get("enabled") is not True:
        errors.append("Codex subagents must be enabled")
    if agents_cfg.get("max_concurrent_threads_per_session",0) < 4:
        errors.append("Codex subagent concurrency cap must allow at least 4 review threads")

required={
    "forge":"forge.toml",
    "evidence_scout":"evidence-scout.toml",
    "cold_reader":"cold-reader.toml",
    "drama_reviewer":"drama-reviewer.toml",
    "mystery_reviewer":"mystery-reviewer.toml",
    "logic_scout":"logic-scout.toml",
    "synthesizer":"synthesizer.toml",
}
loaded={}
for role,filename in required.items():
    p=root/".codex/agents"/filename
    if not p.exists():
        errors.append(f"Missing Codex custom agent: {filename}")
        continue
    data=tomllib.loads(p.read_text(encoding="utf-8"))
    loaded[role]=data
    if data.get("name") != role:
        errors.append(f"Agent name mismatch in {filename}: {data.get('name')} != {role}")
    if not data.get("model") or not data.get("model_reasoning_effort"):
        errors.append(f"Agent must pin model and reasoning effort: {filename}")

for role in ["forge","evidence_scout","cold_reader","drama_reviewer","mystery_reviewer","logic_scout","synthesizer"]:
    if role in loaded and loaded[role].get("sandbox_mode") != "read-only":
        errors.append(f"Subagent must be read-only; primary thread owns writes: {role}")

if "forge" in loaded and "cold_reader" in loaded:
    if loaded["forge"].get("model") == loaded["cold_reader"].get("model"):
        errors.append("Cold Reader model must differ from Forge model to reduce same-model self-validation")

print("PROJECT LINT:", "PASS" if not errors else "FAIL")
for e in errors:
    print("ERROR:",e)
sys.exit(1 if errors else 0)
