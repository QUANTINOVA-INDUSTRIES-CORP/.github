# {{REPOSITORY_NAME}} — Agent Roster

Defines the agents available for work in this repository and how work routes between them.
Extends the organization standards; does not override owner approval gates.

## Roster

| Agent | Role | Model | Tools |
|---|---|---|---|
| {{AGENT_NAME}} | {{ROLE}} | {{MODEL}} | {{TOOLS}} |

## Routing

- Planning: {{PLANNING_LANE}}
- Implementation: {{IMPLEMENTATION_LANE}}
- Review / verification: {{REVIEW_LANE}}

## Rules

- One orchestrator owns the task list and merges results.
- Workers stay within their assigned scope and file allowlist.
- No agent pushes, merges, or submits anything externally without explicit owner approval.
- All agent output is DRAFT until the owner approves.
