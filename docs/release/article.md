---
title: "The numbers disagree. Start with the definitions."
subtitle: "An interview-driven, open-source starting point for documenting what a business means, one contributor at a time."
slug: "start-with-the-definitions"
description: "Different teams can use the same KPI name and count different things. An interview-driven skill and knowledge repository help make those definitions explicit."
author: "Brice Luu"
status: "draft"
release_version: "0.1.0"
---

You get the data into the warehouse. You clean it up, build a few models, give people dashboards they can actually use. Things are moving.

Then someone puts two numbers next to each other.

Same business. Same month. Supposedly the same KPI. Different results.

I've seen this across client work, with different teams and different systems. You start by checking the queries, the refresh times, the filters. Sometimes you find a bug. Sometimes the data arrived late. And sometimes you eventually realize that the people asking for the number were counting different things all along.

The dashboards just made it visible.

On my last mission, I worked on a knowledge base for the data domain: the business concepts, the relationships between them, and the KPI definitions behind the terms people used. That got me thinking about how to make the construction of that knowledge base more systematic, and easier for people across the organization to contribute to.

I've put together a first version of that method as **Ontolog**: an agent interview skill and a matching knowledge repository template. Both MIT licensed.

Here's the reasoning behind it.

## The definition is hiding in the workflow

Take a simple example: an “active customer.”

For Product, that might be an account that logged in during the previous 30 days. For Finance, it might be a billing customer with a settled invoice in the calendar month.

A trial user can qualify for the first and fail the second. A paying customer who hasn't logged in can do the opposite. One person with several accounts adds another little surprise.

You can write perfectly valid queries for both definitions. Put the results under the same label, though, and now you have a recurring argument in your reporting meeting.

Even after everyone agrees on a sentence, there are details left. Does a refunded invoice count? Which timestamp matters? What happens to an event arriving three days late? Are we counting people, accounts, or contracts?

These details often live in someone's head, in a query, or in the explanation they give every time a new colleague joins. You can ask for a definition and get a reasonable answer. Follow an actual piece of work and you'll usually discover a few conditions that didn't make it into that answer.

That's where I want the interview to start.

## The semantic layer is part of the answer

