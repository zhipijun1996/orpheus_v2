# Changelog

## v0.6.8
Seed-aware divergence:
- adds a curated `project/ideas/creative_seeds.yaml` pool that remains `default_load: false` and never enters ordinary Context Packs
- keeps one permanent BLIND Forge control while Route Engine fanout can expose other fresh workers to optional single or cross-kind Seeds
- Seeds are non-authoritative provocations: workers may use, mutate, fuse, invert, or reject them; explicit Seed IDs can pin a test without changing Project State
- default ROUTE_ENGINE fanout becomes 4 Forge sessions × 2 candidates, normally yielding 8 raw candidates before Review
- Seed provenance is stripped from frozen candidate/reviewer/synthesis inputs and restored only for the primary Orchestrator after convergence
- Meta Seeds stay out of ordinary Routes by default; adversarial probes are addressable explicitly rather than randomly injected
- CI/lint verifies the Seed pool is isolated, diverse, non-default, and paired with a blind control

## v0.6.7
Route fusion and mystery closure:
- separates `Story Engine / Route Truth / Evidence`; evidence recovery cannot substitute for causal Deep Truth
- requires ordinary Routes to close designated core mysteries locally while Shared answers remain open across Routes
- gives NULL a full answer contract covering ontology, agency, actions, motive, objective, causal impact, and apparent contradiction; identity-only reveals are insufficient
- adds `STRONG / PARTIAL / DETACHED` Route Engine fusion diagnostics across character causality, Route-defining speculative premise, and Shared core mystery; only DETACHED is a hard failure
- replaces option-like `must_remain_open` lists with dimension-only `shared_open_dimensions` plus explicit `route_dimensions`, separating Shared openness from Route engagement
- removes a fixed adult-at-2054 daughter prior from active Project State without promoting the human seed into Forge context
- adds core-cast causal-function checks and motive-continuity review without requiring every Route to close every distant outcome
- adds quarantined calibration for evidence-heavy but detached Route Engines and anti-overfit controls

## v0.6.6
Mechanism leverage discipline:
- protects generative mechanism novelty during EXPLORE instead of treating mechanism count as a quality penalty
- classifies mechanism-heavy work as `ENGINE / SUPPORT / PATCH`; strong ENGINE ideas are encouraged, while PATCH chains are complexity debt
- adds plain-language legibility and observable-setup checks without requiring terminology to appear before the reveal
- Synthesis prefers higher narrative leverage and shallower PATCH dependency at comparable story quality, not mechanically fewer mechanisms
- fresh-session and native reviewer roles now distinguish useful mechanism invention from jargon/scaffolding overload
- adds calibration coverage proving a high-leverage new mechanism must survive the new discipline

## v0.6.5
Story-spine retention:
- adds task-semantic context routing through Registry `load_for_modes` instead of relying only on target dependencies
- adds a Project Story Contract so ordinary Route Engines must remain attached to the shared story anchor without forcing one Route mechanism
- defines the current chapter function contract: Ch2 shared mystery experience, Ch4 2054 Working Truth, Ch5 entry into the 2036 causal layer; physical future return remains Route-local
- Route Interfaces can add Route-specific `story_obligations`
- Story Gate now rejects internally coherent but detached Route Engines whose main causal story survives removal of the required shared anchor
- Forge/Review/Synthesis role adapters explicitly enforce Story Contract obligations
- adds regression coverage for detached Route Engines and CI coverage for semantic Context Packs

## v0.6.4
Fresh-session execution:
- distinguishes `FRESH_SESSION`, `SUBAGENT_THREAD`, and `SELF_REVIEW` instead of treating native subagents as guaranteed context-isolated reviewers
- Cold Reader full-independence claims now require a new external Codex thread
- adds a compact Codex SDK adapter that automatically runs fresh Forge, parallel Review, and fresh Synthesis sessions
- model/reasoning profiles are role-routed and overridable without changing Harness policy
- fresh workers are read-only, network-disabled, and receive embedded allowlisted context; active State remains single-writer
- worker artifacts stay outside the four Formal Sprint outputs and are consumed by the primary Orchestrator

## v0.6.3
Execution independence:
- formal creative Sprints delegate cognition-sensitive roles to fresh subagent threads when the runtime supports them
- independent reviewers run from frozen artifacts and do not inherit author rationale or other review conclusions
- model diversity is preferred for at least one independent reviewer
- parallelism is concentrated in divergent generation and read-heavy review; active State writes remain single-writer
- audit outputs record agent/model/effort/context provenance
- platform-specific model routing lives outside generic Harness policy

## v0.6.2
Dimension evolution:
- replaced the soft 3–5 target with an explicit `REFINE / SPLIT / ADD / MERGE / DELETE` decision protocol
- made 3–6 a normal range rather than a fixed cap
- new dimensions require cross-case recurrence and measurable decision value
- exceeding 6 triggers consolidation review rather than automatic rejection

## v0.6.1
Self-learning hardening:
- fixed one self-modification protocol for Core, Modules, Router, Gates, and Templates
- added narrowest-layer Failure Localization
- made Module evolution the default learning channel
- isolated concrete Calibration Cases from creative context
- added regression requirements before stable promotion
- enforced replace/merge/delete before add
- added context-conservation and Harness simplify triggers

## v0.6.0
Architecture hardening:
- separated workflow state from content lifecycle
- added Harness self-change policy
- made Core example-free and positive-principle oriented
- added Route Interfaces and recurrent Cross-route Synthesis
- added Artifact Policy and Registry semantics
- made Sprint reports provenance by default
- added motive-continuity and earned-reversal checks as evaluation criteria
- added Harness lint
