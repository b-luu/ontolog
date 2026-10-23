# Eliciting a metric contract

A metric is a precise measure; a KPI additionally has an explicit business objective and decision use. Avoid declaring every dashboard number a KPI.

## Ask progressively

Begin with the decision the number supports and an ordinary-language definition. Then resolve the parameters below, using concrete examples. Do not ask the contributor to write SQL or fill a metadata form.

1. **Population and grain:** what is counted, and what identifies a unique member? Is the grain person, account, transaction, session, or contract?
2. **Qualifying events and exclusions:** statuses, test/internal accounts, refunds, chargebacks, bonus activity, retries, and duplicates where relevant.
3. **Calculation:** formula, input measures, numerator/denominator, zero-denominator behavior, units, currency conversion, precision, and rounding.
4. **Time:** event versus ingestion date, half-open boundaries, rolling versus calendar period, timezone, late arrivals, restatements, and effective date.
5. **Aggregation:** allowable dimensions, distinct counts across groups, additivity, and how subtotals behave.
6. **Implementation:** authorized data sources, transformation/query/semantic-model locator, refresh expectations, ownership, and discrepancies with current dashboards.
7. **Examples:** at least one included case, one excluded case, and an exact-boundary or duplicate case with expected output.

Use `unknowns` to record unsettled parameters. A proposed metric can be incomplete. An approved metric must settle all applicable parameters; use an explicit “not applicable: reason” rather than silently omitting one.

## Reproducibility

Write the business rule separately from implementation details. For a count, specify deduplication identity and time scope; for a ratio, define both populations and zero handling. Distinct monthly users cannot generally be summed from daily distinct counts or across overlapping dimensions.

If the organization already has a governed semantic definition, link its canonical metric/model and revision in `implementation_ref`. Use the `formula` field to describe that definition with its reference, or label an illustrative copy with its source revision. Deployed code establishes the current calculation; approved business intent establishes what it should mean. If they disagree, record an implementation question and review the evidence, including whether the code needs correction. Interview discoveries become reviewable proposals; do not silently redefine deployed logic or promise automatic synchronization.

If source access is absent, record a proposed metric and an implementation validation question. A checked formula does not imply checked SQL. Approval requires an implementation reference and reproducible examples, or an explicit approved contract describing a future implementation with that limitation stated in the record.

In the repository schema, `worked_examples` stores compact cases as strings, e.g. “one person, two qualifying accounts in June → 1 person”. Longer fixtures and calculations belong in the note body or linked authorized artifacts. Do not put identifiable customer records into examples.
