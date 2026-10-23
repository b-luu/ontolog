# Release posts

[Release workspace and editorial status](README.md) · [Article draft](article.md)

Draft copy. Replace `{ARTICLE_URL}` and `{REPOSITORY_URL}` with live public URLs before use. Suggested spacing is relative to the article's publication, not a scheduled campaign. Each occurrence has a distinct angle; adjust timing to replies and feedback. No post claims pilot results.

## Occurrence 1: release, publication day

### LinkedIn

Same KPI. Same month. Two different numbers.

I've seen this across client work. You check the queries, refresh times, filters... and sometimes discover that the teams were counting different things from the start. Even the word “customer” can hide a few surprises.

On my last mission I worked on a knowledge base for the data domain. I've now put together a reusable starting point: Ontolog, an agent interview skill and a matching knowledge repository template, both MIT licensed.

The idea is to interview people about their actual work, capture their definitions with examples, then compare the different perspectives. Contributors can use their own agents. Shared definitions go through an explicit human decision.

It's early. The next step is a real multi-contributor pilot. I wrote up the reasoning and what's in this first version here:

{ARTICLE_URL}

### Twitter / X

Same KPI. Two dashboards. Different numbers.

Sometimes the teams are counting different things.

I've put together an agent interview skill + knowledge repo template to make those definitions explicit. MIT licensed, early version.

{ARTICLE_URL}

## Occurrence 2: the boundary case, roughly day 3–4

### LinkedIn

A trial user logs in every day. A paying customer hasn't opened the app in a month.

Which one is “active”?

Product and Finance can reasonably answer differently. The trouble starts when both answers end up in dashboards with the same label and people expect the numbers to match.

That's the kind of detail I want an interview agent to uncover. What qualifies? What doesn't? Are we counting a person or an account? Which time window applies?

Ontolog gives that conversation a procedure and somewhere to land: attributed definitions, examples, open questions, and proposals for alignment.

Here's the longer explanation, including why a useful definition needs more than a sentence:

{ARTICLE_URL}

### Twitter / X

A trial user logs in daily. A paying customer hasn't logged in for a month.

Which one is “active”?

Your teams may have good reasons to answer differently. Put the scope and examples next to the definition.

{ARTICLE_URL}

## Occurrence 3: preserve specialized knowledge, roughly day 7–8

### LinkedIn

The support team knows an exception. Finance knows why a refund needs special treatment. Product is looking at another stage of the customer lifecycle.

I'd like a business knowledge base to keep those perspectives attached as the shared model takes shape.

That's one of the choices behind Ontolog. Each contribution carries its source, scope, and review status. The agent helps compare accounts and propose mappings. A genuine contradiction stays visible until someone responsible resolves it.

And “yes, that's how I understand it” stays separate from “this is the approved definition for our reporting.”

I've written up the approach here. I'd be interested in examples where a department-specific definition was worth keeping:

{ARTICLE_URL}

### Twitter / X

“Yes, that's how I understand it” and “this is our approved reporting definition” are separate decisions.

Ontolog keeps contributor confirmation and shared approval separate, with scope and evidence attached.

{ARTICLE_URL}

## Occurrence 4: the practical starting point, roughly day 12–14

### LinkedIn

For a first experiment with Ontolog, I'd pick one reporting disagreement and three people who use the number.

Let each person explain their workflow independently. Ask for examples and exceptions. Read the definitions back, then compare what actually qualifies in each account.

The starting kit is deliberately small: an agent skill, Markdown with YAML front matter, record templates, and a validator. Obsidian works as an editor. Each contributor's agent can prepare reviewable changes to the same organizational repository.

It's MIT licensed. Your company's populated knowledge base stays under your own sharing rules.

The useful test: can a fourth colleague use the result to choose the right metric and explain what it counts?

Repository: {REPOSITORY_URL}

Background: {ARTICLE_URL}

### Twitter / X

Pick one reporting disagreement. Interview three people independently. Compare their definitions with actual examples.

Can a fourth person now choose the right metric?

That's the first pilot I'd run with Ontolog.

{REPOSITORY_URL}

## Additional angle: the semantic layer

Use this as an alternative follow-up, or after the four occurrences above if the discussion calls for it.

### LinkedIn

A semantic layer gives us governed metrics to query. An agent also needs to choose which one fits the decision someone is trying to make.

That means understanding the team's vocabulary, why a definition exists, where its limits are, and which disagreements are still unresolved. Some semantic-layer tools support more of that context already. The practical question I'm working on is how to elicit it from people and keep it reviewable.

Ontolog starts with interviews and attributed business knowledge. Where an executable metric already exists, the record should point to it. I'd rather avoid creating another independently maintained copy of the formula...

General analyst methods can live in companion skills. Company-specific interpretation caveats belong with the relevant organizational context.

I added that boundary to the write-up:

{ARTICLE_URL}

### Twitter / X

A governed metric tells an agent what it can query. Business context helps it choose and explain that metric.

I'm building an interview method for capturing that context, linked to existing semantic definitions.

{ARTICLE_URL}
