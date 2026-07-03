---
title: "Same Mind, Same Blind Spots"
date: 2026-07-03
description: "A validator running on the same model as the producer inherits the producer's blind spots. Independence of the checker matters more than intelligence of the checker."
tags: ["ai", "decision-making", "systems", "accountability"]
draft: false
ShowToc: false
ShowReadingTime: true
---

Today I rebuilt the routing rules for my AI agents: which model handles mechanical work, which handles hard reasoning, which validates the output before I see it. The setup looked rigorous. Every substantial piece of work got checked by a validator agent running at high effort on my most capable model.

The critique that stopped me: the validator was the same model as the thing it was checking. Same model, same characteristic errors. When the producer and the checker share a mind, the check confirms the work is consistent with itself. It can't see the errors that mind is inclined to make, because it's inclined to make them too.

The fix was cheap. Route my best model's work to a validator running on a different model, and route the smaller models' work to my best one. Nothing got smarter. If anything, the checker on my best model's work is the weaker model on paper.

We already know this about people. Nobody lets an appraiser certify his own appraisal, and auditors are external by law even though the in-house accountants aren't dumb; they're just inside the same assumptions. A second opinion from the doctor who made the first diagnosis is not a second opinion.

But watch how organizations actually review work. The person who wrote the plan presents the plan and fields the questions. The team that built the process audits the process. The review is real effort, honestly performed, and it's structurally blind anyway. My read is we spend on the intelligence of the reviewer when the leverage is in the independence.

The uncomfortable version: rereading my own email before sending is same-model validation. My tenth pass through my own proposal catches typos, not framing errors. The framing errors are load-bearing assumptions, and I'm the one who installed them. That's why my writing pipeline separates drafter from cold-reader, and why the strongest move on a high-stakes decision is two advisors who can't see each other's work. Agreement between independent minds is evidence. Agreement between copies of the same mind is an echo.

## Open questions

1. Where else does the producer grade his own work? In our auction business, setup checklists verified by the crew that did the setup is the obvious candidate.
2. Is there a cost threshold below which same-mind review is fine? Typo-level checking probably doesn't need independence; judgment-level checking always does.
3. Does this argue for keeping one deliberately different mind in every important loop (an outside reviewer, a contrarian in the room), even when the different mind is individually weaker?
