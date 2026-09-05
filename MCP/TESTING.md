# QIC MCP — Test Matrix

Results are filled in as each is actually run against the deployed service; see the final report
in this work session for the live run's outcomes. This file is the checklist template kept in the
repo for future re-validation (after any deploy, credential rotation, or dependency bump).

## MCP transport

- [ ] `GET /health` returns 200 with status/version fields, no secrets.
- [ ] `qic_directive_get` returns the current directive with the expected version.
- [ ] Calling an unknown tool name returns a clean MCP error, not a stack trace with internals.
- [ ] The endpoint is unreachable without valid Cloudflare Access credentials.

## GitLab read

- [ ] `gitlab_whoami` returns the expected GitLab identity.
- [ ] `gitlab_project_search` returns results for a known search term.
- [ ] `gitlab_project_get` returns details for a known project.
- [ ] `gitlab_file_read` returns file content for a known path/ref.

## GitLab security

- [ ] With `QIC_GITLAB_PAT` unset, every GitLab tool fails closed with a clear error (not a crash,
      not a hang).
- [ ] With an invalid PAT, GitLab tools fail with GitLab's own 401, surfaced without headers.
- [ ] `gitlab_file_write` against `main` is rejected regardless of other flags.
- [ ] `gitlab_file_write` against `master` is rejected regardless of other flags.
- [ ] Any mutation tool with `QIC_ENABLE_MUTATIONS=false` is rejected before any GitLab API call is made.
- [ ] Any mutation tool with mutation mode on but no fresh approval file is rejected.
- [ ] Any mutation tool with mutation mode on, approval file present, but `owner_approved=false` is rejected.
- [ ] No merge tool exists in the tool listing.

## GitLab mutation (disposable branch only: `TEST/MCP-INTEGRATION`)

- [ ] `gitlab_branch_create` succeeds with all three authorization factors present.
- [ ] `gitlab_file_write` (create) succeeds on the disposable branch.
- [ ] `gitlab_file_write` (update) succeeds on the disposable branch.
- [ ] `gitlab_merge_request_create` succeeds; the MR is **not** merged by any tool.
- [ ] The approval file is consumed (gone) after the first mutation call, and a second mutation
      call without recreating it is rejected.
- [ ] Test branch/MR cleaned up (or explicitly left for owner review) after verification.

## Claude Code

- [ ] Remote MCP connects (`claude mcp get qic-control-plane` / `/mcp` in-session).
- [ ] `qic_directive_get` works from within Claude Code.
- [ ] Read tools work from within Claude Code.
- [ ] No PAT appears anywhere in Claude Code's tool output, transcript, or logs.
- [ ] Fail-closed behavior: with Cloudflare Access credentials removed, the connection fails
      cleanly and Claude Code does not silently fall back to an unauthenticated path.

## ChatGPT integration

- [ ] Whatever can be verified without publishing production credentials or completing OpenAI's
      Developer Mode connector setup in a live ChatGPT account — see `CHATGPT/TEST-PLAN.md`.
