# Email dimensions: the 20-dimension rubric

Load this when the user asks for a full email scorecard, or when you are not
sure an element is a problem. Each section is one dimension of the email
framework: what it measures, the indicators with their adjustments, what a 5
looks like, and the patterns that fix it.

How to score a dimension: start at 3, apply the adjustments the email shows,
round, clamp to 1-5. An item marked **critical** sets the dimension to 1 on
its own. Score "not scored" when the element is not visible (no send time, no
layout, plain text only).

Scale: 1 critical deficiency (do not send), 2 below standard, 3 acceptable,
4 strong, 5 exceptional.

## 1. Attention Capture

What it measures: whether the subject, preheader and sender name earn the open.
Primary outcome: open rate. The subject drives roughly 35-50% of the open
decision.

**Subject line**

| Indicator | Adjustment |
|---|---|
| Length 30-50 characters | ideal; over 70 is a penalty (over 60 already truncates on phones, see dimension 18) |
| 4-8 words | ideal; over 12 is a penalty |
| Personalization token, used naturally | +0.5 |
| Relevant question | +0.3; clickbait question -0.3 |
| Specific, credible number ("3 tips", "47%") | +0.3; implausible number -0.5 |
| Genuine urgency | +0.3; false urgency -1.0 |
| Tasteful curiosity gap | +0.5; pure clickbait -1.0 |
| Explicit benefit | +0.5 |
| Relevant power words | +0.2 each, max +0.6 |
| Emoji | +0.3 in casual B2C; -0.5 in formal B2B |
| ALL CAPS word | -0.3 each |
| Spam trigger ("Free", "Act now", "Limited time") | -0.5 each |

**Preheader**

| Indicator | Adjustment |
|---|---|
| Custom preheader | +0.5; default "View in browser" -0.5 |
| Adds to the subject | +0.5 |
| 40-100 characters | ideal; under 30 is a penalty |
| Hints at the CTA | +0.3 |
| Repeats the subject | -0.5 |

**Sender name**

| Indicator | Adjustment |
|---|---|
| Recipient will recognise it | critical to opens; unrecognised means low opens |
| Person at brand ("Sarah from Acme") | typically +15% opens vs brand only |
| Relevant authority (CEO, Dr.) | +0.3 |
| Consistent with past sends | +0.3; unexplained change -0.5 |
| Looks reply-friendly (not no-reply) | +0.2 |

**Score 5:** 35-50 character subject with a clear benefit; custom preheader
that adds new information; personal, recognised sender; genuine curiosity
without clickbait; zero spam triggers; fits on mobile; tokens used well.

