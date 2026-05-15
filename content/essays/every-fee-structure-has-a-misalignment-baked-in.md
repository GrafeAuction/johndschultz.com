---
title: "Every fee structure has a misalignment baked in"
date: 2026-05-15
description: "Why no fee structure is self-policing, and how to design the override."
tags: ["principles", "strategy", "operations", "auctions", "incentives"]
series: []
ShowToc: true
TocOpen: false
draft: false
---

Two observations stacked on the same Friday morning.

The first one I've lived. Marketing agencies typically charge a percentage of marketing spend as their fee. The agency makes more money when the client spends more money. The incentive is to grow the budget, not the results. I've been quietly dismantling that arrangement in our vendor stack for the last couple of years.

The second one I heard this morning. Pavel Durov on the Lex Fridman Podcast (#482, Sept. 30, 2025), making the point that drug companies aren't actually incentivized to find the root-cause cure. They're incentivized for you to keep taking the drug. Recurring revenue. Maintenance, not resolution.

The two examples sat next to each other and a question formed. How many of your vendors are paid in a way that incentivizes them against you, and you haven't noticed?

I want to take this further than the easy version of the essay, because the easy version (incentives are everywhere, audit your vendors, Munger said something about this) doesn't actually help anyone. The harder version is that fixing the fee structure isn't enough. And when you do the audit honestly, it reaches you too.

## The fee structure is the strategy

That was my working theory for a while. Both of the marketing agencies we work with as advisors are now on a flat monthly fee, independent of our marketing spend. That move solved the original problem. They don't make more money when our ad budget grows, so the suggestion to "increase the Facebook spend" no longer comes wrapped in self-interest.

But here's what I didn't see at first. Flat fee creates the inverse problem. Once you're getting paid the same amount whether you answer the phone or ghost the client for three weeks, the rational move is to do the minimum to keep the contract alive. Different incentive, same structural issue.

What actually keeps those advisors productive isn't the flat fee. It's that I hold them accountable directly. I ask for the work. I challenge the recommendations. I expect responsiveness. The fee structure removed one misalignment, and accountability covers the new one.

The principle started forming there. Fee structures aren't self-policing. They never have been. The structure sets the default behavior, but the actual outcome depends on something outside the structure doing the work.

## The audit reaches you

Here's where it gets uncomfortable.

The auction industry runs on commission. We typically take a percentage of the sale, plus a buyer's premium. I've always thought of this as the most aligned fee structure in business. Seller wants the most money for the asset, auctioneer wants the most money for the asset, both parties pull the same direction. Clean.

When I audited it the way I'd audit someone else's industry, the alignment got messier.

There's a marginal effort cliff. Working harder to push a $500K auction to $550K nets the auctioneer maybe $5K at 10%. The seller cares about that last $50K. The auctioneer's incentive flattens at the top of the bidding band well before the seller's does.

There's the absolute-vs-reserve question. The auctioneer almost always prefers absolute, because it guarantees the sale closes and the commission gets paid. The seller might prefer reserve, because it protects against a bad day in the room.

There's the buyer's premium split. We're paid by both sides, which means when we're advising a seller on whether to accept an offer, we're not 100% on the seller's side. We're also thinking about the buyer who's coming back next month for a different auction.

And there's lot consolidation. On a 1,200-item industrial auction, the seller's interest is probably best served by cataloging each item individually. That maximizes search visibility, maximizes specificity, probably nets 10% more gross. Our operating reality says we consolidate similar items into bigger lots, drop the lot count to 300 or 400, and we tell the seller that item-level cataloging means higher non-commissioned setup fees.

That conversation is real. The seller does see the choice. But the architecture of the decision still reflects something the seller probably doesn't know. Setup typically runs 14 days before the auction. Payment comes 14 days after it concludes. Our crew's labor sits uncompensated for the better part of a month. Every day spent building item-level catalogs is a day they're not on the next project. Consolidation isn't preference. It's the model surviving itself.

## Misalignment is load-bearing

That last sentence is the part I want to defend.

The misalignment in the auction commission model isn't malice. It isn't greed. It's the way the business model actually works. If we cataloged every widget on every job, the float on uncompensated setup labor would break the business. The misalignment is what makes the model viable in the first place.

The same is true everywhere I look.

The marketing agency on a percentage of spend isn't evil. That's how they pay their account managers between client wins, and how they smooth revenue across an industry where contracts open and close on uneven cycles. Take away the spend-based fee and they have to charge retainers that most clients won't agree to.

Pharma's recurring-revenue incentive partly covers the cost of every drug that fails in trial. Most candidates never make it to market. The companies that get to a cure have to fund the ten that didn't. A pure cure-or-nothing pricing model would either price drugs out of reach or kill the development pipeline.

Lawyers billing hourly have a famous incentive to drag the work out. It's also how they price the case they can't predict the length of, and how they absorb the risk of the matter taking three times as long as either party expected.

Misalignment isn't always a flaw. Sometimes it's the load-bearing wall the building rests on. You can't just remove it.

There's a fine line between honoring the client and honoring the model. We walk it on every job. Drift is constant, and the default drift is away from the client.

Which means the only honest move is to design the override.

## The override

If the fee structure can't be self-policing, and the misalignment can't be removed, then the only thing left is whatever you put in place to override the misalignment when it matters.

Look at what's already there at Grafe and the pattern shows up. Transparency, because we surface the cataloging tradeoff to the seller in the form of a setup fee they can opt to pay. Accountability, because I'm the one keeping the advisor relationships productive. Repeat-business reputation, because every seller in the industry talks to every other seller, and bad outcomes travel.

None of those overrides are part of the fee structure. They're all things that sit on top of it.

Here's the part I owe myself the honest answer to. Are those overrides designed, or are they accidental? When we tell a seller the setup fee goes up with item-level cataloging, are we architecting a check on our own incentive, or are we just being fair dealers because that's how we'd want to be treated? The honest answer is mostly the second one. The overrides are real, but they're reflex, not architecture. They'd disappear the moment any of us got distracted, or the moment somebody with a different temperament ran the desk.

That's the gap. Reflex doesn't transfer. Reflex doesn't audit. Reflex doesn't survive a stressful quarter or a bad hire. If the overrides are the only thing keeping the structure honest, the overrides have to be designed, not assumed.

## The friction test

The sharper version of this came out of the pharma example.

The reason pharma's misalignment wins despite the FDA, despite malpractice law, despite the generic competition that eventually shows up, despite physician discretion, is that all of those overrides ask the patient to do harder work than swallowing a pill. The lifestyle change, the diet rework, the behavioral intervention. Each one is harder than the medication.

That's the real test for an override. Not "is it present?" but "is it easier than the default it's overriding?"

Run each of the Grafe overrides through it and they don't all hold up.

A flat-fee advisor relationship works as an override on the percentage-of-spend incentive, but only if the client actually engages and asks for the work. If the client is too busy to push, the flat fee turns into pure margin for the agency and the override stops doing anything.

A transparent setup fee works as an override on the lot consolidation incentive, but only if the seller knows what to ask for. If they don't know there's an item-level option in the first place, the transparency is theoretical.

Repeat-business reputation works, but only if the buyers and sellers actually talk to each other. In a fragmented market with no shared communication channel, the reputation override breaks down.

The presence of an override doesn't matter. The friction of the override relative to the default does.

## Trying to be a fair dealer

If I'm honest about what's actually keeping our fee structure aligned with our clients, it's that we're trying to be fair dealers. That's the override. Not the commission percentage, not the buyer's premium structure, not the line item on the setup fee. It's us, deciding case by case that the seller's interest should win the close calls.

That's a fragile system. It works while we're paying attention. It doesn't scale, it doesn't transfer to a new hire, and it doesn't survive a stressful month.

The principle the audit produced for me is this. Every fee structure has a misalignment baked in. The misalignment is usually load-bearing. The only thing that can override it is something built on top of the structure, designed deliberately, made easier than the default it's competing against. Reflex isn't enough. Good intentions aren't enough. The override has to be intentional, visible, and operationally cheaper than the misaligned path.

If that's true, the question every business owner should be asking isn't "how do I find the perfect fee structure?" That question doesn't have an answer. The right question is "what is the misalignment in my fee structure, what override am I depending on to correct it, and is that override actually easier than the default behavior the structure rewards?"

I owe myself a real audit of that. I suspect most of the overrides at Grafe are sitting in our heads as reflex, and we haven't done the work to design them into the operating system. The auction model is more aligned than the agency model. It's also less aligned than I've been telling myself.

The fee structure isn't the strategy. The override is.
