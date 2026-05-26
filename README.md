# Workflow Orchestration Skill

> Multi-step workflow engine — create processes with approval gates, advance steps, handle failures with retry/rollback, and track all state transitions.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

| Workflow | Calls | Achieves |
|----------|-------|----------|
| Create & Run | 3 | Define steps → start → monitor |
| Handle Approvals | 2 | List pending → approve/reject |
| Advance | 1 | Move to next step |
| Cancel | 1 | Abort with rollback |

### Without this skill:
- Approval gates skipped for convenience
- Workflows stuck without escalation
- No rollback on failure
- State transitions unlogged

### With this skill:
- Every gate enforced (no shortcuts)
- Stuck workflows escalated automatically
- Rollback steps for critical paths
- Full audit trail on every transition

## Installation

```bash
git clone https://github.com/zavora-ai/skill-workflow-orchestration.git \
  ~/.skills/skills/workflow-orchestration
```

## Requirements

**Required:** `mcp-workflow (10 tools)`

**Cross-MCP:** mcp-payments (governed payment flows), mcp-hris (onboarding workflows)

## Folder Structure

```
workflow-orchestration/
├── SKILL.md                       # Decision tree + workflows + MUST DO/MUST NOT DO
├── scripts/
│   └── check_gates.py
├── references/
│   ├── tool-sequences.md
│   ├── cross-mcp-workflows.md
│   └── examples.md
├── README.md
└── LICENSE
```

## Example

**User:** "What approvals are pending?"

**Result:**
```
2 pending approvals:
1. Payment ,000 → Acme Corp (waiting: @finance_mgr, 2h)
2. Deploy v2.3.1 → production (waiting: @eng_lead, 30m)
```

## Scripts

### `check_gates.py`
```bash
python scripts/check_gates.py '{"gates": [{"name": "finance", "status": "approved"}, {"name": "security", "status": "pending"}]}'
```

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;" alt=""/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0 — Part of [ADK-Rust Enterprise](https://enterprise.adk-rust.com). Built with ❤️ by [Zavora AI](https://zavora.ai)
