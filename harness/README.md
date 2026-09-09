# Narrative Harness v0.6.2

Purpose: a compact, project-agnostic process OS for generating, testing, integrating, and distilling narrative candidates.

The Harness owns:
- context routing
- task state
- review gates
- cross-route integration
- artifact lifecycle
- distillation
- self-change policy

Project facts, character facts, Route truths, Scene facts, Ideas, and Ledgers belong to Project Data.

Primary flow:
`EXPLORE -> BUILD -> REVIEW -> SYNTHESIZE -> INTEGRATION_CHECK -> NEXT | HUMAN_GATE | ROLLBACK_PARENT`

Default working context is current state, not process history.

v0.6.0 adds:
1. self-change rules that keep Core generic and compact
2. Route Interfaces and recurrent cross-route synthesis
3. strict artifact lifecycle and registry
4. separation of workflow state from content status
5. automated Harness lint
