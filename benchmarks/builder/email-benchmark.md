# email-score planted-flaw benchmark

Ten realistic marketing emails from fictional brands. Nine carry 4-6 planted,
objectively checkable flaws; one is a clean control. Each email also carries
1-2 decoys: aspects a careless reviewer flags but the framework rates as fine.
The grading key under each email is the answer sheet.

## What it measures

| Metric | Definition | Pass bar (Haiku) |
|---|---|---|
| Flaw recall | Planted flaws named anywhere in the output (fix list or scorecard), with the quote or number that proves them | 80% or more |
| Gate recall | Flaws marked **gate** that appear in the top fixes and push the verdict to "Do not send" | 90% or more |
| Fix precision | Share of the 3-5 ranked fixes that map to a planted flaw (or, for the control, to a real issue a grader accepts) | 75% or more |
| Decoy false positives | Decoys flagged as a problem in the fixes or scored 2 or lower for that reason | 10% or less |
| Rewrite repair | Planted flaws within the ranked fixes that are gone in the rewrite | 85% or more |
| Rewrite fabrication | Rewrites that add a price, date, statistic, review, name, address or claim not in the original and not a bracketed placeholder | 0 |
| Score ordering | Control scores higher than every flawed email; control is not "Do not send" | must hold |
| Goal question | Emails 5 and 6 (offer missing) produce a question to the marketer or a bracketed placeholder for the offer, never an invented amount | must hold |

## How to run

1. Feed each email to the skill exactly as written in the "Input" block,
   with the context line as the user's message ("Score this email. Context:
   ..."). Run each email 3 times; report the mean.
2. Grade each planted flaw as **hit** when the output identifies the same
   problem on the listed dimension or an adjacent one, with evidence. Wording
   does not need to match. "Subject too long" without the count is a hit;
   "subject could be punchier" is not.
3. Deterministic graders can check: character and word counts quoted, raw
   token strings, the verdict line, placeholders in the rewrite, and the
   presence of each decoy phrase in the fix list. Use an LLM judge with this
   key for the rest.
4. A flaw the skill reports as "not visible, confirm" counts as a miss when
   the element is in the input.

---

## Email 1: Larkspur & Vine, flash sale

Context: Promotional. Audience: Value Seeker. Rendered test send.

```
From: Larkspur & Vine <hello@larkspurandvine.com>
Subject: FREE SHIPPING + 40% OFF EVERYTHING!!! Act now, these deals will NOT last long
Preheader: View this email in your browser

Hi Jordan,

Our biggest sale of the season is here. Take 40% off everything sitewide,
plus free shipping on every order.

Linen Wrap Dress: $77.40 (was $129)
Everyday Wide-Leg Trouser: $53.40 (was $89)
Woven Market Tote: $35.40 (was $59)

Hurry, the sale ends soon and sizes are going fast.

[Button: Click here]

You are receiving this because you signed up at larkspurandvine.com.
Unsubscribe | Privacy policy
© 2026 Larkspur & Vine
```

| ID | Planted flaw | Dimension | Objective check |
|---|---|---|---|
| 1.1 | Subject is 77 characters, truncated on phones | 18, 1 | len(subject) = 77 > 60 |
| 1.2 | Spam signals: 5 ALL CAPS words, "!!!", "FREE", "Act now" | 20, 1 | regex for caps words, `!!`, trigger list |
| 1.3 | Default preheader "View this email in your browser" | 1 | exact default string |
| 1.4 | No end date or time zone: "ends soon"; unsupported scarcity "sizes are going fast" | 9, 3, 14 | no date in body |
| 1.5 | CTA "Click here" | 8, 16 | CTA label in vague list |
| 1.6 | No physical postal address in footer | 15, 6, 20 | no address in footer |

Decoys: **D1.a** the discounted prices are exactly 60% of the originals
(correct; do not flag as wrong prices). **D1.b** sender name matches the brand
in the body.

## Email 2: Tallyhawk, B2B webinar invite

Context: Promotional (event invite). Audience: B2B finance leaders. Rendered
test send, scheduled Tuesday 10:00 recipient local time.

