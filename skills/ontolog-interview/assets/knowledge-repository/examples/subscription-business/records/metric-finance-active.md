---
schema_version: 1
id: metric-finance-active
type: metric
title: Active customer count (finance)
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
definition: Count of customers qualifying as a billing customer with at least one
  positive-value invoice settled in the calendar month. Trial-only and fully refunded
  invoices do not qualify.
business_purpose: Monitor paying customer base.
formula: COUNT(DISTINCT billing_customer_id) over qualifying records
population: Production billing customers
grain: one billing customer
identity_rule: billing_customer_id; multiple invoices per customer count once
unit: customers
time_window: Calendar month [month start, next month start), UTC
time_field: invoice.settled_at
timezone: UTC
aggregation: Distinct count; nonadditive across overlapping groups and time windows
zero_handling: No qualifying records yields zero; denominator not applicable
late_data_policy: Restate the previous 60 days on each daily refresh
rounding: Integer count; no rounding
implementation_ref: 'Approved future contract: implement in reporting layer; code
  has not been verified'
concept_ids:
- concept-finance-active
inclusions:
- Positive-value settled invoice
exclusions:
- Test customers
- Trial-only customers
- Fully refunded invoices
dimensions:
- plan
worked_examples:
- One customer with two settled invoices in the month -> 1
- Trial-only customer with login but no settled invoice -> 0
- Invoice settled exactly at next month start -> 0 for this month
confirmed_by_ids:
- contributor-sam
confirmation_source_ids:
- source-finance-summary
decision_id: decision-finance-active
effective_from: '2026-10-16'
---

# Active customer count (finance)

See structured contract for calculation. Examples use fictional accounts.

Finance settlement is evaluated against the current invoice state, including full refunds, with restatements limited as stated. The choice of a longer restatement period may require a new definition.

Implementation reference is a contract, not a claim of inspected code.
