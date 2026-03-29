---
title: "Memory Half-Life"
date: 2026-03-28
description: "Human memory decays by design, and that decay is a feature. Persistent memory systems miss this. A half-life model could bring the same advantage to AI memory without losing the safety nets."
tags: ["ai", "technology", "decision-making"]
ShowToc: false
ShowReadingTime: true
draft: false
---

## The Idea

This came up while fixing a bug where stale cached data was silently injecting garbage into every outbound email for a full day. The cache never questioned itself. It just kept serving bad data.

Human memory has a built-in half-life for each memory. The things you use stay strong. The things you don't fade. That's not a bug, it's what keeps the signal-to-noise ratio manageable. You naturally surface what's relevant because relevance reinforces the memory.

Persistent AI memory systems don't have that. Every memory sits at equal weight forever until someone manually prunes it. A project note from three months ago carries the same authority as one from this morning. That's a problem, because unbounded compounding memory can actually degrade performance over time. Stale context doesn't just take up space. It introduces contradictions, crowds out high-signal recent knowledge, and actively misleads.

The Ebbinghaus forgetting curve backs this up. Decay reduces cognitive noise and forces consolidation of what's actually important. Spaced repetition systems like Anki exploit this. They use the decay curve rather than fight it.

## The Design Question

What if memories had decay rates tied to both time and usage?

Not all memories decay the same way. Corrections ("don't do X") shouldn't decay at all. They're load-bearing regardless of how often they fire. But project context ("merge freeze for the mobile release") has a natural shelf life measured in days.

A rough model:

- Feedback memories: Near-infinite half-life. A correction that hasn't been needed in months is a success, not a signal to forget.
- User memories: Long half-life. Identity and preferences move slowly.
- Reference memories: Medium half-life. Systems change, links break, tools get replaced.
- Project memories: Short half-life. These are the ones that rot fastest and mislead most when stale.

## The Usage Dimension

Time alone isn't enough. A memory that keeps getting accessed is proving its value. One that hasn't been touched in 90 days is either stale or a safety net that hasn't been needed yet. The hard part is distinguishing those two.

The real advantage of human memory decay isn't forgetting. It's forcing re-derivation. When you half-remember something and have to re-check, you're validating it against current reality. Instead of binary present/absent, you get a confidence gradient: fresh memories get trusted, aging ones get verified before use.

## Consolidation as Sleep

The brain doesn't just decay passively. Sleep-based memory consolidation actively reviews and strengthens what matters. I've built a consolidation process into my own AI memory system that does a version of this: it reviews accumulated learnings, clusters by theme, and graduates confirmed patterns into durable memory. That's the consolidation step. The missing piece is the decay side. The automatic downweighting of what consolidation doesn't touch.

## The Bigger Pattern

Technology is the default. Human relationships must be actively defended. The same logic applies here: persistence is the default for digital memory. Relevance must be actively defended. Without decay, memory systems drift toward noise the same way organizations drift toward automation. Not because anyone chose it, but because no one built in the friction that keeps things honest.
