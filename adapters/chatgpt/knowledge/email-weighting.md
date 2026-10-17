# Email weighting, personas and outcomes

Load this for a full email scorecard, or to decide which email fix matters
most for this audience. Weight of a dimension = email-type multiplier x
persona multiplier. Example: Persuasive Power in a Promotional email to an
Impulse Buyer = 1.5 x 1.5 = 2.25.

Weighted email score (0-100) = ((weighted mean of the scored dimensions) - 1)
/ 4 x 100, rounded. Leave "not scored" dimensions out. Any dimension at 1
means "Do not send" whatever the total.

## Email type multipliers

| Dimension | Promotional | Transactional | Newsletter | Re-engagement | Welcome |
|---|---|---|---|---|---|
| 1 Attention Capture | 1.3 | 0.8 | 1.2 | 1.4 | 1.0 |
| 2 Interest Generation | 1.2 | 0.7 | 1.3 | 1.3 | 1.2 |
| 3 Desire Creation | 1.4 | 0.5 | 0.8 | 1.2 | 1.0 |
| 4 Naturalness | 1.0 | 0.8 | 1.2 | 1.1 | 1.3 |
| 5 Structure | 1.0 | 1.2 | 1.3 | 0.9 | 1.0 |
| 6 Professionalism | 1.1 | 1.4 | 1.1 | 1.0 | 1.2 |
| 7 Brand Enhancement | 1.0 | 0.8 | 1.1 | 0.9 | 1.4 |
| 8 Persuasive Power | 1.5 | 0.3 | 0.7 | 1.3 | 0.8 |
| 9 Completeness | 1.2 | 1.5 | 0.9 | 0.8 | 1.1 |
| 10 Product Image | 1.4 | 0.6 | 0.7 | 1.1 | 0.8 |
| 11 Clarity | 1.1 | 1.4 | 1.0 | 1.0 | 1.2 |
| 12 Conciseness | 1.2 | 1.0 | 0.8 | 1.3 | 1.0 |
| 13 Personalization | 1.2 | 1.3 | 1.0 | 1.5 | 1.4 |
| 14 Emotional Resonance | 1.2 | 0.5 | 1.0 | 1.4 | 1.3 |
| 15 Trust Signals | 1.2 | 0.8 | 0.9 | 1.2 | 1.5 |
| 16 Action Friction | 1.4 | 1.2 | 0.8 | 1.1 | 1.0 |
| 17 Visual Design | 1.0 | 0.9 | 1.2 | 0.9 | 1.1 |
| 18 Mobile | 1.2 | 1.3 | 1.1 | 1.2 | 1.1 |
| 19 Timing | 1.3 | 0.7 | 1.1 | 1.4 | 1.0 |
| 20 Deliverability Risk | 1.0 | 1.0 | 1.0 | 1.2 | 1.0 |

Cart reminders, flash sales, launches and event invites use Promotional.
Order and account notices use Transactional.

## Persona multipliers

Values without a mark are the framework's own. Values marked * are derived:
the framework names the dimension in that persona's top 5 (1.3) or bottom 5
(0.8) but gives no number. Blank means 1.0.

| Dimension | Impulse | Premium | Loyal | Value | Cold/New | B2B Pro |
|---|---|---|---|---|---|---|
| 1 Attention Capture | 1.3 | 0.9 | 0.8 | 1.2 | 1.5 | |
| 2 Interest Generation | 1.1 | 1.2 | 0.8 | 1.0 | 1.4 | |
| 3 Desire Creation | 1.3 | 1.2 | 0.9 | 1.4 | 1.1 | |
| 4 Naturalness | 0.8 | 1.4 | 1.3 | 0.9 | 1.2 | |
| 5 Structure | 0.9 | 1.2 | 0.8 | 1.1 | | 1.5 |
| 6 Professionalism | 0.7 | 1.5 | 0.9 | 0.8 | 1.3* | 1.6 |
| 7 Brand Enhancement | 0.6 | 1.5 | 1.4 | 0.7 | 1.3 | |
| 8 Persuasive Power | 1.5 | 1.0 | 0.8 | 1.3 | 0.8* | 1.2 |
| 9 Completeness | 0.7 | 1.3 | 0.8 | 1.4 | 1.5 | |
| 10 Product Image | 1.0 | 1.5 | 0.8 | 1.2 | 1.4 | |
| 11 Clarity | 1.3 | 0.9 | 0.8 | 1.2 | 1.3* | |
| 12 Conciseness | 1.4 | 0.8 | 0.9 | 1.2 | 0.8* | 1.6 |
| 13 Personalization | 1.1 | 1.4 | 1.3 | 1.0 | 1.2 | |
| 14 Emotional Resonance | | | 1.3* | 0.8* | | |
| 15 Trust Signals | | 1.3* | 1.3* | | 1.3* | |
| 16 Action Friction | 1.3* | 0.8* | 0.8* | 1.3* | 0.8* | |
| 17 Visual Design | | | | 0.8* | | |
| 18 Mobile | | | | | | |
| 19 Timing | 1.3* | 0.8* | | 0.8* | 0.8* | |
| 20 Deliverability Risk | | 0.8* | | | | |

