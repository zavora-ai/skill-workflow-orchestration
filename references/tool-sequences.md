# Workflow Orchestration Tool Sequences (10 tools)

## Definition (2)
| Tool | Purpose | Risk |
|------|---------|------|
| `list_workflows` | List defined workflow templates | read |
| `get_workflow` | Get workflow definition (steps, gates) | read |

## Lifecycle (3)
| Tool | Purpose | Risk |
|------|---------|------|
| `create_workflow` | Define new workflow with steps/gates | write |
| `start_workflow` | Start workflow instance with input | write |
| `cancel_instance` | Cancel running workflow instance | write |

## Execution (2)
| Tool | Purpose | Risk |
|------|---------|------|
| `list_instances` | List running/completed instances | read |
| `get_instance` | Get instance status, current step | read |

## Progression (1)
| Tool | Purpose | Risk |
|------|---------|------|
| `advance_step` | Advance to next step (after gate clears) | **production** |

## Approvals (2)
| Tool | Purpose | Risk |
|------|---------|------|
| `list_approvals` | List pending approval gates | read |
| `resolve_approval` | Approve/reject at gate | **production** |

## Sequence: Create and Run Workflow (4 calls)
```
1. create_workflow(name: "release-pipeline", steps: [{name: "build", type: "auto"}, {name: "test", type: "auto"}, {name: "approve-deploy", type: "gate", approvers: ["platform-team"]}, {name: "deploy", type: "auto"}]) → {workflow_id: "wf-rel01"}
2. start_workflow(workflow_id: "wf-rel01", input: {version: "v2.5.0", repo: "api-server"}) → {instance_id: "inst-001", status: "running", current_step: "build"}
3. get_instance(instance_id: "inst-001") → {status: "waiting", current_step: "approve-deploy", completed: ["build", "test"]}
4. list_approvals(instance_id: "inst-001") → [{id: "apr-wf01", step: "approve-deploy", status: "pending", approvers: ["platform-team"]}]
```

## Sequence: Approve and Advance (3 calls)
```
1. list_approvals(status: "pending") → [{id: "apr-wf01", workflow: "release-pipeline", step: "approve-deploy", waiting_since: "10min"}]
2. resolve_approval(approval_id: "apr-wf01", decision: "approved", actor: "alice@company.com", reason: "Tests pass, staging verified") → {resolved: true}
3. get_instance(instance_id: "inst-001") → {status: "running", current_step: "deploy", completed: ["build", "test", "approve-deploy"]}
```

## Sequence: Cancel Stuck Workflow (3 calls)
```
1. list_instances(status: "running") → [{id: "inst-003", workflow: "data-migration", current_step: "transform", elapsed: "4h", timeout: "2h"}]
2. get_instance(instance_id: "inst-003") → {status: "running", current_step: "transform", error: "timeout exceeded", started: "4h ago"}
3. cancel_instance(instance_id: "inst-003", reason: "exceeded 2h timeout on transform step") → {cancelled: true, final_status: "cancelled", completed_steps: ["extract"]}
```
