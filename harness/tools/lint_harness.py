from pathlib import Path
import json, re, sys

root = Path(__file__).resolve().parents[1]
core = (root / "00_CORE.md").read_text(encoding="utf-8")

errors = []
rules = re.findall(r"(?m)^\d+\.\s+", core)
if len(rules) > 10:
    errors.append(f"Core has {len(rules)} rules; max is 10.")

if len(core) > 2200:
    errors.append(f"Core is {len(core)} chars; keep it compact.")

example_markers = ["例如", "比如", "举例", "example", "e.g."]
for marker in example_markers:
    if marker.lower() in core.lower():
        errors.append(f"Core contains example marker: {marker}")

negative_markers = ["禁止", "不得", "不要", "避免", "never ", "do not", "don't"]
for marker in negative_markers:
    if marker.lower() in core.lower():
        errors.append(f"Core contains negative-prior wording: {marker}")

for line in core.splitlines():
    if re.match(r"^\d+\.", line) and len(line) > 220:
        errors.append(f"Core rule too long: {line[:80]}...")

required = [
    "08_HARNESS_CHANGE_POLICY.md",
    "09_ROUTE_INTERFACE.md",
    "10_ARTIFACT_POLICY.md",
    "templates/route_interface.yaml",
    "templates/artifact_registry_entry.yaml",
    "adapters/codex/package.json",
    "adapters/codex/roles.json",
    "adapters/codex/runner.mjs",
]
for rel in required:
    if not (root / rel).exists():
        errors.append(f"Missing required file: {rel}")

roles_path = root / "adapters/codex/roles.json"
if roles_path.exists():
    roles = json.loads(roles_path.read_text(encoding="utf-8"))
    required_roles = {"forge", "cold_reader", "drama_reviewer", "mystery_reviewer", "logic_scout", "synthesizer"}
    missing = required_roles - set(roles)
    if missing:
        errors.append(f"Codex adapter missing roles: {sorted(missing)}")
    if roles.get("forge", {}).get("model") == roles.get("cold_reader", {}).get("model"):
        errors.append("Forge and Cold Reader must use different default model profiles.")
    if "ROUTE_*" in roles.get("cold_reader", {}).get("context_ids", []):
        errors.append("Cold Reader default context must not include Route design state.")

runner_path = root / "adapters/codex/runner.mjs"
if runner_path.exists():
    runner = runner_path.read_text(encoding="utf-8")
    for marker in ["startThread", 'sandboxMode: "read-only"', 'independence: "FRESH_SESSION"']:
        if marker not in runner:
            errors.append(f"Codex fresh-session runner missing invariant: {marker}")

if errors:
    print("HARNESS LINT: FAIL")
    for e in errors:
        print("-", e)
    sys.exit(1)

print("HARNESS LINT: PASS")
print(f"Core rules: {len(rules)}")
print(f"Core chars: {len(core)}")

active_policy_files = [
    "00_CORE.md", "01_ORCHESTRATOR.md", "02_CONTEXT_ROUTER.md",
    "03_PIPELINE.md", "04_GATES.md", "05_STATE.md",
    "06_OUTPUTS.md", "07_ROADMAP.md", "08_HARNESS_CHANGE_POLICY.md",
    "09_ROUTE_INTERFACE.md", "10_ARTIFACT_POLICY.md",
]
total_chars = 0
for rel in active_policy_files:
    p = root / rel
    if p.exists():
        total_chars += len(p.read_text(encoding="utf-8"))
print(f"Active policy chars: {total_chars}")
if total_chars > 18000:
    print("HARNESS LINT WARNING: active policy exceeds 18k chars; run HARNESS_SIMPLIFY.")
