# Security practices maintenance

Status: approved by the maintainer; implemented and locally verified, awaiting
independent implementation review and hosted checks.

## Scope and evidence

Address the concrete dependency, policy, and ruleset maintenance gaps identified
in the October 28 security triage. Preserve current governance settings and leave
findings open until evidence supports resolution. No alert dismissals, settings
changes, publishing, or manufactured review approvals belong to this change.

Observed October 28, 2026, on branch `fix/security-practices`; freshly fetched main
was `124cbfb` during inspection; the branch now includes editorial merge `13dea6a`.
The live [Protect main ruleset](https://github.com/b-luu/ontolog/rules/25734352) also contains
CodeQL, code-quality and Copilot rules and additional pull-request parameters
missing from the tracked JSON. Current main and recent PR heads have CodeQL
analyses with zero results ([analyses API](https://api.github.com/repos/b-luu/ontolog/code-scanning/analyses));
this does not prove all historical commits were scanned.

Repository conventions: Python 3.10+, stock pip, unittest, the documentation
checker and template validator. [CI](../../.github/workflows/ci.yml) tests Python
3.10 and 3.14. The distributed [template requirements](../../skills/ontolog-interview/assets/knowledge-repository/requirements.txt)
keep their compatible `PyYAML>=6.0.3,<7` range.

## Planned changes

1. Reconcile `.github/main-ruleset.json` with a fresh live export, preserving every
   editable protection and bypass field. Update `docs/maintenance.md` to export,
   compare and review current rules before any replacement, then read back and
   verify the live rule after an authorized update. Do not execute a PUT here.
2. Add a short root `SECURITY.md`: current alpha support, private GitHub reporting,
   no sensitive public issues, no promised response deadline. Link it from the
   maintenance guide so the documentation checker can reach it.
3. Add `.github/requirements.txt` for CI with an exact supported PyYAML release and
   release artifact SHA-256 hashes; install with `pip --require-hashes` in CI.
   Add weekly Dependabot coverage for that requirements location and document
   a stock-pip download/hash refresh procedure, including review of version,
   provenance and both supported Python versions. Keep template requirements
   unchanged. During each refresh or independent dependency update, verify the CI
   pin satisfies the template range without introducing a resolver dependency.
   Verify any bot hash-update limitations instead of assuming support.
4. Record explicit security finding dispositions in maintenance documentation:
   dependency/policy fixes need post-merge scan evidence; code review and branch
   protection remain open governance limitations; retain one approval and PR-only
   administrator bypass; keep CodeQL default setup and monitor newly merged heads;
   recheck maintenance history after January 21, 2027; defer the optional badge.
5. Investigate a reproduced malformed-YAML depth crash through the actual validator
   CLI. If confirmed, handle that parser failure at the narrow parsing boundary and
   add a small dependency-free, fixed-seed malformed-input exercise for YAML/Markdown
   metadata with a documented local command and bounded CI runtime. Preserve valid
   input behavior and useful validation errors. This is robustness coverage, not a
   claim that recognized continuous fuzzing or the Scorecard fuzzing alert is resolved.
   Do not add a fuzzing platform/dependency or broaden path handling without evidence.

## Verification and completion

- Compare normalized tracked ruleset fields to a newly retrieved live rule;
  explicitly compare bypass, review, required checks, scanning and quality rules.
- Install the hash-checked dependency in clean Python 3.10 and 3.14 environments;
  prove a deliberately wrong hash is rejected without modifying the committed lock.
  Run the existing CI commands: unittest, docs, template/example validation, CLI help,
  ejection, ejected validation, export and ZIP integrity. Exercise refresh commands.
- Reproduce any malformed-input bug at the CLI before editing; verify clean rejection
  after editing. For each claimed regression test, temporarily revert only its fix,
  observe failure, restore it and observe success. Distinguish generated smoke tests
  from security guarantees and preserve a reproducible failing input.
- Inspect workflow changes with the repository's security checker when available.
  Re-read the diff and check for private machine configuration or company content.
- Obtain independent implementation review beyond these checks, including the ruleset
  state combinations and whether tests are load-bearing. No push until APPROVED and
  publication coordinated with the primary session. Real hosted CI/Scorecard and next
  CodeQL coverage can only be confirmed after authorized publication; report that limit.

## Boundaries and decisions

This plan preserves deliberately chosen solo-maintainer governance and defers the
badge and recognized fuzzing service. Adding real additional reviewers
or removing administrator bypass requires a separate owner decision.

The parallel editorial change owns README, CONTRIBUTING, docs/README,
docs/project-structure, .gitignore and removal of release drafts. Do not edit those
files here. Keep this plan reachable through the maintenance guide when implemented.
No root agent configuration is present to modify; configuration policy is maintained
outside this repository. Stop when the scoped patches and evidence are reviewed;
record remaining findings honestly rather than pursuing a score target.

## Verification record

Python 3.10.16 and 3.14.8 both installed the pinned wheels with hash verification
and rejected a deliberately incorrect hash. The documented refresh commands
reproduced both hashes, and pip confirmed the pin satisfies the template range.
Dependabot's upstream requirements updater supports hash replacement; its first
real update in this location remains to be verified.

On both Python versions, all 47 tests and every CI entry point passed: documentation
checks, template/example validation, CLI help, ejection, ejected validation, export
and ZIP integrity. The parser-depth CLI regression failed without the fix and
passed after restoration on both versions. The bounded metadata exercise is smoke
coverage, not a claim of fuzzing-service coverage. Workflow auditing reported no
findings with the existing suppressions.

All writable ruleset fields exactly matched a fresh live export. No settings were
changed and no alerts dismissed. CodeQL analyses for editorial main `13dea6a` and
its PR head had zero results in both languages. Post-publication CI and scanning
for this change remain pending; review/governance, maintenance age, badge and
continuous fuzzing findings retain the dispositions in the maintenance guide.
