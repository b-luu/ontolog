# Contributing

[Project overview](README.md) · [Documentation map](docs/README.md)

Use fictional or independently publishable material only. Describe the user task, observed failure, proposed change, and how you checked the outcome. Keep methodology separate from company-specific policy.

For schema changes, update the [field guide](skills/ontolog-interview/assets/knowledge-repository/docs/model.md), [templates](skills/ontolog-interview/assets/knowledge-repository/templates/README.md), [validator](skills/ontolog-interview/assets/knowledge-repository/tools/validate.py), and [example](skills/ontolog-interview/assets/knowledge-repository/examples/subscription-business/README.md) together. Increment `schema_version` for incompatible changes and document migration. Keep installed skills self-contained and copied knowledge repositories independent of this checkout; see [project structure](docs/project-structure.md).

Before proposing a change, run the [development checks](README.md#development-checks). `python3 tools/check_docs.py` checks local Markdown links, heading fragments, and whether guides are reachable from the README. Keep links inside the distributed skill/template relative to files that travel with them; optional example files must not become required navigation targets in an ordinary ejection.

Use [pilot scenarios](docs/pilot-scenarios.md) for behavioral evaluation. Cases should examine fidelity, missing information, scope, attribution, disagreement, and authority rather than exact phrasing. A useful case includes two plausible but different definitions and enough evidence to determine whether the agent should map, specialize, or dispute them.

Keep unpublished articles, social drafts, and editorial decisions outside this public repository.

Keep one concern per commit, with messages in the form `type(scope): description`
(for example, `fix(validation): reject duplicate record IDs`). Use your GitHub
noreply address for commit authorship. Describe the problem, change, and validation
in pull requests. Run the checks locally before sending a change; CI repeats them.
See [repository maintenance](docs/maintenance.md) for workflows and branch rules.

Do not disclose vulnerabilities or company records in public issues. Use GitHub's
private vulnerability reporting when enabled. Until then, request a private
reporting channel without including the sensitive details.

Public contributions to this repository are offered under its MIT license. Organizational knowledge created using the kit is not a contribution to this project unless its owner explicitly publishes it here.
