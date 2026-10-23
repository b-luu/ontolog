---
schema_version: 1
id: metric-product-active
type: metric
title: Active customer count (product)
status: confirmed
scope_ids:
- domain-product
contributor_ids:
- contributor-alex
source_ids:
- session-product
created: '2026-10-16'
updated: '2026-10-16'
visibility: internal
unknowns: []
definition: Count of customers qualifying as an account with at least one successful
  login during the previous 30 complete UTC days.
business_purpose: Monitor product engagement.
formula: COUNT(DISTINCT account_id) over qualifying records
population: Production accounts
grain: one account
identity_rule: account_id; multiple accounts per person count separately
unit: customers
time_window: Previous 30 complete UTC days, [D-30 days, D) at midnight D
time_field: login.occurred_at
timezone: UTC
aggregation: Distinct count; nonadditive across overlapping groups and time windows
zero_handling: No qualifying records yields zero; denominator not applicable
late_data_policy: Restate the previous 60 days on each daily refresh
rounding: Integer count; no rounding
implementation_ref: Proposed reporting contract; implementation not inspected
concept_ids:
- concept-product-active
inclusions:
- Successful production login
exclusions:
- Test accounts
dimensions:
- plan
worked_examples:
- One account with two successful logins inside the window -> 1
- Paid invoice but no login in the window -> 0
- Login exactly at D is outside [D-30 days, D) -> 0
confirmed_by_ids:
- contributor-alex
confirmation_source_ids:
- source-product-summary
---

# Active customer count (product)

See structured contract for calculation. Examples use fictional accounts.

Finance settlement is evaluated against the current invoice state, including full refunds, with restatements limited as stated. The choice of a longer restatement period may require a new definition.

Implementation reference is a contract, not a claim of inspected code.
