# Alignment and review

## Compare meanings in context

Retrieve the candidate definitions, their assertions, scopes, effective periods, source evidence, and decision history. Compare instances that qualify, events counted, identity, granularity, timing, exclusions, and intended use. Matching labels or embeddings are candidate retrieval signals only.

| Difference | Proposed treatment |
| --- | --- |
| Different labels, same meaning in the relevant context | Propose aliases or an `exact_match` assertion with evidence |
| Similar meaning with meaningful edge differences | `close_match`; preserve both definitions and specify substitution limits |
| One definition is a narrower population/type | `is_a` for modeled subtype, or `broader` for vocabulary organization; do not confuse the two |
| Different legitimate departmental purposes | Keep separately scoped concepts/metrics, provide explicit usage guidance |
| Same scope and time, incompatible rules | Retain both claims; create an open question containing the contradiction |
| Different effective periods | Preserve versions; propose `supersedes` only for an intentional replacement |
| Same business definition, differing SQL | Record implementation divergence and a reconciliation question; do not redefine the business automatically |

`exact_match` is a local scoped mapping proposal, not OWL identity. No mapping in this kit causes automatic merging or logical propagation. Assertions have their own provenance and scope; approved endpoints do not make a proposed mapping approved.

## Propose a resolution

Provide the conflicting records, a concrete case where the difference matters, evidence on each side, possible treatments, and who has authority for the affected scopes. Prefer an explicit shared core with local specializations when supported. Do not seek universal agreement for differences that do not require harmonization.

An unresolved question is a useful output. Never assign a shared definition by majority, inferred seniority, agent confidence, or simply selecting the oldest record.

## Record a decision

Use a decision record linking the affected records, exact effective date, decision scope, authorized approvers, evidence of approval, alternatives considered, and rationale. For adoption, its outcome is `adopt`; other outcomes are `defer` or `reject`. Only an approved adoption decision can make target records `approved`.

Domain stewards are configured in domain records by the organization's chosen governance procedure. The first interview agent may propose a domain and steward, but must not approve its own authority. The validator checks declared stewardship, not real-world mandates or signatures. Steward assignment changes deserve explicit human review.

For a change to an approved meaning, create a replacement record and decision, preserving the previous version and linking `supersedes`. Ordinary typo/source-locator corrections may use Git history without a new semantic version. Re-check references and KPI implementations affected by a replacement. Do not auto-deprecate a record while another scope still uses it.

## Query behavior

When answering a business question, select by scope, effective date, and status. For approved definitions, resolve omitted effective bounds from the adopting decision as described in the repository model, and require the question date to be on or after the start and strictly before any end. Check both definition and decision; an approved status alone does not apply outside that period. Cite the selected record and evidence. State when no approved definition fits, and describe relevant alternatives. Do not silently fall back from an approved shared definition to a contributor's proposed one. Where definitions differ, explain the difference with an example and ask for the missing context only if it changes the answer.
