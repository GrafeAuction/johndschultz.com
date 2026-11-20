---
title: "The 150-Mile Circle"
date: 2026-11-19
description: "What our auction records changed about where we advertise, which marketing tools we turned off, and where automated software stopped paying for itself."
tags: ["marketing", "auctions", "decision-making", "operations", "systems"]
ShowToc: true
TocOpen: false
draft: false
series: []
faq:
  - question: "Why didn't a single 150-mile radius work for every auction?"
    answer: "Different equipment pulls buyers from different distances. In our grocery auctions, everyday kitchen equipment mostly stayed inside 150 miles, while nearly two-thirds of the winning dollars on heavy commercial refrigeration systems came from farther away."
  - question: "Who sets the final price in an online auction?"
    answer: "On a lot with competing bids, second place sets the price, not the winner. Measuring price drive, the dollars each bid pushes a lot upward, showed us where runner-up bidders live and that roughly half the price-setting money comes from accounts opened within 30 days of a sale."
  - question: "Why did you turn off national past-bidder list ads?"
    answer: "Our own site tracking across eight auctions showed small past-bidder audiences maxing out quickly, hitting the same buyers 10 to 20 times, and zero first-time bidders connected to the list or similar-buyer campaigns even while ad platforms claimed thousands in credit."
  - question: "Why shelve automated tests and daily monitors after building them?"
    answer: "Automation has to earn its upkeep. At about 290 auctions a year, a clean split test of our geographic rule would take more than two years, and fresh code reviews kept turning up bugs in tools whose upside or read-only cadence didn't justify maintaining daily software. A quarterly manual check was the better fit."
---

For most of the last two years, whenever we launched a search campaign for an online auction, I defaulted to a 150-mile circle around the building.

Not because a study told me to, or because we had tested 150 against 250 and seen the results change. I picked 150 miles because it felt right. That's roughly a two-and-a-half-hour drive each way, far enough to pull in serious buyers with a trailer and close enough that we wouldn't burn ad money on people who'd never make the trip for a walk-in cooler or a run of shelving.

That default held up fine while nobody checked it. Auctions drew local bidders, equipment sold, and sellers got paid. We even wrote a version of the assumption into our own playbook: heavy commercial refrigeration stays local because it takes a crew and a semi to haul it out.

In October we got three years of our bidding history, buyer ZIP codes, and lot categories into one place and asked a plain question: where do the dollars come from?

## What traveled and what stayed home

The first thing we checked was grocery sales, more than 170 auctions over three years. Setting aside large bulk buyers who took a big share of a single sale, 150 miles held about two-thirds of the winning dollars across all grocery lots.

What we had backwards was which equipment traveled.

On heavy commercial refrigeration systems like compressor racks and condensers, the exact equipment we assumed stayed nearby, only about a third of the winning dollars came from inside 150 miles. Nearly two-thirds came from farther out. Everyday kitchen equipment like exhaust hoods, sinks, and stainless tables stayed close, with roughly four out of five dollars coming from inside 150 miles.

Once you see it, the reason makes sense. Nobody drives three states over for a stainless prep table when another one will show up locally next month. Specialty contractors and equipment dealers will send a crew across state lines for a late-model refrigeration rack system, because they follow the equipment wherever a store closes. Under the same roof, one lot had a local 150-mile market and the lot sitting twenty feet away had a regional or national one.

## Second place and new accounts

Geography was only half of what changed. The other half was who moves a price.

On a lot with competing bids in an online auction, the winner doesn't set the price. Second place does. If one buyer is willing to pay $10,000 for a machine and the runner-up stops at $4,000, with a $100 increment the lot closes at $4,100. The underbidder built the price. The winner just outlasted them.

When we mapped runner-up bidders on grocery lots, the same split showed up. On more than half of those heavy refrigeration lots, the runner-up lived more than 150 miles away.

We also started measuring price drive, the dollars each bid pushes a lot upward, and broke a year of auctions down by account age. Auction companies love talking about the size of their buyer database. We have more than 300,000 registered accounts, and repeat category bidders still carry about half our price drive. That makes it easy to treat the house list as the main event.

Across a full year of sales, accounts opened within 30 days of an auction carried roughly half the price drive. On our largest sales, that share climbed to about two-thirds. Across all lots, about half the price drive came from people with no earlier bid in our records, and on categorized lots, our two-year category lists could reach less than half of it. We still don't have signup-source tracking to see which channel brought those new accounts in, yet the ceiling on known lists is clear enough.

## What we built, and what we turned off

Once we saw those patterns, we started building.

We replaced the fixed 150-mile default with a rule based on each auction's equipment mix. It draws a tighter circle around the building when past winning dollars cluster nearby, or targets the specific states where past buyers came from when equipment pulls from farther out. Looking back across past sales, most landed on a group of states instead of a circle.

