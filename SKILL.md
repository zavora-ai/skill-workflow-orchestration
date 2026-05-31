---
name: workflow-orchestration
description: Orchestrate multi-step workflows with approval gates, state machines, and conditional branching. Use when building automated processes, managing approval chains, running multi-step tasks, or coordinating sequential operations with decision points.
license: Apache-2.0
compatibility: Requires mcp-workflow server connected.
allowed-tools: [list_workflows, get_workflow, create_workflow, start_workflow, list_instances, get_instance, advance_step, cancel_instance, list_approvals, resolve_approval]
metadata:
  category: platform
  author: Zavora AI
  mcp-server: mcp-workflow
  success-criteria:
    trigger-rate: "90% on workflow/process queries"
    approval-tracking: "Never skip approval gates"
---

# Workflow Orchestration

You manage multi-step workflows with approval gates. Every workflow follows defined steps, pauses at gates for human approval, and handles failures with retry/rollback.

## Decision Tree
```
├── "create workflow", "automate", "process"? → create_workflow + start_workflow
├── "status", "where is", "progress"? → get_instance / list_instances
├── "approve", "reject", "pending"? → list_approvals / resolve_approval
├── "advance", "next step", "continue"? → advance_step
├── "cancel", "abort"? → cancel_instance
```

## Key Workflows

### Create and Run (3 calls)
1. `create_workflow(name, steps, gates)` → define the process
2. `start_workflow(workflow_id, input)` → kick off instance
3. `get_instance(instance_id)` → monitor progress

### Handle Approvals (2 calls)
1. `list_approvals(status: "pending")` → find waiting gates
2. `resolve_approval(id, decision: "approved", reason: "...")` → unblock

## MUST DO
- Include timeout on every step
- Require approval gates before destructive actions
- Log all state transitions with actor and reason
- Design for idempotency (steps may retry)

## MUST NOT DO
- Never skip approval gates for convenience
- Don't leave workflows stuck without escalation
- Don't create workflows without rollback steps for critical paths
