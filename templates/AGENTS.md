# {{REPOSITORY_NAME}} — Agent Roster

Defines the agents available for work in this repository and how work routes between them.
Extends the organization standards; does not override owner approval gates.

## Canonical routing authority

All agent harnesses must connect to the `qic-control-plane` MCP server at
`https://mcp.quantinovaindustries.org/mcp` and synchronize the current directive before work.
The control plane is the only approved route for agent-originated GitLab API mutations against
`https://gitlab.quantinovaindustries.org`.

Agents and harnesses must never receive the GitLab PAT. The PAT is held server-side by the MCP
control plane and is never returned in tool output, logs, prompts, configuration, or repository files.

## Roster

| Agent | Role | Model | Tools |
|---|---|---|---|
| {{AGENT_NAME}} | {{ROLE}} | {{MODEL}} | `qic-control-plane`, {{TOOLS}} |

## Routing

- Directive / policy authority: `qic-control-plane` MCP.
- Planning: {{PLANNING_LANE}}
- Implementation: {{IMPLEMENTATION_LANE}}
- Review / verification: {{REVIEW_LANE}}
- GitLab read/write operations: `qic-control-plane` MCP only.

## Rules

- One orchestrator owns the task list and consolidates results.
- Workers stay within their assigned scope and file allowlist.
- Every harness obeys the latest control-plane directive before repository work.
- No direct writes to `main` or `master`.
- No agent pushes, merges, or submits anything externally without explicit owner approval.
- If MCP directive sync fails, GitLab mutation is blocked for that session.
- All agent output is DRAFT until the owner approves.
