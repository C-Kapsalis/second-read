# Second Read planted-flaw benchmark: social, landing pages, blogs

Twenty-one pieces of marketing copy from fictional brands, seven per format.
In each format six carry 3-6 planted, objectively checkable flaws (those
marked **gate** should stop the piece going out) and two decoys (correct
details a careless reviewer flags); the seventh is a clean control. The ten
emails reuse email-benchmark.md. The case script is
cases/second-read-benchmark.py; it writes benchmarks/cases/sr-*.

Today's date for these cases is mid-October 2026; every date in the copy is
in the future unless a flaw says otherwise.

---

## sr-social-01: Northbeam Coffee, X launch post

Context: X (Twitter) post from the Northbeam Coffee brand account, a standard account without Premium. Casual consumer brand. Audience: existing followers, decision stage.
Prompt: Can you give this a second read before I post it on X? It's for our cold brew launch.
File: post.txt

```
Cold brew season is here ☀️ Our new Northbeam Nitro Cold Brew cans just landed: smooth, low-acid and ready in the fridge. It's the world's smoothest cold brew, full stop. Hurry, they're almost gone! A 12-pack is $24, and with code CHILL20 you get 20% off, so $19.20. Shop: https://northbeam.co/nitro #coffee #coldbrew #specialtycoffee #summervibes
```

| ID | Planted flaw | Check |
|---|---|---|
| 1.1 **gate** | Over X's 280-character limit for a standard account: 344 characters with the link counted as 23, so it cannot be posted as written | character count |
| 1.2 | Four hashtags against X's norm of 1-2 | hashtag count = 4 |
| 1.3 | Unsupported superlative: "the world's smoothest cold brew" | no source |
| 1.4 | Scarcity with no number, date or reason: "Hurry, they're almost gone!" (and the code has no end date) | no quantity or deadline |

Decoys: the emoji in a casual consumer post; the discount arithmetic ($24 with 20% off is $19.20, correct).

Facts: Northbeam Coffee; Northbeam Nitro Cold Brew cans; smooth, low-acid; 12-pack $24; code CHILL20; 20% off; $19.20; https://northbeam.co/nitro; claim "world's smoothest cold brew"; claim "almost gone".

## sr-social-02: Ledgerline, LinkedIn report launch

Context: LinkedIn post from Jonas Brandt, CEO of Ledgerline (accounting automation software). Audience: CFOs and finance leaders, consideration stage. Brand voice: competent, precise.
Prompt: Jonas wants to post this on LinkedIn tomorrow morning. Could you give it a second read and tighten it up?
File: post.txt

```
In today's ever-evolving landscape, finance leaders are being asked to do more with less. It's a challenge we think about every single day here at Ledgerline, and honestly, it's one we're passionate about solving. So this year we decided to delve deeper than ever before.

We're thrilled to announce the 2026 Close Benchmark, a game-changer for any finance team that wants to unlock a faster month-end. We surveyed 412 finance teams across Europe and North America.

What we found:
- Teams using automated reconciliations closed in 4 days on average, against 12 days for manual teams. That's 67% less time.
- Industry research shows 87% of CFOs say a slow close costs them deals.
- Only 1 in 5 teams has a documented close checklist.

I'll walk through the full results in a live session on Wednesday, 19 November 2026 at 16:00 CET. Grab your seat: ledgerline.com/benchmark-live

#Finance #CFO #Accounting #FinTech #MonthEnd #Automation #FutureOfWork #Leadership #SaaS
```

| ID | Planted flaw | Check |
|---|---|---|
| 2.1 **gate** | Weekday and date disagree: 19 November 2026 is a Thursday, not a Wednesday | calendar |
| 2.2 | The news (the benchmark) only starts after about 300 characters, past LinkedIn's "see more" cut of about 210; the opening is throat-clearing | position of "2026 Close Benchmark" |
| 2.3 | Template phrasing: "ever-evolving landscape", "delve", "thrilled to announce", "game-changer", "unlock" | phrase list |
| 2.4 | Unsourced statistic: "Industry research shows 87% of CFOs..." with no source, sample or date | no source |
| 2.5 | Nine hashtags against LinkedIn's norm of 3-5 | hashtag count = 9 |

Decoys: "4 days against 12 days" is "67% less time" (correct: 8/12); first-person voice from the named CEO.

Facts: Jonas Brandt, CEO, Ledgerline; 2026 Close Benchmark; 412 finance teams; Europe and North America; automated reconciliations 4 days vs manual 12 days; 67% less time; 87% of CFOs (unsourced); 1 in 5 teams have a documented close checklist; live session Wednesday 19 November 2026, 16:00 CET; ledgerline.com/benchmark-live.

## sr-social-03: Dewlight Skin, Instagram creator post

Context: Instagram caption by creator Juniper Hale (@juniperhale). This is a paid partnership: Dewlight Skin paid for the post and the code is an affiliate code. The paid-partnership label in the app is not switched on. Audience: her followers, UK.
Prompt: This is the caption from our creator partner for Thursday. Can you give it a second read before she posts it?
File: post.txt

```
Okay so you guys know I've been SO busy lately with the move and everything and honestly my skin has been paying for it 😩 between the stress and the new flat's dry air it's been a lot. Enter the Dewlight Barrier Balm. I've used it every night for two weeks and it cleared my eczema in 3 days. Like, actually gone. 🙌

Shop it at https://dewlightskin.com/balm and use my code JUNI15 for 15% off until 30 November, 23:59 GMT.

#skincare #skincareroutine #eczema #barrierrepair #selfcare #glowup #cleanbeauty #skintok #dryskin #nightroutine #skincarecommunity #ad
```

