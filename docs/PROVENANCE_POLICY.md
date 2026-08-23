# Provenance Policy

Rules for recording where imported or cherry-picked material came from. Applies whenever a
change carries the `source:cherry-picked`, `source:migrated`, or `source:reference` label
(`LABEL_POLICY.md` §6).

## 1. Principle

Cherry-pick content, not whole repositories. Every imported material set is traceable back to
its origin without relying on chat history or an agent's memory.

## 2. What to record

For every imported material set, record:

- source organization;
- source repository;
- source path;
- source commit or revision, when available;
- import date;
- imported by (agent or human);
- why retained;
- destination (path in the receiving repository);
- modifications made during import.

## 3. Where to record it

Use a lightweight, per-repository record — `.provenance/` or `docs/provenance/` — only in
repositories that actually import material. Do not create the directory speculatively in a
repository with no imports.

A minimal per-import entry (one file or one table row per import) is sufficient. Do not add
large attribution headers to every imported source file; provenance lives in the record, not
scattered through file comments.

## 4. License check

Before importing material from a repository not owned by QUANTINOVA INDUSTRIES CORP, confirm
license compatibility with the destination repository's own license or proprietary status.
Record the finding in the provenance entry's "why retained" field. Do not import when
compatibility cannot be confirmed.

## 5. Ownership

Claude owns provenance recording for material it curates and imports (`AGENT_POLICY.md` §1).
AGY does not import material — its audit findings feed Claude's cherry-pick plan (Phase D), and
provenance is recorded only once Claude actually implements an approved import (Phase F).
