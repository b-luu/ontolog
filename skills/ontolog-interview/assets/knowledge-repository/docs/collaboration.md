# Contributions from multiple people and agents

[Repository guide](../README.md) · [Domain setup](setup.md) · [Record lifecycle](model.md#lifecycle)

## Contribution boundary

Use one canonical organizational repository. Each contributor gets a branch/working copy and uses their own agent with the interview skill. New IDs use type-prefixed full UUIDs. Filename prefixes can be readable; IDs never depend on file paths or a contributor's name.

Start by recording the canonical revision if Git is available. Create a session and new attributed records before editing shared definitions. A contribution consists of the changed records and any authorized evidence needed to review them. All local `*_id` references must resolve in the canonical repository plus the contribution. Portable exports must include their dependency closure or an explicit manifest identifying missing canonical dependencies; an incomplete export must not be called independently valid.

## Suggested Git workflow

1. Inspect status and use a new branch or isolated working copy without disturbing existing work. Do not switch branches over someone else's uncommitted edits.
2. Capture the contributor's account, read it back, and retain proposed/confirmed states honestly.
3. Refresh the canonical revision before reconciliation. Re-read changed shared definitions; create an alignment question if meaning conflicts.
4. Run `python3 tools/validate.py .` with the configured environment. Include a review note listing captured perspective, confirmations, differences, unknowns, and validation outcome.
5. When authorized, submit a reviewable change. Combining files is editorial acceptance; it does not approve their business meaning. Proposed and disputed records can be merged as useful evidence.
6. An authorized steward records an adoption decision with explicit evidence before target records become approved. If the contributor is also a steward, capture that distinct decision explicitly.

Pushing, merging, or contacting reviewers requires the user's authorization. The interviewing workflow itself does not grant it.

## Resolve conflicts at two levels

Mechanical conflict: two agents edited the same file. Preserve both changes and compare against their base; rerun validation. A clean Git merge does not prove semantic agreement.

Meaning conflict: same scope/time but incompatible statements. Keep both attributed accounts and create a disagreement question referencing them. Offer a boundary case and possible resolutions. Do not let the later contribution overwrite the earlier account by default.

When two agents independently create the same concept, propose a mapping with evidence. Only merge identity deliberately after review, preserving superseded records and references. Do not rewrite contributor history to create apparent consensus.

## Reviews and maintenance

Review source quality, scope, examples, authority, and downstream effects separately. Approved definitions change through replacement records and new decisions when meaning changes. Git history records edits but is not proof that the organization accepted them. Keep effective dates alongside recorded dates, and retain older definitions needed to explain historical reports.

## Sharing boundaries

Everything in one Git repository is visible to its readers; `visibility` does not partition access. Separate restricted storage from broadly shared definitions. Record only permitted source pointers, summaries, and contributor identifiers. Do not commit raw recordings by default. Share individual perspectives to the audience agreed with the contributor, rather than assuming that use of an organizational agent authorizes broad disclosure.

If a full transcript is requested, settle its retention and access location first. Redaction must happen before entering shared Git history. The open-source kit contains no organization interview data.