```
From: Dana Whitfield, Head of Finance Ops at Tallyhawk <dana@tallyhawk.io>
Subject: Webinar: close the month in 3 days, not 10
Preheader: Two controllers show how they cut their close by 70%. Live on Thursday, 12 November.

Hi {{first_name}},

In today's fast-paced world, finance teams are under more pressure than ever.
That's why we're thrilled to invite you to an exclusive webinar that will
unlock a seamless month-end close and elevate your team's productivity. It's
a true game-changer.

On Thursday, 12 November at 4 PM, two controllers from mid-size companies
will show how they cut their close from 10 days to 3 with automated
reconciliations. You'll leave with their checklist and a template you can
use the same week.

[Button: Register now]
[Button: Download our 2026 Close Benchmark ebook]
[Button: Book a 1:1 demo]
[Link: Follow us on LinkedIn]

Tallyhawk Inc., 410 Harbor Street, Suite 900, Boston, MA 02110
Unsubscribe | Manage preferences
```

| ID | Planted flaw | Dimension | Objective check |
|---|---|---|---|
| 2.1 **gate** | Raw merge token in the greeting: "Hi {{first_name}}," | 13, 6 | literal `{{first_name}}` in rendered copy |
| 2.2 | Template phrasing: "In today's fast-paced world", "thrilled", "unlock", "seamless", "elevate", "game-changer" | 4 | phrase list match (6 hits) |
| 2.3 | Four CTAs to four different goals (register, ebook, demo, LinkedIn) | 16, 8, 5 | count of distinct CTA goals = 4 > 3 |
| 2.4 | "4 PM" with no time zone for a remote webinar | 9 | time with no zone |

Decoys: **D2.a** send time Tuesday 10:00 local is right for B2B.
**D2.b** personal sender with a relevant role (an authority signal, +0.3).
Also correct: 12 November 2026 is a Thursday, and 10 to 3 days is 70%.

## Email 3: Ember Grind, cart reminder

Context: Promotional (cart reminder) to shoppers who left items in the cart.
Audience: Impulse Buyer. Cart data is available to the sender (Ember Burr
Grinder Pro; 2 x Single-Origin Ethiopia 250g).

```
From: Ember Grind <orders@embergrind.com>
Subject: Your order has shipped
Preheader: Plus 10% off your next favourite brew.

Hi Chris,

Ember Grind started in 2014 in a garage in Leeds, when our two founders,
Tom and Aisha, got tired of coffee that tasted of nothing. They bought a
second-hand roaster, burnt their first forty batches, and slowly learned how
heat, time and airflow shape every bean. Today we roast six days a week in
small batches, and every bag is stamped with its roast date so you know
exactly how fresh it is.

We buy most of our beans directly from farms we have visited, in Ethiopia,
Colombia, Guatemala and Rwanda. Paying above the market price is not
charity; it is how we make sure the same growers can keep producing the
coffee we love, year after year, and it is why our relationships with them
now go back more than a decade in some cases.

Our grinders are built the same way. We spent two years testing burr shapes
before launching the Ember Burr Grinder, because grind consistency matters
more to flavour than almost anything else you can control at home. Uneven
grounds extract unevenly, which means bitter and sour notes in the same cup.
A good burr set fixes that, and it lasts for years.

We also care about what happens after you finish your coffee. Our bags are
fully compostable, our shipping boxes are made from recycled card, and we
offset the carbon from every delivery through a reforestation partner in
Uganda. We publish an impact report every spring so you can see the numbers
for yourself.

By the way, it looks like you left some items in your cart. They are still
waiting for you, but we cannot hold them forever. Use code EMBER10 for 10%
off your order, valid until Sunday 23:59 CET.

Complete your order here: https://bit.ly/3xEmbr

Ember Grind Ltd, Unit 4, Canal Works, Leeds LS1 4BR, United Kingdom
Unsubscribe | Privacy
```

| ID | Planted flaw | Dimension | Objective check |
|---|---|---|---|
| 3.1 **gate** | Subject "Your order has shipped" misdescribes a cart reminder | 20, 2 | no order shipped; body is a cart reminder |
| 3.2 | About 310 words against a 75-150 cart-reminder budget (twice the ceiling); the only CTA comes after ~290 words, far below the first screen | 12, 18, 16 | word count; position of the first link |
| 3.3 | Shortened URL (bit.ly) as the only link | 20 | `bit.ly` string |
| 3.4 | Cart items never named ("some items") although cart data exists | 13 | no product name from the cart in the reminder paragraph |
| 3.5 | No button: the only CTA is a bare link with "Complete your order here" text | 8, 16, 5 | no button element |

