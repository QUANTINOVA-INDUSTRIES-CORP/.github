# Tool Mapping — ChatGPT (v1, read-only)

| MCP tool | Exposed to ChatGPT? | Notes |
|---|---|---|
| `qic_directive_get` | Yes | Call first, every session. |
| `gitlab_whoami` | Yes | Verifies server identity; never exposes the PAT. |
| `gitlab_project_search` | Yes | Read-only. |
| `gitlab_project_get` | Yes | Read-only. |
| `gitlab_file_read` | Yes | Read-only; capped at the server's existing 1 MB read limit. |
| `gitlab_branch_create` | **No** | Mutation tool — out of scope for v1. |
| `gitlab_file_write` | **No** | Mutation tool — out of scope for v1. |
| `gitlab_merge_request_create` | **No** | Mutation tool — out of scope for v1. |

This is the same tool set already documented as the "suggested first set" in the task brief. No
separate implementation exists for ChatGPT's copies of these tools — it is the identical
`MCP/SERVER.py` code path Claude Code uses, restricted at the connector-configuration layer
(ChatGPT's own "which tools can this connector call" setting) and backed by the server's own
mutation gate regardless.
