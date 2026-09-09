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
shared_delta: null
collision_surface: []
```

`shared_open_dimensions` stores unresolved dimension names, never candidate answers. Omitted Shared details are undefined. `shared_delta` is used only when a Route gains material value from a minimal change to the common observable scene; it does not modify Shared until cross-route review accepts it.

Integration compares Interfaces and any Shared Deltas, checks Route commitments, tickets collisions, and updates Shared only after the Gate passes. Interfaces store functions, dependencies, dimensions, and deltas—not solution catalogs.
