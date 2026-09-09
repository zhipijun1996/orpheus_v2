# Route Interface

Purpose: let Routes develop independently while remaining composable.

```yaml
route_id:
status:
promise:
shared_inputs:
  required: []
shared_open_dimensions: []
route_dimensions:
  <dimension_id>:
    engagement: REQUIRED | OPTIONAL
    resolution: LOCAL_COMMITMENT_REQUIRED | FUNCTION_REQUIRED | PARTIAL_ALLOWED | MAY_REMAIN_OPEN
story_obligations:
  shared_anchor:
  must_reinterpret: []
route_outputs:
  can_explain: []
  leaves_unexplained: []
collision_surface: []
```

`shared_open_dimensions` names unresolved dimensions only; never enumerate candidate answers. Shared openness is an integration policy, not permission to skip a Route question. Project Story Contracts and `route_dimensions` independently decide Route engagement and closure.

Integration compares Interfaces, preserves Shared-open dimensions, checks required Route commitments, tickets collisions, and hardens Shared only after the Gate passes.

The Interface records functions, dependencies, and open dimensions—not solution catalogs. Route obligations may tighten, never weaken, a Project Story Contract.
