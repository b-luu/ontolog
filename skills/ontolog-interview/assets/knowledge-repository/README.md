# Business knowledge repository

Start at [domain setup](docs/setup.md), then use the [record model](docs/model.md) and [collaboration procedure](docs/collaboration.md). This folder is an independent template: copy it for an organization and choose that repository's access policy and content license.

Keep the organization's instance separate from the public kit and its forks. Create your own private remote when using hosting; copying files alone does not establish hosted privacy. [Scope boundaries](docs/boundaries.md) explain links to executable semantic definitions and companion analytical methods.

## Reading paths

| Task | Guide |
| --- | --- |
| Establish scope and ownership | [Domain setup](docs/setup.md) |
| Create a knowledge record | [Record templates](templates/README.md), then [field guide](docs/model.md) |
| Combine contributions and record decisions | [Collaboration](docs/collaboration.md) |
| Connect metrics and analyst context | [Scope boundaries](docs/boundaries.md) |
| Understand agent behavior in this repository | [Agent instructions](AGENTS.md) |

## Contents

- `records/`: one Markdown file per domain, contributor, source, session, concept, assertion, metric, question, or decision, organized by type.
- [templates/](templates/README.md): unfinished record patterns; replace placeholders before moving them into `records/`.
- `docs/`: schema and working procedures.
- `tools/validate.py`: structural and provenance checks; never a guarantee of truth or authority.
- `examples/`: an optional, isolated fictional dataset. It is never part of the organization's records.

Metadata ID references are authoritative. Add relative Markdown links in bodies for human navigation. Obsidian will display Markdown and YAML properties without plugins; opening the root folder as a vault is sufficient. The visible graph comes from note links, not automatically from ID references.

## Check records

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python tools/validate.py .
```

For the optional example: `.venv/bin/python tools/validate.py examples/subscription-business`.

An empty repository validates but contains no business knowledge. Create a domain, contributor, source, and session before writing attributed concepts. Unknowns are expected in proposed records; approval has additional requirements. The validator reports records with unknown fields to catch typos; organization-specific scalar/list extensions use an `x_` prefix.

## Privacy and publication

Treat this as private until the organization chooses otherwise. `visibility` is a descriptive label, not access control. All people with repository access can read its files and potentially its Git history. Keep restricted interviews in a separate access-controlled location and contribute only authorized summaries. A Git ignore rule or later deletion does not remove already-committed data.

The included MIT license covers the reusable template/tooling. Choose and document the rights and sharing rules for newly authored organizational records separately.
