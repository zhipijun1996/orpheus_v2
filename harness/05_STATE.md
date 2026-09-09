# State

## Workflow state
`EXPLORE / BUILD / REVIEW / SYNTHESIZE / INTEGRATION_CHECK / READY_FOR_HUMAN / ROLLBACK_PARENT`

## Content lifecycle
`RAW_SEED -> CANDIDATE -> PROVISIONAL -> LOCKED`

Any content may move to:
`ARCHIVED`

`READY_FOR_HUMAN` is workflow state, not content truth.

## Default-loading rule
- `PROVISIONAL` and `LOCKED`: dependency-loadable
- `CANDIDATE`: explicit task reference only
- `RAW_SEED`: Forge only
- `ARCHIVED`: provenance only

## Truth record
```yaml
id:
scope: shared | route | meta
routes: []
statement:
closure: plausible | solvable | proven
status: candidate | provisional | locked | archived
exposure: {}
depends_on: []
```

## Idea seed
```yaml
id:
raw:
scale: spark | mechanism | route_engine | architecture | meta
status: raw_seed | candidate | provisional | archived
source:
```

## Route Interface status
`DRAFT / CURRENT / STALE`

## Active budgets
- Core <= 10 rules
- default must-read artifacts <= 5
- active raw seeds <= 20
- Human Pack candidates <= 3
- one main active Story Artifact per Route
