# Harness Change Policy

Purpose: let the Harness learn without turning local failures into global creative bias or growing default context.

## A. Fixed self-modification protocol

Every Harness modification follows:

`OBSERVE -> LOCALIZE -> PATCH -> CALIBRATE -> REGRESS -> DISTILL -> STABLE | REVERT`

### 1. OBSERVE
Record the failure as evidence, not as a new rule.

### 2. LOCALIZE
Assign the narrowest responsible layer:
- `PROJECT_DATA` — story-specific state or preference
- `TEMPLATE` — schema or output contract
- `MODULE` — evaluator, Forge, Closure, Integration, Simplifier, etc.
- `ROUTER_ORCHESTRATOR` — context selection or task flow
- `CORE` — cross-module invariant

Default to the narrowest layer that can fully repair the failure.

### 3. PATCH
Prefer:
`REPLACE -> MERGE -> DELETE -> ADD`

A patch must:
- be general within its owning layer
- describe a quality test or process behavior rather than a preferred story solution
- avoid project-specific examples in active policy
- have one authoritative home

### 4. CALIBRATE
The motivating concrete failure becomes a Calibration Case.

Calibration Cases may contain full project examples, but:
- Creative agents do not read them
- Context Router never loads them for ordinary story generation
- they are used only to test Harness behavior

### 5. REGRESS
Before promotion, test:
- the motivating case
- at least 2 meaningfully different unrelated cases

Check:
- original failure is now detected or prevented
- unrelated strong candidates are not falsely rejected
- the patch does not force a recurring dramatic shape
- default context does not grow

### 6. DISTILL
After a successful patch:
- replace superseded rules rather than stacking them
- merge overlapping audit dimensions
- remove explanatory residue
- archive old wording and Calibration evidence
- keep active module policy compact

### 7. PROMOTE
Change lifecycle:
`CHANGE_CANDIDATE -> EXPERIMENTAL -> STABLE | REVERTED`

Core changes additionally require Human approval.

---

## B. Module evolution rules

Most quality-learning belongs to the responsible Module, not Core.

A Module may change:
- audit dimensions
- Gate criteria
- required inputs
- output schema
- failure classification

### Dimension mutation decision

Audit dimensions are working hypotheses, not fixed slots.

When a new failure appears, decide in this order:

1. `REFINE`
   - the failure belongs to an existing quality concept
   - add or rewrite a diagnostic question inside that dimension
   - no new dimension

2. `SPLIT`
   - one dimension currently bundles two genuinely independent judgments
   - the bundling causes misses or contradictory verdicts
   - split only if regression shows better discrimination

3. `ADD`
   - the failure is orthogonal to all current dimensions
   - it recurs across at least 2 meaningfully different cases
   - the new dimension changes a Gate, verdict, or candidate ranking
   - otherwise keep it as a diagnostic note or Calibration tag

4. `MERGE / DELETE`
   - dimensions overlap heavily
   - one dimension rarely changes decisions
   - one exists mainly because of historical wording rather than current need

### Module complexity budget
- 3–6 primary dimensions is a normal operating range, not a hard limit
- exceeding 6 triggers a consolidation review, not automatic rejection
- any net increase must show measurable regression benefit
- repeated exceptions trigger redesign rather than more dimensions

### Example-free active policy
Active Module policy states the general test only.
Specific successes and failures live in Calibration / provenance.

---

## C. Core discipline

Core is the last promotion layer.

A Core rule is eligible only when:
- the same principle repeatedly appears across distinct Modules
- it remains solution-neutral
- it can be stated in one sentence
- no narrower layer can own it cleanly

Core limits:
- maximum 10 rules
- no examples
- no rejected story ideas
- no project nouns
- no calibration anecdotes
- no solution catalogs

---

## D. Negative-prior hygiene

Failed ideas remain evidence, not active prohibitions.

Prefer:
> evaluate whether a motive is causally earned

over:
> never use anonymous future messages

Negative constraints enter active policy only when they protect a genuine hard boundary, safety rule, or architectural contract.

---

## E. Context conservation

Self-learning must not automatically increase ordinary creative context.

Rules:
- stable patches replace old active wording
- Calibration Cases are non-default context
- superseded Module versions are archived
- one concept has one authoritative active file
- Context Router loads only the current owning Module plus task dependencies

A change that permanently increases default context requires an explicit benefit justification and Human approval.

---

## F. Harness health check

After every stable Harness change, check:
1. Core rule count
2. active policy size
3. duplicate concepts
4. default task context size
5. number of audit dimensions per Module
6. archived-vs-active artifact ratio
7. regression status

If active policy grows for 2 consecutive versions without a demonstrated capability gain:
> run `HARNESS_SIMPLIFY` before further feature additions.
