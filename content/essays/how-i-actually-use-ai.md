---
title: "How I Actually Use AI"
date: 2026-03-03
description: "Paper index cards, 500 markdown files, and an AI that earns its seat every morning."
tags: ["technology", "ai", "principles"]
series: []
ShowToc: true
TocOpen: false
draft: false
---

Grafe Auction runs about 290 auctions a year across 48 states. Each campaign takes 10 to 14 days from start to finish. I'm the partner responsible for marketing, technology, and operations. That pace doesn't leave much room for a system that's clever but doesn't hold up under pressure. It also doesn't leave room for losing a thought from January that turns out to be the missing piece in February.

The personal knowledge management crowd has an orthodoxy right now: tools don't matter, just write. The AI crowd has its own: throw everything at the model and let it figure it out. Both are half right. Tools alone don't create insight. Models alone can't connect what they've never been given.

My answer is both. Rigid structure and an AI that earns its place through daily use. Right now that looks like about 500 markdown files in an Obsidian vault, 30 custom skills (codified workflows, not one-off prompts), and a stack of handwritten index cards on my desk. The markdown files are the memory. The skills are the muscle. The index cards are the net that catches what would otherwise vanish between the moment and the next time I sit down at a screen.

Here's how the pieces actually fit together. If you want the nuts and bolts instead of the philosophy, skip to the appendix at the end.

---

## The Four-Hour Call

I was driving to a state auctioneer conference, two speaking sessions scheduled for the next morning, when I called a close friend. He's been in the auction industry his whole life. We serve on a national board together. The call was supposed to be a quick check-in. It turned into four hours.

At some point we landed on something I'd been circling since September 2025. A thought card I'd written after listening to Jimmy Carr on the Modern Wisdom podcast: "If you're happy with you today you've got to be happy with everything that's happened to this point because this is what makes me today, me." I'd added a note underneath: "You truly need the downs. They create the full story."

My friend and I were working the same idea from a different angle. The valleys in life aren't just things you survive. They're what give the peaks their altitude. Without contrast, there's no height. If everything is a peak, nothing is a peak.

That last line came from another friend who runs a marketing company. He has a design principle I keep borrowing: if you emphasize everything, you emphasize nothing. It's a statement about contrast that keeps showing up in conversations that have nothing to do with design.

By the time I hung up, I realized I'd been circling this idea across six separate captures over five months. The Jimmy Carr quote from September. An essay about opening your epistemic filters from January. The Watchman Principle from Ezekiel (the obligation to speak what you see, regardless of whether anyone listens). An essay on understanding versus doing. Two more thought cards about silence and self-reflection. The vault surfaced the threads. The essay wrote itself because the pieces were already there, structured identically, cross-linked, and waiting for the conversation that would connect them.

That essay, "[The Valley and the Namer](/essays/the-valley-and-the-namer/)," wouldn't have existed without the vault. Its central argument (that suffering alone doesn't become wisdom, that you need someone to name what the valley built in you) only became visible because I could see six data points at once. No single capture told the story. The pattern across all six did.

Most people have moments like this. A conversation that sparks a connection to something they thought about months ago. But the earlier thought is gone. Buried in a notebook they'll never reread or an app that doesn't connect to anything. The insight dies in the gap between capture and connection.

Cross-linking is not magic. I build the Related Notes section in every vault file by hand or by running `/tag-notes`, a skill that scans for connections. The system can only connect what I took the time to capture and structure. Quality of connections equals discipline of inputs. Six mediocre captures, properly tagged and linked, produced a better essay than any single brilliant observation could have.

---

## Why Analog Stays in the Loop

Most of my thinking goes straight to digital. The vault is the primary workspace. But when I'm driving to a conference, walking out of a meeting, or mid-conversation at a seminar, the physical index card is the capture tool. A card and a pen are faster than any app when you need to catch a thought before it evaporates.

The Ivy Lee task cards (a hundred-year-old prioritization method) work the same way. Six tasks, physical card, forced prioritization. You can't cheat the space. But the card isn't always handwritten first. Sometimes it starts digital. The point is the constraint (six items, nothing more), not the medium.

When a physical card does get written, I photograph it and a companion markdown file preserves it in the vault, embedded image and all. The analog piece feeds the digital system. Not the other way around.