Decoys: **D3.a** the discount has a clear code, amount and expiry with time
zone (EMBER10, 10%, Sunday 23:59 CET). **D3.b** the footer is complete
(address and unsubscribe).

## Email 4: Stridewell, weekly running newsletter

Context: Newsletter. Audience: Loyal Buyer (club members). Previous sends came
from "Coach Mia at Stridewell".

```
From: noreply@mail-sw-news.com
Subject: Stridewell Weekly: hill repeats and a race-day checklist
Preheader: Stridewell Weekly: hill repeats and a race-day checklist

[IMAGE: hero.jpg, no alt text. The image contains the headline "Spring Half
Marathon: registration closes Friday" and the only "Register" button.]

Hill repeats, done properly

Hill repeats are the cheapest speed work you can do, and most runners do
them wrong. The mistake is treating the hill as a sprint: you charge up the
first two reps, your form falls apart by the fourth, and the session turns
into a grind that builds fatigue rather than strength. Instead, pick a hill
that takes 60 to 90 seconds to climb at a hard but controlled effort, keep
your cadence quick and your stride short, drive your arms, and jog back down
slowly enough that you start every rep feeling ready. Six to eight reps is
plenty for most of you. Run the last rep at the same pace as the first, and
if you cannot, the session was too long or too fast. Do this once a week for
six weeks and you will feel it on every climb in the half.
[Read the full post]

Three new routes for spring

We mapped three new routes this month. The Riverside Loop is a flat 8 km
with a water fountain at the halfway bridge. The Quarry Hill Out-and-Back is
12 km with 180 m of climbing, ideal for the hill session above. The Old
Railway Path is a soft, traffic-free 15 km for your long run.
[Read the full post]

Your race-day checklist

Pin your number the night before. Lay out your kit, including the socks you
have actually trained in. Eat the breakfast you have practised, three hours
before the start. Arrive 45 minutes early, warm up for ten minutes, and
start slower than you want to. Most personal bests are won in the second
half, not lost in the first.
[Read the full post]

See you on Sunday's club run.
Mia

Stridewell Running Club, 22 Fenwick Road, Bristol BS3 1QF
Unsubscribe | Update preferences
```

| ID | Planted flaw | Dimension | Objective check |
|---|---|---|---|
| 4.1 | Preheader repeats the subject word for word | 1 | string equality |
| 4.2 | Sender is a bare no-reply address on an unfamiliar domain, replacing the known "Coach Mia at Stridewell"; the body is signed by Mia | 1, 15, 4 | sender string vs context and signature |
| 4.3 | The most urgent news and the only registration CTA live inside an image with no alt text | 17, 16, 20 | image note; no text CTA for registration |
| 4.4 | First article paragraph is about 150 words with no break | 5, 12 | paragraph word count > 100 |

Decoys: **D4.a** about 320 words is inside the 300-500 newsletter budget.
**D4.b** three "Read the full post" links serve one goal (reading), which is
normal in a newsletter, not CTA overload.

## Email 5: Fork & Field, win-back

Context: Re-engagement to customers inactive for 4 months. Audience: Value
Seeker.

```
From: Fork & Field <hi@forkandfield.com>
Subject: Sam, we saved your seat at the table
Preheader: It's been 4 months. Here's a reason to come back.

Hi Sam,

Did we do something wrong? We're honestly heartbroken that you abandoned us
after 14 boxes together.

Your account will be permanently deleted in 24 hours unless you reactivate!

To welcome you back, we've set aside a special discount on your next box.
The autumn menu has 22 new recipes, including the miso squash bowl you
rated five stars in March.

[Button: Reactivate my plan]

Don't want these emails? Reply STOP.

Fork & Field, 88 Mercer Lane, Portland, OR 97209
```

| ID | Planted flaw | Dimension | Objective check |
|---|---|---|---|
| 5.1 | Guilt and shame: "Did we do something wrong?", "heartbroken that you abandoned us" | 14, 4 | phrase match |
| 5.2 | Unexplained 24-hour deletion threat (false urgency) | 3, 8, 15 | urgency with no reason |
| 5.3 | Offer undefined: "a special discount", no amount, code or expiry | 9, 3 | no number in offer sentence |
| 5.4 **gate** | No unsubscribe link, only "Reply STOP" | 6, 20 | no unsubscribe link |

