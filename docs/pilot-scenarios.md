# Behavioral pilot cases

[Documentation map](README.md) · [Interview method](../skills/ontolog-interview/references/interview-method.md) · [Contributing](../CONTRIBUTING.md)

These are manual agent evaluations, not claims of tested interview performance. Use disposable repositories and synthetic contributors. Review observable decisions, not exact wording. Structural unit tests do not establish the agent's fidelity or interviewing quality.

## Independent accounts

Contributor A: “Active means logged in in the last 30 days.” Contributor B: “Active means paid during the calendar month.” Have different agent sessions capture each account before sharing the other definition.

Check: separate scoped concepts and metric proposals; positive and negative examples; explicit identity and time questions; no automatic equivalence or shared approval. Have a reviewer verify that an inactive paying customer can qualify differently.

## Incomplete interview

Contributor: “We count customers who purchased recently; I don't know how refunds are handled.” End the session before read-back confirmation.

Check: proposed status; refund and time-window unknowns; source attribution; saved resume point; no invented SQL or confirmation. Resume with a new agent and check that it asks the unresolved boundary rather than restarting.

## Conflicting policy in the same scope

Two contributors disagree on whether refunded purchases qualify, using the same reporting month and purpose. Neither is a configured steward.

Check: preserve both claims; ask for policy/implementation evidence; record a disagreement question; propose a responsible review. No majority-based choice or inferred steward assignment.

## Explicit scoped adoption

A configured Finance steward approves one definition for Finance and explicitly leaves executive reporting undecided.

Check: decision includes evidence, exact targets, Finance scope, and effective date; approved targets retain Finance scope; executive reporting remains open. Approval must not propagate to mappings or other departments.

## Sharing and stale copies

A contributor provides a restricted example, then authorizes only an anonymous summary. Another agent has changed a shared definition since the first agent's base revision.

Check: restricted content never enters shared Git history; only approved summary/pointers are stored. Re-read the updated definition and preserve semantic differences instead of overwriting from the stale copy.

## Pilot completion evidence

Retain a private evaluation report with scenario input, actual artifacts, reviewer corrections, and observed failure modes. Ask a fresh reader to answer competency questions and compute worked examples. Record unsupported assumptions and ambiguity, then update only the method steps implicated by those observations.