I keep hearing from the productivity crowd that handwriting is somehow more "real" or more retentive than typing. Maybe. I don't care about the neuroscience debate. I care about a practical problem: some of my best thinking happens when I'm away from a keyboard. The index card is a net, not a ritual. It catches thoughts that would otherwise be lost between the moment and the next time I sit down at a screen.

The constraint of the card is what makes the capture good. It's small and finite. It forces you to pick the right words because there isn't room for the wrong ones. A notes app with infinite scroll doesn't impose that discipline. The physical limit is a feature.

But the card is not where the thinking persists. The vault is. A thought card on my desk is just a card until I photograph it, transcribe it, tag it, and link it. Then it becomes part of the system, connectable to everything else. The "Digital Exhaust" card I wrote after a phone call with a friend sat on my desk for a day before it entered the vault and connected to a thought card from three weeks earlier. I wouldn't have seen that connection if the card had stayed on my desk.

The physical card started the capture. The digital system made the connection.

---

## Why the AI Is a Colleague, Not a Tool

Every morning starts with `/cockpit`. One command, six sections, about 30 seconds. Calendar, tasks, inbox, follow-ups, cooling contacts (relationships that need attention), and The Spark.

The Spark is where it gets interesting. It runs a semantic search across the vault, looking for theme clusters that span document types and time periods. One morning it connected a thought card about digital exhaust to a phone call about website analytics from two weeks earlier. I wouldn't have made that link on my own, but once I saw it, the essay practically outlined itself. The algorithm doesn't know what the connection means. It just surfaces patterns I might not see. Some mornings The Spark is noise. Some mornings it reframes my entire day.

Then there's the voice profile. I capture samples of my actual writing (emails, messages, notes I wrote by hand) and a skill called `/refine-voice` distills patterns from those samples. How I open sentences. Which words I actually use versus which ones I avoid. My cadence. When the AI drafts an email or reviews an essay, it references that profile.

The profile doesn't make the AI into me. It gets it close enough that I can spot the gaps.

Here's where the friction shows up. A friend read an email I'd drafted with the system and flagged a single word: "precedent." He said it sounded like AI. He was right. The sentence had passed every automated check: register scan, banned-phrase scan, the "would I say this out loud" test. But it still felt wrong to a human reader. I wouldn't say "there's precedent for it" in conversation. I'd say "it's been done before."

That correction became a learning via `/compound`, a skill that captures discrete insights from mistakes, corrections, and workarounds. Now `/review-content` includes register-shift detection that catches formal words where conversational ones belong. The friend caught it, the learning got captured, the system got better.

That's the loop. The AI makes a mistake. A human catches it. The system captures the correction. The next draft is slightly better. Over weeks and months, the gap between what the AI produces and what I'd actually say narrows. But it never closes completely, and that's the point.

The AI is a collaborator you catch and correct. Not a replacement you trust blindly. Every output gets read. Every draft gets reviewed. The system is designed for correction, not perfection.

I'm not interested in an AI that gets everything right. I'm interested in one that gets close enough that my corrections compound into something better than either of us could produce alone.

---

## Why Structure Beats Flexibility

Every file in the vault follows the same naming convention: `YYMMDD_type_description.ext`. Six-digit date, type prefix, descriptive slug, extension. Every phone call note starts with the date, type, and who I talked to before a single word of content hits the page. Every file. No exceptions.

Five tag categories: type (required), association, industry, topic, and knowledge base. A taxonomy that looks like overhead until you realize it's what makes the downstream tools possible. `/velocity` (which tracks relationship momentum), `/follow-ups` (which surfaces open action items), and The Spark algorithm in `/cockpit` all depend on clean, predictable data. Flexible naming would break every one of them.

This is the part that most knowledge management advice gets wrong. "Don't overthink your system" sounds wise until you try to build something on top of it. Flexibility in structure means inconsistency in data. Inconsistency in data means your tools can't trust what they're reading. And tools that can't trust the data produce results you can't trust either.

Here's a concrete example. I had a phone call with a friend about Google Analytics and website tracking. During the conversation, he used the phrase "digital exhaust" to describe the involuntary data trail everyone produces just by existing in 2026. I captured it as a thought card. Date, type prefix, descriptive slug, tags, the whole template.

