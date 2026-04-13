---
title: "We Automated Our Entire Marketing Stack With a Single Skill"
date: 2026-04-12
description: "How one auction company replaced campaign-by-campaign marketing with a repeatable system."
tags: ["technology", "ai", "marketing", "operations"]
series: []
ShowToc: true
TocOpen: false
draft: false
---

Grafe Auction runs about 290 auctions a year across 48 states. Each campaign takes 10 to 14 days from start to finish. That's roughly one new marketing campaign going live every business day. Ad copy, search keywords, geographic targeting, photo selection, platform-specific formatting. Every time.

For years, each campaign started the same way: a blank page. Someone opens the lot catalog, scans through it, figures out what's worth highlighting, writes the ad copy, picks the photos, formats everything for Facebook and Google, selects the target markets. Then does it again tomorrow. And the day after that.

The work was good. It was also completely dependent on whoever was doing it. A different person, a different day, a different mood, and the output shifted. Not dramatically, but enough. Enough that quality was a function of who showed up, not what the system produced.

As our deal flow kept climbing, the math got simple: hire a marketing person or build a system. I chose the option that didn't need an interview process. The insight wasn't that the work could be automated. It was that the work already followed a pattern. We just hadn't named the pattern yet.

So we named it. Then we codified it. Then we built a single skill that runs the entire marketing pipeline. One command. Copy, photos, targeting, formatting. Here's what we learned building it.

---

## Start with the data, not the blank page

The old workflow started with a person reading a lot catalog and deciding what mattered. The new one starts with the catalog itself.

When a campaign kicks off, the system pulls the full lot catalog from our auction platform's API. Every lot, every title, every category. Then it does what a good marketing person would do if they had unlimited time: it reads every single listing, identifies the top-value items, breaks down the category mix, and builds a profile of who's going to bid on this stuff.

That analysis happens before anyone writes a word of copy.

Here's why that matters. A 300-lot manufacturing auction might be 40% CNC equipment, 25% welding, 20% material handling, and 15% office furniture. The copy should reflect that mix. The photo selection should reflect that mix. The geographic targeting should reflect that mix. When a person is scanning a catalog by hand, they're doing this intuitively. Sometimes they nail the proportions. Sometimes the first interesting item they see dominates the whole campaign because that's what caught their eye first.

The system doesn't have that bias. It reads everything, counts everything, and hands the analysis to the next phase as structured data. The creative work that follows starts from a complete picture, not a first impression.

The human still makes the calls. They just start somewhere better than a blank page and 300 lot titles they skimmed 20 minutes ago.

---

## Define quality as a measurement, not a feeling

"Does this ad copy look good?" is a question that gets a different answer depending on who you ask and what time of day it is. We replaced it with questions you can actually check.

Facebook primary text: 125 characters or fewer. Not approximately. Not "around 125." The system counts every character and rejects anything over the limit before a human ever sees it. Google Ads headlines: 30 characters max. Descriptions: 90. These aren't suggestions. They're hard ceilings enforced by the platforms, and they're enforced in our system before the copy leaves the pipeline.

Character counts are the easy example. The harder one is photo selection.

Picking marketing photos used to be entirely subjective. Someone would scroll through 60 images and pick the ones that "felt right." Which was fine until you compared Tuesday's picks to Thursday's picks from the same person. Now the system runs a two-pass review. First pass is triage: keep or skip, based on defined criteria. Storage unit backgrounds? Skip. Blue tape or lot stickers visible? Skip. Sideways orientation? Skip. Good lighting, real-world setting, recognizable brand? Keep.

Second pass ranks the keepers against a priority list: hero shot potential first, then visual punch, brand recognition, category diversity (does the photo selection represent the full breadth of the auction?), composition quality, and platform versatility (will it work as both a square and landscape crop?).

None of that is subjective once the criteria exist. It's a rubric. Two people applying the same rubric to the same photos will get closer to the same answer than two people following their gut. And when the rubric is wrong (which happens), you fix the rubric. The fix applies to every future campaign, not just the one where you noticed the problem.

Quality becomes a property of the system, not the operator.

---

## Build decision gates, not revision cycles

The most expensive mistake in a marketing pipeline isn't bad copy. It's bad copy you don't catch until the end.

Here's the old pattern: generate everything, present it all at once, get feedback, revise, present again, get more feedback, revise again. Each cycle burns time. The deeper the revision, the more time burned. And the later you catch a misalignment, the more work you throw away.

The skill has a steering check built into the middle of the pipeline. After the catalog analysis but before the expensive work (copy generation, photo selection), it pauses. It shows the auction theme, the top three highlights, and the category breakdown. Does this match what you know about this sale?

Thirty seconds. If the analysis is off (maybe the seller has a piece that isn't reflected in the lot titles, or a whole category that should be de-emphasized), the correction happens before any downstream work begins. One adjustment at the steering check saves three rounds of revision at the end.

This is a principle that applies well beyond marketing. Any pipeline where the expensive work comes later should have a cheap check up front. The cost of a 30-second pause is trivial. The cost of revising 50 search keywords, 15 ad headlines, 10 descriptions, and a full photo set because the theme was wrong from the start is not.

---

## Let the system carry the volume

A single campaign through this pipeline takes about 10 to 15 minutes. My active involvement is maybe 60 seconds: confirming the steering check and approving the final output. The rest is the system doing what I've already decided it should do.

That's the part that changes everything at 290 campaigns a year. Campaign quality holds steady, maybe more consistent. What changes is that the volume becomes sustainable without scaling the team.

Before the skill, marketing capacity was directly tied to headcount. More campaigns meant more people or more hours. Now it's tied to the system. The same person can run five campaigns in an afternoon because the decisions are encoded, the quality checks are automated, and the creative work is seeded with real data instead of starting from scratch.

And the system compounds. Every correction (a rubric tweak, a new skip criterion for photos, an updated character limit that a platform changed) improves every future campaign. A team of people making individual creative decisions doesn't compound that way. Each campaign starts over. Each person carries their own lessons. Institutional knowledge lives in people's heads instead of in the system.

The skill file is a markdown document. It describes the workflow in plain text. When the workflow changes, I edit the file. The next campaign uses the updated version. No deployment, no build step, no waiting for someone to push an update. It's a living document that gets better every time it runs because the corrections are structural, not personal.

---

## What actually changed

The copy didn't get dramatically more creative. The photos didn't become art. What changed is that campaign 290 is as good as campaign 1. On a Tuesday afternoon in November, under deadline, with three other auctions competing for attention, the output holds.

That's the thing about treating a creative process as an engineering problem. You don't lose the creativity. You just stop depending on it. The system provides the foundation (correct data, enforced limits, structured criteria), and the human provides the judgment that the system can't: is this the right theme, does this photo tell the right story, does this copy sound like us. The split is clean.

Most businesses running high-volume marketing haven't made this shift yet. The technology exists. Treating each campaign as unique just feels right. It feels like you're paying attention. But attention doesn't scale. Systems do.

If you're running 20 or 50 or 200 campaigns a year and each one starts with a blank page, the question isn't whether you can do it. You clearly can. The question is whether you should.
