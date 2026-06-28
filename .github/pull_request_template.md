## Summary

<!-- State what changed and why. Keep the scope precise. -->

## Change classification

Select all that apply:

- [ ] Bug fix
- [ ] Feature
- [ ] Refactor
- [ ] Documentation
- [ ] Test
- [ ] Build or dependency change
- [ ] CI/CD or infrastructure
- [ ] Security or compliance
- [ ] Breaking change
- [ ] Data migration
- [ ] Other: <!-- describe -->

## Linked work

<!-- Use "Closes #123", "Fixes #123", or link the approved work item. -->

- Issue or work item:
- Requirement, decision record, or specification:

## Scope

### Included

<!-- List the concrete changes included in this pull request. -->

### Excluded

<!-- State intentionally deferred or out-of-scope work. -->

## Risk assessment

- **Overall risk:** Low / Medium / High / Critical
- **Affected systems or users:**
- **Failure mode:**
- **Data impact:** None / Read-only / Schema / Migration / Deletion / NOT STATED
- **Security or privacy impact:** None / Yes — described below / NOT STATED
- **Backward compatibility:** Compatible / Breaking / NOT STATED

### Risk controls

<!-- Describe validation, feature flags, access controls, backups, approvals, and safeguards. -->

## Testing and evidence

- [ ] Automated tests added or updated
- [ ] Existing test suite passes
- [ ] Linting and static analysis pass
- [ ] Type checking passes where applicable
- [ ] Manual verification completed
- [ ] Failure and rollback paths tested
- [ ] Test evidence is attached or linked

**Test commands and results:**

```text
[PASTE_SANITIZED_COMMANDS_AND_RESULTS]
```

## Security, privacy, and secrets

- [ ] No secrets, credentials, tokens, private keys, or confidential records are included
- [ ] New permissions follow least privilege
- [ ] User-controlled input is validated and safely handled
- [ ] Logging excludes sensitive values
- [ ] Dependency changes were reviewed for provenance, license, and known vulnerabilities
- [ ] Security review is requested when required

## Documentation and operations

- [ ] User or operator documentation is updated
- [ ] API, schema, configuration, or environment-variable changes are documented
- [ ] Monitoring, logging, and alerting changes are documented
- [ ] Deployment instructions are included
- [ ] Rollback instructions are included
- [ ] No documentation change is required; reason stated below

**Documentation exception or notes:**

<!-- Explain any unchecked item that would normally apply. -->

## Deployment plan

1. <!-- pre-deployment validation -->
2. <!-- deployment step -->
3. <!-- post-deployment verification -->

## Rollback plan

1. <!-- rollback trigger -->
2. <!-- rollback step -->
3. <!-- data-restoration or verification step -->

## Breaking changes and migrations

<!-- Write "None" when not applicable. Include consumer impact, migration order, compatibility window, and deprecation notice when applicable. -->

## Reviewer focus

<!-- Direct reviewers to the highest-risk files, assumptions, or design decisions. -->

## Author checklist

- [ ] The branch is current with the target branch
- [ ] The change is focused and contains no unrelated modifications
- [ ] Commit messages follow the organization convention
- [ ] Generated files and lockfiles are intentional
- [ ] All placeholders and temporary debugging code are removed
- [ ] Comments explain decisions, not obvious syntax
- [ ] Required approvals are identified
- [ ] I reviewed the final diff as a reviewer would
