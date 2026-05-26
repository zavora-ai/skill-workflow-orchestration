# Workflow Cross-MCP Workflows

## Workflow + Payments: Governed Payment Flow
```
WORKFLOW: start_workflow(name: "payment_approval", input: {amount: 50000, customer: "acme"})
WORKFLOW: get_instance(id) → step: "create_intent"
PAYMENTS: create_checkout_intent(amount: 50000)
WORKFLOW: advance_step(id, step: "request_approval")
WORKFLOW: list_approvals() → pending
→ Human approves
WORKFLOW: advance_step(id, step: "execute")
PAYMENTS: execute_approved_intent(payment_id)
```

## Workflow + HRIS: Onboarding Flow
```
WORKFLOW: start_workflow(name: "employee_onboarding", input: {employee: "Alex"})
HRIS: create_employee(name: "Alex", dept: "Engineering")
IDENTITY: lifecycle_task(type: "onboard", user_id: "emp_456")
CALENDAR: create_event(title: "Onboarding Kickoff")
WORKFLOW: advance_step(id, step: "complete")
```
