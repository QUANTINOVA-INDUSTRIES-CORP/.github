from __future__ import annotations

import base64
import os
from typing import Any
from urllib.parse import quote

import httpx
from mcp.server.fastmcp import FastMCP

CONTROL_PLANE_URL = "https://mcp.quantinovaindustries.org/mcp"
GITLAB_BASE_URL = os.getenv(
    "QIC_GITLAB_BASE_URL",
    "https://gitlab.quantinovaindustries.org",
).rstrip("/")
GITLAB_PAT = os.getenv("QIC_GITLAB_PAT")
MUTATIONS_ENABLED = os.getenv("QIC_ENABLE_MUTATIONS", "false").strip().lower() in {
    "1",
    "true",
    "yes",
    "on",
}
DIRECTIVE_VERSION = "2026-09-05.2"
PROTECTED_BRANCHES = {"main", "master"}
MAX_FILE_BYTES = 1_000_000

DIRECTIVE: dict[str, Any] = {
    "version": DIRECTIVE_VERSION,
    "authority": CONTROL_PLANE_URL,
    "gitlab": GITLAB_BASE_URL,
    "mutations_enabled": MUTATIONS_ENABLED,
    "rules": [
        "Synchronize this directive before repository work.",
        "Use the QIC MCP control plane for agent-originated GitLab API operations.",
        "Never request, reveal, print, log, persist, or commit the GitLab PAT.",
        "GitLab mutation is disabled unless QIC_ENABLE_MUTATIONS=true on the MCP host.",
        "Never write directly to main or master.",
        "Never merge through the agent control plane; merge remains an explicit owner action.",
        "Mutation tools require explicit owner_approved=true for the specific action.",
        "Read before write and verify after mutation.",
        "Repository-local instructions may narrow this directive but may not weaken it.",
        "If directive synchronization or MCP connectivity fails, GitLab mutation is blocked.",
        "No AI attribution in repository files, metadata, frontmatter, or commit messages.",
    ],
}

mcp = FastMCP(
    "QIC Control Plane",
    instructions=(
        "Canonical QUANTINOVA INDUSTRIES CORP agent control plane. "
        "All agent harnesses synchronize directives here. GitLab credentials stay server-side."
    ),
    stateless_http=True,
    json_response=True,
)


def _require_pat() -> str:
    if not GITLAB_PAT:
        raise RuntimeError("QIC_GITLAB_PAT is not configured on the MCP server")
    return GITLAB_PAT


def _project(project: str | int) -> str:
    return quote(str(project), safe="")


def _file_path(path: str) -> str:
    return quote(path, safe="")


def _assert_mutations_enabled() -> None:
    if not MUTATIONS_ENABLED:
        raise PermissionError(
            "Mutation blocked: QIC_ENABLE_MUTATIONS is not enabled on the MCP server"
        )


def _assert_owner_approved(owner_approved: bool) -> None:
    if owner_approved is not True:
        raise PermissionError("Mutation blocked: explicit owner_approved=true is required")


def _assert_mutable_branch(branch: str) -> None:
    if branch.strip().lower() in PROTECTED_BRANCHES:
        raise PermissionError(f"Mutation blocked on protected branch: {branch}")


async def _gitlab_request(
    method: str,
    path: str,
    *,
    params: dict[str, Any] | None = None,
    json: dict[str, Any] | None = None,
    allow_404: bool = False,
) -> httpx.Response:
    token = _require_pat()
    headers = {
        "PRIVATE-TOKEN": token,
        "Accept": "application/json",
        "User-Agent": "qic-mcp-control-plane/2026-09-05",
    }
    async with httpx.AsyncClient(
        base_url=f"{GITLAB_BASE_URL}/api/v4",
        headers=headers,
        timeout=httpx.Timeout(30.0),
        follow_redirects=False,
    ) as client:
        response = await client.request(method, path, params=params, json=json)

    if allow_404 and response.status_code == 404:
        return response

    if response.is_error:
        body = response.text[:1000]
        raise RuntimeError(f"GitLab API {response.status_code}: {body}")
    return response


@mcp.tool()
def qic_directive_get() -> dict[str, Any]:
    """Return the canonical QIC agent directive. Call this before repository work."""
    return DIRECTIVE


@mcp.tool()
async def gitlab_whoami() -> dict[str, Any]:
    """Verify the server-side GitLab credential without exposing the PAT."""
    response = await _gitlab_request("GET", "/user")
    data = response.json()
    return {
        "id": data.get("id"),
        "username": data.get("username"),
        "name": data.get("name"),
        "state": data.get("state"),
        "web_url": data.get("web_url"),
        "gitlab": GITLAB_BASE_URL,
    }