| ID | Planted flaw | Check |
|---|---|---|
| 3.1 **gate** | Paid partnership not disclosed up front: "#ad" is the last of 12 hashtags at the end, after the cut, and the label is off | position of "#ad" |
| 3.2 **gate** | Medical claim for a cosmetic: "it cleared my eczema in 3 days" | health claim |
| 3.3 | A URL in an Instagram caption is not clickable | URL in caption |
| 3.4 | The product is not named in the first 125 characters (the visible part); the opening is about the move | position of "Dewlight Barrier Balm" |

Decoys: the code is complete (JUNI15, 15% off, until 30 November 23:59 GMT); emojis in a creator's casual voice.

Facts: Juniper Hale; Dewlight Skin; Dewlight Barrier Balm; used every night for two weeks; "cleared my eczema in 3 days" (claim); https://dewlightskin.com/balm; code JUNI15; 15% off; until 30 November, 23:59 GMT; paid partnership (user).

## sr-social-04: Ironleaf Fitness, Facebook offer

Context: Facebook post from the Ironleaf Fitness page, a single gym in Manchester. Audience: local people, decision stage. Posting on 2 January.
Prompt: Quick one: can you give our January Facebook post a second read? Want it to get people through the door.
File: post.txt

```
Fresh start in January? 💪 Memberships at Ironleaf Fitness were £45/month, now just £30/month. That's 50% off! For a limited time only.

Comment YES and tag 3 friends who need a gym buddy!

Call us on 0161 555 0142, send us a DM, book through the Ironleaf app, or pop in to sign up.

No joining fee. Cancel anytime with 30 days' notice.

Ironleaf Fitness, 18 Mill Street, Manchester M4 2AB. Open 6am to 10pm, 7 days a week.
```

| ID | Planted flaw | Check |
|---|---|---|
| 4.1 **gate** | Wrong arithmetic: £45 to £30 is a third off (about 33%), not 50% | 15/45 |
| 4.2 | Engagement bait: "Comment YES and tag 3 friends" (Facebook demotes it) | phrase match |
| 4.3 | Vague deadline: "For a limited time only", no end date | no date |
| 4.4 | Four ways to act (call, DM, app, walk in) and no primary action or link | action count = 4 |

Decoys: the terms are clear ("No joining fee. Cancel anytime with 30 days' notice."); the address and opening hours.

Facts: Ironleaf Fitness; £45/month before; £30/month now; "50% off" (wrong); limited time; 0161 555 0142; DM; Ironleaf app; no joining fee; cancel anytime with 30 days' notice; 18 Mill Street, Manchester M4 2AB; open 6am to 10pm, 7 days a week.

## sr-social-05: Crumb & Copper, Instagram giveaway

Context: Instagram post from Crumb & Copper, an independent bakery in Hove. Brand voice guide: warm, neighbourly and gently funny (Sincerity personality, Caregiver archetype). Audience: local followers, retention and advocacy.
Prompt: Our giveaway goes up tomorrow. Can you give the caption a second read? I want it to feel like us.
File: post.txt

```
🎉 GIVEAWAY TIME 🎉 We're giving away a dozen sourdough loaves: one fresh loaf a week for 12 weeks, from our Hove bakery to your table.

To enter:
1. Follow @crumbandcopper
2. Like this post
3. Tag a friend who deserves good bread

Winner announced Friday 6 November! Don't be a loser, enter NOW or cry later 😈

#giveaway #competition #win #free #contest #bread #sourdough #bakery #hove #brighton #sussex #baking #breadlover #sourdoughbread #realbread #artisanbread #localbusiness #shoplocal #supportlocal #foodie #instafood #foodlover #eeeeeats #yum #carbs #breadmaking #homemade #brunch #breakfast #morning #weekend #treatyourself #giveawaytime #winning
```

| ID | Planted flaw | Check |
|---|---|---|
| 5.1 **gate** | Giveaway with no rules: no closing date and time for entries, no eligibility (age, area), no statement that Instagram does not sponsor or run it | missing rule elements |
| 5.2 **gate** | 34 hashtags, over Instagram's hard limit of 30, so the post fails as written | hashtag count = 34 |
| 5.3 | Off-voice line for a warm, neighbourly Caregiver brand: "Don't be a loser, enter NOW or cry later 😈" | quote vs voice guide |

Decoys: the prize is concrete (one fresh loaf a week for 12 weeks); the three numbered entry steps.

Facts: Crumb & Copper; Hove bakery; a dozen sourdough loaves; one loaf a week for 12 weeks; follow @crumbandcopper; like the post; tag a friend; winner announced Friday 6 November.

## sr-social-06: Sproutvest, Facebook investment post

Context: Facebook post from Sproutvest, a UK investing app. The product is a Stocks and Shares ISA (an investment, so returns are not guaranteed). Audience: UK adults, consideration stage.
Prompt: Can you give this a second read before I schedule it? Compliance is out this week so I'd love a sanity check.
File: post.txt

```
Hey everyone! Hope you're all having a great week and enjoying the autumn sunshine. We've got some exciting news to share with our community today, so read on!

Sproutvest now offers a Stocks and Shares ISA with guaranteed 8% returns every year and zero risk. Most high-street banks pay 0.1%, so why leave your money sitting there?

Rated 4.7 stars from 12,400 reviews on the App Store (October 2026).

Learn more: sproutvest.co.uk/isa | Download the app: sproutvest.co.uk/app | Book a call: sproutvest.co.uk/call

Capital at risk. The value of investments can go down as well as up. Sproutvest Ltd is authorised and regulated by the Financial Conduct Authority (FRN 912345).
```

| ID | Planted flaw | Check |
|---|---|---|
| 6.1 **gate** | "Guaranteed 8% returns every year and zero risk" on an investment product, contradicting the post's own "Capital at risk" line | claim vs risk warning |
| 6.2 | Unsourced comparison: "Most high-street banks pay 0.1%" with no source or date | no source |
| 6.3 | The product is not named in the first 125 characters; the opening is pleasantries | position of "Stocks and Shares ISA" |
| 6.4 | Three links competing and a vague "Learn more" label | link count = 3 |