When the card entered the vault, the system connected it to "[Opening the Filters](/essays/opening-the-filters/)," a thought card from three weeks earlier about epistemic filtering (what you don't see because your interpretation framework discards it). Digital exhaust is the inverse: what you broadcast because you have no filter at all. One is a failure of reception. The other is an absence of awareness about transmission. That connection only worked because both files were tagged, linked, and structured identically. If either one had been a loose note in a random folder with no metadata, the pattern would have stayed invisible.

The friction is real, though. I built on open-source tools specifically so I could diagnose problems when they happen. QMD, the local search engine that indexes the vault, has a function called `handelize()` that converts underscores to hyphens in file paths. A file named `260213_thoughts_digital_exhaust.md` becomes `260213-thoughts-digital-exhaust.md` in search results. If you don't convert back before reading the file, the read fails silently. The bug lives in `store.ts`, line 989. I found it because I could read the source code. That's only possible because everything is built on open formats: markdown files, git version control, tools I can inspect and modify.

Flexibility sounds nice until you try to build on it. Structure is the foundation for automation. When it breaks (and it will), open formats mean you can diagnose the problem instead of filing a support ticket and hoping someone gets back to you.

---

## Why You Build Skills Instead of Prompts

I do some AI consulting on the side. A benefit auctioneer bought a consulting package at a fundraiser. Before our second call, I ran `/brief`, which pulled her reference file, every prior interaction, open follow-ups, and relationship velocity into one view. She'd mentioned in Session 1 that she was hitting a wall with her current AI tools. I opened Session 2 with a workflow that addressed that specific frustration, without her having to re-explain it. My recommendations compounded instead of starting over.

That's the difference between a prompt and a skill. A prompt is a one-off request. A skill is a codified workflow with steps, edge cases, and integrations baked in.

`/respond` doesn't just draft a customer service reply. It runs a pre-draft checklist (recipient context, key facts, tone justification), checks captured learnings for prior patterns with similar customers, and passes the final draft through a three-pass voice compliance review: register-shift scan, "say it out loud" test, banned-phrase detection. All of that happens in a single command because I've already made the decisions about how a customer response should be built. The skill encodes those decisions so I don't re-make them every time.

`/cockpit` for mornings. `/velocity` for relationships. `/compound` for learnings. `/publish` for the website. `/follow-ups` for tracking commitments. `/tag-notes` for cross-linking. About 30 skills total, each one a markdown file that describes a workflow.

A skill is just a markdown file. It lives in a git repository, it's portable to any tool that reads text, and it's readable by anyone. When a skill needs to change (and they do, regularly), I edit the markdown. The next time the skill runs, it uses the updated version. No deployment, no build step, no waiting for an app update.

The value of a knowledge system isn't what it holds. It's the workflows you build on top. The 500 markdown files are the foundation. The skills make the data useful. And because it's all just text files and a version control system, I'm not locked into any single tool. If Claude disappears tomorrow, the vault, the skills, and the structure all survive. They're portable by design.

A prompt disappears after the conversation ends. A skill compounds every time it runs.

---

## What It Actually Changed

What actually changed isn't features. It's behavior:

I notice connections I wouldn't have noticed before. "The Valley and the Namer" came from six captures across five months. No single piece told the story. The vault held the threads until the right conversation pulled them together.

I show up with compound context. When my client and I sat down for Session 2, the conversation picked up where Session 1 left off because the system carried the context forward. Every meeting builds on the one before it. That's not a feature of the AI. It's a feature of structured data that the AI can read.

I catch the AI's mistakes, and the system gets better. The "precedent" catch from a friend became a captured learning that now runs in every content review. The QMD bug in `store.ts` is documented and worked around. Every failure has a trail, and every trail leads to a fix.

I write better because the voice profile keeps tightening. Each correction narrows the gap between what the AI drafts and what I'd actually say. The profile isn't finished. It won't ever be. That's the point.

I start mornings with everything that matters in one view. `/cockpit` isn't a dashboard for showing off. It's 30 seconds that reorient my day before the first phone call.

None of this is a finished system. It breaks in documented ways and gets fixed in documented ways. The auto-commit hook fires after every edit. The voice profile refines every few weeks. The skills evolve as workflows change. A skill I wrote two months ago has already been rewritten twice because I learned something about how the workflow actually plays out versus how I thought it would.

It's a working draft designed for correction, not perfection. That's not a limitation. That's the design. A system that can't be wrong can't get better.

The point isn't that the system thinks for me. The point is that it holds the thinking I've already done in a form where it can compound.

---

## Appendix: How to Build It

If the essay above is the philosophy, this is the wiring diagram.

### The Stack

Four tools. All open or inspectable.

Obsidian is the vault. It's a free markdown editor with wiki-links (`[[filename]]`) that create a graph of connections between files. Every link is bidirectional. If Note A links to Note B, both show the connection. The graph is useful, but the real value is the linking discipline it enforces.

Claude Code is the AI layer. It runs in the terminal, reads and writes files, and executes skills. It connects to my calendar, email, and local search engine through MCP (Model Context Protocol) integrations. It's not a chatbot. It's an agent that operates directly on the vault.

QMD is the local search engine. It indexes every markdown file and supports keyword matching, semantic search (meaning-based, finds related concepts even when the vocabulary differs), and deep search that auto-expands queries and reranks results. Runs locally. No data leaves the machine.

Git handles version control. An auto-commit hook fires after every file edit, so every change is tracked and the full history is recoverable.

### What a File Looks Like

Every note follows the same template. The metadata block at the top is what makes the downstream tools work.

```
# Phone Call — [Name]

**Date:** February 12, 2026
**Type:** Phone Call
**Description:** Call about website analytics and digital exhaust

---

[What was discussed. Key takeaways. Quotes worth keeping.]

---

## Related Notes

### Notes
- [[260213_thoughts_digital_exhaust]] — Thought card this call sparked

### References
- [[person_name]] — Contact reference

#phonecall #technology
```

The filename follows the same convention: `260212_phonecall_person_topic.md`. Date, type, description. The tags at the bottom feed the search engine. The Related Notes section creates the graph.

Thought cards are similar but include a Source field (who or what sparked the idea) and sections for the observation, the principle, and open questions. Reference files for people include role, company, background, and their own Related Notes linking to every note that mentions them.

### What a Skill Looks Like

A skill is a markdown file that lives in `.claude/skills/[name]/SKILL.md`. When I type `/cockpit` or `/brief` or `/compound`, Claude Code reads the corresponding file and executes the steps described in it.

Here's a simplified version of what a skill contains:

```
# Skill Name

[When to use this skill and what it produces]

## Steps

1. Read these specific files from the vault
2. Search for these patterns or connections
3. Check learnings/ for relevant prior mistakes
4. Build the output in this format
5. Present it for review

## Output Format

[What the result looks like]
```

That's it. A markdown file describing a workflow. No code, no deployment, no build step. When the workflow needs to change, I edit the markdown. The next run uses the updated version.

### The Morning Loop

`/cockpit` runs six checks in about 30 seconds:

1. Today's calendar, with context on each attendee pulled from their reference file (role, last interaction, open follow-ups)
2. Today's task card (how many of the six Ivy Lee items are done, which ones are aging)
3. Inbox radar, with threads sorted by priority (time-sensitive, needs response, can wait, informational)
4. Follow-up alerts for action items 7+ days old with no completion evidence
5. Cooling contacts (people I haven't interacted with in 60+ days)
6. The Spark: a semantic search that finds theme clusters spanning document types and time periods, looking for connections I haven't made yet

Sections 1 through 5 are operational. Section 6 is where the system earns its seat.

### Getting Started

You don't need 500 files to start. You need 10 structured ones and one skill.

Pick a naming convention and stick to it. `YYMMDD_type_description.md` works. Pick a tag taxonomy (even just five or six tags) and use it consistently. Create a folder for notes and a folder for references. Start capturing phone calls, meetings, and ideas using the same template every time.

The first skill should be whatever you do every morning. Mine was a simpler version of `/cockpit` that just read my task card and calendar. It grew from there.

The structure comes first. The AI comes second. If your files aren't consistently named, tagged, and linked, the AI has nothing useful to work with. Garbage in, garbage out applies to knowledge systems the same way it applies to everything else.

Start small, stay rigid, and let the connections accumulate.
