from pathlib import Path
import yaml, sys

root = Path(__file__).resolve().parents[1]
errors=[]
route_ids={"FLESH","ECHO","ORIGIN","BLINDSPOT","NOBODY","NULL"}
ordinary=route_ids-{"NULL"}
found={p.stem for p in (root/"project/state/routes").glob("*.yaml")}
if found != route_ids: errors.append(f"Route set mismatch: expected={sorted(route_ids)} found={sorted(found)}")
iface={p.stem for p in (root/"project/state/interfaces").glob("*.yaml")}
if iface != ordinary: errors.append(f"Interface set mismatch: expected={sorted(ordinary)} found={sorted(iface)}")
shared=yaml.safe_load((root/"project/state/shared.yaml").read_text(encoding="utf-8")); shared_text=yaml.safe_dump(shared,allow_unicode=True)
for phrase in ["未来程砚作为独立身体回到2036","成熟阿尔戈传递人格/神经状态而非新增肉身","NULL就是未来程砚"]:
    if phrase in shared_text: errors.append(f"Route-local truth leaked into shared state: {phrase}")
for phrase in ["未来人已确认","未来制造物已确认","客观证明来自未来","未来访客已确认"]:
    if phrase in shared_text: errors.append(f"NOBODY-killing future-origin assertion in shared state: {phrase}")
for old in ["BODY","ZERO","OBSERVATION","NO_SOURCE"]:
    if (root/f"project/state/routes/{old}.yaml").exists(): errors.append(f"Legacy active route file exists: {old}.yaml")
ch2=yaml.safe_load((root/"project/state/scenes/CH2.yaml").read_text(encoding="utf-8")); unknown=" ".join(ch2["character_knowledge"]["does_not_know"])
if "未来是否成功发展出成熟阿尔戈" not in unknown: errors.append("CH2 missing future-success knowledge boundary")
for p in (root/"harness").rglob("*"):
    if not p.is_file() or p.name == "CHANGELOG.md": continue
    txt=p.read_text(encoding="utf-8",errors="ignore")
    for term in ["程砚","林岚","周启明","FLESH","ECHO","ORIGIN","BLINDSPOT","NOBODY","奥菲斯计划"]:
        if term in txt: errors.append(f"Project-specific term leaked into active Harness: {term} in {p.relative_to(root)}")
print("PROJECT LINT:", "PASS" if not errors else "FAIL")
for e in errors: print("ERROR:",e)
sys.exit(1 if errors else 0)
