from pathlib import Path
import yaml, sys
root=Path(__file__).resolve().parents[1]
reg=yaml.safe_load((root/"project/registry/ARTIFACT_REGISTRY.yaml").read_text(encoding="utf-8")); errors=[]; ids=set()
for e in reg["entries"]:
    if e["id"] in ids: errors.append(f"Duplicate registry id: {e['id']}")
    ids.add(e["id"]); p=root/e["path"]
    if not p.exists(): errors.append(f"Missing registry path: {e['path']}")
    if e["status"]=="archived" and e["default_load"]: errors.append(f"Archived artifact default_load=true: {e['id']}")
    if e["kind"] in {"sprint","calibration","legacy_baseline"} and e["default_load"]: errors.append(f"Provenance artifact default_load=true: {e['id']}")
for e in reg["entries"]:
    for d in e.get("depends_on",[]):
        if d not in ids: errors.append(f"Unknown dependency {d} from {e['id']}")
print("REGISTRY:", "PASS" if not errors else "FAIL")
for e in errors: print("ERROR:",e)
sys.exit(1 if errors else 0)