Decoys: the risk warning and FCA line are required, not bloat; the App Store rating has a count, a source and a date.

Facts: Sproutvest; Stocks and Shares ISA; "guaranteed 8% returns every year and zero risk" (claim); "most high-street banks pay 0.1%" (claim); 4.7 stars from 12,400 reviews on the App Store (October 2026); sproutvest.co.uk/isa, /app, /call; Capital at risk; Sproutvest Ltd; FCA; FRN 912345.

## sr-social-07: Brightledger, LinkedIn control

Context: LinkedIn post from Rosa Lind, Head of Customer Success at Brightledger (bookkeeping software). Audience: small-business finance managers, consideration stage. Brand voice: competent, plain.
Prompt: Rosa asked me to check her LinkedIn post before it goes out this afternoon. Can you give it a second read?
File: post.txt

```
Our customers cut their month-end close from 9 days to 5 after switching on automated bank matching. That's the median across 38 teams in our 2026 customer review.

Three things the fastest teams did differently:
1. They matched bank lines daily, not at month-end.
2. They kept one shared close checklist.
3. They stopped chasing receipts by email and used the mobile upload.

I'll share the full review, with the checklist the fastest team uses, in a 30-minute session on Tuesday, 24 November 2026 at 15:00 GMT.

Save your seat: brightledger.com/close-review

#SmallBusiness #Bookkeeping #MonthEnd
```

Control: no planted flaws. Expected verdict "Ready to send" (at most two optional notes), never "Do not send".

Facts: Rosa Lind, Head of Customer Success, Brightledger; month-end close from 9 days to 5; automated bank matching; median across 38 teams; 2026 customer review; daily bank matching; one shared close checklist; mobile receipt upload; 30-minute session Tuesday 24 November 2026 at 15:00 GMT; brightledger.com/close-review.

---

## sr-landing-01: Pipewise, free trial page

Context: Landing page for paid search traffic. The Google Ads ad that sends visitors here reads: "Pipewise CRM: Free for 30 Days. No Credit Card Needed." Audience: sales managers at small companies, decision stage.
Prompt: Our new trial page goes live with the ads on Monday. Can you give it a second read? Conversion is all I care about.
File: landing-page.md

```
[Nav: Product | Solutions | Pricing | Customers | Resources | Blog | Log in]

# Welcome to the future of work

Pipewise brings your whole team together in one place.

## Why Pipewise?

Sales teams lose hours every week to spreadsheets, sticky notes and inboxes that never agree with each other. Deals slip because nobody knows who spoke to the customer last, and forecasts are built on guesswork. Pipewise was built by former sales managers who were tired of that chaos. Every deal, email and call sits in one shared pipeline, so your team always knows the next step, and you always know what will close this month.

## Features

- Pipeline board: drag deals between stages and see the value of each stage.
- Email sync: every customer email is logged against the right deal.
- Forecasts: see what will close this month based on deal stage.

## What our customers say

"This tool changed everything!" A happy customer

## Pricing

- Starter: $29 per user per month, or $290 per user per year (2 months free)
- Growth: $59 per user per month, or $590 per user per year (2 months free)

## Start your 14-day free trial

Form fields: First name, Last name, Work email, Phone, Company, Company size, Job title, Annual budget, Credit card number

[Button: Start free trial]

We never share your data. Read our privacy policy.
```

| ID | Planted flaw | Check |
|---|---|---|
| L1.1 **gate** | Message mismatch: the ad promises 30 days with no card; the page offers a 14-day trial and asks for a credit card | ad vs page |
| L1.2 | The H1 "Welcome to the future of work" does not say what Pipewise is or what the visitor gets | H1 text |
| L1.3 | Nine form fields for a trial, including phone, budget and card | field count = 9 |
| L1.4 | The only CTA is at the bottom, after about 220 words; nothing to act on in the first screen | CTA position |
| L1.5 | Anonymous, vague testimonial: "This tool changed everything!" A happy customer | no name or role |

Decoys: annual prices are 10x monthly, so "2 months free" is correct; the privacy note under the form.

Facts: Pipewise; ad: free for 30 days, no credit card; page: 14-day free trial; built by former sales managers; pipeline board; email sync; forecasts; testimonial "This tool changed everything!"; Starter $29 per user per month or $290 per year; Growth $59 per user per month or $590 per year; 2 months free; nine form fields listed; "We never share your data".

## sr-landing-02: Cobalt Ridge, ebook download page (HTML)

Context: HTML landing page for an ebook, meant to rank in search for "marketing attribution playbook" and to receive LinkedIn ad traffic. Audience: B2B marketing leaders, consideration stage. Visitors are in the UK and EU.
Prompt: Dev sent over the HTML for our playbook page. Can you give it a second read before we publish? SEO matters on this one too.
File: landing-page.html

```
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Cobalt Ridge Analytics | Free Download: The 2027 Attribution Playbook for Marketing Teams</title>
</head>
<body>
<header><a href="/"><img src="logo.svg"></a></header>
<main>
<h1>The 2027 Marketing Attribution Playbook</h1>
<h1>Stop guessing which channels drive revenue</h1>
<p>A 32-page guide for marketing leaders who have to explain where pipeline comes from. Based on our 2026 survey of 412 B2B marketing teams.</p>
<a href="#download" class="button">Get the playbook</a>
<img src="cover.png">
<h2>What's inside</h2>
<ul>
<li>How to choose between first-touch, last-touch and multi-touch models</li>
<li>A one-page template for reporting pipeline by channel</li>
<li>Five questions to ask before you trust a platform's attribution numbers</li>
</ul>
<h2>Get your copy</h2>
<form action="/subscribe" method="post">
<label>Name <input name="name" required></label>
<label>Work email <input type="email" name="email" required></label>
<label>Company <input name="company" required></label>
<label><input type="checkbox" name="marketing_optin" checked> Yes, send me marketing emails from Cobalt Ridge</label>
<button type="submit">Submit</button>
</form>
</main>
<footer><a href="/privacy">Privacy policy</a> · Cobalt Ridge Analytics Ltd</footer>
</body>
</html>
```

