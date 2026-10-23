# Record model, schema version 1

[Repository guide](../README.md) · [Record templates](../templates/README.md) · [Review procedure](collaboration.md)

This is the machine-checked field guide. Records live under `records/` as Markdown with YAML front matter. Templates and examples are outside that root and are not organizational records. YAML keys must be unique; metadata is flat scalars or lists of scalars, never nested maps. Quote dates and string values that resemble YAML booleans. Empty lists mean none recorded, not a universal negative claim.

## Common fields

| Field | Meaning |
| --- | --- |
| `schema_version` | Integer `1` |
| `id` | Immutable, unique, lowercase type-prefixed ID; new records use full UUIDs |
| `type` | `domain`, `contributor`, `source`, `session`, `concept`, `assertion`, `metric`, `question`, or `decision` |
| `title` | Human-readable label; not identity |
| `status` | Lifecycle state from the table below |
| `scope_ids` | List of domain IDs; required and nonempty except contributors |
| `contributor_ids` | Required list of attributed authors/reporters, not automatically reviewers; may be empty for domains and contributors |
| `source_ids` | Required list of evidence source/session IDs; may be empty for domains, contributors, and sources |
| `created`, `updated` | ISO `YYYY-MM-DD`, updated at least created |
| `visibility` | `public`, `internal`, or `restricted`; advisory only |
| `unknowns` | Required list of unresolved items; may be empty |
| `effective_from`, `effective_to` | Optional valid-time dates; the end is exclusive |
| `supersedes_ids` | Optional references to earlier records of the same type |
| `decision_id` | Optional approving adoption decision; required for approved concepts/assertions/metrics |
| `confirmed_by_ids` | Optional contributors who explicitly confirmed the account |
| `confirmation_source_ids` | Optional source/session evidence of that confirmation |

Contributor `contributor_ids`, `source_ids`, and `scope_ids` may be empty. A domain is scoped to itself, which is the only permitted self-reference. Source evidence terminates at a concrete `locator`; `source_ids` on a source may be empty to avoid circular provenance. Sessions reference a source such as a private interview locator or contributor-approved summary; derived records can reference the session.

## Lifecycle

| Type | Allowed states |
| --- | --- |
| domain, contributor | `draft`, `active`, `deprecated` |
| source | `draft`, `available`, `deprecated` |
| session | `draft`, `proposed`, `confirmed` |
| concept, assertion, metric | `draft`, `proposed`, `confirmed`, `approved`, `disputed`, `deprecated` |
| question | `open`, `resolved` |
| decision | `proposed`, `approved`, `rejected` |

`confirmed` means an attributed contributor recognizes the account. It requires `confirmed_by_ids` and `confirmation_source_ids`. Confirmation evidence should identify the explicit read-back response and records covered. It does not approve a business policy. `approved` on a definition requires an approved adoption decision covering that exact record and all its scopes. Approved assertions must be explicitly `stated` or `derived`, rather than an unchecked agent `inferred` claim. Approved records cannot have unresolved `unknowns`.

An approved decision requires approver IDs and approval evidence, with at least one declared steward of **each** decision scope among its approvers. It records a real human decision; a validator cannot authenticate it. Adding a steward is governance configuration, not something an interviewing agent may do unilaterally. `approved` on a decision indicates authorization of its outcome, which can be `adopt`, `defer`, or `reject`. Only `adopt` authorizes target definitions. `rejected` as a decision status means the proposed decision itself was not authorized.

## Type-specific fields

Fields listed here are required unless marked optional. Strings must be nonempty except optional fields; lists may be empty unless noted.

### Domain

`definition` (string), `steward_ids` (contributor list). Body: scope boundaries, purposes, interfaces with other domains. Do not derive parent/child scope inheritance automatically; list each applicable scope explicitly.

### Contributor

`role` (string), `team` (string). Body: expertise and responsibilities. A person's identity is not a claim that they represent all colleagues. A pseudonym is allowed.

### Source

`source_kind` (`interview`, `document`, `query`, `dashboard`, `practice`, `other`), `locator` (string with a precise location or anchor). Source evidence can be external or a summary stored in this source's own Markdown body. For a self-contained summary, use `locator: "#summary"` and include `## Summary`. Body: access boundary, relevant evidence, paraphrase/quotation distinction, limitations. Do not fabricate URLs or read access. A source may record contributor confirmation but must include the explicit response and covered IDs.

