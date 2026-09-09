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

## Integration procedure
1. compare current Interfaces, not full Route documents
2. derive common required observations
3. preserve facts any viable Route requires to remain open
4. create a collision ticket for incompatible needs
5. resolve a collision by changing shared story, changing a Route, merging Routes, or escalating to Human Gate
6. harden shared facts only after the Integration Gate passes

## Interface rule
The Interface states dependencies, freedoms, and Route-specific story obligations, not the full solution. `story_obligations` may tighten a Project Story Contract for one Route but may not replace or weaken it.