| ID | Planted flaw | Check |
|---|---|---|
| L2.1 **gate** | Marketing consent checkbox is pre-ticked (`checked`) for UK and EU visitors | `checked` attribute |
| L2.2 | Two H1 tags | H1 count = 2 |
| L2.3 | Title tag is 89 characters (over 60) and there is no meta description | title length; no meta description |
| L2.4 | CTA button "Submit" | button label |
| L2.5 | Images with no alt text (logo, cover) | `<img>` without alt |
| L2.6 | `href="#download"` points to an id that does not exist on the page (broken in-page link) | no `id="download"` |

Decoys: a 3-field form (name, work email, company) is right for an ebook; the survey figure has its source (our 2026 survey of 412 B2B marketing teams).

Facts: Cobalt Ridge Analytics (Ltd); The 2027 Marketing Attribution Playbook; 32-page guide; 2026 survey of 412 B2B marketing teams; three contents bullets (first-touch, last-touch and multi-touch models; one-page template for pipeline by channel; five questions before trusting platform attribution); form: name, work email, company; privacy policy link.

## sr-landing-03: Tidewell, product page

Context: E-commerce product page for the Tidewell Voyager Mug. Audience: shoppers arriving from an Instagram ad, decision stage. Today is 20 October 2026.
Prompt: Can you give our new mug page a second read? It goes live with the Instagram campaign this week.
File: landing-page.md

```
# Tidewell Voyager Mug: hot coffee from your first meeting to your last

Keeps drinks hot for 24 hours and cold for 24 hours.

$34 (was $42)

[Button: Add to cart: $39]

★ 4.8 out of 5 from 2,316 reviews

Today only! Sale ends at midnight.

## Why you'll love it

The Voyager has a double steel wall and a lid that seals with a quarter turn, so it survives a bag, a bike basket and a long commute. The handle fits four fingers, even in gloves.

## Specs

- Capacity: 470 ml
- Hot: up to 12 hours
- Cold: up to 24 hours
- Dishwasher-safe lid

## Shipping

[INSERT SHIPPING DETAILS]

## Our story

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

## Returns

Free returns within 30 days.

Offer valid until 31 December 2026.
```

| ID | Planted flaw | Check |
|---|---|---|
| L3.1 **gate** | Placeholder text left in: "[INSERT SHIPPING DETAILS]" and a "Lorem ipsum" story | placeholder strings |
| L3.2 **gate** | Two prices for the same mug: $34 in the hero, $39 on the button | price mismatch |
| L3.3 | Contradictory claim: hot for 24 hours in the hero, up to 12 hours in the specs | spec mismatch |
| L3.4 | Fake urgency: "Today only! Sale ends at midnight" contradicts "Offer valid until 31 December 2026" | date conflict |

Decoys: free returns within 30 days; the rating with its review count.

Facts: Tidewell Voyager Mug; hot 24 hours (hero) vs hot up to 12 hours (specs); cold 24 hours; $34 (was $42) vs $39 on button; 4.8 out of 5 from 2,316 reviews; double steel wall; quarter-turn lid; handle fits four fingers; 470 ml; dishwasher-safe lid; free returns within 30 days; offer valid until 31 December 2026; "today only".

## sr-landing-04: Signal & Noise Summit, event page

Context: Registration page for a marketing conference, in person in Lisbon with a live stream. Audience: marketing managers across Europe, decision stage.
Prompt: Registration opens next week. Can you give the event page a second read before we announce it?
File: landing-page.md

```
# Signal & Noise Summit 2027: two days of marketing measurement that works

Europe's #1 marketing conference returns to Lisbon on Thursday 10 March 2027.

[Button: Register] [Button: Become a sponsor] [Button: Download the agenda] [Button: Join our Slack community]

## Who it's for

Marketing managers and analysts who need to prove what their spend does. Twelve sessions, two workshops, no vendor pitches on the main stage.

## Tickets

Early bird pricing available. Group discounts for teams of 5 or more.

## Live stream

Can't travel? Every main-stage session is streamed live. The stream starts at 9:00 on both days.

## Venue

Centro de Congressos do Tejo, Rua das Gaivotas 14, 1200-205 Lisboa, Portugal.

## Refunds

Full refund until 30 days before the event. After that, you can transfer your ticket to a colleague at no cost.
```

| ID | Planted flaw | Check |
|---|---|---|
| L4.1 **gate** | Weekday and date disagree: 10 March 2027 is a Wednesday, not a Thursday | calendar |
| L4.2 | Live stream "starts at 9:00" with no time zone, for an audience across Europe | no time zone |
| L4.3 | "Early bird pricing available" with no price or deadline (no ticket price anywhere) | no price |
| L4.4 | Four CTAs to four goals in the hero (register, sponsor, agenda, Slack) | CTA count = 4 |
| L4.5 | Unsupported superlative: "Europe's #1 marketing conference" | no source |

Decoys: the venue address is complete; the refund policy is clear.

Facts: Signal & Noise Summit 2027; Lisbon; Thursday 10 March 2027 (weekday wrong); two days; twelve sessions; two workshops; no vendor pitches on the main stage; group discounts for teams of 5 or more; live stream starts 9:00 both days; Centro de Congressos do Tejo, Rua das Gaivotas 14, 1200-205 Lisboa, Portugal; full refund until 30 days before; free ticket transfer; claim "Europe's #1 marketing conference".

