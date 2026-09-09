# Route Interface

Purpose: let Routes develop independently while remaining composable.

Each active Route maintains one compact Interface.

```yaml
route_id:
status: draft | current | stale
promise:
shared_inputs:
  required: []
  must_remain_open: []
story_obligations:
  shared_anchor:
  must_reinterpret: []
shared_observations:
  accepts: []
route_outputs:
  can_explain: []
  leaves_unexplained: []
route_local_truth:
  owns: []
exposure:
  required: []
collision_surface:
  sensitive_facts: []
depends_on: []
```

## Integration
Compare Interfaces; derive common observations; preserve required-open facts; ticket incompatible needs; resolve by changing Shared/Route or escalating; harden Shared only after the Gate passes.

## Rule
The Interface states dependencies, freedoms, and Route-specific story obligations, not the full solution. Story obligations may tighten, never weaken, a Project Story Contract.