### Session

`participant_ids` (nonempty contributor list), `purpose` (string), `retention` (`summary_only`, `transcript_authorized`, `external_only`), `resume_point` (string), `captured_ids` (list of concepts/assertions/metrics/questions). Body: numbered question/answer anchors, confirmation record, unresolved questions, next step. `summary_only` stores a shareable summary, not a transcript. `external_only` stores only permitted metadata and an authorized external pointer, not interview content.

### Concept

`definition` (string), `concept_kind` (`entity`, `event`, `state`, `category`, `role`, `other`), `aliases` (string list). Body: positive and negative examples, boundaries, usage notes. Represent alternate scoped meanings as separate concepts, not incompatible definitions in one field.

### Assertion

`subject_id` (record ID), `predicate` (string), `evidence_kind` (`stated`, `inferred`, `derived`). Exactly one of `object_id` (record ID) or `value` (nonempty string). Body: evidence locator, interpretation, exceptions, derivation when relevant.

Preferred predicates: `is_a` (modeled subtype), `part_of`, `related_to`, `broader` (vocabulary hierarchy), `exact_match`, `close_match`, `requires`, `precedes`, `qualifies_when`, `excludes_when`, `implemented_by`. An extension predicate must define its meaning in the assertion body. Relations can themselves be proposed or disputed, independently of endpoints.

Assertions record positive relationships unless the predicate explicitly expresses negation/exclusion. Scope and valid time qualify the assertion. No automatic symmetry, transitivity, identity merging, or closed-world inference is implemented. Evidence must support the actual subject-predicate-object/value claim, not just mention the terms.

### Metric

Strings: `definition`, `business_purpose`, `formula`, `population`, `grain`, `identity_rule`, `unit`, `time_window`, `time_field`, `timezone`, `aggregation`, `zero_handling`, `late_data_policy`, `rounding`, `implementation_ref`.

Lists: `concept_ids`, `inclusions`, `exclusions`, `dimensions`, `worked_examples`.

For proposed metrics, unavailable string parameters may be empty and must be called out in `unknowns`. The essential `definition` and `business_purpose` cannot be empty. For approved metrics, every string must be nonempty, `concept_ids`, `inclusions`, and `worked_examples` must be nonempty, and there must be at least three worked cases. Include positive, negative, and boundary/deduplication cases with expected results. The validator counts examples but cannot assess their quality. A legitimately inapplicable string parameter says `not applicable: reason`; an empty exclusions/dimensions list must be explained in the body. Formula defines numerator/denominator for ratios. For currency, `unit` and body explain conversion. `implementation_ref` may explicitly describe an approved future implementation with a linked plan; it never implies code was verified.

### Question

`question_kind` (`competency`, `clarification`, `disagreement`, `implementation`), `question` (string), `related_ids` (record list), `answer_ids` (record list). A `resolved` question needs answer IDs and a supported answer in its body. Open competency questions are acceptance goals; do not fill them with invented answers.

### Decision

`target_ids` (nonempty concept/assertion/metric list), `outcome` (`adopt`, `defer`, `reject`), `rationale` (string), `approver_ids` (contributor list), `approval_source_ids` (source/session list). Body: exact decision, scope, alternatives, effective date, and affected downstream definitions. Approved decisions require `effective_from`. An approval source cannot be the decision itself.

## Links, extensions, and validation limits

Every `*_id`/`*_ids` reference must resolve inside this dataset; external references belong in `locator` or `implementation_ref`. Standard Markdown links in bodies provide clickable navigation. Links must not be used to infer relation semantics. New fields use `x_` to distinguish extensions from typos, and remain scalar/list values. Evolve `schema_version` for incompatible changes.

The validator checks IDs, reference types, flat front matter, dates, lifecycle, confirmation, approval, scope coverage, and basic metric completeness. It does not validate external locators, logical consistency, arithmetic, absence of sensitive data, semantic equivalence, signatures, or real-world authority. Review these with the responsible humans and applicable data tooling.
