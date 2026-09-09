# Output Contracts

Every Task declares:
```yaml
task:
mode:
target:
decision_required:
context:
  must: []
  may: []
  late: []
output:
  required: []
  max_length:
terminal_state:
```

## Formal Sprint close
Every formal Sprint must leave exactly four human/machine-facing outputs in `runtime/CURRENT_SPRINT/`:

1. `SPRINT_REPORT.md` — compact human summary.
2. `PRIMARY_ARTIFACT` — the actual creative/analysis deliverable; may be one file or a `PRIMARY/` folder.
3. `AUDIT_REPORT.md` — review evidence and verdicts.
4. `STATE_DELTA.yaml` — machine-readable writeback summary.

`CONTEXT_PACK.yaml` remains separate runtime evidence and is not repeated in the report.

### SPRINT_REPORT.md
Keep it concise. Use these sections:
1. Task
2. Result — `PASS / RISK / FAIL / HUMAN_GATE / ROLLBACK_PARENT`
3. What Changed
4. What Did Not Change
5. Key Findings
6. Audit Summary
7. Files Changed
8. Remaining Debt
9. Next
10. Human Decision — only at Human Gate, one decision only

### AUDIT_REPORT.md
Record only audits actually run. For each:
- verdict
- decisive evidence
- unresolved risk

Also record compact execution provenance for cognition-sensitive roles:
```yaml
role:
agent:
model:
reasoning_effort:
context_mode: FRESH_ALLOWLIST | INHERITED | SELF_REVIEW
independent: true | false
```

`Cold Reader: PASS` is independence-qualified only when `context_mode: FRESH_ALLOWLIST` and `independent: true`.
End with one final Harness verdict.

### STATE_DELTA.yaml
Record only real state changes:
```yaml
created: []
updated: []
status_changes: []
interface_changes: []
open_questions:
  added: []
  closed: []
shared_state_changed: false
human_decisions_changed: false
archive: []
terminal_state:
```

## Writeback
A Sprint is incomplete until relevant Project State, Route Interface, Open Question / Closure Debt, Artifact Registry, and Archive changes described by `STATE_DELTA.yaml` are applied.

Process notes and superseded variants move to Archive after distillation.

## Human Review Pack
When `terminal_state: HUMAN_GATE`, the report shows only:
- current best 1–3 candidates
- one spine per candidate
- key difference
- largest risk
- strongest objection
- one Human decision