We also built category emails for past bidders and started testing two kinds of national ads built off those past-bidder lists: social ads aimed directly at people who had bid in that category before, and broader ads asking the ad platforms to find new buyers who looked like them.

In mid-November, right before turning those national list ads on for every sale by default, we checked our own website tracking across the eight auctions where we had complete data.

The evidence wasn't there. The direct past-bidder audiences were small enough that they maxed out quickly, showing the same ads to the same people 10 to 20 times while the ad platforms claimed thousands in credit our own site records couldn't find. The broader campaign meant to find similar new buyers spent $210 and tied back to $68 of price drive on our site while the platform claimed over $4,000. Across all eight tracked auctions, our own records couldn't connect a single first-time bidder to either type of ad.

That same day we turned both off by default and kept that budget inside our main auction campaigns. Our category emails don't have enough closed test sales yet to prove their own gain either, though sending an email to past buyers costs almost nothing compared with paying ad platforms for repeated views and credit we didn't trust.

## Where the tools stopped paying for themselves

Three quieter limits showed up around the same time.

First, past-sales math goes blind on anything new. On one contractor sale led by specialized equipment we had never sold before, we had no past pricing history for those machines. The targeting tool weighted the whole auction off the familiar trailers and generators on the lot sheet and recommended a regional circle. It couldn't see the main assets in the sale at all, so we had to plan a separate national search push by hand.

Second, wider geography has a real trade-off and an unproven payoff. Testing this circle-or-states rule against an earlier variable-radius rule across several hundred past sales raised the share of auctions covering most of our winners and runner-ups, while roughly doubling the share of the US population targeted. Better coverage on paper doesn't prove better results on the same budget. We had even run wide before, spending a full year advertising at 500 miles on most sales before tightening down to 150 miles. One analysis showed more distant bidders and winners in the 500-mile year, with no detectable change in the share of winning dollars from beyond 150 miles. When we paired similar auctions from the two periods, we couldn't detect a difference, with time period and sale mix tangled into the numbers.

Running a clean live split test of the new rule would take roughly 350 auctions on each side. Even at about 290 auctions a year across all 50 states and Puerto Rico, splitting our whole calendar down the middle would take more than two years to settle. We still kept the circle-or-states default because it doesn't add ad spend, we saw no clear sign of harm in the 500-mile year, and it lines our geography up with where buyers live in each category.

Third, automation has to earn its upkeep. After turning list ads off, we designed an automated test to see whether ads brought more of those distant past bidders back to bid, plus an automated daily monitor to watch the new geographic rule for large drops in distant winners or total proceeds. After building and simplifying both, fresh code reviews still turned up 25 issues in roughly 2,700 lines of list-test code and 19 more in the daily monitor.

On November 18 we shelved both automated jobs. For the list test, the potential upside was a handful of distant bidders per sale, list ads were already off, and our simpler email test could check whether those past buyers respond at all first. For the geographic monitor, a read-only check that moves no money wasn't worth maintaining automated daily software for. We kept the underlying analysis as a command we run by hand once a quarter, starting in February, to compare recent sales against our 150-mile baseline by eye.

## What's left for judgment

A lot of talk about using data in a business treats it as replacing gut feel with dashboards and automated tests. This fall didn't work out that cleanly. Putting our records in one place broke a few comfortable habits and stopped us from funding ads with no evidence behind them. It also showed us how quickly a piece of software can start costing more to maintain than the decision is worth.

What I keep wondering now is how many other 150-mile circles are sitting quietly inside our business. We caught this one only because we finally put the bidding records together and looked. In February I'll run that quarterly check by hand, and in the meantime I'm looking harder at the other round numbers we haven't checked yet.

## FAQ

### Why didn't a single 150-mile radius work for every auction?

Different equipment pulls buyers from different distances. In our grocery auctions, everyday kitchen equipment mostly stayed inside 150 miles, while nearly two-thirds of the winning dollars on heavy commercial refrigeration systems came from farther away.

### Who sets the final price in an online auction?

On a lot with competing bids, second place sets the price, not the winner. Measuring price drive, the dollars each bid pushes a lot upward, showed us where runner-up bidders live and that roughly half the price-setting money comes from accounts opened within 30 days of a sale.

### Why did you turn off national past-bidder list ads?

Our own site tracking across eight auctions showed small past-bidder audiences maxing out quickly, hitting the same buyers 10 to 20 times, and zero first-time bidders connected to the list or similar-buyer campaigns even while ad platforms claimed thousands in credit.

### Why shelve automated tests and daily monitors after building them?

Automation has to earn its upkeep. At about 290 auctions a year, a clean split test of our geographic rule would take more than two years, and fresh code reviews kept turning up bugs in tools whose upside or read-only cadence didn't justify maintaining daily software. A quarterly manual check was the better fit.

Related: [We Automated Our Entire Marketing Stack With a Single Skill](/essays/we-automated-our-entire-marketing-stack-with-a-single-skill/), [The Report That Covers You](/essays/the-report-that-covers-you/)
