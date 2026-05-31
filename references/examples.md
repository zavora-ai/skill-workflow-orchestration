# Workflow Orchestration Examples

## Example 1: "Create a release workflow with an approval gate before production"
```
create_workflow(name: "release-pipeline", steps: [{name: "build", type: "auto", timeout: 600}, {name: "test", type: "auto", timeout: 900}, {name: "deploy-staging", type: "auto", timeout: 300}, {name: "approve-prod", type: "gate", approvers: ["platform-team", "eng-lead"]}, {name: "deploy-prod", type: "auto", timeout: 300}]) → {workflow_id: "wf-rel01", steps: 5, gates: 1}
start_workflow(workflow_id: "wf-rel01", input: {version: "v4.0.0", repo: "web-app", triggered_by: "ci-bot"}) → {instance_id: "inst-r40", status: "running", current_step: "build"}
```
Response: "🚀 Created and started release-pipeline for web-app v4.0.0:\n• build (10min timeout) → test (15min) → deploy-staging (5min) → **approval gate** → deploy-prod (5min)\n\nCurrently running: build step. Will pause at approve-prod for platform-team/eng-lead sign-off."

## Example 2: "What workflows are waiting for my approval?"
```
list_approvals(status: "pending") → [{id: "apr-101", workflow: "release-pipeline", instance: "inst-r40", step: "approve-prod", waiting_since: "25min", context: {version: "v4.0.0", tests_passed: true}}, {id: "apr-102", workflow: "data-migration", instance: "inst-dm5", step: "approve-execute", waiting_since: "2hr", context: {tables: 3, rows_affected: 50000}}]
resolve_approval(approval_id: "apr-101", decision: "approved", actor: "james@company.com", reason: "All tests pass, staging verified") → {resolved: true, workflow_advancing: true}
```
Response: "📋 2 pending approvals:\n1. **release-pipeline** v4.0.0 — approve-prod (waiting 25min, tests pass) → ✅ Approved\n2. **data-migration** — approve-execute (waiting 2hr, 50K rows affected) → Still pending\n\nRelease pipeline advancing to deploy-prod."

## Example 3: "The data migration workflow is stuck — cancel it"
```
get_instance(instance_id: "inst-dm5") → {status: "waiting", current_step: "approve-execute", elapsed: "3h", completed: ["validate-schema", "dry-run"], timeout: "4h"}
cancel_instance(instance_id: "inst-dm5", reason: "Migration plan needs revision — schema conflicts found in dry-run") → {cancelled: true, final_status: "cancelled", completed_steps: ["validate-schema", "dry-run"], resources_released: true}
list_instances(status: "running") → [{id: "inst-r40", workflow: "release-pipeline", current_step: "deploy-prod"}]
```
Response: "⛔ Cancelled data-migration workflow (inst-dm5). Completed steps: validate-schema, dry-run. Reason: schema conflicts need revision. Resources released.\n\n1 workflow still active: release-pipeline (deploying to prod)."
