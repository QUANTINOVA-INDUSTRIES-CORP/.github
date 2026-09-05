# Discovery — GitLab CE

Date: 2026-09-05

- Instance: `https://gitlab.quantinovaindustries.org`, reachable, API v4 confirmed working via `glab`.
- Authenticated identity (via `glab`, on the Windows operator machine): user id 2, username `ceobetch`, "President, Chairman & Chief Executive Officer" — i.e. the owner's own personal account, with `can_create_project: true` and `projects_limit: 100000`.
- **No projects exist yet** on the instance (`GET /projects` returns `[]` for this user, both with and without the membership filter). This is a fresh GitLab CE install with no repositories migrated/created yet.
- No GitLab Personal Access Token currently exists anywhere on the homelab server (`/etc` has no `qic`-named files, no `/etc/qic-mcp`). The only working GitLab credential today is the personal token `glab`/`git` already use from the Windows operator machine's OS keyring.
- **Open decision:** the task brief assumes an "existing" PAT will be placed server-side. The only candidate today is the CEO's own personal token. Reusing a personal, full-scope owner credential as a network-facing service identity is a real security trade-off versus minting a new, narrowly-scoped token for a dedicated `qic-mcp` bot/service account. See the question asked in-conversation; this file records the trade-off, not the decision.