## sr-landing-05: Brightwell Dental, whitening page

Context: Service landing page for teeth whitening at a dental clinic in Leeds, meant to rank in search for "teeth whitening Leeds" and to receive Facebook ad traffic. URL: brightwelldental.co.uk/page?id=4471. Audience: adults in Leeds, consideration to decision.
Prompt: Could you give our whitening page a second read? We want more bookings from it and it should rank locally.
File: landing-page.md

```
# Smile!

Call us today on 0113 496 0721.

## Why choose Brightwell?

Our whitening treatment is 100% painless and gives permanent results, guaranteed. Our dentists have whitened thousands of smiles across Yorkshire, and we use the same gentle gel on every patient.

## The treatment

In-chair whitening takes about 90 minutes. Your dentist protects your gums, applies the gel in three short rounds, and checks the shade after each one. Most patients go back to work the same day.

## Price

In-chair whitening: £199, including a free take-home touch-up kit.

## Free consultation

Not sure whitening is right for you? Book a free consultation, with no obligation to go ahead.

[Button: Click here]

Brightwell Dental, 40 Park Row, Leeds LS1 5HD · 0113 496 0712 · Open Monday to Saturday, 8am to 6pm
```

| ID | Planted flaw | Check |
|---|---|---|
| L5.1 **gate** | Health claims: "100% painless", "permanent results, guaranteed" | health claim |
| L5.2 | Phone numbers disagree: 0113 496 0721 in the hero, 0113 496 0712 in the footer | number mismatch |
| L5.3 | H1 "Smile!" says neither the service, the offer nor the place, and lacks the target keyword; the price only appears far down | H1 text |
| L5.4 | CTA "Click here" | CTA label |
| L5.5 | URL slug "page?id=4471" carries no keyword | URL |

Decoys: the free consultation with no obligation; the opening hours.

Facts: Brightwell Dental; 40 Park Row, Leeds LS1 5HD; 0113 496 0721 (hero) vs 0113 496 0712 (footer); Monday to Saturday, 8am to 6pm; in-chair whitening about 90 minutes; three rounds; £199 including a free take-home touch-up kit; free consultation, no obligation; "thousands of smiles across Yorkshire" (claim); "100% painless", "permanent results, guaranteed" (claims).

## sr-landing-06: The Margin Note, newsletter sign-up page

Context: Sign-up page for a free newsletter for e-commerce operators. Traffic from podcast mentions and X. Audience: store owners, awareness stage.
Prompt: Can you give our newsletter sign-up page a second read? Sign-ups have been flat and I want to know what's off.
File: landing-page.md

```
# The Margin Note: the newsletter that helps store owners keep more of every sale

Join 50,000+ e-commerce operators who read it.

## Why we started

We started The Margin Note because we spent years running our own online store and kept making the same expensive mistakes: discounting when we should have raised prices, paying for ads that only reached people who would have bought anyway, and shipping orders that lost money once returns and payment fees came off. None of the newsletters we read talked about margin; they talked about traffic, followers and growth hacks. So we wrote the newsletter we wished we had, about the numbers that decide whether a store survives, explained by operators who have made those mistakes themselves, in plain English and without the hype that fills most of the e-commerce advice you will find online today.

## What our readers say

"The only newsletter I read the day it lands." Dee Okafor, founder, Fernhill Candles

Our 12,000 readers run stores of every size, from side projects to eight-figure brands.

## Subscribe

[Email field] [Button: Get the next issue]

Free. Unsubscribe in one click.
```

| ID | Planted flaw | Check |
|---|---|---|
| L6.1 **gate** | Reader count contradicts itself: "50,000+" in the hero, "12,000 readers" below | number mismatch |
| L6.2 | Never says how often it arrives or what an issue contains | no frequency |
| L6.3 | The sign-up form is only at the bottom, after about 180 words; nothing to act on in the first screen | form position |
| L6.4 | One paragraph of about 115 words (over 80) | paragraph word count |

Decoys: a single email field is right for a newsletter; "Free. Unsubscribe in one click."

Facts: The Margin Note; "50,000+ e-commerce operators" vs "12,000 readers"; founders ran their own online store; about margin; testimonial from Dee Okafor, founder, Fernhill Candles; stores from side projects to eight-figure brands; free; unsubscribe in one click; button "Get the next issue".

## sr-landing-07: Harbor Notes, control

Context: Landing page for a meeting-notes app, paid search traffic. The ad reads: "Harbor Notes: Meeting Notes That Write Themselves. Free 14-Day Trial." Audience: team leads, decision stage.
Prompt: Our trial page is ready to go live. Can you give it a second read before we switch the ads on?
File: landing-page.md

```
# Meeting notes that write themselves

Harbor Notes records your call, writes the summary and sends the action items to everyone who attended. Free for 14 days.

[Button: Start my free trial]

No credit card needed. Works with Zoom, Google Meet and Microsoft Teams.

"We stopped losing action items after the first week." Lena Ortiz, Engineering Manager, Quayside Labs

## How it works

1. Connect your calendar.
2. Harbor Notes joins the meetings you choose.
3. Within 5 minutes of the call ending, everyone gets the summary and their action items.

## Pricing

After the trial: $12 per user per month, billed monthly. Cancel anytime.

## Start your trial

Form fields: Work email, Password

[Button: Start my free trial]

We only use your email to run your account. Read our privacy policy.
```

Control: no planted flaws. Expected verdict "Ready to send" (at most two optional notes), never "Do not send".

Facts: Harbor Notes; records the call, writes the summary, sends action items to attendees; free for 14 days; no credit card needed; Zoom, Google Meet, Microsoft Teams; testimonial Lena Ortiz, Engineering Manager, Quayside Labs; summary within 5 minutes of the call ending; $12 per user per month billed monthly; cancel anytime; form: work email, password.