Sources for the combined columns:

- **Cold/New** merges the framework's Cold Prospect (dimensions 1-4), New
  Customer (7, 13 and the top/bottom-5 list) and First-Time Buyer (9, 10).
- **B2B Pro** merges Time-Pressed Executive (5, 12), B2B Decision Maker (6)
  and Skeptical Professional (8).
- For a non-native-speaker audience, set Clarity to 1.5.
- **General** (audience unknown): all 1.0.

Deliverability keeps its gate role whatever the weight: a 1 on dimension 20
means "Do not send" even for a Premium audience.

## What each persona cares about most

| Persona | Top 5 | Bottom 5 |
|---|---|---|
| Impulse Buyer | Attention, Persuasion, Conciseness, Timing, Friction | Naturalness, Structure, Professionalism, Brand, Completeness |
| Premium Shopper | Professionalism, Brand, Product Image, Trust, Naturalness | Conciseness, Persuasion, Friction, Timing, Deliverability |
| Loyal Buyer | Personalization, Emotional, Brand, Naturalness, Trust | Attention, Persuasion, Friction, Completeness, Product Image |
| Value Seeker | Completeness, Clarity, Desire, Friction, Conciseness | Brand, Emotional, Naturalness, Visual Design, Timing |
| New Customer | Trust, Completeness, Clarity, Professionalism, Brand | Conciseness, Timing, Personalization, Friction, Persuasion |

What moves each persona:

- Impulse: urgency, curiosity, scarcity, instant gratification. Short.
- Premium: sophistication, quality signals, exclusivity, flawless polish.
  Gimmicks hurt.
- Loyal: appreciation, insider access, a personal voice. Opens anyway.
- Value: specific numbers and savings, comparisons, ROI. FOMO reads as
  manipulation.
- Cold/New: a hook, proof, guarantees, clear next steps. No pressure.
- B2B Pro: structure, brevity, authority, risk reversal, zero errors.

## Dimension to outcome

| Dimension | Primary outcome | Secondary |
|---|---|---|
| 1 Attention Capture | Open rate | Time to open |
| 2 Interest Generation | Scroll depth | Time on email |
| 3 Desire Creation | Conversion rate | Order value |
| 4 Naturalness | Reply rate | Unsubscribe rate (down) |
| 5 Structure | Click rate | Comprehension |
| 6 Professionalism | Brand trust | Spam reports (down) |
| 7 Brand Enhancement | NPS | Repeat purchase |
| 8 Persuasive Power | Conversion rate | Revenue per email |
| 9 Completeness | Conversion rate | Support tickets (down) |
| 10 Product Image | Conversion rate | Returns (down) |
| 11 Clarity | Click rate | Support tickets (down) |
| 12 Conciseness | Read rate | Click rate |
| 13 Personalization | All engagement | Lifetime value |
| 14 Emotional Resonance | Brand sentiment | Reply rate |
| 15 Trust Signals | Conversion rate | Spam reports (down) |
| 16 Action Friction | Click-to-conversion | Cart abandonment (down) |
| 17 Visual Design | Brand perception | Engagement |
| 18 Mobile | Mobile engagement | Mobile conversion |
| 19 Timing | Open rate | Conversion rate |
| 20 Deliverability Risk | Inbox placement | Every other metric |

## Reading order for leverage

1. **Inbox first.** Deliverability below 95% means nothing downstream counts.
   Fix authentication, list hygiene, spam signals, misleading subject or
   sender, and the unsubscribe before anything else.
2. **Judge on the click, not the open.** The open is directional only (privacy
   features inflate it). The click proves the content matched what the
   reader wanted. When two fixes tie, the one that moves clicks wins.
3. **Then the conversion.** Offer completeness, trust and friction decide
   whether a click becomes revenue.
4. **Protect the list.** Fixes that cut complaints and unsubscribes protect
   the asset every future send depends on. A great campaign on a shrinking
   list is a short-term win and a long-term loss.

## Benchmarks to quote when the user shares results

| Metric | Definition | Good |
|---|---|---|
| Deliverability rate | delivered / sent | 95% or higher |
| Bounce rate | bounced / sent | under 2% |
| Open rate | opens / delivered | directional only; watch the trend |
| CTR | clicks / delivered | roughly 2-5% |
| CTOR | clicks / opens | about 10%; 14-17% in the strongest industries |
| Unsubscribe rate | unsubscribes / delivered | under about 0.5% per send |
| Complaint rate | spam reports / delivered | 0.1% warning, 0.3% critical (Google sender guidelines) |

If the user shares performance data with the email, use it as evidence: a
low CTOR with a normal open rate points at the body, offer or CTA
(dimensions 3, 8, 11, 16), not at the subject.

Lifecycle beats blast: triggered and segmented emails consistently
out-convert one-size-fits-all sends, so a generic blast to a mixed list caps
Personalization and Timing whatever the copy says.
