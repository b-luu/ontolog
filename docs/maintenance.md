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

### Refresh the CI dependency

CI installs [exact, hashed requirements](../.github/requirements.txt) with
`--require-hashes --only-binary=:all:`. Only the Linux x86_64 wheels for CPython
3.10 and 3.14 are included. The distributed template keeps its portable compatible
range; this CI file is not an installation guide for other platforms.

Dependabot monitors both requirement files. Review each update to ensure the CI
pin still satisfies the template range and that hashes change with the release.
Dependabot supports hashed requirements, but its first update here still needs
verification; it may include hashes for additional release artifacts.

To refresh manually, choose a reviewed PyYAML release within the template range.
From an environment with pip, download both CI wheels into a fresh directory:

```sh
version=6.0.3 # Replace with the reviewed release.
wheel_dir=$(mktemp -d)
for python_version in 310 314; do
  python3 -m pip download --index-url https://pypi.org/simple --only-binary=:all: \
    --no-deps --python-version "$python_version" --implementation cp \
    --abi "cp$python_version" --platform manylinux2014_x86_64 \
    --dest "$wheel_dir" "PyYAML==$version"
done
python3 -m pip hash "$wheel_dir"/*.whl
```

Replace the version and hashes together in `.github/requirements.txt`. Check the
release provenance and notes; calculating a hash does not establish trust in a
new release. In clean Python 3.10 and 3.14 environments, install with the exact CI
command and run all CI checks. Run `python -m pip install --dry-run -r
skills/ontolog-interview/assets/knowledge-repository/requirements.txt` after that
installation to confirm the installed pin satisfies the template range (no upgrade
or replacement should be proposed). Revisit wheel selection when changing CI
platforms or Python versions; do not disable hash verification to fix a mismatch.

See pip's [secure installation guidance](https://pip.pypa.io/en/stable/topics/secure-installs/).

## GitHub configuration

Keep default workflow tokens read-only, require full-SHA action pins, and disallow
Actions from approving pull requests. Enable issues, disable the unused wiki, allow merge and squash commits,
disable rebase merging, and delete merged branches automatically. Merge commits
preserve reviewed atomic commits; squash is useful for noisy contributor branches.
The [code owner](../.github/CODEOWNERS) reviews external contributions.
Workflows from all outside contributors require maintainer approval.

The [main ruleset](../.github/main-ruleset.json) prevents deletion and force pushes,
requires a reviewed pull request and successful Python/zizmor checks, and requires
review threads to be resolved. It also gates CodeQL findings and code-quality
errors and requests Copilot review. Repository administrators can bypass through a
pull request for solo maintenance; check CI before using that bypass.

The repository is public. The ruleset is active as
[Protect main](https://github.com/b-luu/ontolog/rules/25734352). To update the live
rule, first export its current writable fields and compare them with the tracked
configuration. A replacement can silently remove rules added through GitHub:

```sh
rules_dir=$(mktemp -d)
gh api repos/b-luu/ontolog/rulesets/25734352 \
  --jq '{name, target, enforcement, bypass_actors, conditions, rules}' > "$rules_dir/live.json"
diff -u "$rules_dir/live.json" .github/main-ruleset.json
```

Review semantic differences, not formatting. Preserve every current rule and
parameter unless its removal is explicitly approved. Verify required check names
against a successful run. Immediately before an authorized replacement, fetch
again and stop if live settings changed since review. Only then apply the reviewed
file with `gh api --method PUT repos/b-luu/ontolog/rulesets/25734352 --input
.github/main-ruleset.json`. Fetch again afterwards and compare all writable fields,
including bypass actors, review parameters, required checks, scanning and quality
rules. The file alone does not enforce protection. The earlier export provides a
recovery reference, not permission to overwrite concurrent changes.

CodeQL default setup is enabled for Python and Actions, with weekly scanning.
Dependabot alerts and automated security fixes, private vulnerability reporting,
secret scanning, and push protection are enabled. These are GitHub settings;
committing workflow files does not configure them. Report vulnerabilities through
the [private reporting form](https://github.com/b-luu/ontolog/security/advisories/new).
The [security policy](../SECURITY.md) describes support and reporting expectations.

## Security finding follow-up

The October 28, 2026 [security plan](plans/security-practices.md) addresses concrete
maintenance gaps. [Scorecard findings](https://github.com/b-luu/ontolog/security/code-scanning)
are evidence about practices, not a count of confirmed exploitable defects:

- **Dependency pinning and policy:** hash-checked CI installs and a discoverable
  policy address the identified gaps. Confirm the next hosted scan before claiming
  the alerts resolved.
- **Review and branch protection:** one required approval and administrator bypass
  through a PR remain deliberate solo-maintainer choices. Local agent review is
  not a GitHub approval or a second maintainer. Keep these findings open; seek an
  actual additional reviewer when practical, without manufacturing approvals.
- **SAST:** CodeQL scans current main and recent PR heads in Python and Actions.
  Historical coverage was incomplete. Keep default setup and its ruleset gate;
  check analyses for each newly merged head and investigate missing new coverage.
  Do not assume repository startup explains every missed historical commit.
- **Fuzzing:** bounded deterministic malformed-metadata tests exercise parser
  failure handling, including excessive nesting. Run them with
  `python3 -m unittest discover -s tests -p test_repository.py -v`.
  They are not a recognized continuous fuzzing service and do not resolve that
  finding. Defer service infrastructure until the input surface warrants it.
- **Maintenance history:** reassess after January 21, 2027 and ordinary ongoing
  maintenance; age alone does not guarantee a passing result.
- **Best-practices badge:** defer the optional self-assessment until sustained use
  and maintenance capacity justify it. Missing certification is not a code defect.

## Identity and releases

Use a GitHub noreply address for both commit author and committer. Set it locally
before committing; a mailmap does not remove an address from existing Git objects.
Keep one concern per commit and use `type(scope): description` messages.

Before a release, run the checks in the README, inspect the diff for company data,
and generate the skill ZIP from the exact reviewed revision with
`python3 ontolog.py export-skill`. Generated archives stay out of Git. Do not reuse
an older local archive after changing the skill. Publishing an archive or the
article is separate from pushing source code.