If you work in data, this probably sounds familiar. Agreeing on metric definitions and making them consistent across tools is a big part of what we build a semantic layer for. [dbt's Semantic Layer](https://docs.getdbt.com/docs/use-dbt-semantic-layer/dbt-sl), for example, centralizes metric definitions and handles joins over the underlying models.

That gives an agent something useful to query. It should use those governed definitions when they apply, rather than quietly reconstructing the calculation from raw tables.

But consider what happens before it queries anything. Someone asks whether customer activity is healthy. The agent can find two approved measures, engagement and paying customers. Which one fits this decision? Why do they differ? What happened to the definition last quarter? Who can settle the exception the user just brought up?

The executable model is one part of that knowledge. There is also the reasoning behind the choices, the language used by different teams, the unresolved questions, and business processes that may never become a metric.

Semantic-layer tools can carry descriptions and increasingly support broader agent context too. [Cube explicitly describes this broader context](https://cube.dev/articles/ai-context-layer). The boundaries overlap. I'm interested in the practical work of getting that knowledge out of people's heads, checking it with them, and keeping its sources and scope attached.

Where a metric already exists in a semantic layer, the knowledge record should point to it. That tells us how the number is currently calculated. The approved business definition tells us what it is supposed to mean. If the business rule excludes refunded purchases but the deployed code still counts them, the implementation needs correcting. An interview can surface that mismatch for review, with evidence and examples attached.

Keep one maintained implementation of the calculation, and make discrepancies visible until they're resolved. Manually maintaining two independent copies of the formula would give us another reconciliation problem... we've got enough of those already.

## Ask people how their business works

The skill starts with a contributor's responsibilities and a concrete example. A decision they made. A report they investigated. A customer moving through a process.

From there, the agent asks about the terms they use, what qualifies, what doesn't, which events change a status, and what evidence supports the rules. One useful follow-up at a time. Nobody should need an ontology course to explain their job.

Say someone describes a customer becoming active after their first purchase. The follow-up could be about a purchase that gets refunded. Then about two accounts belonging to the same person. The useful questions depend on what they've actually said.

The agent turns that conversation into proposed concepts, relationships, business rules, and metric definitions. It reads the important parts back with examples, so the contributor can correct the interpretation.

Anything the agent inferred stays visibly proposed until it's checked. Anything the contributor doesn't know stays an open question.

There are established methods behind this. Ontology development gives us concepts, relationships, and “competency questions”: concrete questions the model should be able to answer. Vocabulary modeling helps distinguish a word from the thing it names, and map related concepts across teams. Provenance tells us who contributed a statement and where it came from.

The practical result should be something you can read, correct, and use. For example: “Can a customer be active without paying?” The knowledge base should either answer that for a stated context or show exactly what's still unresolved.

## Keep the perspectives attached

This part matters quite a bit to me.

Each contributor has a particular view of the business. Someone in support knows exceptions that never appear in the happy-path process diagram. Someone in Finance knows why a seemingly obvious calculation needs another condition. Someone in Product may be measuring a different stage of the same customer lifecycle.

I want those perspectives to remain available as we build the shared model.

So a contribution records who said it, the context it applies to, its evidence, and whether it has been confirmed or approved. Two teams can keep separate, explicitly named definitions when their purposes differ. A genuine contradiction in the same context becomes a question to resolve, with both accounts preserved.

The agent can help identify synonyms, narrower concepts, different time windows, or incompatible rules. The people responsible for the business decide which definitions become shared policy.

“Yes, that describes how I work” and “this is our approved reporting definition” are separate decisions. The repository keeps them separate too.

## There's analyst know-how around this too

A capable analyst also knows to check the grain before joining tables, investigate a sudden change before explaining it, and distinguish an immature cohort from one that is performing badly. An agent needs access to that kind of practice as well.

For this first version, I'm keeping the reusable analysis methods separate from the business interview skill. The repository focuses on understanding a particular organization. It doesn't currently package a general analyst playbook or a query-writing workflow.

Some of that knowledge is company-specific, though. “Our billing migration makes pre-June cohorts difficult to compare” belongs with the organization's context, with evidence and a scope. So does the business reason a refund changes a customer's status. A procedure for checking join multiplication can live in a companion analysis skill and refer to the relevant data models.

Those pieces should connect through explicit references. That leaves room for an analytics agent to use them together, while keeping the business knowledge useful to people and agents doing other work too.

## Give the conversation somewhere to land

Each person can use their own agent with the same interview skill. Their contributions go into a shared organizational repository through reviewable changes. The connection between agents is the knowledge they contribute, with its sources and context attached.

The repository is plain Markdown with structured metadata, readable in Obsidian or a text editor. Ontolog's eject command creates a clean company repository outside the public project. Your team keeps that instance private and controls who can contribute; the reusable method and template stay public. The setup guide covers the mechanics.

For a KPI, a record captures population, identity rules, qualifying events, exclusions, time boundaries, aggregation behavior, and worked examples. Before implementation, it can hold a proposed calculation contract. Once a governed implementation exists, it should link to that definition and make any unverified assumptions visible.

The included validator catches missing references and incomplete approval records. Checking whether the definitions are true and the examples make sense still takes business review.

An API or MCP interface can come later, once we have a better idea of which interactions need it. For now, I want to see whether people can contribute useful knowledge and recognize their own understanding in the result.

## Start with one disagreement

This is an early starter. The procedure and repository structure are in place; the interview method still needs a real multi-contributor pilot.

The first experiment I'd run is small: pick one recurring reporting disagreement, interview a few people independently, then compare their definitions with concrete cases. Ask another colleague to use the result to choose a metric and explain what it counts.

That should tell us quite a lot. Did we capture what people actually meant? Did we miss an exception? Did we force agreement where the difference was useful? Can someone find the answer without having to locate the one person who remembers why the query works that way?

The reusable skill and repository template are available under the MIT license: [Ontolog]({REPOSITORY_URL}). Your organization's populated knowledge base stays under your own access and sharing rules.

If you've spent time reconciling numbers across teams, I'd like to hear which definition keeps coming back to bite you. “Active customer” is only the beginning... ;-)
