---
schema_version: 1
id: concept-finance-active
type: concept
title: Active customer (finance)
status: approved
scope_ids:
- domain-finance
contributor_ids:
- contributor-sam
source_ids:
- session-finance
created: '2026-10-16'
updated: '2026-10-16'
visibility: internal
unknowns: []
definition: a billing customer with at least one positive-value invoice settled in
  the calendar month. Trial-only and fully refunded invoices do not qualify.
concept_kind: role
aliases:
- active customer
confirmed_by_ids:
- contributor-sam
confirmation_source_ids:
- source-finance-summary
decision_id: decision-finance-active
effective_from: '2026-10-16'
---

# Active customer (finance)

Includes customers meeting this function's definition. Counterexample: a trial user who logged in without a settled invoice.

Evidence: [session](session-finance.md#q1).
