# Output Contracts

Every Task declares target, context, required output, max length, and terminal state.

## Formal Sprint close
`runtime/CURRENT_SPRINT/` contains exactly four human/machine-facing outputs:
1. `SPRINT_REPORT.md` — compact human summary.
2. `PRIMARY_ARTIFACT` or `PRIMARY/` — actual deliverable.
3. `AUDIT_REPORT.md` — review evidence and verdicts.
4. `STATE_DELTA.yaml` — machine-readable writeback.

`CONTEXT_PACK.yaml` and fresh-session worker artifacts remain separate runtime evidence.

### SPRINT_REPORT.md
Use: Task; Result (`PASS / RISK / FAIL / HUMAN_GATE / ROLLBACK_PARENT`); What Changed; What Did Not Change; Key Findings; Audit Summary; Files Changed; Remaining Debt; Next; and one Human Decision only when gated.

### AUDIT_REPORT.md
For each audit record:
- role, verdict, decisive evidence, unresolved risk
- independence: `FRESH_SESSION / SUBAGENT_THREAD / SELF_REVIEW`
- thread/session id when available
- requested/used model + reasoning effort when available

Only `FRESH_SESSION` may claim full context independence. End with one Harness verdict.

### STATE_DELTA.yaml
Record only real changes:
```yaml
created: []
updated: []
status_changes: []
interface_changes: []
open_questions: {added: [], closed: []}
shared_state_changed: false
human_decisions_changed: false
archive: []
terminal_state:
```

## Writeback
A Sprint is incomplete until its State / Interface / Open Question or Closure Debt / Registry / Archive changes are applied.

At `HUMAN_GATE`, surface only the best 1–3 candidates, one spine each, key difference, largest risk, strongest objection, and one Human decision.
