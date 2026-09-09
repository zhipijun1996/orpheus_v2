# Route Interface

Purpose: independent Routes remain composable.

```yaml
route_id:
status:
promise:
shared_inputs: {required: []}
shared_open_dimensions: []
route_dimensions:
  <id>:
    engagement: REQUIRED | OPTIONAL
    resolution: LOCAL_COMMITMENT_REQUIRED | FUNCTION_REQUIRED | PARTIAL_ALLOWED | MAY_REMAIN_OPEN
story_obligations: {}
route_outputs: {}
collision_surface: []
```

`shared_open_dimensions` stores unresolved dimension names, never candidate answers. Shared openness controls Integration only; it does not imply Route omission. Project contracts and `route_dimensions` determine Route engagement/closure.

Integration compares Interfaces, preserves Shared-open dimensions, checks Route commitments, tickets collisions, and hardens Shared only after the Gate passes. Interfaces store functions/dependencies/open dimensions, not solution catalogs.
