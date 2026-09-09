from pathlib import Path
import yaml, sys

root=Path(__file__).resolve().parents[1]
target=sys.argv[1] if len(sys.argv)>1 else "ROUTE_NOBODY"
task=sys.argv[2] if len(sys.argv)>2 else "UNSPECIFIED"
reg=yaml.safe_load((root/"project/registry/ARTIFACT_REGISTRY.yaml").read_text(encoding="utf-8"))["entries"]
byid={e["id"]:e for e in reg}
if target not in byid:
    raise SystemExit(f"Unknown target id: {target}")
selected=["HARNESS_CORE","PROJECT_BRIEF","HUMAN_DECISIONS",target]
if target.startswith("ROUTE_") and target != "ROUTE_NULL":
    rid=target.removeprefix("ROUTE_")
    iid=f"IFACE_{rid}"
    if iid in byid:
        selected.append(iid)
for d in byid[target].get("depends_on",[]): selected.append(d)
for sid in list(selected):
    for d in byid[sid].get("depends_on",[]) if sid in byid else []:
        if byid[d]["kind"] in {"state","route_interface","decision_state"}: selected.append(d)
seen=set(); selected=[x for x in selected if not (x in seen or seen.add(x))]
files=[]; chars=0
for sid in selected:
    e=byid[sid]
    if e["status"]=="archived" or e["kind"] in {"sprint","calibration","legacy_baseline"}:
        raise SystemExit(f"Archive/provenance leak: {sid}")
    p=root/e["path"]; text=p.read_text(encoding="utf-8"); chars+=len(text)
    files.append({"id":sid,"path":e["path"],"status":e["status"],"chars":len(text)})
pack={"state":"GENERATED","task_id":task,"target":target,"files":files,"total_chars":chars,"budget_chars":14000,"within_budget":chars<=14000}
print(yaml.safe_dump(pack,allow_unicode=True,sort_keys=False))
if chars>14000: raise SystemExit("Context budget exceeded")
