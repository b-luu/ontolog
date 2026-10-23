# Scope and integration

[Documentation map](README.md) · [Operational guidance in the template](../skills/ontolog-interview/assets/knowledge-repository/docs/boundaries.md)

## Business knowledge and executable semantics

This project elicits and maintains an organization's business concepts, perspectives, rules, rationale, and open questions. A semantic layer centralizes executable analytical definitions. Its metrics and model relationships are valuable inputs to the knowledge base, and interview findings can motivate proposed changes to them.

The boundary is functional, not a claim that semantic-layer products lack documentation or agent context. See [dbt's Semantic Layer](https://docs.getdbt.com/docs/use-dbt-semantic-layer/dbt-sl) and [Cube's discussion of broader context](https://cube.dev/articles/ai-context-layer). Capabilities overlap; this project's specific contribution is the elicitation and attributed-review procedure.

When an executable definition exists, reference its canonical locator in `implementation_ref`, with its version or revision where possible. Explain business purpose, scope, evidence, and decision history in the knowledge record. A calculation contract before implementation is proposed knowledge; it is not a second deployed semantic layer.

The implementation establishes how a number currently executes; the approved business definition establishes intended meaning. If they disagree, review the evidence and correct whichever is wrong, including deployed code when it fails to implement an approved rule. An interview proposes a correction; it does not authorize an automatic change to production.

The existing `formula` field remains required by schema version 1. For implemented metrics, use a concise description tied to the canonical reference; explicitly label any formula copied for readability with its source revision. Approval review should check that it agrees with the implementation. There is no automated synchronization or drift detector in this release. If they disagree, open an implementation question and avoid claiming consistency until reviewed. Do not silently overwrite an existing implementation from an interview.

## Three kinds of analyst knowledge

| Knowledge | Recommended home | Example |
| --- | --- | --- |
| Reusable analytical method | Companion analysis skill/playbook | Check grain and cardinality before a join; validate a denominator |
| Organization-specific business or interpretation context | Organization knowledge repository | Refunds change qualification; a policy change limits historical comparability |
| Warehouse-specific implementation practice | Organization's data/model documentation, linked from the repository | Approved join path, snapshot caveat, query performance convention |

These are connected responsibilities. They need not share one interviewing skill or one schema. The current release does not include a generic analyst playbook, a dedicated operational-practice record type, query generation, or data execution tools.

Use sourced scoped assertions and source documents for company-specific caveats that fit the existing model. An analyst's intuition starts as a hypothesis or reported practice, not an approved universal business rule. Record evidence, limits, and questions; formalize new record types only after concrete pilot needs emerge. A future analytics agent can combine business context, methodological skills, executable metrics, and authorized data tools.

## Public method and private instance

The template and skill share one source project; each organization's ejected instance is independently maintained. Keep its records and review branches in the organization's private repository. `visibility` metadata is descriptive and does not enforce access.

See [project structure](project-structure.md) for the packaging decision and [installation](installation.md) for ejection, access settings, and updates. The ejected repository carries its own [setup](../skills/ontolog-interview/assets/knowledge-repository/docs/setup.md) and [collaboration](../skills/ontolog-interview/assets/knowledge-repository/docs/collaboration.md) guidance.
