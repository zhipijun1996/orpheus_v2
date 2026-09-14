# Narrative Harness v0.7.0

Purpose: a compact, project-agnostic process OS for generating, testing, integrating, and distilling narrative candidates.

The Harness owns context routing, task state, review gates, cross-route integration, artifact lifecycle, distillation, self-change policy, and role independence. Project facts, Human Constraints, Route truths, Story Contracts, Ideas, Human Baselines, and Ledgers belong to Project Data; platform-specific model mappings belong to adapters.

Primary flow:
`ARCHITECTURE_PREFLIGHT -> EXPLORE -> BUILD -> REVIEW -> SYNTHESIZE -> INTEGRATION_CHECK -> NEXT | HUMAN_GATE | ROLLBACK_PARENT`

`ARCHITECTURE_PREFLIGHT` is the story-worth gate. It uses concise human-authored common constraints, the current Route constraints, a short cross-route experience map, and core character state. It judges readable story, character causality, emotional movement, Shared-scene reread value, Route identity, and foreshadow potential before demanding a finished technical closure or evidence ledger.

Single-Route authors do not receive sibling Routes' detailed answers during first-pass creation. Cross-route synthesis reads the frozen Route outputs together and checks repetition, truth differentiation, Shared compatibility, and proposed Shared Deltas.

Full Route Engine work still begins from the current Shared Scene, separates Story Engine / Route Truth / Evidence, closes required mysteries, and audits mechanism dependencies after story eligibility is established.

The Codex adapter now defaults its formal fresh-session roles to GPT-6 Astra with role-specific reasoning depth: medium for cold reading, high for generation/drama/mystery, and xhigh for logic/convergence. Native subagents use the same model family. The project SDK dependency is updated for current Astra-capable Codex clients.

Default working context is current state, not process history. Calibration and rejected ideas remain outside ordinary creative context.