---

## sr-blog-01: Cartwheel Commerce, cart recovery post

Context: Blog post for an e-commerce platform's blog. Target keyword: "abandoned cart email". Audience: small online store owners, awareness stage. Draft excerpt (intro and first sections).
Prompt: Here's a blog draft from our freelancer. Can you give it a second read before I send it to the editor? We want it to rank.
File: draft.md

```
Title tag: The Ultimate Guide to Getting Back Customers Who Leave Without Buying
Meta description: Learn how to win back shoppers who leave items in their cart, with five simple steps any store can set up this week.
URL: cartwheel.com/blog/abandoned-cart-email

# The Ultimate Guide to Winning Back Lost Shoppers

In today's fast-paced digital landscape, online shopping has changed the way we live, work and buy. Consumers have more choice than ever before, and their attention is pulled in a hundred directions at once. Brands of every size are working harder than ever to stand out, to build loyalty, and to turn browsers into buyers. It is no surprise, then, that so many store owners feel overwhelmed. The good news is that there are proven ways to get more from the traffic you already have, and one of them is surprisingly simple.

Most shoppers who add something to their cart never check out. A reminder email, sent at the right moment, brings a share of them back. Here is how to set one up.

## Step 1: Send the first reminder within an hour

Timing matters more than anything else in a reminder. Emails with emojis in the subject line get 56% more opens, so add one to your first reminder. Name the items left in the cart and show a photo of each. Keep the email short, put one button near the top, and link straight back to the cart, not to your home page, because every extra click loses people who were already close to buying and the whole point of the email is to make finishing the order as easy as possible for someone who was nearly there, which means removing every step and every distraction between them and the checkout page, including your navigation menu, social links and any other offers you might be tempted to add.

## Step 2: Follow up the next day

If the first email does not bring them back, a second abandoned cart email 24 hours later can answer the question that stopped them: shipping cost, returns or sizing.

Want more guides like this? Join our newsletter for one practical tip a week.
```

| ID | Planted flaw | Check |
|---|---|---|
| B1.1 | Title tag is 69 characters (over 60) | character count |
| B1.2 | The target keyword "abandoned cart email" is missing from the title tag, the H1 and the first 100 words (it first appears in Step 2) | keyword position |
| B1.3 | Throat-clearing intro: about 95 words of generic scene-setting ("In today's fast-paced digital landscape") before the point | intro word count |
| B1.4 | Unsourced statistic: "Emails with emojis in the subject line get 56% more opens" | no source |
| B1.5 | A paragraph of about 125 words in Step 1, mostly one long sentence | paragraph word count |

Decoys: numbered steps as H2s; the soft newsletter CTA fits an awareness article.

Facts: Cartwheel (blog URL cartwheel.com/blog/abandoned-cart-email); five simple steps (meta); send the first reminder within an hour; "emails with emojis get 56% more opens" (unsourced); name the items and show a photo; one button near the top; link to the cart; second email 24 hours later; shipping cost, returns, sizing; newsletter: one practical tip a week.

## sr-blog-02: Fernhill Growth, CAC listicle

Context: Blog post on a growth agency's site. Target keyword: "lower customer acquisition cost". Audience: founders of small subscription businesses, awareness stage.
Prompt: Can you give this post a second read before it goes up on Thursday? I think it's close.
File: draft.md

```
Title tag: 7 Ways to Lower Customer Acquisition Cost
Meta description: Customer acquisition cost is the number that decides whether a subscription business grows profitably or burns cash, so in this guide we walk through seven practical, proven ways to lower customer acquisition cost this quarter without cutting growth.
URL: fernhillgrowth.com/blog/lower-customer-acquisition-cost

# 7 Ways to Lower Customer Acquisition Cost

Customer acquisition cost (CAC) is what you spend on sales and marketing to win one new customer. If you spent $12,000 last month and won 80 customers, your CAC is $150. Here is how to lower customer acquisition cost without slowing growth.

## 1. Fix the leak before you buy more traffic

Look at where trial users drop off. If half leave at the payment page, more ads will only buy more drop-offs.

## 2. Cut the channels that only look good

Judge each channel on paying customers, not clicks. See our guide to [reading channel reports](/blog/reading-channel-reports).

#### Watch your attribution window

A channel that claims every customer who saw an ad in the last 30 days will look better than it is.

## 3. Ask your best customers for referrals

Referred customers cost less to win because someone else did the convincing.

## 4. Raise prices for new customers

A higher price lifts what each customer is worth, which makes the same CAC easier to carry.

## 5. Shorten the trial

A shorter trial brings the decision forward. Read more in [how long a free trial should be](/blog/free-trial-length).

Ready to cut your CAC? Book a demo today, prices go up Friday!
```

| ID | Planted flaw | Check |
|---|---|---|
| B2.1 **gate** | The title promises 7 ways; the body has 5 | section count = 5 |
| B2.2 | Heading level skipped: an H4 ("Watch your attribution window") directly under an H2 | H2 to H4 |
| B2.3 | Meta description is about 250 characters (over 160) | character count |
| B2.4 | Hard sell and unexplained urgency in an awareness article: "Book a demo today, prices go up Friday!" | stage vs CTA |

Decoys: the CAC example is correct ($12,000 / 80 = $150); internal links with descriptive anchor text.

Facts: Fernhill Growth; CAC definition; $12,000 spend, 80 customers, CAC $150; half leave at the payment page (hypothetical); 30-day attribution window example; internal links /blog/reading-channel-reports and /blog/free-trial-length; "prices go up Friday" (claim).

## sr-blog-03: Larchmont Insights, survey article

Context: Data article on a research firm's blog, presenting its own survey. Target keyword: "checkout conversion rate". Audience: e-commerce managers, consideration stage.
Prompt: This is going out with our survey launch. Can you give it a second read? The numbers have to be bulletproof.
File: draft.md

