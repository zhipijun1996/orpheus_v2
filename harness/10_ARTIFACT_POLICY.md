# Artifact Policy

## Principle
Process history is provenance.
Current state is context.

## Content lifecycle

### RAW_SEED
Uninterpreted idea fragment.
Default load: Forge only.

### CANDIDATE
Developed possibility without commitment.
Default load: only when a Task names it.

### PROVISIONAL
Current working direction approved for continued development.
Default load: by dependency.

### LOCKED
Human-committed constraint.
Default load: by dependency and protected from ordinary mutation.

### ARCHIVED
Superseded, rejected, parked, or process-only material.
Default load: provenance only.

## Sprint documents
Sprint reports are process artifacts.
At Sprint close:
- distill current decisions into Project State
- distill reusable possibilities into Candidate Cards
- update Route Interfaces
- register supersession
- archive the Sprint report

A file's existence never grants it active authority.

## Artifact Registry
Each artifact has:
```yaml
id:
path:
kind: state | candidate | seed | interface | sprint | review | ledger | other
status: raw_seed | candidate | provisional | locked | archived
default_load: true | false
scope:
supersedes: []
superseded_by: []
source: []
notes:
```

The Context Router trusts Registry status over file age or filename.
