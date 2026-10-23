# Ontolog documentation

[Project overview](../README.md)

## Use Ontolog

1. [Install the skill and eject a company repository](installation.md). This covers local agents, app import, examples, and access boundaries.
2. [Set up the domain](../skills/ontolog-interview/assets/knowledge-repository/docs/setup.md). Define the purpose, contributors, and ownership of your private instance.
3. [Follow the interview method](../skills/ontolog-interview/references/interview-method.md), then [clarify metrics](../skills/ontolog-interview/references/metrics.md) and [compare perspectives](../skills/ontolog-interview/references/alignment.md) as needed.
4. [Review contributions](../skills/ontolog-interview/assets/knowledge-repository/docs/collaboration.md) and [evaluate a pilot](pilot-scenarios.md).

## Explore the repository format

The [template guide](../skills/ontolog-interview/assets/knowledge-repository/README.md) is also the README of every ejected repository. Its [record model](../skills/ontolog-interview/assets/knowledge-repository/docs/model.md), [record templates](../skills/ontolog-interview/assets/knowledge-repository/templates/README.md), and [scope boundaries](../skills/ontolog-interview/assets/knowledge-repository/docs/boundaries.md) travel with that repository.

Use the [fictional subscription-business example](../skills/ontolog-interview/assets/knowledge-repository/examples/subscription-business/README.md) to see two different definitions and a scoped approval. Examples are opt-in when ejecting.

## Understand the design

| Document | Question it answers |
| --- | --- |
| [Project structure](project-structure.md) | Why bundle the template inside the skill, and when should packaging change? |
| [Storage decision](storage-decision.md) | Why Markdown/YAML, and when might another store make sense? |
| [Scope and integration](scope-and-integration.md) | How does business knowledge relate to semantic layers and analytical practice? |
| [Method sources](method-sources.md) | Which ideas come from ontology/provenance standards, and which are Ontolog conventions? |

## Contribute or prepare a release

[Repository maintenance](maintenance.md) covers CI, dependency updates, GitHub settings, and the steps to enable branch protection when publishing.

Read [contributing](../CONTRIBUTING.md) for change and validation expectations, and [pilot scenarios](pilot-scenarios.md) for behavioral evaluation. The [skill entry point](../skills/ontolog-interview/SKILL.md) is the maintained instruction set installed in agents.

The [release workspace](release/README.md) is for maintainers editing the blog and social copy. It records the current draft status and unresolved editorial decisions; it is not required reading to use Ontolog.
