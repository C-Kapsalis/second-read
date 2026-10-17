# Email: hard checks

Run every check before any judgement. Count characters and words; do not
estimate. Each failure needs a quote or a number. If an element is not in what
the user pasted (no footer, no send time), write "not visible, confirm"
unless the user says the email is complete.

## Read the input

Collect: sender name and address, subject, preheader, body, CTA buttons and
links, footer, and if given: send time and time zone, audience, email type.

- **Type:** Promotional (sale, launch, cart reminder, event invite),
  Transactional, Newsletter, Re-engagement, Welcome. Infer it if not stated.
- **Persona:** Impulse Buyer, Premium Shopper, Loyal Buyer, Value Seeker,
  Cold/New, B2B Pro, or General if unclear (say so).

## Checks

| # | Check | Fails when | Severity |
|---|---|---|---|
| E1 | Subject length | Over 60 characters (cut off on most phones) | Major |
| E2 | Spam signals | Any ALL CAPS word, "!!" or more, or trigger words: free, act now, limited time, cash, earn, bonus, guaranteed, risk-free, winner, cure | Major |
| E3 | Preheader | Missing, default ("View in browser", only the brand name), under 30 characters, or repeats the subject | Major |
| E4 | Sender | No-reply address, unfamiliar domain, or a name that does not match the brand or signer in the body | Major |
| E4b | Deceptive sender | Claims a role it is not ("Security Team" on a promo; "action required" framing on marketing) | Blocker |
| E5 | Merge tokens | Raw or broken token in rendered copy: `{{first_name}}`, `*|FNAME|*`, `[Name]`, "Hi ," | Blocker |
| E6 | Subject vs body | The subject misdescribes the email ("Your order has shipped" on a cart reminder) or promises an offer the body does not give (no code, link or terms) | Blocker |
| E7 | Footer | No unsubscribe link ("Reply STOP" alone does not count) | Blocker |
| E7b | Footer address | No physical postal address | Major |
| E8 | Offer facts | Discount, price, deadline or time zone missing or vague ("ends soon", "a special discount") | Major |
| E8b | Offer dates | Date already passed; weekday and date disagree | Blocker |
| E9 | CTAs | No clear primary CTA; more than 3 CTAs to different goals; vague label ("Click here", "Submit", "Learn more"); the only CTA is a bare link | Major |
| E10 | CTA position | Primary CTA not in the first screen (about the first 150 words, or before the first long block) | Major |
| E11 | Length | Word count over the budget for the type by more than 25%, or any paragraph over 100 words | Major (Minor if just over) |
| E12 | Risky links and files | Shortened URL (bit.ly), http:// link, attachment, embedded form, image-only email, key text or the only CTA inside an image, image with no alt text | Major |
| E13 | Template phrasing | "In today's fast-paced world", "We're thrilled to announce", "unlock", "elevate", "seamless", "game-changer", "Look no further", "I hope this email finds you well", unsupported "best", "revolutionary", "#1" | Minor (Major at 3+) |
| E14 | Pressure | Urgency or scarcity with no deadline or reason; guilt or shame ("you abandoned us"); threats ("deleted in 24 hours") | Major |
| E15 | Clarity | Acronyms the audience may not know, left undefined; sentences averaging over 25 words; a first sentence over 40 words | Major for a non-expert audience, else Minor |
| E16 | Send time | 22:00-06:00 recipient local time; B2B on a weekend | Major |
| E17 | Personalisation unused | Data the sender has is not used (a cart reminder that does not name the items) | Major |
| E18 | Health and money claims | "Cure", "clinically proven", "guaranteed returns", "#1 in the world" with no source | Blocker |

**Word budgets:** flash sale 75-150, promo 150-250, welcome 150-200,
re-engagement 100-150, newsletter 300-500, event invite 150-250, cart
reminder 75-150, transactional 50-150.

## Ranking order for email

Funnel order: inbox first (compliance, deceptive sender or subject, spam
signals), then the open (subject, preheader, sender), then the click (CTA,
clarity, offer, friction). Judge on the click, not the open: opens are
inflated by privacy features. When two fixes tie, the one that moves clicks
wins.

## Rewrite rules for email

- Subject 30-50 characters, with the count shown. Preheader 40-100
  characters that adds to the subject.
- One primary CTA button, action plus benefit from ledger facts ("See the new
  glazes"), placed in the first screen.
- Keep merge tokens in the platform's syntax with a fallback:
  `Hi {{first_name|default:"there"}}`.
- Stay inside the word budget. Footer: unsubscribe link plus postal address
  (use [postal address] if it is not in the ledger).

## Usually fine in email (do not flag)

A relevant emoji in a casual B2C subject; a personal sender name; a real
deadline with its reason; several "Read more" links in a newsletter; a
newsletter of 300-500 words; a short email inside its budget; required
regulatory text; personalisation from real purchase history; a personal
story opening from a named sender.

## You cannot check from pasted copy

Links working, rendering in each client, dark mode, authentication (SPF,
DKIM, DMARC), list health, complaint and bounce rates. Name them under "Not
checked". For performance data the user shares, the benchmarks and the
outcome each fix moves are in [email-weighting.md](email-weighting.md).

## Full scorecard (only when asked)

Score the 20 dimensions with [email-dimensions.md](email-dimensions.md) and
weight them with [email-weighting.md](email-weighting.md). A dimension at 1
is a Blocker in Second Read terms.
