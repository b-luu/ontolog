# Repository maintenance

[Documentation map](README.md) · [Contributing](../CONTRIBUTING.md)

## Continuous integration

[CI](../.github/workflows/ci.yml) runs the offline test suite, documentation
checks, template and example validation, and CLI ejection/export on Python 3.10
and 3.14. Tests exercise installed skills and ejected repositories independently.
Dependency installation requires network access; the tests themselves do not.

[zizmor](../.github/workflows/zizmor.yml) checks GitHub Actions security on every
pull request. Both workflows use immutable action revisions, explicit read-only
permissions, disabled checkout credential persistence, and timeouts. Required
checks have no path filters, so documentation-only pull requests can complete.
[Dependabot](../.github/dependabot.yml) proposes weekly Python and Actions updates.

## GitHub configuration

Keep default workflow tokens read-only, require full-SHA action pins, and disallow
Actions from approving pull requests. Enable issues, disable the unused wiki, allow merge and squash commits,
disable rebase merging, and delete merged branches automatically. Merge commits
preserve reviewed atomic commits; squash is useful for noisy contributor branches.
The [code owner](../.github/CODEOWNERS) reviews external contributions.

The [main ruleset](../.github/main-ruleset.json) prevents deletion and force pushes,
requires a reviewed pull request and successful Python/zizmor checks, and requires
review threads to be resolved. Repository administrators can bypass through a
pull request for solo maintenance; check CI before using that bypass.

GitHub currently does not allow rulesets for this private repository on the
account's plan. Keeping the file here does **not** enforce protection. Once the
repository is public (or its plan supports private rulesets), apply it once:

```sh
gh api --method POST repos/b-luu/ontolog/rulesets --input .github/main-ruleset.json
```

Inspect existing rulesets before running that command again; update the existing
rule rather than creating duplicates. Verify the required check names against an
actual successful run. Changing repository visibility is a separate owner action.

Dependabot alerts and automated security fixes are enabled while private.
After making the repository public, enable GitHub CodeQL default setup for Python
and Actions, private vulnerability reporting, and secret scanning/push protection
where available. Verify each feature's status;
none is implied by committing workflow files. CodeQL and public Scorecard reporting
are deferred while private rather than requiring unavailable security features or
publishing analysis results from the private repository.

## Identity and releases

Use a GitHub noreply address for both commit author and committer. Set it locally
before committing; a mailmap does not remove an address from existing Git objects.
Keep one concern per commit and use `type(scope): description` messages.

Before a release, run the checks in the README, inspect the diff for company data,
and generate the skill ZIP from the exact reviewed revision with
`python3 ontolog.py export-skill`. Generated archives stay out of Git. Do not reuse
an older local archive after changing the skill. Publishing an archive or the
article is separate from pushing source code.