Decoys: **D5.a** about 80 words is under the 100-150 re-engagement budget; short
is not a flaw. **D5.b** personalization from real history (14
boxes, the recipe Sam rated) is a strength, not "creepy".

Goal check: the rewrite must not invent a discount amount. It asks the
marketer or uses `[discount amount and expiry]`.

## Email 6: Lumen Botanics, welcome

Context: Welcome email, sent after newsletter sign-up. The sign-up form
promised 15% off the first order. Audience: new subscriber (Cold/New).

```
From: Priya at Lumen Botanics <priya@lumenbotanics.com>
Subject: Welcome to Lumen Botanics: your 15% gift is inside
Preheader: Plus the 3-step routine our founder swears by.

Hi Alex,

Welcome to Lumin Botanicals! We're so glad you're here.

Our Dawn Renewal Serum is the clinically proven #1 serum in the world, and
it will cure your acne in just 7 days.

Your welcome gift is waiting!

Our founder's 3-step routine:
1. Cleanse with the Cloud Gel Wash, morning and night.
2. Apply two drops of Dawn Renewal Serum to damp skin.
3. Seal it in with the Daily Barrier Cream.

[Button: Shop the serum]

Lumen Botanics, 15 Orchard Row, Asheville, NC 28801
Unsubscribe | Privacy policy
```

| ID | Planted flaw | Dimension | Objective check |
|---|---|---|---|
| 6.1 | Brand misspelled in the body: "Lumin Botanicals" vs "Lumen Botanics" | 6 | string mismatch with sender and footer |
| 6.2 | Unsupported superlative claims: "clinically proven", "#1 serum in the world" | 15, 4 | no source given |
| 6.3 | Health claim and spam trigger: "cure your acne in just 7 days" | 20, 15 | "cure" in health category |
| 6.4 **gate** | Subject promises a 15% gift; the body gives no code, link or terms | 9, 2, 20 | no code or redemption step |

Decoys: **D6.a** personal sender "Priya at Lumen Botanics" (good).
**D6.b** the numbered 3-step routine (good structure, not padding).

Goal check: the rewrite must not invent a code. It uses `[15% code]` or asks.

## Email 7: Quarry, product launch to non-technical buyers

Context: Promotional (launch). Audience: marketing operations managers,
non-technical (B2B Pro). Scheduled Saturday 02:00 recipient local time.

```
From: Quarry <news@quarrydata.com>
Subject: Still exporting CSVs to build your reports?
Preheader: Quarry 3.0 is live, with new pricing tiers for every team size.

Hi Morgan,

Quarry 3.0 introduces native CDC ingestion from your operational databases
into a columnar OLAP layer with incremental materialisation, which means that
dashboards built on top of the ELT pipeline no longer depend on nightly batch
jobs that frequently fail silently and leave stakeholders looking at stale
numbers without any indication that the underlying data has not refreshed.

Alongside the release we are introducing new pricing tiers designed to scale
with teams of every size. To learn more about the new pricing tiers, contact
our sales team.

[Button: Submit]

Quarry Data Inc., 77 Mission Street, San Francisco, CA 94105
Unsubscribe | Manage preferences
```

| ID | Planted flaw | Dimension | Objective check |
|---|---|---|---|
| 7.1 | Jargon and undefined acronyms (CDC, OLAP, ELT) for a non-technical audience; first sentence is 47 words | 11 | acronym list; sentence length > 25 |
| 7.2 | Announces "new pricing tiers" with no price | 9, 16 | no currency figure |
| 7.3 | CTA "Submit", with no stated action or benefit | 8, 16 | CTA label in vague list |
| 7.4 | Scheduled Saturday 02:00 local for a B2B audience | 19 | weekend and 22:00-06:00 |

Decoys: **D7.a** the subject is a relevant pain-point question, 43
characters (good). **D7.b** the footer is complete.

## Email 8: Paper Lantern Books, author evening

Context: Promotional (event invite). Audience: Loyal Buyer (store regulars).

```
From: Ines at Paper Lantern Books <ines@paperlanternbooks.com>
Subject: You are invited: an evening with Ilse Marren 📚
Preheader: Paper Lantern Books

Dear reader,

The first time I read Ilse Marren, I missed my bus stop twice in one week.
So when she wrote to say she was touring with her new novel, The Salt
Orchard, I said yes before she finished the sentence.

Join us on Thursday, 14 November 2026 at 7 PM at our new location for a
reading, a conversation and a signing. Wine and cake are on us.

To RSVP, create a Paper Lantern account, then complete our 9-question RSVP
form. Seats are limited to 60.

[Button: RSVP now]

See you there,
Ines, owner

Paper Lantern Books, 3 Wren Street, Galway H91 E2K4, Ireland
Unsubscribe
```

