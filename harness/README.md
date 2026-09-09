# Narrative Harness v0.6.3

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

Project facts, character facts, Route truths, Scene facts, Ideas, and Ledgers belong to Project Data.
Platform-specific agent/model mappings belong to execution adapters such as `.codex/`.

Primary flow:
`EXPLORE -> BUILD -> REVIEW -> SYNTHESIZE -> INTEGRATION_CHECK -> NEXT | HUMAN_GATE | ROLLBACK_PARENT`

Default working context is current state, not process history.
