---
title: "When the AIs Disagree, I Pay Attention"
date: 2026-10-20
description: "I no longer read everything my AI agents produce. Models from different companies check each other's work, and I read where they disagree."
tags: ["ai", "technology", "systems", "leadership", "decision-making"]
series: []
ShowToc: true
TocOpen: false
draft: false
faq:
  - question: "What computer does John Schultz use for AI?"
    answer: "A used Lenovo ThinkCentre M70q Tiny with 32 GB of memory and a 2 TB drive, running Omarchy Linux. It has no graphics card, because the models run in the cloud."
  - question: "Should a different AI model check an AI's work?"
    answer: "Yes. A checker running on the same model shares its blind spots. I have a different model check routine work, and on high-stakes work I bring in a model from a different company, usually Codex."
  - question: "If you don't read everything your AI agents produce, what do you read?"
    answer: "Where the models disagree, where something failed, and the edge cases nobody's rules cover. Anything with my name on it, I still read in full before it goes out."
  - question: "How should someone just starting with AI begin?"
    answer: "Install the desktop app for Claude or ChatGPT, connect it to your own files, and use it on one real task you already do. Ten structured notes and one skill is still the right first step."
---

An auctioneer friend texted me this week. He wanted to know what computer I use for AI and what my tech stack is.

It's a fair question. A few weeks earlier I'd been on his podcast talking about running a lot of agents at once, and when somebody says that, you picture a server rack in the basement.

The computer is a used Lenovo ThinkCentre, the little office kind that sits under a monitor. I put more memory and a bigger drive in it. It doesn't have a graphics card, because the AI doesn't run on it. The models run in the cloud. The box holds my notes and a lot of terminal windows.

So the honest answer is that the computer doesn't matter much, and the stack matters less than most people think. Over the last seven months the gear changed some. My job changed more.

## What I got wrong in March

In March I wrote an essay called "[How I Actually Use AI](/essays/how-i-actually-use-ai/)." Most of it still holds. One line doesn't: "Every output gets read. Every draft gets reviewed."

That was true when I had one assistant and about 30 skills. The AI made a mistake, I caught it, the correction got written down, and the next draft came out a little better. I was the inspector, and the whole loop ran through me.

That loop doesn't scale. I now have a crew of agents working in parallel across a lot of windows, and most weeks I put more than 2 billion tokens (the chunks of text the models read and write) through Claude. Nobody reads 2 billion tokens. If I tried, every agent would sit waiting on me, and I'd be the slowest part of my own system.

So I stopped reading everything. What I read now is a much smaller pile, and a lot of my week goes into deciding what belongs in it.

## The firm

Grafe already works this way. Our catalogers write the lot descriptions for about 290 auctions a year, and I don't re-read every one. An AI compares each description to the photos, and when the photos show a real mistake, like a mistyped model number, it goes to the person who runs that team. That's how a good firm works. Associates do the work, someone more senior checks it, and the partner deals with what the check turns up.

So that's how I set up the agents. Some are junior associates doing the mechanical work. Some are senior associates doing the hard thinking. And every piece of real work gets checked by a different model than the one that made it.

That last rule came from a thought card I wrote in July, "[Same Mind, Same Blind Spots](/thoughts/same-mind-same-blind-spots/)." A checker running on the same model as the producer shares its blind spots, so all it can confirm is that the work agrees with itself. The fix was to always have a different model do the checking.

That turned out to be only the starting point. Inside Claude, I'd have one model, Fable, check another, Opus, and Fable kept catching things Opus missed. Then one day I asked Codex, OpenAI's model, to review work that Opus and Fable had already signed off on. It agreed with most of it and flagged new problems both Claude models had missed.

So now there are two levels of review. Routine work gets checked by a different model from the same company. When the stakes are high, I bring in a model from a different company, usually Codex. World class is coming from that teamwork. No single model gets there on its own, and neither did I when I was reading everything myself.

## 757 tests passed

Here's what that looks like on a real job. Every night, one of my agents reads a stack of public filings looking for sales leads. Last week it misread three of them. On one, the scan turned an 88 into a euro sign and an 8, and one line swallowed the dollar figure from the line below it.

The agents fixed all three. The fixes passed 757 automated tests. We replayed 15 past nights of filings through the new version, and nothing changed that shouldn't have. By every check I had, it was done.

Then I asked Codex to break it. Its job was to make up filings designed to break each new rule. In two rounds it found six real bugs. One was a rule written to trim a person's initials off the end of a company name, which would also have trimmed letters that belonged to the name.

The tests weren't wrong. They checked exactly what they were built to check. The problem is that tests confirm the cases the builder already imagined, and a model from another company, told to break the work, finds the ones the builder didn't. Two days later it happened again on a website change: Codex caught a bug the tests would have missed, before anything went live.

