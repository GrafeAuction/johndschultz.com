---
title: "The Movie That Matches the Outcome"
date: 2026-03-16
description: "Four product design convictions from Dave Plummer: customization as a confession, dropping niche features, defaulting for the user, and slot machines as dynamic rendering."
tags: ["technology", "ai", "operations", "principles", "scaling"]
ShowToc: false
ShowReadingTime: true
draft: false
---

Dave Plummer is a retired Microsoft engineer. He created Windows Task Manager, ported Space Cadet Pinball to Windows, built the ZIP folder support, and wrote the Windows activation system for XP. He's been coding since the TRS-80 days. Dropped out of high school. Worked at 7-Eleven. Went back to school, cold-emailed his way into Microsoft from Saskatchewan, and stayed for years building tools that billions of people still use daily. He now runs a YouTube channel called Dave's Garage. Lex Fridman had him on [episode #479](https://lexfridman.com/dave-plummer-transcript/), and four things from their conversation stuck with me.

## The Customization Confession

Plummer and Lex were arguing about whether you should be able to move the Windows 11 taskbar. Lex was frustrated. He wanted customization, options, power user freedom. Plummer pushed back with an engineering argument first:

> "The freedom to put the Start menu on the left or the top or the right really increases the complexity of the code that renders the Start menu and lays out the tabs and does all the things, and now it's a much larger surface for bugs and it's a much larger piece of code to maintain." — Dave Plummer ([47:13](https://lexfridman.com/dave-plummer-transcript/#chapter7_start_menu_and_taskbar))

Then he dropped the Steve Jobs framing:

> "How do you respond to the Steve Jobs aspect of giving you customization implies that we couldn't figure out the right answer for you?" — Dave Plummer ([52:37](https://lexfridman.com/dave-plummer-transcript/#chapter7_start_menu_and_taskbar))

That line stopped me. I've been saying a version of this for a while without connecting it to Jobs. The mom test I use for our auction platform is the same instinct. If I need a settings panel, I haven't finished designing. If my mom can't figure out the workflow without calling someone, I didn't ship a product. I shipped a confession that I couldn't decide.

Plummer's practical framing helps too. He wasn't being philosophical about it. He was saying: somebody looked at a deadline and cut the four-position taskbar because they could ship four months sooner with one position. That's not lazy. That's a decision. And the Jobs line gives the decision a spine.

## The Niche Feature Discipline

Plummer asked the question plainly:

> "The question becomes at what point is it still worth it to satisfy the niche needs of a small set of users?" — Dave Plummer ([48:28](https://lexfridman.com/dave-plummer-transcript/#chapter7_start_menu_and_taskbar))

His answer, implied: usually, it isn't.

I push back on this regularly with our dev team. It's not just that solving for the 1% isn't worth the effort. It's that solving for the 1% actively creates friction for the 99%. Every edge case you accommodate adds a toggle, a conditional, a branch in the UI that the majority of users now have to navigate around. You're not just wasting time on a small audience. You're degrading the experience for everyone else.

But Lex made the counterargument, and it's worth sitting with:

> "If there's a guy or a girl in there who takes ownership of it, who has a passionate... For them, it's a thing that they take pride in over a period of time, they can by themselves in a short amount of time create something truly wonderful." — Lex Fridman ([51:06](https://lexfridman.com/dave-plummer-transcript/#chapter7_start_menu_and_taskbar))

He called it craftsmanship. He compared it to filmmakers who insert details only a small number of viewers will notice, and argued the reputation that builds over time pays off in ways that are hard to measure. Including hiring.

I think both are true. The line between them is whether the niche feature adds complexity the majority has to deal with, or whether it's invisible to them. A taskbar that works on all four edges adds code and bugs for everyone. An Easter egg in Pinball adds delight for the few and costs the many nothing. The discipline is knowing which one you're building.

The hard part isn't saying no upfront. It's dropping something you've already started building once you realize the audience is too small. By then you've invested time, you've started solving the problem, you've got momentum. Walking away from momentum takes more discipline than never starting.

Simplicity isn't a starting point. It's what's left after you've had the courage to cut.

## Recommended Settings for the User, Not for You

Plummer and Lex also got into Microsoft's "recommended settings" trick. You upgrade Windows, click through the wizard, and "use recommended settings" sounds like the right call. But it resets your default browser to Edge and opts you into things you didn't ask for.

> "You don't want your operating system to be an adversary. And sometimes Windows can feel adversarial. Like, it doesn't have your best interests at heart." — Dave Plummer ([1:14:10](https://lexfridman.com/dave-plummer-transcript/#chapter14_best_windows_version))

That conversation got me thinking about our own platform. Right now, a new bidder gets all notification settings turned off by default. That means a first-time bidder registers, wins nothing, and never knows she was outbid because she didn't find the settings page. Same mom test I apply to every screen on our platform. That's not respecting her preferences. That's punting on the decision.

What if we instituted recommended settings for a bidder's profile? Text alerts when outbid, email notifications for auctions closing soon, saved payment info. The things a reasonable bidder would want turned on. Not marketing emails, not data sharing. Just the stuff where the bidder would thank us for defaulting it on rather than resent us for it.

The Microsoft version fails because it serves Microsoft. The test for us is simple: does this default serve the bidder or serve us? If the answer is the bidder, turn it on. If it's us, leave it off and let them opt in.

The outcome we want, an engaged, informed bidder, is already determined. The settings are just the configuration that matches it.

## The Slot Machine Movie

This one came out of nowhere. Plummer plays slot machines. He knows they're a losing bet, but he likes the dopamine, the bright lights, the high contrast. Then he explained how they actually work.

> "Internally, there's basically a black box mechanism that does nothing more than generate the next random number and what the outcome is in terms of probability and payout. And then the game says, 'I've got to make up a movie to go along with that.' ... It's not spinning the reels, seeing where they land, and looking that up to see what you won. It's completely the other direction. It determines whether or not or if you won and then makes something up to fit that scenario." — Dave Plummer ([1:17:40](https://lexfridman.com/dave-plummer-transcript/#chapter15_slot_machines))

The spinning reels, the near-misses, the bonus animations. None of it determines anything. The outcome is already decided. The experience is theater built after the fact.

I've watched people play these things a hundred times. But I never thought about the architecture of it until Plummer said it that way.

And it immediately made me think about where websites are heading. The outcome is already determined: the business knows what it wants to serve this customer, or this AI agent, based on who they are and what they need. The page itself is just the movie assembled in real time to match. No static templates. No one-size-fits-all layout. The UI is constructed for that specific visitor in that specific moment. The slot machine is basically the model for AI-generated websites rendered on demand.