Patterns that work: benefit plus time frame ("Double your opens in 7 days");
curiosity gap ("The one metric most marketers ignore"); personal touch
("Sarah, about your cart from yesterday"); social proof ("Join 10,000+
marketers who..."); pain question ("Still struggling with deliverability?");
authority lead ("Our CEO's top 3 picks for you").

## 19. Timing Alignment

What it measures: whether the send time fits the recipient and the moment.
Primary outcome: open rate, then conversion. Score only if a send time,
trigger or schedule is given; otherwise "not scored".

| Indicator | Adjustment |
|---|---|
| Sent in the recipient's own best window | +1.0 |
| Correct for the recipient's time zone | +0.5 |
| Timed to behaviour (trigger, activity) | +0.5 |
| Time backed by past results | +0.3 |
| Right day for the content | +0.3 |
| B2B in working hours; B2C flexible | +0.3 |
| Fits the season or a relevant event | +0.3 each |
| Avoids sensitive news moments | +0.3 |
| Sensible gap since the last send | +0.3 |
| Right place in the sequence | +0.3 |
| Fresh trigger (sent within hours of the action) | +0.5 |
| Deadline is real and actually matters | +0.3 |
| Avoids crowded send times | +0.2 |
| Sent 22:00-06:00 local, or B2B on a weekend | treat as -1.0 (framework: "never send 3am local time") |

**Score 5:** individual send time from behavioural data, correct time zone,
contextually appropriate, right point in the sequence.

## 20. Deliverability Risk

What it measures: the chance the email reaches the inbox rather than spam.
A 5 means minimal risk. Primary outcome: inbox placement, which gates every
other metric. Deliverability below 95% means fix this before anything else.

| Indicator | Adjustment |
|---|---|
| Spam trigger word | -0.3 each |
| ALL CAPS subject | -0.5 |
| Extra exclamation marks | -0.3 per extra "!" |
| Suspicious link domain | -1.0 |
| Image-heavy, little text | -0.5 |
| Broken HTML | -0.5 |
| Attachment (unless expected) | -0.3 |
| Embedded form | -0.3 |
| Shortened URL (bit.ly etc.) | -0.5 |
| Misleading subject | -1.5 (**critical**) |
| Deceptive sender name | -1.5 (**critical**) |
| Working unsubscribe | +0.3; missing is **critical** (see dimension 6) |
| Authenticated (SPF, DKIM, DMARC), clean list, good reputation | +0.5 each, only if the user states it |
| Volume spike, over-frequency, high bounces, complaint history | -0.5 to -1.0, only if the user states it |

Spam word risk by category: Financial (free, earn, cash, bonus) medium-high;
Urgency (act now, limited, expire) medium; Health (cure, lose weight, diet)
high; Gambling (casino, jackpot, winner) high; Adult very high; Pharma very
high.

Since February 2024 Google and Yahoo require SPF, DKIM and DMARC and a working
one-click unsubscribe for bulk senders. Complaint rate 0.1% is a warning,
0.3% is critical.

## 2. Interest Generation

The opening (first 100-150 words, visible without scrolling) makes the reader
keep going. The first 50 words carry most of the read probability. Outcome:
scroll depth, and whether the reader reaches the CTA.

- Strong first-sentence hook +1.0; generic greeting only -0.5
- Immediate relevance to the reader +0.5; names their pain point +0.5
- Hints at the value to come +0.3
- First paragraph 20-40 words; reading level grade 6-8
- Visual break or scannable elements early +0.3 each
- CTA available without scrolling +0.5
- Story or anecdote +0.5; early specific number +0.3
- Opening does not deliver on the subject: -2.0 (**critical** if the subject
  misdescribes the email)
- Smooth greeting-to-value transition +0.3; tasteful pattern interrupt +0.5

**Score 5:** hook in sentence one, clear relevance, smooth subject-to-body
continuity, grade 6-8, personalized beyond the name.

Patterns: empathy open; startling stat with a bridge; direct address ("You
left these in your cart. Here's 10% off"); story hook; provocative question;
subject continuation.

## 3. Desire Creation

The body turns interest into wanting the offer. Outcome: conversion rate and
order value.

- Crystal-clear benefit +1.0; specific outcome +0.5; differentiation +0.5
- Credible proof +0.3 each; vivid outcome picture +0.5; pain and gain both +0.3
- Genuine FOMO +0.5; fake FOMO -1.0
- Aspiration +0.5; belonging, achievement, relief, sustained curiosity +0.3 each
- Features turned into outcomes +0.5; before/after or comparison +0.3
- Each objection handled +0.3; social proof +0.3; authority +0.3
- Offer stated unambiguously +0.5; smart price framing +0.3
- Bonus +0.3 each; strong guarantee +0.5; genuine exclusivity +0.3
- Genuine deadline or scarcity +0.3; fake -1.0

**Score 5:** clear, specific benefit for this persona, proof, objections
handled, an offer with genuine urgency, vivid outcome.

Patterns: transformation promise ("from X to Y in Z"); specificity ("save
$347 a month", not "save money"); social proof stack (count + result + named
quote); objection sandwich; scarcity with the reason ("only 50 spots because
we give each person feedback"); future pacing ("Imagine...").

## 4. Naturalness and Authenticity

Reads as a real person, not a template or a machine. Outcome: reply rate;
lower unsubscribes.

- Conversational +0.5; contractions +0.2; varied sentences +0.3
- Jargon fits the audience +0.3; "you/your" +0.3; active voice +0.3
- Consistent voice +0.5; specific details +0.3; honest about limits +0.3
- Sender personality +0.3; real anecdote +0.5
- Acknowledges history with the reader +0.5; uses relevant context +0.5
- Marketing cliché -0.3 each; awkward transition -0.3 each
- Same sentence pattern repeated -0.3; unsupported superlative -0.3 each
- Unnaturally uniform formatting -0.2; sterile, no warmth -0.5

Template and AI tells to flag: "In today's fast-paced world", "We're thrilled
/ excited to announce", "unlock", "elevate", "seamless", "game-changer",
"Look no further", "I hope this email finds you well", "Whether you're X or
Y", "delve", "revolutionary", "take it to the next level", three adjectives
in a row, every paragraph the same length.

**Score 5:** reads like a thoughtful note from a trusted colleague; distinct
voice; specific; honest; written for this reader.

Patterns: real person signature with a reply invitation ("Hit reply, I read
every one. Sarah"); specific detail ("Maria from Austin saved 3 hours on day
one"); honest positioning ("We're not the cheapest. Here's why."); relationship
reference ("Since you downloaded our guide last month...").

## 8. Persuasive Power

Moves the reader to act. Outcome: conversion rate, revenue per email.

- Cialdini, each applied honestly: reciprocity, real scarcity, credible
  authority, relevant social proof, consistency with a prior commitment
  +0.5 each; liking, unity +0.3 each
- CTA stands out +0.5; action clearly described +0.5; benefit-framed +0.3
- CTA urgency where fair +0.3; placed early and at the end +0.3; smart
  repetition of the same CTA +0.3; low-friction CTA +0.5
- Handles price, trust, time, need objections +0.3 each; risk reversal +0.5
- Loss aversion, anchoring, choice design, contrast, cognitive ease +0.3 each

CTA copy: not "Submit", "Click here", "Learn more". Yes "Start my free
trial", "Get my 50% off", "See my results".

**Score 5:** several principles applied honestly, a visible benefit-framed
CTA, objections handled, urgency without pressure.

Patterns: Problem-Agitate-Solution; risk reversal ("Cancel anytime", "No card
needed"); specificity; proof cascade (big number, testimonial, authority);
urgency with its reason ("Prices rise Jan 1 because supplier costs rose").

## 11. Message Clarity

The meaning is clear on first read. Outcome: click rate; fewer support tickets.

- Reading grade 6-8 ideal; penalty above 10
- Average sentence 15-20 words ideal; penalty above 25
- Unexplained jargon is a penalty; undefined acronym -0.3 each
- Mostly active voice +0.3
- One core message +0.5; supporting points aligned +0.3; no tangents +0.3
- Little redundancy +0.2; high signal-to-noise +0.3
- Specific CTA +0.5; next step after the CTA clear +0.5
- Simple process, clear timing, clear conditions +0.3 each
- Logical flow, clear hierarchy, consistent terms +0.3 each

**Score 5:** one message, grade 6-8, specific CTA, no interpretation needed.
Test: can the reader say the one thing you want them to do? "[Do this] +
[get this] + [by this date]".

## 12. Conciseness and Economy

Minimum words for full meaning. Outcome: read rate, then click rate.

Word budgets: flash sale 75-150 (2-3 paragraphs); promo 150-250 (3-4);
welcome 150-200 (3-4); re-engagement 100-150 (2-3); newsletter 300-500 (5-7);
event invite 150-250 (3-5); cart reminder 75-150 (2-3); transactional 50-150
(2-3). Read time 30-90 seconds. Paragraphs 40-60 words.

- High value per word +0.5; single purpose +0.5; every element earns its
  place +0.5; direct path to CTA +0.3
- Skimmable +0.3; CTA before the end +0.3
- Repeated idea -0.3 each; filler phrase ("in order to", "due to the fact
  that") -0.2 each; empty intensifier ("very", "really") -0.1 each
- Long preamble -0.5; bloated sign-off -0.3; off-topic section -0.5 each
- More than 3 scrolls is a penalty

**Score 5:** nothing to cut, nothing missing.

## 14. Emotional Resonance

The right emotion for the persona, without manipulation. Outcome: brand
sentiment, reply rate.

- Clear emotional intent +0.5; emotion fits the persona +0.5
- Authentic +0.5; manipulative -1.0 (guilt, shame, invented threats)
- Calibrated intensity +0.3; several touchpoints +0.3
- Empathy +0.5; emotional story +0.5; shared experience, warmth,
  vulnerability +0.3 each
- Aspiration, pain acknowledged, belonging, achievement, relief +0.3 each
- Hope/fear balance right for the context +0.3; vivid positive future +0.3

| Persona | Use | Avoid |
|---|---|---|
| Impulse Buyer | excitement, FOMO, instant gratification; joy, surprise | guilt, shame |
| Premium Shopper | pride, aspiration, exclusivity; achievement | fear, desperation |
| Loyal Buyer | appreciation, belonging, trust; nostalgia, warmth | manipulation |
| Value Seeker | security, relief, satisfaction; pride | FOMO (reads as manipulative) |
| Cold/New | hope, curiosity, trust; relief | fear, pressure |

**Score 5:** the right emotion for the persona, authentic, memorable.

## 6. Professionalism

Polish, accuracy and compliance. Each visible mistake costs roughly 3-5% of
conversion. Outcome: brand trust; fewer spam reports.

- Grammar or spelling error -0.5 each; punctuation error -0.3 each
- Inconsistent capitalisation -0.3
- Wrong proper noun (brand, product, person) -1.0 each
- Wrong product or service term -0.5 each
- Precise word choice +0.3; consistent voice +0.5; right formality +0.3
- Broken link -1.0 each; broken image -0.5 each; alt text +0.2
- Broken on mobile -1.5
- Expired or wrong date -1.0 (**critical** if it is the offer date)
- Wrong price -2.0 (**critical**)
- Wrong recipient name -1.5 (**critical**); raw merge token in a greeting
  (**critical**)
- Missing legal footer elements -1.0; missing or broken unsubscribe -2.0
  (**critical**)

**Score 5:** zero errors, consistent brand, all details right, complete
legal footer.

Pre-flight: spell check; test every link; preview on 3+ screens; test
tokens; check dates and prices against the source; Gmail, Outlook, Apple
Mail, dark mode, images off.

## 7. Brand Image Enhancement

The email leaves the brand stronger. Outcome: NPS, repeat purchase.

- Reflects brand values +0.5; consistent positioning +0.5; differentiates +0.5
- Quality signals that fit the positioning +0.3; mission link +0.3
- Credibility element +0.3 each; quality social proof +0.5; authority +0.3
- Stability signal +0.2; meaningful award +0.5
- Customer-centric +0.5; helpful +0.3; genuine thanks +0.2; community +0.3;
  long-term relationship +0.3
- Proper logo, brand colours, image quality, design quality +0.3 each;
  typography +0.2

**Score 5:** embodies the brand, builds credibility, leaves a positive
feeling, differentiates.

## 9. Informational Completeness

Everything needed to decide and act is in the email. Outcome: conversion
rate; fewer support tickets.

- Core questions: what +0.5, why +0.5, how +0.5, how much +0.5,
  when +0.3, where +0.3, who it is for +0.3
- Key features +0.3; features as benefits +0.5; comparison, use cases,
  requirements, honest limitations +0.3 each
- Proof, testimonials, credentials, guarantee terms +0.3 each; support and
  company info +0.2 each
- What happens after the click +0.5; when they get it +0.3; what they commit
  to +0.3; can they cancel +0.3; how to ask questions +0.3

Treat as a strong penalty (-1.0 or more): an announced price, discount or
gift with no amount or code; an event with no date, time zone or place; a
condition that changes the deal hidden in small print.

**Score 5:** all core questions answered, action path clear, complete but not
overwhelming.

Pattern, the complete offer block: WHAT YOU GET (items with benefits),
PRICE ($X, normally $Y), DEADLINE (date and time zone), GUARANTEE (terms).

## 10. Product or Service Image

The specific product looks desirable and better than alternatives. Outcome:
conversion; fewer returns.

- Clear value proposition +0.5; clear differentiators +0.5; benefit order
  +0.3; problem-solution fit +0.5; outcome visualised +0.3
- Quality claims +0.3; materials, process +0.2 each; certifications +0.3
- Quality product images +0.5; in-context images +0.3; angles, scale,
  detail shots +0.2 each
- Reviews +0.5; star rating, user content, expert review, popularity +0.3 each

**Score 5:** compelling value proposition up front, differentiated, strong
visuals and social validation.

Patterns: before/after; feature "which means" benefit; claim, proof, claim.

## 15. Trust and Credibility Signals

The reader believes the sender and the claims. Outcome: conversion rate;
fewer spam reports.

- Relevant credentials +0.5; meaningful recognition +0.5; press, credible
  sender, credible partners +0.3 each
- Customer count +0.3; credible testimonials +0.5; reviews +0.5; case study
  +0.5; client logos +0.3; specific customer results +0.5
- Clear sender identity +0.3; contact options +0.3; physical address +0.2;
  privacy clarity +0.3; honest limits +0.3; price transparency +0.5
- HTTPS links +0.3; visible unsubscribe +0.3; privacy policy +0.2;
  transaction security +0.3; GDPR/CCPA signal +0.2
- Unsupported claims ("clinically proven", "#1 in the world", "guaranteed
  returns") with no source: treat as -0.5 each; in health or finance, -1.0

Trust signal strength, high to low: third-party certification; specific
customer results; customer count; media mentions; general testimonials;
years in business; generic social proof; self-claimed credentials.

**Score 5:** strong authority, specific proof, full transparency, risk
reversal. A skeptic would be comfortable.

## 5. Structural Organisation

Easy to scan and navigate. Average read time is 11-13 seconds. Outcome: click
rate, comprehension.

- Logical flow +0.5; clear hierarchy +0.5; single message +0.5
- Clear sections, key info first, clear wrap-up +0.3 each
- Whitespace, lists for lists, strategic bold, useful subheads +0.3 each
- Visual anchors +0.2; CTA visually distinct +0.5
- Paragraphs 40-60 words ideal; over 100 words -0.3 each
- Key content on the F-scan path, good chunking, several entry points +0.3
  each; meaningful first words +0.2; understandable when skimmed +0.5
- Long emails: table of contents +0.3, jump links +0.2
- CTA repeated through a long email +0.3

**Score 5:** main value extractable in a 5-second scan; one focus; CTA
prominent and repeated.

Patterns: inverted pyramid; problem, solution, proof, action; scannable
summary (hook, 3-5 benefit bullets, proof line, CTA, details below).

## 13. Personalization Depth

Built for this recipient. Personalization lifts opens about 16%, clicks 52%,
conversions 104% (Venkatasubramaniam et al., 2025). Outcome: all engagement,
lifetime value.

Levels: 0 none (same blast to all); 1 token (name only); 2 segment; 3
behavioural (triggered by an action); 4 individual; 5 predictive. Level 0-1
is a 2 at best unless the email type does not need more.

- Name used well +0.3; role, company, location, demographic fit +0.3 each
- Purchase history, browse behaviour, engagement history, lifecycle stage,
  stated preferences +0.5 each
- Personal send time +0.5; trigger-based +0.5; season +0.3; frequency +0.3
- Personal product picks, content, offer, dynamic blocks +0.5 each; image
  per segment +0.3
- Raw or broken token in rendered copy ("Hi {{first_name}}", "Hi ,"):
  **critical**. It shows the reader they are a row in a list.
- Data available but unused (a cart reminder that does not name the items):
  -0.5

**Score 5:** could not have been sent to anyone else.

## 16. Action Friction

How hard it is to act after reading. Outcome: click-to-conversion; fewer
abandoned carts.

- Each click beyond 2 to convert -0.3; each form field beyond 3 -0.2
- Forced account creation -0.5; extra payment or confirmation step -0.3 each
- CTA highly visible +0.5; hidden CTA -1.0
- Good tap size, strong contrast, clear action copy +0.3 each
- More than 3 competing CTAs -0.3 (choice overload)
- Decision info complete +0.5; price known before the click +0.5;
  requirements clear +0.3; FAQ answered +0.3
- Mobile-friendly landing +0.5; broken link -2.0 (**critical**)

Audit: CTA above the fold and contrasting; 3 or fewer steps; 3 or fewer form
fields; tap target 44px or more; price visible; requirements stated before the
CTA; links tested; page under 3 seconds.

**Score 5:** one tap to act, no surprises after the click.

## 17. Visual Design Quality

Looks professional and supports the message. Outcome: brand perception,
engagement.

- Clean alignment +0.5; clear visual hierarchy +0.5; whitespace, balance,
  eye flow +0.3 each
- Readable fonts, few fonts, clear size steps +0.3 each; line height and
  line length +0.2 each
- Harmonious colours +0.3; brand palette +0.5; readable contrast +0.5;
  colour used for emphasis +0.3; colour-blind safe +0.3
- Quality images +0.5; relevant images +0.5; consistent style +0.3; alt text
  +0.2; broken images -1.0
- Key text or the only CTA inside an image: treat as -1.0 (it vanishes with
  images off and hurts deliverability)

**Score 5:** publication quality, on brand, design helps comprehension.

## 18. Mobile Optimization

Works on a phone, where 60%+ of email is opened. Outcome: mobile engagement
and conversion.

- Responsive +1.0; single column +0.5; readable without zoom +0.5; images
  fit +0.3; no horizontal scroll +0.5
- Tap targets 44px or more +0.5; spaced +0.3; forgiving touch +0.3
- Key content early +0.5; CTA in the first screen +0.5; brief +0.3;
  necessary, light images +0.3
- Fast load +0.5; works across apps +0.5; dark mode +0.3
- Subject over 60 characters: truncated on most phones, -0.5; preheader that
  front-loads the key point helps

**Score 5:** mobile-first; CTA in the first screen; fast; dark mode works.

## Fix patterns for the remaining dimensions

Use these when a fix needs a shape. Fill every slot from the fact ledger or a
[placeholder]; the patterns never license a new fact.

| Dimension | Patterns |
|---|---|
| 6 Professionalism | Pre-flight: spell check, test every link, preview on 3+ screens, test tokens, check prices and dates against the source. Brand voice guide: key phrases, formality, banned words, on-brand vs off-brand examples. Read aloud to catch errors |
| 7 Brand Enhancement | Value shown in action ("Because we believe in [value], we [action]"); credibility stack (count, recognition, result, expert); genuine thanks; behind-the-scenes process; insider framing for members |
| 11 Clarity | Short sentences, simple words, active voice, one idea per sentence; the one-thing test (can the reader say the one thing to do?); the "so what?" filter after each statement; the non-expert test; [Do this] + [get this] + [by this date] |
| 12 Conciseness | Cut 20%, then 20% more; word budget per type; delete any sentence whose removal loses nothing; swap filler ("in order to" -> "to", "due to the fact that" -> "because", "at this point in time" -> "now", "make a decision" -> "decide"); front-load the key fact |
| 13 Personalization | Name the behaviour ("You left these in your cart"); honour stated preferences; reference history ("Your last order was [product]"); dynamic blocks per segment; send in the reader's own window and time zone |
| 14 Emotional Resonance | Empathy before solution; a vivid picture of the outcome; a short customer story from struggle to result (only if the story is in the ledger); belonging ("Join [number] others", ledger number only); relief ("No more [frustration]") |
| 15 Trust Signals | Proof stack (authority, count, guarantee); specific testimonial with name, role and result; prominent risk reversal; transparent footer; trust early, proof in the body, risk reversal at the CTA |
| 16 Action Friction | One-click action with saved details; smart default; everything needed to decide is in the email; ask only for what is needed now; warn about unavoidable friction ("you'll need your [requirement]") |
| 17 Visual Design | Clean alignment, one size step per level of hierarchy, brand palette with readable contrast, relevant images with alt text, no key text inside images |
| 18 Mobile | Design for the phone first; tap targets 44px or more with padding; cut content for mobile; compress images; write the preheader for the preview pane |
| 19 Timing | Send in each reader's best window; trigger on behaviour within hours; never 22:00-06:00 local; space a sequence sensibly and warm up before a promotion; avoid major news moments and overloaded holiday days |
| 20 Deliverability | Remove trigger words and extra "!"; full domain links over shorteners; balanced text and images; honest subject and sender; working one-click unsubscribe; authentication and list hygiene (only if the user states them) |

## How each dimension is measured

You can only run the first column from pasted copy. Say so for the rest.

| Kind | Dimensions it settles | You can check from copy? |
|---|---|---|
| Counts and pattern matches: characters, words, paragraph length, reading level, trigger words, tokens, CTA count, link format, footer elements | 1, 2, 5, 11, 12, 13 (tokens), 16 (CTA count, fields), 20 (content risks) | Yes: always run these first |
| Judgement against the rubric: hook quality, benefit clarity, voice, emotion fit, proof credibility, manipulation | 2, 3, 4, 7, 8, 10, 14, 15 | Yes, with a quote as evidence |
| Rendering and technical tests: links, images, mobile, dark mode, load speed, authentication, reputation, list health | 6, 16, 17, 18, 20 | No: put under "Not checked" |
| Outcome validation: correlate scores with opens, clicks, conversions, replies, unsubscribes, complaints per segment | all | No: suggest it as the follow-up test |

Recommended workflow (the framework's own order): automated checks first
(deliverability, technical, lengths), then judgement on the subjective
dimensions, human review for critical sends, aggregate, compare with
benchmarks, then send or iterate. The same framework also serves A/B variant
comparison and template audits: score both variants and compare dimension by
dimension.
