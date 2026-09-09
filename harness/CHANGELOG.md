# Changelog

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
