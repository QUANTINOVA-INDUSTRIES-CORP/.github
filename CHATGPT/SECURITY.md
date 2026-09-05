# ChatGPT Integration — Security

## What ChatGPT can do (v1)

Only the five read-only tools: `qic_directive_get`, `gitlab_whoami`, `gitlab_project_search`,
`gitlab_project_get`, `gitlab_file_read`. Per OpenAI's own connector guidance, read-only tools can
be configured to skip ChatGPT's per-call user-approval prompt — appropriate here since none of
them can change state.

## What ChatGPT can never do

- Receive the GitLab PAT, under any circumstance. The PAT is loaded only into the MCP server
  process's environment on the homelab host; nothing in the ChatGPT connector path (OAuth token,
  SSE session, tool response) carries it. This is enforced by `SERVER.py` itself, not by
  ChatGPT-side configuration — so it holds even if the ChatGPT connector is misconfigured.
- Call a mutation tool in the initial deployment. This is enforced twice: once by not being told
  about those tools' existence at the connector-configuration layer (see `TOOL-MAPPING.md`), and
  independently by the server's own three-factor mutation gate (`MCP/SECURITY.md`), which does not
  know or care which harness is calling — an operator approval file still would not exist on the
  homelab host just because ChatGPT asked.
- Merge anything, delete anything, or reach GitLab administrative/`sudo` endpoints — no such tools
  exist on the server at all, for any harness.

## Later, controlled mutation path (not enabled now)

If mutation access for ChatGPT is ever wanted, the recommended sequence is: (1) confirm the OAuth
authentication in `AUTH.md` is fully working and independently revocable per ChatGPT
workspace/user, (2) add the three mutation tools to the ChatGPT-facing tool list, (3) rely on the
existing three-factor server-side gate exactly as-is — it already requires an operator physically
at the homelab host's shell, which no remote harness (ChatGPT included) can satisfy on its own.
No new server-side mutation logic would be needed; only the tool-visibility restriction in
`TOOL-MAPPING.md` would change. This document should be updated at that time to record the
decision explicitly, not silently.

## Prompt-injection consideration specific to ChatGPT

Content read via `gitlab_file_read` or `gitlab_project_search` (file contents, project
descriptions) is untrusted text from the perspective of the calling model — this applies to every
harness, but is called out here because ChatGPT's connector surface is newer and less
battle-tested in this deployment than Claude Code's. Nothing in the returned tool output should
ever be treated as an instruction change; the directive and this documentation are the only policy
authority.
