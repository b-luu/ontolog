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

[Scorecard](../.github/workflows/scorecard.yml) checks repository security settings
on main and weekly, and publishes its results for this public project. Its job
alone has permissions to upload security results and obtain a publishing identity.

## GitHub configuration

Keep default workflow tokens read-only, require full-SHA action pins, and disallow
Actions from approving pull requests. Enable issues, disable the unused wiki, allow merge and squash commits,
disable rebase merging, and delete merged branches automatically. Merge commits
preserve reviewed atomic commits; squash is useful for noisy contributor branches.
The [code owner](../.github/CODEOWNERS) reviews external contributions.
Workflows from all outside contributors require maintainer approval.

The [main ruleset](../.github/main-ruleset.json) prevents deletion and force pushes,
requires a reviewed pull request and successful Python/zizmor checks, and requires
review threads to be resolved. Repository administrators can bypass through a
pull request for solo maintenance; check CI before using that bypass.

The repository is public. The ruleset is active as
[Protect main](https://github.com/b-luu/ontolog/rules/25734352). To update the live
rule from the versioned configuration:

```sh
gh api --method PUT repos/b-luu/ontolog/rulesets/25734352 --input .github/main-ruleset.json
```

Verify required check names against an actual successful run before changing them.
The file alone does not enforce protection; verify the live rule after updating it.

CodeQL default setup is enabled for Python and Actions, with weekly scanning.
Dependabot alerts and automated security fixes, private vulnerability reporting,
secret scanning, and push protection are enabled. These are GitHub settings;
committing workflow files does not configure them. Report vulnerabilities through
the [private reporting form](https://github.com/b-luu/ontolog/security/advisories/new).

## Identity and releases

Use a GitHub noreply address for both commit author and committer. Set it locally
before committing; a mailmap does not remove an address from existing Git objects.
Keep one concern per commit and use `type(scope): description` messages.

Before a release, run the checks in the README, inspect the diff for company data,
and generate the skill ZIP from the exact reviewed revision with
`python3 ontolog.py export-skill`. Generated archives stay out of Git. Do not reuse
an older local archive after changing the skill. Publishing an archive or the
article is separate from pushing source code.