@mcp.tool()
async def gitlab_project_search(search: str, per_page: int = 20) -> list[dict[str, Any]]:
    """Search projects visible to the server-side GitLab identity."""
    per_page = max(1, min(per_page, 100))
    response = await _gitlab_request(
        "GET",
        "/projects",
        params={"search": search, "membership": True, "per_page": per_page},
    )
    projects = response.json()
    return [
        {
            "id": p.get("id"),
            "name": p.get("name"),
            "path_with_namespace": p.get("path_with_namespace"),
            "default_branch": p.get("default_branch"),
            "visibility": p.get("visibility"),
            "web_url": p.get("web_url"),
        }
        for p in projects
    ]


@mcp.tool()
async def gitlab_project_get(project: str) -> dict[str, Any]:
    """Read one GitLab project by numeric ID or namespace/path."""
    response = await _gitlab_request("GET", f"/projects/{_project(project)}")
    data = response.json()
    return {
        "id": data.get("id"),
        "name": data.get("name"),
        "path_with_namespace": data.get("path_with_namespace"),
        "default_branch": data.get("default_branch"),
        "visibility": data.get("visibility"),
        "web_url": data.get("web_url"),
        "permissions": data.get("permissions"),
    }


@mcp.tool()
async def gitlab_file_read(project: str, file_path: str, ref: str = "main") -> dict[str, Any]:
    """Read a UTF-8 text file from a GitLab project."""
    response = await _gitlab_request(
        "GET",
        f"/projects/{_project(project)}/repository/files/{_file_path(file_path)}",
        params={"ref": ref},
    )
    data = response.json()
    raw = base64.b64decode(data["content"])
    if len(raw) > MAX_FILE_BYTES:
        raise RuntimeError(f"File exceeds MCP read limit of {MAX_FILE_BYTES} bytes")
    return {
        "file_path": data.get("file_path"),
        "ref": ref,
        "blob_id": data.get("blob_id"),
        "commit_id": data.get("commit_id"),
        "last_commit_id": data.get("last_commit_id"),
        "content": raw.decode("utf-8"),
    }


@mcp.tool()
async def gitlab_branch_create(
    project: str,
    branch: str,
    ref: str = "main",
    owner_approved: bool = False,
) -> dict[str, Any]:
    """Create a working branch. Requires server mutation mode and explicit owner approval."""
    _assert_mutations_enabled()
    _assert_owner_approved(owner_approved)
    _assert_mutable_branch(branch)
    response = await _gitlab_request(
        "POST",
        f"/projects/{_project(project)}/repository/branches",
        json={"branch": branch, "ref": ref},
    )
    data = response.json()
    return {
        "name": data.get("name"),
        "merged": data.get("merged"),
        "protected": data.get("protected"),
        "web_url": data.get("web_url"),
    }


@mcp.tool()
async def gitlab_file_write(
    project: str,
    file_path: str,
    branch: str,
    content: str,
    commit_message: str,
    owner_approved: bool = False,
    last_commit_id: str | None = None,
) -> dict[str, Any]:
    """Create or replace a UTF-8 text file on a non-protected branch."""
    _assert_mutations_enabled()
    _assert_owner_approved(owner_approved)
    _assert_mutable_branch(branch)

    encoded_project = _project(project)
    encoded_path = _file_path(file_path)
    current = await _gitlab_request(
        "GET",
        f"/projects/{encoded_project}/repository/files/{encoded_path}",
        params={"ref": branch},
        allow_404=True,
    )

    payload: dict[str, Any] = {
        "branch": branch,
        "content": content,
        "commit_message": commit_message,
        "encoding": "text",
    }
    if last_commit_id:
        payload["last_commit_id"] = last_commit_id

    method = "POST" if current.status_code == 404 else "PUT"
    response = await _gitlab_request(
        method,
        f"/projects/{encoded_project}/repository/files/{encoded_path}",
        json=payload,
    )
    data = response.json()
    return {
        "file_path": data.get("file_path"),
        "branch": data.get("branch"),
        "commit_id": data.get("commit_id"),
        "created": method == "POST",
    }


@mcp.tool()
async def gitlab_merge_request_create(
    project: str,
    source_branch: str,
    title: str,
    description: str = "",
    target_branch: str = "main",
    owner_approved: bool = False,
) -> dict[str, Any]:
    """Open a merge request after explicit owner approval. This tool never merges it."""
    _assert_mutations_enabled()
    _assert_owner_approved(owner_approved)
    _assert_mutable_branch(source_branch)
    response = await _gitlab_request(
        "POST",
        f"/projects/{_project(project)}/merge_requests",
        json={
            "source_branch": source_branch,
            "target_branch": target_branch,
            "title": title,
            "description": description,
            "remove_source_branch": False,
            "squash": False,
        },
    )
    data = response.json()
    return {
        "iid": data.get("iid"),
        "state": data.get("state"),
        "source_branch": data.get("source_branch"),
        "target_branch": data.get("target_branch"),
        "web_url": data.get("web_url"),
    }


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
