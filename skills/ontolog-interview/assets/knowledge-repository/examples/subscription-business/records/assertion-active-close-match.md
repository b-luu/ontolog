---
schema_version: 1
id: assertion-active-close-match
type: assertion
title: Similar labels, differing populations
status: proposed
scope_ids:
- domain-customer-lifecycle
contributor_ids:
- contributor-alex
source_ids:
- session-product
- session-finance
created: '2026-10-16'
updated: '2026-10-16'
visibility: internal
unknowns: []
subject_id: concept-product-active
predicate: close_match
object_id: concept-finance-active
evidence_kind: derived
---

# Similar labels, differing populations

The concepts overlap but are not substitutes. A trial user can log in without paying; a paying customer can have no login. `close_match` is proposed for discovery only.

Evidence: [Product](session-product.md#q1) and [Finance](session-finance.md#q1).