## I stop reading the agreements

So here's the pile. When models from different companies look at the same internal work and agree, I don't read it. Anything with my name on it, I still read in full before it goes out. What I do read is where the models disagree, where something failed, and the edge cases nobody's rules cover.

The partner's job changed shape. I write the standards the associates work from: how my writing should sound, what a good lot description looks like, the lessons from every past mistake. I decide how much review each piece of work gets, and whether it's routine or worth sending to another company's model.

The risk is that three models can agree and all be wrong. When that happens, it shows up later as a lead we missed or a number that doesn't add up, and that failure lands in my pile like any other.

## Where the attention goes

Who has bid on walk-in coolers more than once, within 300 miles of this sale?

Grafe has been selling equipment since 1959, and until this month we couldn't answer that question. We had the data: more than 750,000 lots and every bid placed on them. But a lot was mostly a title and some photos, and nothing tied a bidder to the kind of equipment they buy.

That's what I've been building with the attention I'm not spending on agreements. An AI is sorting our lots into the website's categories. This week it sorted the last three years, about 312,000 lots, for around $50. On our test set, 98% of the ones it was confident about were right. The bids landed in Google's BigQuery this week, so the cooler question is now a query.

What that buys is a real audience for every auction. A restaurant sale can reach people who have bid on restaurant equipment and live within driving distance, instead of everyone who ever bid on anything. We also get email to repeat buyers in that category, from a list we own, with no ad spend. And each pilot holds back 20% of the audience, so we compare bid rates from our own site instead of taking the ad platforms' word for what worked.

Not long ago, a project like this meant hiring a data team. Now the agents handle the plumbing, and my part is picking which questions to ask.

It isn't done. The pilots start in November, and the first real numbers come in early next year. I don't know yet what they'll show.

---

## Appendix: the setup, October 2026

This is what my friend actually asked for. It will be out of date in a few months, which is part of the point.

### The computer

- **Lenovo ThinkCentre M70q Tiny**, bought used. Intel i7-10700T processor.
- **Upgraded to 32 GB of memory and a 2 TB drive** (WD_BLACK SN7100). The memory helps with a lot of agents running at once. The drive is mostly for space.
- **No graphics card.** The models run in the cloud, so the box doesn't need one.
- **A MacBook Pro for the road.** It connects to the desktop over Tailscale, so the agents keep running at the office and I can reach them when I travel.

### The operating system

- **Omarchy** (omarchy.org), a setup of Arch Linux with a tiling window manager. Every window snaps into place, and I move between five and ten workspaces with the keyboard. It replaced Mac and Windows on my desk.

### Where I work

- **Ghostty**, a terminal, with **tmux** to keep sessions running. I work almost entirely at the command line now.
- **Claude Code** is my daily driver. I also run **Codex** (OpenAI) as the outside reviewer on high-stakes work, and keep **Grok Build** (xAI) and **Antigravity** (Google) installed for a second outside opinion.

### The notes

- **About 3,900 Markdown files** in one folder, synced through Dropbox and tracked in git. Most of my work since January has a note.
- **Obsidian is gone.** I view the notes in vault-wiki, a small local web app my agents built.
- **QMD**, a local search engine, indexes everything on the machine itself.
- **Nearly 70 skills** and **17 agent types**, each one a Markdown file that describes a workflow or a role. On a busy day several are running at once.

### If you're just starting

Skip all of this. Install the desktop app for Claude or ChatGPT, connect it to your own files, and use it on one real task you already do. Then read the "Getting Started" section of "[How I Actually Use AI](/essays/how-i-actually-use-ai/)." Ten structured notes and one skill is still the right first step.

## FAQ

**What computer does John Schultz use for AI?**

A used Lenovo ThinkCentre M70q Tiny with 32 GB of memory and a 2 TB drive, running Omarchy Linux. It has no graphics card, because the models run in the cloud.

**Should a different AI model check an AI's work?**

Yes. A checker running on the same model shares its blind spots. I have a different model check routine work, and on high-stakes work I bring in a model from a different company, usually Codex.

**If you don't read everything your AI agents produce, what do you read?**

Where the models disagree, where something failed, and the edge cases nobody's rules cover. Anything with my name on it, I still read in full before it goes out.

**How should someone just starting with AI begin?**

Install the desktop app for Claude or ChatGPT, connect it to your own files, and use it on one real task you already do. Ten structured notes and one skill is still the right first step.

Related: [How I Actually Use AI](/essays/how-i-actually-use-ai/), [Same Mind, Same Blind Spots](/thoughts/same-mind-same-blind-spots/)
