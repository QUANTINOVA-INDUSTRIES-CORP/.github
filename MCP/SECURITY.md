# QIC MCP Control Plane — Security Model

## Threat model summary

The MCP server is the only component that holds the GitLab credential. Every agent harness
(local or cloud-hosted, including a third-party product like ChatGPT) is treated as a
potentially-compromised or careless client: it can be tricked by prompt injection, it can have
bugs, and its tool-call arguments are entirely client-controlled. The security design assumes the
client cannot be trusted to self-report authorization truthfully, and puts every real control on
the server side instead.

## Credential boundary

- `QIC_GITLAB_PAT` exists only in the MCP server process environment on the homelab host, loaded
  from `/etc/qic-mcp/qic-mcp.env` (root-owned, mode `0600`).
- It is sent upstream only as the `PRIVATE-TOKEN` header on server-originated HTTPS requests to
  `QIC_GITLAB_BASE_URL`.
- No tool returns it, no log line contains it, no error message includes it (`_gitlab_request`
  truncates and returns only response bodies from GitLab, never request headers).
- There is no `get_token`, `show_pat`, `get_credentials`, `debug_env`, or `dump_env` tool, and none
  may be added.
- The `/health` endpoint returns only: status, directive version, build version, GitLab hostname,
  and whether mutation mode is enabled. It never enumerates environment variables or headers.

## Mutation authorization — three independent factors

A mutation tool call (`gitlab_branch_create`, `gitlab_file_write`, `gitlab_merge_request_create`)
only proceeds if **all three** are true:

1. `QIC_ENABLE_MUTATIONS=true` is set in the server's environment (operator-controlled, requires a
   service restart to change — not reachable from any tool call).
2. The tool call itself carries `owner_approved=true`.
3. A fresh, single-use approval file exists on the MCP host at `/run/qic-mcp/approve` (path
   configurable via `QIC_MCP_APPROVAL_FILE`), created within the last `QIC_MCP_APPROVAL_TTL_SECONDS`
   (default 300s). The server deletes this file the instant it checks it, whether the check passes
   or fails, so it cannot be reused for a second call.

(2) alone is explicitly insufficient: it is a plain boolean argument, and the client fully controls
tool-call arguments (including under prompt injection). (1) is a coarse, restart-gated global
switch. (3) is the real per-action authorization: only someone who already has a shell (or `sudo`)
on the MCP host — i.e. the CEO/operator, not any agent or remote client — can create that file.
This is Option C from the task brief ("operator-controlled approval file"), chosen because the
operator is a single person who already has passwordless SSH/sudo access to the homelab host, so it
adds real per-action authorization with no new network-facing listener, no nonce-distribution
channel, and no extra service to maintain.

Even with all three factors satisfied, direct file mutation on `main` or `master` is still blocked
unconditionally (`_assert_mutable_branch`), and no merge tool exists at all — opening a merge
request is as far as the control plane goes; merging is always a manual, human action in the
GitLab or GitHub UI.

## What is never exposed

- No merge tool.
- No repository or project deletion.
- No GitLab instance-administration or `sudo` functionality.
- No broadening of PAT scope from a tool call.

## Client authentication (edge)

The MCP endpoint itself is protected by CLOUDFLARE ACCESS, independent of the GitLab credential.
Claude Code (and other first-party harnesses) authenticate with a CLOUDFLARE ACCESS service token
(`CF-Access-Client-Id` / `CF-Access-Client-Secret`), which is revocable independently of the GitLab
PAT and never touches GitLab at all — see `MCP/DEPLOYMENT.md` and `CHATGPT/AUTH.md` for the
per-harness specifics.

## Audit logging

Every tool call emits one structured JSON line to stdout (captured by `journald` under the
`qic-mcp` systemd unit): timestamp, tool name, operation class (`read`/`mutation`), success/failure,
project, branch, and the directive version in effect. GitLab PAT, request headers, and file content
are never logged. See `MCP/OPERATIONS.md` for how to query these.

## Fail-closed behavior

If a client cannot reach the MCP control plane (network failure, Access denial, service down), the
directive (`templates/CLAUDE.md`, `templates/AGENTS.md`) instructs every harness to fall back to
read-only, local-only analysis: no GitLab mutation, no external submission, no merge. There is no
"assume the directive and proceed" path.
