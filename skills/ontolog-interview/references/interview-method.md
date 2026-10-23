# Interview procedure

## Scope and pacing

Default to a focused 20–30 minute session on one workflow or decision; adapt to the contributor. A shorter session should still capture one useful concept and an unresolved boundary. Avoid exhaustive question banks. Explain that the aim is to represent their understanding and identify shared or differing meanings. Ask what summary may be shared and where; if scope is unclear, keep the material in the current conversation until the sharing boundary is settled.

Use an existing session's resume point and open questions. Ask whether responsibilities or definitions changed since the last session. Do not assume a person's account is representative of their entire department.

## 1. Anchor the domain in actual work

Start with: “What decision or activity are you responsible for, and can you walk me through a recent example?”

Follow the episode: trigger, participants, objects, state changes, systems, outputs, and decisions. Ask which terms newcomers misunderstand. Learn who uses the outputs and what happens if their meaning is wrong. Keep scope bounded; record adjacent domains as follow-up questions rather than expanding indefinitely.

Output: provisional domain scope, contributor responsibilities, a concrete episode, and 2–5 competency questions in business language. These are questions the knowledge base should answer, not a demand that the contributor know ontology terminology.

## 2. Elicit concepts and relationships

Choose terms used in the episode. Ask what qualifies, how the person recognizes an instance, and what does not qualify. Probe identity and lifecycle: can two records represent the same person? When does a prospect become a customer? Can the transition be reversed?

Distinguish:

- Label versus concept: the same word may name different things.
- Type versus instance: “subscription” versus a specific subscription.
- `is_a` versus `part_of`: a premium subscription is a subscription; a payment is not a subtype of customer.
- Entity versus event versus state: account, deposit, verified.
- Business rule versus current system behavior: a policy may differ from the implementation.
- Absence of knowledge versus a negative claim: “I don't know of exceptions” does not mean there are none.

Draft only useful concepts and assertions. Do not invent a comprehensive class hierarchy from a list of nouns. Explain proposed relationships in business language and check them with examples.

## 3. Probe decisions, rules, and measurements

Ask “How do you tell whether this is going well?” and “Which number would change your decision?” Follow [metrics.md](metrics.md) when an actual measure emerges. Record qualitative rules and exceptions even when no KPI is involved.

Use a boundary case matched to the answer. If “paying customer” means someone who paid, ask about refunds, test accounts, partial payments, delayed events, and the relevant time boundary only as needed. Do not list every conceivable exception.

## 4. Ground the account

Ask what supports the definition: a policy, dashboard, query, procedure, or experienced practice. Record a precise locator and provenance. A dashboard title is evidence of usage, not proof of a calculation. Request authorized artifacts if necessary; never fabricate source access or claim to have checked a query that was not inspected.

Use session answer anchors, e.g. `#q3`, for capture. Record whether text is paraphrased. A source may point to a restricted system without copying its content, provided the pointer itself is appropriate for the shared audience. If it is not, keep it outside the shared repository too.

## 5. Read back and validate

Present a compact model: “I understand X to mean ..., in your workflow ..., which includes A and excludes B. Y remains uncertain.” Ask the contributor to correct it. Ask whether each definition is personal practice, team practice, written policy, or something they are uncertain about. That attribution is itself their report unless independently supported.

Record explicit confirmation evidence and exactly which records it covers. Correct errors with an auditable revision; do not claim that a general “looks good” approves organizational policy. If the session ends before confirmation, save `proposed` records and a pending read-back task.

## 6. Compare without erasing

Now introduce relevant existing definitions neutrally, with their scopes and sources. Ask whether the difference changes who or what counts and under which circumstances. Follow [alignment.md](alignment.md). Do not prompt “everyone else says X, do you agree?”

## 7. Close and persist

Deliver a short contribution: key terms, relationships, KPI candidates, examples, evidence, unknowns, differences, and next questions. Create or update the session note with purpose, retention boundary, confirmed record IDs, and resume point. Save incremental records when authorized; if a repository is unavailable, return the same records as a bundle with suggested relative paths.

## Evaluate a pilot

Ask each contributor to review a sample for fidelity. Have a different contributor use the model to answer competency questions and select a metric for a concrete scenario. Track unanswerable questions, missed boundary cases, unsupported equivalences, and corrections after read-back. Success is faithful capture and usable definitions, not maximum note count or apparent consensus.
