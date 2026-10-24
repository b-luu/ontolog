# Synthetic interview evaluation: 2026-10-24

[Pilot cases](pilot-scenarios.md) · [Documentation map](README.md)

This is a synthetic agent evaluation, not a real organizational pilot or evidence
of production interview quality. A coordinating agent played fictional
contributors. Separate `gpt-6-luna` sessions received the skill, a realistic user
request, and only their assigned disposable repository. They were not given the
evaluation checklist or expected findings. The coordinator reviewed their actual
questions, read-backs, records, and validation output.

The interview skill was taken from revision `604fafa`; the adoption and final
checks used the approval-period correction merged through PR #9. Model/provider
behavior and sampling can change, so these observations are not a repeatability
guarantee. No real people, companies, customer accounts, or production queries
were used.

## Independent accounts and read-back

Alex, a Product analyst, was initially told only to discuss active customers as
accounts that logged in within the last 30 days. Follow-up answers supplied the
onboarding decision, account identity, UTC half-open rolling window, exclusions,
and deduplication. Late-event handling and implementation were left unknown.
The agent asked about the actual decision and source authority, then read back
the definition before receiving explicit confirmation. Its ten records included
a confirmed concept and metric, a proposed session, and four open questions.
There was no organizational approval or invented SQL.

Lee, in a separate empty repository, initially discussed active customers as
accounts that paid during the calendar month. Answers supplied distinct account
identity, settlement event time, UTC month boundaries, refund handling, and close.
The agent's read-back ambiguously referred to “same-month payment reversals.”
Lee corrected it: refunds occurring in the following month still apply if
recorded before 00:00 UTC on the fifth day. The seven saved records retained
that correction. The concept and metric were confirmed only as Lee's account;
implementation remained unverified and no steward was configured.

These independently generated records were combined only after both interviews
finished. Product's login-based scope and Finance's payment-based scope remained
distinct.

## Interrupted interview and fresh-session continuation

Morgan said: “We count customers who purchased recently; I don't know how refunds
are handled,” then ended before read-back. The agent saved eight records with a
proposed metric and session, open questions, and an exact resume point.

A fresh session received only Morgan's request to resume and the saved repository.
It read back the existing unknowns instead of restarting. Morgan supplied a
14-day UTC window, account-level counting, and support-prioritization purpose,
while correcting attribution to individual practice rather than team policy.
Refunds and implementation stayed unknown. The complete metric remained proposed
because only the corrected account/time rules had been confirmed.

## Conflicting Finance practices

Sam reported counting an account even when its payments were fully refunded
before close, agreeing with Lee on the other parameters. After Sam confirmed a
read-back, the reconciliation agent retained both Finance definitions and wrote
an open disagreement question. It distinguished that same-purpose conflict from
Product's legitimate separate scope. The combined repository contained 23 records;
no vote, inferred authority, or automatic equivalence resolved the conflict.

## Restricted sharing and stale input

A separate copy contained a later contributor's unresolved suspended-account
boundary in Lee's concept. Sam then supplied an older account and a restricted
fictional example, permitting only an anonymous refund example. The agent added
the anonymized evidence to Sam's records without editing Lee's newer concept.
A before/after SHA-256 comparison confirmed Lee's file was unchanged; a scan of
every file found neither the restricted account token nor its amount. The
official-policy question remained open. Validation passed for 25 records.

This tested stale content preservation in one working copy, not concurrent Git
merges or synchronization between machines. The instances deliberately had no
Git history, so the test establishes no initial persistence of restricted text,
not removal of data already committed elsewhere.

## Scoped adoption and fresh-reader check

The coordinator explicitly configured Lee as Finance steward in another copy.
Lee adopted only the Finance concept, effective 2026-10-01, leaving metric
implementation and executive reporting undecided. The agent created a decision
and approval evidence and approved only that concept. Sam's account, Product's
concept, and the implementation retained their previous status.

A fresh reader was given only the resulting repository and six business
questions. It selected the approved Finance concept for October 15, identified
the implementation as unapproved, rejected company-wide extrapolation, and found
no approved Finance meaning before October 1. For a fully refunded October
account with no login, it returned Lee = 0, Sam = 1, Product = 0. It counted a
single account with multiple users/logins once, included the rolling-window start,
and excluded the report-time boundary. It also identified the unresolved source,
query, and late-event gaps instead of inventing deployed numbers.

The reader exposed a consistency failure: the Finance policy question still said
no authority or answer was known after the adoption. The initial agent had
preserved the question instead of updating it. Adding a question-review step to
the alignment reference alone did not correct this in a second fresh session.
Explicitly routing decision recording to the alignment procedure also left the
question stale in a third session. The requirement was therefore moved into the
skill's core decision instructions. In the final fresh session, the agent resolved
the Finance refund-boundary question, linked the decision in `answer_ids`, and
removed the obsolete unknown. Implementation remained open and only Lee's Finance
concept was approved. All three failed snapshots are retained as evidence; they
are not examples of the desired outcome. One successful repeat supports this
narrow correction, not a claim that every model will always follow it.

## Retained artifacts

The [v0.1.0-alpha.1 release](https://github.com/b-luu/ontolog/releases/tag/v0.1.0-alpha.1)
includes a separate `pilot-evidence.zip` containing generated record snapshots,
scenario notes, and validation counts. It is evaluation material, not a company
repository template. `SHA256SUMS` covers this archive and the separate skill ZIP.

| Snapshot | Records | Result |
| --- | ---: | --- |
| `product` | 10 | Independent confirmed Product account; no approval |
| `finance` | 7 | Independent Finance account with corrected refund boundary |
| `incomplete` | 8 | Final resumed state; metric still proposed |
| `shared` | 23 | Both Finance accounts preserved; disagreement open |
| `stale` | 25 | Anonymous example retained; newer Lee file unchanged |
| `adoption` | 25 | Initial approval correct; policy question stale |
| `adoption-repeat` | 25 | Reference-only change; policy question still stale |
| `adoption-routed` | 26 | Router-only change; policy question still stale |
| `adoption-final` | 25 | Core instruction applied; scoped policy question resolved |

Every snapshot passed the corrected structural validator. The first interrupted
state is described above from the observed session; the `incomplete` snapshot is
the final state after continuation, not an untouched before/after pair.

## Evidence and limitations

All generated repositories are disposable and contain fictional summaries rather
than full transcripts. The evaluator recorded observations and inspected statuses
and worked examples in addition to running structural validation. Successful
validation alone does not establish the quality of an interview.

Native-app imports, genuine contributor consent and satisfaction, adversarial
prompt injection, large organizations, and long-running concurrent editing were
not evaluated. The next real-user pilot still needs an authorized organization,
contributors reviewing their own accounts, and a fresh colleague answering the
organization's competency questions.
