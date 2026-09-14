from pathlib import Path
import yaml, sys

root=Path(__file__).resolve().parents[1]
target=sys.argv[1] if len(sys.argv)>1 else "ROUTE_NOBODY"
task=sys.argv[2] if len(sys.argv)>2 else "UNSPECIFIED"
mode=sys.argv[3] if len(sys.argv)>3 else None

if not mode:
    active_path=root/"runtime/ACTIVE_TASK.yaml"
    if active_path.exists():
        active=yaml.safe_load(active_path.read_text(encoding="utf-8")) or {}
        if active.get("task_id")==task and active.get("mode"):
            mode=active["mode"]
if not mode:
    upper=str(task).upper()
    if "ARCHITECTURE_PREFLIGHT" in upper or "PREFLIGHT" in upper:
        mode="ARCHITECTURE_PREFLIGHT"
    elif "ROUTE_ENGINE" in upper or "STORY_ENGINE" in upper:
        mode="ROUTE_ENGINE"
    else:
        mode="GENERAL"

reg=yaml.safe_load((root/"project/registry/ARTIFACT_REGISTRY.yaml").read_text(encoding="utf-8"))["entries"]
byid={e["id"]:e for e in reg}
if target not in byid:
    raise SystemExit(f"Unknown target id: {target}")

ordinary_target=target.startswith("ROUTE_") and target != "ROUTE_NULL"
rid=target.removeprefix("ROUTE_") if ordinary_target else None

if mode=="ARCHITECTURE_PREFLIGHT":
    selected=["HARNESS_CORE","PROJECT_BRIEF","AUTHOR_SHARED","AUTHOR_EXPERIENCE_MAP","AUTHOR_PREFLIGHT_PROTOCOL"]
    if ordinary_target:
        author_id=f"AUTHOR_{rid}"
        if author_id not in byid:
            raise SystemExit(f"Missing human author constraints for {target}: {author_id}")
        selected.extend([author_id,"CHAR_CHENG","CHAR_LIN","CHAR_ZHOU","CHAR_DAUGHTER"])
elif mode=="META_PLANNING":
    selected=["HARNESS_CORE","PROJECT_BRIEF","AUTHOR_SHARED","AUTHOR_EXPERIENCE_MAP","META_RESERVATIONS"]
    for route_id in ["FLESH","ECHO","ORIGIN","BLINDSPOT","NOBODY"]:
        aid=f"AUTHOR_{route_id}"
        if aid in byid:
            selected.append(aid)
        rid_state=f"ROUTE_{route_id}"
        if rid_state in byid:
            selected.append(rid_state)
else:
    selected=["HARNESS_CORE","PROJECT_BRIEF","HUMAN_DECISIONS",target]
    if ordinary_target:
        iid=f"IFACE_{rid}"
        if iid in byid:
            selected.append(iid)
        for aid in ["AUTHOR_SHARED","AUTHOR_EXPERIENCE_MAP",f"AUTHOR_{rid}"]:
            if aid in byid:
                selected.append(aid)

for e in reg:
    if mode in e.get("load_for_modes", []):
        selected.append(e["id"])

seen=set()
queue=list(selected)
selected=[]
while queue:
    sid=queue.pop(0)
    if sid in seen:
        continue
    if sid not in byid:
        raise SystemExit(f"Unknown dependency id: {sid}")
    seen.add(sid)
    selected.append(sid)
    queue.extend(byid[sid].get("depends_on", []))

files=[]; chars=0
for sid in selected:
    e=byid[sid]
    if e["status"]=="archived" or e["kind"] in {"sprint","calibration","legacy_baseline"}:
        raise SystemExit(f"Archive/provenance leak: {sid}")
    p=root/e["path"]
    text=p.read_text(encoding="utf-8")
    chars+=len(text)
    files.append({"id":sid,"path":e["path"],"status":e["status"],"chars":len(text)})

pack={
    "state":"GENERATED",
    "task_id":task,
    "mode":mode,
    "target":target,
    "files":files,
    "human_constraints":[f["id"] for f in files if f["id"].startswith("AUTHOR_")],
    "total_chars":chars,
    "budget_chars":14000,
    "within_budget":chars<=14000,
}
print(yaml.safe_dump(pack,allow_unicode=True,sort_keys=False))
if chars>14000:
    raise SystemExit("Context budget exceeded")