```
Title tag: Checkout Conversion Rate: 2026 Survey Results
Meta description:
URL: larchmontinsights.com/blog/checkout-conversion-rate-2026

# What 1,200 Marketers Told Us About Checkout Conversion Rate

We surveyed 1,200 e-commerce marketers in August 2026 about what changed their checkout conversion rate this year. Here is what moved the number.

## Guest checkout made the biggest difference

Stores that added guest checkout saw their checkout conversion rate rise from 2.0% to 3.0%, a 33% increase. Among the 800 respondents who answered this question, 64% said guest checkout was the change they would make again.

## Abandonment is still the norm

Today, 61% of shoppers abandon a checkout because of unexpected shipping costs (Northgate Retail Report, 2017).

## Fewer fields, fewer drop-offs

In our survey, stores with five or fewer checkout fields reported a median checkout conversion rate of 3.4%, against 2.6% for stores with more than ten (Larchmont Checkout Survey, August 2026).

![Bar chart: median checkout conversion rate by number of checkout fields, 3.4% for five or fewer, 2.6% for more than ten](fields-chart.png)

Download the full report for every chart and the method.
```

| ID | Planted flaw | Check |
|---|---|---|
| B3.1 **gate** | Wrong percentage: 2.0% to 3.0% is a 50% increase, not 33% | (3.0 - 2.0) / 2.0 |
| B3.2 | Sample size given two ways: 1,200 surveyed vs "the 800 respondents" with no explanation that only 800 answered | count mismatch |
| B3.3 | A 2017 statistic presented as current ("Today, 61%...") | source year vs "today" |
| B3.4 | Meta description is empty | missing meta |

Decoys: the fields statistic carries its source and date; the chart has descriptive alt text.

Facts: Larchmont Insights; survey of 1,200 e-commerce marketers, August 2026; guest checkout: 2.0% to 3.0%; "33% increase" (wrong); 800 respondents; 64% would make the change again; 61% abandon because of unexpected shipping costs (Northgate Retail Report, 2017); five or fewer fields 3.4% vs more than ten fields 2.6% (Larchmont Checkout Survey, August 2026).

## sr-blog-04: Calmroot, supplement article

Context: Blog post on a supplement shop's site. The two product links are affiliate links that earn the site a commission. Target keyword: "ashwagandha for stress". Audience: adults interested in natural wellness, awareness stage. UK and US readers.
Prompt: Can you give this a second read? It's for our wellness blog and I want it live before the weekend.
File: draft.md

```
Title tag: Ashwagandha for Stress: What the Research Says
Meta description: What ashwagandha can and can't do for stress, what the research shows, and how to choose a supplement.
URL: calmroot.com/blog/ashwagandha-for-stress

# Ashwagandha for Stress: What the Research Says

Ashwagandha is everywhere right now, and ashwagandha for stress is one of the most searched wellness topics. Ashwagandha is a herb, and ashwagandha supplements come as capsules, powders and gummies. If you are wondering whether ashwagandha for stress works, ashwagandha has been studied more than most herbs, and ashwagandha cures anxiety for many people within weeks.

In a 2019 randomised trial of 60 adults published in the journal Medicine, people taking ashwagandha reported lower stress scores after eight weeks than people taking a placebo. It was a small study, and larger trials are still needed.

Ashwagandha is not right for everyone. If you are pregnant, take thyroid medication or have an autoimmune condition, talk to your doctor before taking ashwagandha.

Our two favourite ashwagandha supplements are the [Calmroot KSM-66 Capsules](https://calmroot.com/go/ksm66) and the [Stillwater Ashwagandha Gummies](https://calmroot.com/go/stillwater). Both use a standardised root extract and are tested by an independent lab.
```

| ID | Planted flaw | Check |
|---|---|---|
| B4.1 **gate** | Medical claim: "ashwagandha cures anxiety for many people within weeks" | health claim |
| B4.2 **gate** | Affiliate links with no disclosure | no disclosure text |
| B4.3 | Keyword stuffing: "ashwagandha" 7 times in the first paragraph of 56 words | keyword count |
| B4.4 | No H2 subheadings in the body | H2 count = 0 |

Decoys: the 2019 trial is described with its size, design and limits; the "talk to your doctor" safety line.

Facts: Calmroot; ashwagandha is a herb; capsules, powders, gummies; 2019 randomised trial, 60 adults, journal Medicine, lower stress scores after eight weeks vs placebo, small study; not for pregnancy, thyroid medication or autoimmune conditions without a doctor; Calmroot KSM-66 Capsules (calmroot.com/go/ksm66); Stillwater Ashwagandha Gummies (calmroot.com/go/stillwater); standardised root extract; tested by an independent lab; "cures anxiety" (claim).

## sr-blog-05: Quillford Advisory, thought-leadership post

Context: Blog post from a small marketing consultancy. Audience: owners of small local businesses (not marketers), awareness stage. Target keyword: "marketing measurement for small business".
Prompt: I wrote this one myself. Can you give it a second read before I publish it? Be honest.
File: draft.md

```
Title tag: Marketing Measurement for Small Business: Where to Start
Meta description: A plain guide to working out which of your marketing actually brings in customers, without expensive tools.
URL: quillford.com/blog/marketing-measurement-for-small-business

# Marketing Measurement for Small Business: Where to Start

Last spring a bakery owner asked me why her Instagram looked busy but her tills did not. It's important to note that her question is the one every small business owner eventually asks.

## Why measurement feels hard

As you navigate the ever-changing marketing landscape, it becomes increasingly clear that the sheer number of channels, tools and metrics available to a small business today makes it extremely difficult to delve into what is really working without spending a great deal of time and money on systems that were originally designed for much larger companies with dedicated teams. Most owners end up looking at likes and followers because those numbers are easy to find, even though they rarely connect to what ends up in the till at the end of the week.

## The tools the big companies use

Large brands combine a CDP with MMM and MTA to see which channels drive sales. You do not need any of that to start, and I will be honest: no method gives a perfect answer. See how one client did it in [link to case study]. TK: add the bakery's before and after numbers.

## Start with one question per channel
```

