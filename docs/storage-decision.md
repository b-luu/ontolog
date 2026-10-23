# Storage decision: portable Markdown with flat YAML

[Documentation map](README.md) · [Record model](../skills/ontolog-interview/assets/knowledge-repository/docs/model.md)

Status: initial choice for phase one; reconsider after a multi-contributor pilot.

## Decision

Use Markdown for definitions, examples, rationale, and interview summaries. Use flat YAML front matter for stable IDs, typed references, status, scope, dates, and metric parameters. Each record is a single file. Body prose and structured fields must agree; structured fields are authoritative for indexing and validation, and conflicts must be resolved explicitly.

Use immutable IDs independent of paths and labels. Use full UUIDs prefixed by record type for new records, e.g. `concept-<uuid>`. File names can be human-readable but include a unique ID suffix. Never merge records based solely on equal labels. Standard relative Markdown links make navigation work without wiki-link interpretation; structured references remain IDs. An indexer can derive a graph from records and assertions later.

Obsidian is optional. Its [properties documentation](https://obsidian.md/help/properties) supports YAML properties but describes limitations around nested properties and Markdown in properties. Therefore, use scalars and lists of scalars, keeping explanations in the body and qualified relationships in separate assertion notes. A link in prose assists navigation; it does not imply an approved semantic relationship. No `.obsidian` settings or community plugins are required.

## Alternatives

| Option | Useful when | Tradeoff for this project |
| --- | --- | --- |
| Markdown + YAML | Humans review definitions and agents exchange small versioned contributions | Needs validation; Git conflict handling is a learned workflow |
| JSON/YAML records plus generated Markdown | Strict machine contracts dominate | More difficult for contributors to edit; avoid two writable sources of truth |
| Notion or another collaborative wiki | Nontechnical browser editing is essential | Export, version review, and structured relationships need evaluation |
| SQL database with a review application | Concurrent editing, permissions, and queries become central | Requires operating an application; can retain the same logical model |
| RDF/SKOS/OWL store | Interoperability, graph querying, or formal entailment is a demonstrated requirement | Requires additional modeling and tooling expertise; named/contextual assertions still need design |
| Property graph | Relationship traversal dominates | A graph alone does not establish meaning, evidence, or approval |
| Vector index | Finding related passages | Use as a derived search index; approximate retrieval cannot be the canonical definition store |

## Migration triggers

Move storage behind an API when Git review blocks participation, access boundaries differ within a repository, or concurrent writes are frequent. Introduce executable semantic models when metrics must run centrally. Add RDF/OWL only when explicit reasoning or interchange requirements justify formal semantics.

This schema is not a formal ontology language. For example, absence of a statement never means the statement is false. An `is_a` assertion expresses a modeled subtype claim; the current validator does not compute its logical consequences. `part_of` is not interchangeable with `is_a`, and `close_match` never licenses substituting one metric for another.
