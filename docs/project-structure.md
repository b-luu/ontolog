# Project structure and packaging

[Documentation map](README.md) · [Installation](installation.md)

## Current decision

Keep one canonical knowledge repository template inside the interview skill. Make it a first-class destination in the README and documentation map. Distribute an independent organizational instance through `eject`, and a complete skill through `install` or `export-skill`.

Human discoverability matters: people need to inspect the schema and examples before committing to the method. Prominent links provide that entry point without making readers understand an agent's asset hierarchy first.

```text
README.md                            project entry point
docs/                                user guides and design explanations
  release/                           unpublished article and social drafts
skills/ontolog-interview/
  SKILL.md                           agent instructions
  references/                        interview, metric, and alignment methods
  scripts/init_repository.py          initializer usable by an installed skill
  assets/knowledge-repository/        canonical, independently usable template
    README.md                        ejected repository entry point
    docs/                            schema and organization procedures
    templates/                       record patterns and their index
    records/                         empty organization records
    examples/                        isolated fictional demonstration
    tools/validate.py                record checks
ontolog.py                           eject, install, and export commands
tools/check_docs.py                   documentation navigation checks
tests/                               behavior and packaging checks
```

## Source location and distributed ownership

The [template](../skills/ontolog-interview/assets/knowledge-repository/README.md) has its own instructions and validator. A team can use it without installing an interview skill. The [installation guide](installation.md) explains how to copy it into an independent private repository.

Bundling serves the other direction: a copied or uploaded skill has the files needed to initialize a repository, even when the public source checkout is unavailable. There is no build step, download dependency, or duplicated template to keep synchronized.

After ejection, the organization owns and versions its instance. Its documents refer only to files that travel with it. It has no runtime dependency on Ontolog's public checkout. Optional examples remain a separate dataset, never seed company records.

## Alternatives and when to revisit

| Layout | Benefit | Cost |
| --- | --- | --- |
| Current: one template inside a self-contained skill | Direct skill copies work; compatibility is maintained in one place | Deep source path; requires good human navigation |
| Top-level canonical template, bundled into skill during packaging | More visible source tree; separate release artifacts | Requires a build step and checks preventing stale generated copies |
| Separate template repository/package | Independent ownership and release cycle | Requires version compatibility and cross-project maintenance |

If the template gains independent maintainers or releases, move its canonical source to a top-level directory or a separate project and generate the bundled skill asset from it. Do not maintain two editable copies. A standalone downloadable template archive could also be generated from today's canonical source without moving it; that command is not implemented yet. `eject` already provides an independent local copy.

## Documentation boundaries

Project docs explain installation and design. Template docs explain how an organization maintains its records and must stay useful after ejection. Skill references teach the agent how to conduct the work and must stay useful after installation. Some brief overlap is intentional at these independent boundaries; detailed instructions should have one owner within each distributed artifact.

## Name and descriptor

The author selected **Ontolog** (O-N-T-O-L-O-G) on 2026-10-19, with **Shared business knowledge, built through interviews.** Use `ontolog` for the project/command and `ontolog-interview` for the skill. An organization chooses its own repository name.

The name evokes ontology and a log of developing understanding. [Ontolog Forum](https://ontologforum.org/info/) is an existing use in the ontology community; no affiliation is implied. The name does not establish search ranking or domain/package availability.
