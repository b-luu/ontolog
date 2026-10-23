# Record templates

[Repository guide](../README.md) · [Field guide](../docs/model.md) · [Domain setup](../docs/setup.md)

Copy a pattern into the appropriate `records/` subfolder, give it a unique type-prefixed UUID, and replace its placeholders. Templates are intentionally incomplete and are excluded from record validation until copied into `records/`. Leave unknown business facts explicitly unresolved rather than inventing values.

| Template | Captures |
| --- | --- |
| [Domain](domain.md) | Scope, purpose, and declared stewards |
| [Contributor](contributor.md) | A person's role and area of expertise |
| [Source](source.md) | Evidence and its location |
| [Session](session.md) | An interview summary, confirmation, and resume point |
| [Concept](concept.md) | A business concept with boundaries and examples |
| [Assertion](assertion.md) | An attributed, scoped relationship or claim |
| [Metric](metric.md) | A calculation contract and intended decision use |
| [Question](question.md) | A competency question, clarification, or unresolved disagreement |
| [Decision](decision.md) | An explicit review outcome and its authority |

Start with contributor and domain context, then sources and a session. Definitions and relationships can remain proposed while confirmation or business approval is pending. See the [lifecycle rules](../docs/model.md#lifecycle) before changing status, and the [collaboration procedure](../docs/collaboration.md) before adopting a shared definition.