| ID | Planted flaw | Check |
|---|---|---|
| B5.1 **gate** | Unfinished draft: "[link to case study]", "TK: add the bakery's before and after numbers", and an empty final section | placeholder strings |
| B5.2 | Undefined acronyms for a non-marketer audience: CDP, MMM, MTA | acronym list |
| B5.3 | Template phrasing: "It's important to note", "navigate the ever-changing marketing landscape", "delve" | phrase list |
| B5.4 | A first sentence of about 64 words in "Why measurement feels hard" | sentence length |

Decoys: the first-person anecdote opening reaches the point in two sentences; the honest limitation ("no method gives a perfect answer").

Facts: Quillford (Advisory); a bakery owner asked last spring why her Instagram looked busy but her tills did not; owners look at likes and followers; large brands combine a CDP with MMM and MTA; no method gives a perfect answer; one client case study (no link or numbers yet).

## sr-blog-06: Pipewise, comparison post

Context: Comparison article on the Pipewise blog (Pipewise makes a CRM; Dealdesk is a competitor). Target keyword: "Pipewise vs Dealdesk". Audience: sales managers choosing a CRM, consideration to decision stage.
Prompt: Can you give our comparison post a second read? Sales wants to send it to prospects next week.
File: draft.md

```
Title tag: Pipewise vs Dealdesk: Which CRM Fits a Small Sales Team?
Meta description: An honest side-by-side of Pipewise and Dealdesk on price, setup time and integrations, for sales teams of 2 to 20.
URL: pipewise.com/blog/pipewise-vs-dealdesk

## Pipewise vs Dealdesk: an unbiased review

Choosing a CRM is a big decision, so this is an unbiased review for sales teams of 2 to 20.

## Price

Pipewise Starter costs $29 per user per month. Dealdesk costs $99 per user per month.

## Setup

Most Pipewise teams import their deals and start working on day one. Dealdesk usually needs a consultant.

## Integrations

| | Pipewise | Dealdesk |
|---|---|---|
| Native integrations | 120 | 300 |
| Email sync | Yes | Yes |
| Free trial | 30 days | 14 days |

Dealdesk has more integrations, so if you rely on niche tools, check its list first.

## Security

Dealdesk has a history of leaking customer data, so think twice before you trust it with your pipeline.

## Our verdict

For most small teams, Pipewise does what you need for less. Start a free trial and see for yourself.
```

| ID | Planted flaw | Check |
|---|---|---|
| B6.1 **gate** | Unsourced, damaging claim about a named competitor: "Dealdesk has a history of leaking customer data" | no source |
| B6.2 | Competitor price stated with no date or source ("Dealdesk costs $99 per user per month") | no source or date |
| B6.3 | Calls itself "an unbiased review" without saying it is written by Pipewise | no authorship disclosure |
| B6.4 | No H1: the page title is an H2 | H1 count = 0 |

Decoys: the table admits Dealdesk wins on integrations (300 vs 120); the "Start a free trial" CTA fits a decision-stage comparison.

Facts: Pipewise; Dealdesk; teams of 2 to 20; Pipewise Starter $29 per user per month; Dealdesk $99 per user per month (unsourced); Pipewise teams start on day one; Dealdesk usually needs a consultant (claim); integrations 120 vs 300; email sync both; free trial Pipewise 30 days, Dealdesk 14 days; "history of leaking customer data" (unsourced claim).

## sr-blog-07: Tallow & Twine, control

Context: Blog post on a candle-making supply shop's blog. Target keyword: "candle wick size". Audience: hobby candle makers, awareness stage.
Prompt: Can you give this how-to a second read before it goes live tomorrow?
File: draft.md

```
Title tag: Candle Wick Size: How to Choose the Right Wick
Meta description: Pick the right candle wick size for your jar in three steps, and fix tunnelling, soot and drowning flames.
URL: tallowandtwine.com/blog/candle-wick-size

# Candle Wick Size: How to Choose the Right Wick

The right candle wick size depends mostly on the diameter of your container. Measure it, match it to the wick chart for your wax, then test-burn one candle before you pour a batch.

## Step 1: Measure the inside of your jar

Measure across the top, inside the rim. A 7.5 cm jar needs a different wick from a 9 cm jar, even if they hold the same amount of wax.

## Step 2: Match the diameter to the wick chart

Every wick series has a chart that lists the diameter each size is made for. Start with the size the chart gives for your jar and wax. Our [wick sizing chart](/guides/wick-chart) covers every wick we sell.

## Step 3: Test-burn before you pour a batch

Burn one test candle for 3 hours. A full melt pool that reaches the edge without smoke means the size is right.

## Fix the three common problems

- **Tunnelling** (wax left on the sides): try one size up.
- **Soot or a tall flame:** try one size down.
- **The flame drowns:** try one size up, or a wick made for your wax type.

Next: read [how to choose a candle wax](/blog/choosing-candle-wax), or browse the [wick range](/collections/wicks).
```

Control: no planted flaws. Expected verdict "Ready to send" (at most two optional notes), never "Do not send".

Facts: Tallow & Twine; candle wick size depends on container diameter; measure inside the rim; 7.5 cm vs 9 cm jar example; wick chart (/guides/wick-chart); test-burn for 3 hours; full melt pool to the edge without smoke; tunnelling one size up; soot one size down; drowning one size up or a wick for your wax type; link /blog/choosing-candle-wax.
