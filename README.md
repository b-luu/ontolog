# Ontolog

**Shared business knowledge, built through interviews.**

An interview-driven method for building a business ontology, preserving individual perspectives, and agreeing on precise metric definitions. This is an initial local-first starter, ready to pilot; it has not yet been evaluated with real organizational interviews.

The kit contains a portable [agent skill](skills/ontolog-interview/SKILL.md) and a self-contained [knowledge repository template](skills/ontolog-interview/assets/knowledge-repository/README.md). Both are MIT licensed. There is no API, MCP server, hosted service, or required Obsidian plugin.

For apps that support skill ZIP import, download the tested package from the
[v0.1.0-alpha.1 prerelease](https://github.com/b-luu/ontolog/releases/tag/v0.1.0-alpha.1).
See [compatibility evidence](docs/compatibility.md) for tested CLI environments and
the limits of native-app support.

## Find what you need

| I want to… | Start here |
| --- | --- |
| Set up a company repository and agent | [Installation guide](docs/installation.md) |
| Explore the knowledge repository before using it | [Template guide](skills/ontolog-interview/assets/knowledge-repository/README.md), [record templates](skills/ontolog-interview/assets/knowledge-repository/templates/README.md), [fictional example](skills/ontolog-interview/assets/knowledge-repository/examples/subscription-business/README.md) |
| Understand how interviews work | [Interview method](skills/ontolog-interview/references/interview-method.md) |
| Understand the design or improve Ontolog | [Documentation map](docs/README.md), [contributing](CONTRIBUTING.md) |

The template is bundled with the skill so an installed skill can initialize a repository independently. Ejection gives your organization its own standalone copy. See [project structure](docs/project-structure.md) for the packaging tradeoffs.

## Start a private knowledge repository

Requires Python 3.10+. From this checkout:

```sh
python3 ontolog.py eject /absolute/path/to/company-knowledge
cd /absolute/path/to/company-knowledge
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python tools/validate.py .
```

The initializer refuses an existing destination. Add `--with-example` to include a separate fictional example. The empty template is the default. Open the generated folder as an Obsidian vault, in a text editor, or through your Git host.

Choose a destination **outside this kit checkout**. The initializer enforces that boundary, including through symlink paths. The result is an independent copy with no inherited Git history or remote. It does not create a hosted repository or configure privacy. If using Git hosting, create a separate private repository, verify its access settings, and invite your organization there. Contributor branches belong to that private repository. Keep the template bundled here empty; do not populate a public fork with company knowledge. See [setup](skills/ontolog-interview/assets/knowledge-repository/docs/setup.md).

## Give each contributor's agent the skill

Run the interactive installer to choose your agent:

```sh
python3 ontolog.py install
```

Or specify `--agent codex` or `--agent claude-code`. It copies the complete skill and refuses to overwrite an existing installation. Use `python3 ontolog.py export-skill` to create a ZIP for apps with skill import, including Claude web/Cowork. Local installation and app import have different discovery and file-access boundaries; see the [installation guide](docs/installation.md). The package follows the [Agent Skills specification](https://agentskills.io/specification).

An example invocation:

> Use $ontolog-interview to interview me about our customer lifecycle. Our knowledge repository is at /absolute/path/to/company-knowledge. I work in customer support. Capture my perspective first, then compare it with existing definitions.

Each contributor uses their own agent and a branch or working copy of the same private repository. They share versioned records, with explicit provenance, through ordinary Git review. No direct communication between agents is required. File access without Git also works; see the [collaboration procedure](skills/ontolog-interview/assets/knowledge-repository/docs/collaboration.md).

## What the method produces

- A bounded domain and competency questions defining what the knowledge base must answer.
- Contributor-confirmed concepts, business relationships, rules, and metric definitions.
- Attributed assertions with evidence, context, and uncertainty.
- Proposed alignments and explicit disagreement records.
- Human decisions establishing approved definitions within a stated scope.

Contributor confirmation means “this represents my understanding.” Organizational approval requires a recorded decision by a configured domain steward. An agent cannot infer that mandate from seniority or agreement counts.

## Storage choice

The default is one Markdown note per record, flat YAML front matter for structured fields, stable record IDs for references, and relative Markdown links for navigation. See [the format decision](docs/storage-decision.md) for alternatives and migration criteria. Obsidian is an optional reader/editor; its graph view is a navigation aid, not an ontology reasoner.

The structured schema is deliberately lightweight. It borrows from SKOS vocabulary modeling, competency-question-driven ontology development, and provenance modeling, without claiming RDF/OWL conformance or formal reasoning support. [Method sources](docs/method-sources.md) distinguish established ideas from this kit's conventions.

## Semantic layers and analyst practice

An existing semantic layer describes the current executable calculation; approved business intent establishes what it should mean. A mismatch can require correcting that implementation. This repository captures context, rationale, perspectives, and proposed changes, linking to the calculation rather than maintaining a second independent implementation. General query-writing and analysis methods belong in companion skills; company-specific interpretation caveats can be sourced here or linked from the organization's data documentation. See [scope and integration](docs/scope-and-integration.md).

## Open-source boundary

Publish this reusable kit, templates, tooling, and fictional examples. Keep each company's populated repository separate and private by default. Its license and access policy are chosen by that organization; the kit's MIT license does not grant rights to interview content or company knowledge.

Do not put client transcripts, identities, formulas, or schemas in issues or examples here. [Contributing](CONTRIBUTING.md) describes how to improve the method using synthetic cases.

## Development checks

```sh
python3 -m pip install -r skills/ontolog-interview/assets/knowledge-repository/requirements.txt
python3 -m unittest discover -s tests -v
python3 tools/check_docs.py
python3 skills/ontolog-interview/assets/knowledge-repository/tools/validate.py skills/ontolog-interview/assets/knowledge-repository
```

The validator checks record structure, references, and minimum review evidence. It cannot determine business truth, verify a contributor's identity, or enforce access control. The first pilot should assess interview fidelity, whether differences survive reconciliation, and whether users can correctly select and reproduce a metric.

## Later phases

After a pilot: improve the method from observed failures, introduce search/indexes as needed, then expose the same IDs and proposal/review operations through an API and MCP. Database adoption should preserve attribution, scoped definitions, and decision history.

Unpublished articles and social drafts are maintained separately from this public repository.
