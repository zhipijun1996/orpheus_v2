# Narrative Harness v0.6.6

Purpose: a compact, project-agnostic process OS for generating, testing, integrating, and distilling narrative candidates.

The Harness owns:
- context routing
- task state
- review gates
- cross-route integration
- artifact lifecycle
- distillation
- self-change policy
- role independence and execution semantics

Project facts, character facts, Route truths, Scene facts, Story Contracts, Ideas, and Ledgers belong to Project Data.
Platform-specific agent/model mappings belong to execution adapters.

Primary flow:
`EXPLORE -> BUILD -> REVIEW -> SYNTHESIZE -> INTEGRATION_CHECK -> NEXT | HUMAN_GATE | ROLLBACK_PARENT`

Context routing uses target dependencies plus task-semantic dependencies, so required story/chapter anchors load without expanding unrelated context.
Mechanism review protects generative novelty during Explore, then distinguishes high-leverage `ENGINE` ideas from necessary `SUPPORT` and explanatory `PATCH` debt during convergence.

For local/Remote Codex, `adapters/codex/` can run independence-sensitive roles as fresh SDK sessions rather than relying on native subagent history isolation.

Default working context is current state, not process history.