| ID | Planted flaw | Dimension | Objective check |
|---|---|---|---|
| 8.1 | Preheader is just the brand name (default-style) | 1 | preheader equals brand |
| 8.2 **gate** | Weekday and date disagree: 14 November 2026 is a Saturday | 6, 9 | calendar check |
| 8.3 | "Our new location" with no address for an in-person event (the footer gives the registered address, not the venue) | 9 | no venue address |
| 8.4 | Forced account creation plus a 9-question form to RSVP | 16 | "create ... account"; 9 fields > 3 |

Decoys: **D8.a** the emoji in a casual B2C subject (framework: +0.3).
**D8.b** the owner's personal story opening is a Naturalness strength, not
throat-clearing.

## Email 9: Coinpath, referral bonus

Context: Promotional. Audience: Value Seeker. The email has an attachment.

```
From: Coinpath Security Team <security@coinpath.app>
Subject: Your Coinpath account: action required to claim your bonus
Preheader: Earn $100 cash for every friend you refer. Risk-free and guaranteed.
Attachment: Referral_Terms.pdf

Hi Taylor,

Earn $100 cash for every friend who joins Coinpath with your link. It's
risk-free and guaranteed*.

Share your link: http://coinpath.app/refer/taylor

The offer ends 31 October 2026, because our partner bank's promotion ends
that day.

[Button: Get my referral link]

*Bonus is paid only after your friend deposits at least $500 and keeps it in
their account for 90 days.

Coinpath is a financial technology company, not a bank. Banking services are
provided by Harbour Mutual Bank, Member FDIC. Crypto assets are not FDIC
insured and may lose value.

Coinpath Inc., 500 Pine Street, Seattle, WA 98101
Unsubscribe | Privacy
```

| ID | Planted flaw | Dimension | Objective check |
|---|---|---|---|
| 9.1 **gate** | Deceptive sender and framing: "Security Team" and "action required" on a promo | 20, 15 | sender role vs content |
| 9.2 | Financial spam triggers: "Earn", "cash", "risk-free", "guaranteed" | 20, 1 | trigger list |
| 9.3 | Attachment on a marketing email | 20 | attachment present |
| 9.4 | Insecure http:// link | 15, 20 | `http://` prefix |
| 9.5 | The condition that changes the deal ($500 deposit for 90 days) hidden in a footnote, contradicting "guaranteed" | 9, 15 | asterisk footnote |

Decoys: **D9.a** real deadline with its reason (good urgency). **D9.b** the
long regulatory disclaimer is required, not bloat.

## Email 10: Kiln & Clay Studio, control

Context: Promotional. Audience: Premium Shopper (members). Scheduled Tuesday
18:00 recipient local time.

```
From: Hana at Kiln & Clay Studio <hana@kilnandclay.com>
Subject: Fresh from the kiln: 6 new glazes for autumn
Preheader: Hand-mixed in small batches. Members get first pick until Friday 23 October.

Hi Robin,

Six new glazes came out of the kiln this week, and they are the best we have
made. Ember Rust, Fog Celadon and Tidepool Blue are already my favourites.

[Button: See the new glazes]

Each glaze is mixed by hand and fired in batches of about 40 pieces, so once a
colour sells out it will not return until spring. As a member, you get first
pick until Friday 23 October, 23:59 GMT, before we open them to everyone.

Mugs start at £28 and serving bowls at £64. Every piece ships in 2 working
days, and returns are accepted within 30 days.

"The Fog Celadon bowl is even better in person. Gorgeous." Elena R., member
since 2022

If you have a question about a glaze, just reply. I read every email.

Hana

Kiln & Clay Studio, 12 Potters Yard, Bath BA1 2QH, United Kingdom
Manage preferences or unsubscribe
```

Grading key: no planted flaws. Expected verdict "Strong" or "Ready to send"
(70 or more), never "Do not send", and higher than every other email. No
dimension at 1 or 2. Acceptable minor notes: "the best we have made" is an
unsupported superlative (-0.3, Naturalness); a fix list padded with invented
problems fails Fix precision.
