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

## Sprint close
A Sprint must produce:
1. primary readable artifact
2. state delta
3. candidate / provisional delta
4. Route Interface delta when Route assumptions changed
5. Closure Debt delta when relevant
6. provenance links

Process notes and superseded variants move to Archive at Sprint close.

## Human Review Pack
Contains only:
- current best 1–3 candidates
- one spine per candidate
- key difference
- largest risk
- strongest objection
- one Human decision
