---
schema_version: 1
id: question-different-counts
type: question
title: Why can Product and Finance counts differ?
status: resolved
scope_ids:
- domain-customer-lifecycle
contributor_ids:
- contributor-alex
source_ids:
- session-product
created: '2026-10-16'
updated: '2026-10-16'
visibility: internal
unknowns: []
question_kind: competency
question: Why can Product and Finance report different active customer counts?
related_ids:
- concept-product-active
- concept-finance-active
answer_ids:
- metric-product-active
- metric-finance-active
---

# Why can Product and Finance counts differ?

Product counts recent logged-in accounts. Finance counts customers with settled invoices in a calendar month. A trial user and an inactive paying customer demonstrate differences.

The question is answered with sourced scoped definitions; this does not choose one shared metric.
