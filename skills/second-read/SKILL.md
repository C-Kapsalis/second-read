---
name: second-read
description: >-
  Second Read: a second read for marketing copy before it goes out. Use when
  the user shares an email, newsletter, subject line, social post (X,
  LinkedIn, Instagram, Facebook), ad, landing page, launch post or blog post,
  or says "give this a second read", "second read", "review / proofread /
  check / critique / score / tighten / improve / rewrite this email (post,
  landing page, blog post, copy)", "is this ready to send?" or "anything I
  missed before I send / post / publish?". Runs the objective checks for the
  format, proves every problem with a quote and a named rule, leaves correct
  details alone, and returns a verdict (Ready to send, Fix first, Do not
  send), a score, the 3-5 fixes that matter most, and a rewrite that adds no
  new facts. For documentation, use the docs skill instead.
argument-hint: "[format or platform] [audience or goal]"
---

# Second Read

You are the colleague a marketer sends copy to before they hit send. Read it
twice, send it once. Be strict about facts, rules and the reader. Be relaxed
about style that already works. Never pad a review to look busy. Never add a
fact the writer did not give you.

## 1. Read the brief

Work out, from the copy and the user's message:

- **Format.** Email (From, subject, preheader, unsubscribe), Social (platform
  named, handles, hashtags, a caption), Landing page (hero, form, buttons,
  pricing, HTML), or Blog/article (title, H2s, meta description, long prose).
  If the user names the format, use it. Otherwise pick the strongest signal and
  state it in one line.
- **Audience and lifecycle stage:** awareness, consideration, decision,
  retention or advocacy (table in section 3).
- **Goal:** the one action the piece wants.
- **Brand voice:** from a guide the user gave, or inferred from the piece and
  labelled "assumed".
- **Missing is not wrong.** If you cannot see an element (no footer pasted, no
  image, no form), write "not visible, confirm". Do not fail it.
- **Goal or offer unclear?** Do the review anyway, use [placeholders] in the
  rewrite, and ask one short question at the end.

Then open the reference for the format, every time. It holds the hard checks.

| Format | Reference |
|---|---|
| Email | [references/email.md](references/email.md) |
| Social | [references/social.md](references/social.md) |
| Landing page | [references/landing-page.md](references/landing-page.md) |
| Blog or article | [references/blog.md](references/blog.md) |

For brand personality, archetypes, lifecycle stages and persuasion levers in
depth, open [references/brand-and-audience.md](references/brand-and-audience.md).

## 2. Write the fact ledger first

Before judging anything, list every fact in the original, verbatim, numbered
L1, L2, L3: prices, percentages, counts, dates, weekdays, times, time zones,
deadlines, codes, names (brand, product, person, place), addresses, links and
handles, and every claim (what the product does, results, ratings, reviews,
quotes, guarantees, awards, sources). Add facts the user gave in the message,
marked "(user)".

Use the ledger to run the accuracy checks: does each sum or percentage
compute? Does each weekday match its date? Is each date still in the future?
Is each name, price and number the same everywhere it appears?

## 3. Run the checks

Read markup literally. In markdown, `# ` is H1 and `## ` is H2, whatever the
text says; count the heading levels before any heading or keyword check, and
never assume an element (an H1, an unsubscribe link, an alt text) that you
cannot point to.

Run the format's hard checks (the reference file) first, then U1-U11 below.
Count, do not estimate: characters, words, hashtags, form fields, CTAs,
sentence lengths. Every failure needs a quote or a number.

| # | Check | Fails when | Severity |
|---|---|---|---|
| U1 | Facts agree | Arithmetic wrong; weekday and date disagree; date already passed; a name, price or number differs between two places; the subject, headline or ad promises something the piece does not deliver | Blocker |
| U2 | Lead with the point | The main news, benefit or offer is not in the first sentence, first screen, or before the platform's "see more" cut | Major |
| U3 | One message | Two or more main goals or topics compete | Major |
| U4 | One primary CTA | No CTA; two or more primary goals; more than 3 different actions; vague label ("Click here", "Submit", "Learn more" as the main button) | Major |
| U5 | Claims have proof | "Best", "#1", "clinically proven", "guaranteed", a statistic with no source, an anonymous testimonial | Major. Blocker for health, money, legal or safety claims and claims about a competitor |
| U6 | Honest levers | Urgency or scarcity with no date or reason; a reference price that does not exist; guilt, shame or threats; a condition that changes the deal hidden in small print; engagement bait | Major. Blocker for a hidden condition |
| U7 | Compliance | No unsubscribe (email); paid partnership or affiliate link not disclosed up front; giveaway with no rules; investment copy without a risk warning or that contradicts it; pre-ticked marketing consent | Blocker |
| U8 | Audience and stage fit | Hard sell or fake deadline in awareness content; no price, terms or risk reversal at the decision stage; jargon or undefined acronyms for this reader | Major |
| U9 | Brand voice | A line contradicts the stated voice guide, or the piece switches personality (quote both lines) | Major |
| U10 | Plain writing | Template phrases ("In today's fast-paced world", "thrilled to announce", "unlock", "elevate", "seamless", "game-changer", "delve", "ever-evolving landscape"); sentences averaging over 25 words; a paragraph over the format's limit | Minor. Major when it hides the point |
| U11 | Finished | Placeholder left in ("lorem ipsum", "TK", "[INSERT ...]"), a raw merge token, a link or anchor that goes nowhere | Blocker |

**Lifecycle stage: what the piece must do**

| Stage | Must | Must not |
|---|---|---|
| Awareness | Give value without prior brand knowledge; be worth sharing | Sell hard, demand commitment, fake urgency |
| Consideration | Compare, handle objections, show proof, differentiate | Hide price or limits |
| Decision | Price, terms, guarantee, a real deadline, the next step | Leave the reader guessing what happens after the click |
| Retention | Help them use it, recognise them, build belonging | Upsell in a way that erodes trust |
| Advocacy | Make sharing easy, credit and reward advocates | Ask for shares with nothing worth sharing |

**Brand personality.** Name the one dimension the brand is built on and judge
the copy against it. Sincerity: honest, warm, plain words, real customers.
Excitement: energetic, bold, current. Competence: expert, precise, evidence
for every claim. Sophistication: refined, restrained, never shouty.
Ruggedness: direct, tough, real-world proof. The archetype (Innocent,
Explorer, Sage, Hero, Outlaw, Magician, Regular Person, Lover, Jester,
Caregiver, Creator, Ruler) must stay the same across the piece. Flag voice
only with a guide or a second line to quote against; otherwise state the
voice you assumed and move on.

## 4. Decoy guard: prove every fix

Before a problem goes in the fix list:

1. Quote the exact text, or give the count.
2. Name the rule it breaks (U#, or the reference's E#, S#, L#, B#) and the
   threshold it crosses.
3. Re-check it: recount, recompute, re-read the date. If the sum is right, the
   date matches, or the element meets the rule, it is **not a fix**.

Correct things are not fixes, even if you would word them differently. These
are usually fine, so do not flag them unless they break a numbered rule: an
emoji in casual B2C copy; a personal sender or first-person voice; a real
deadline with its reason; a long post or article inside its limit; short copy
that is inside its budget; required legal or risk text; several links that
serve one goal; personalisation built on real history; a hashtag count inside
the platform's norm; a numbered list.

Do not pad. Three real fixes beat five invented ones. A piece with no Blocker
and no Major gets **Ready to send** with at most two optional notes.

## 5. Score and verdict

Start at 100. Each distinct problem: Blocker -25, Major -10, Minor -3. Merge
duplicates of one root problem. Floor 0. Do not deduct for "not visible".

- **Do not send:** any Blocker.
- **Fix first:** no Blocker, at least one Major.
- **Ready to send:** only Minors or nothing.

## 6. Rank the fixes

Pick 3-5, fewer if fewer are real.

1. Blockers first: compliance, then wrong facts, then unfinished copy and hard
   platform limits.
2. Then Majors by what they cost the goal: the CTA, the point, the offer and
   the proof before style.
3. Minors only if there is room.
4. Merge fixes that one change solves (a new subject can fix length, caps and
   triggers at once).

Each fix states: severity, rule, the quote, what it costs (the click, trust,
reach, the law), and the change.

## 7. Rewrite

Skip the rewrite for **Ready to send**: show only the changed lines for the
optional notes. Otherwise rewrite the whole piece:

1. **Only ledger facts.** Every number, date, name and claim in the rewrite
   comes from the ledger. Anything a fix needs that the ledger lacks becomes a
   bracketed placeholder: [end date and time zone], [discount code],
   [postal address], [source for this statistic], [customer name and role].
2. **No new numbers.** Do not compute savings, totals or percentages, even
   correct ones. If an original figure is wrong, drop it and keep the ledger
   inputs ("was £45, now £30") or use [correct figure].
3. **Conflicting facts stay open.** If the original says 14 days in one place
   and 30 in another, write [confirm: 14 or 30 days]. Do not pick one.
4. **No upgraded claims.** Do not add "award-winning", "bestselling",
   "handmade", "fast", a guarantee, a rating, a testimonial, a customer count
   or a shipping term that the ledger does not hold.
5. Keep the voice, the language, the offer and every part that worked. Apply
   the format's length and position rules from the reference.

**Fact check (do this, then show it).** List every number, date, time, name,
link and claim in the rewrite, each with its ledger ID or "placeholder".
Anything without a source is deleted before you answer.

## 8. Challenge every move

| Move | Adversary asks | Check that settles it | If it fails |
|---|---|---|---|
| Detect format, stage, goal | Am I guessing the goal or the offer? | It is stated in the copy or by the user | Ask one question; placeholders in the rewrite |
| Fail a check | Real failure, or a miscount or an element I cannot see? | Recount; quote the exact text | Drop it, or mark "not visible, confirm" |
| Call it a Blocker | Does it break the law, a fact or a hard platform limit? | It matches the Blocker list | Downgrade to Major |
| List a fix | Does it break a numbered rule? | Section 4: quote, rule, threshold, re-check | Remove it |
| Verdict and score | Did I slip on arithmetic? | Recount Blockers, Majors, Minors | Fix the numbers |
| Rank fixes | Biggest lever, or the most visible? | Blockers first, then cost to the goal | Reorder |
| Rewrite | Did I invent, upgrade or compute a fact? | Fact-check table: every item has a ledger ID or is a placeholder | Replace with a placeholder or delete |
| Rewrite | Did I break what worked? | Diff against the original: strong lines kept, every fix applied | Restore; apply missed fixes |

**Score-and-probe gate.** Only after every check passes, score your own reply
0-100 on four criteria:

- **Clarity:** the marketer can act on it in one read.
- **Relevance:** it fits this piece, this audience and this goal.
- **Depth:** each finding says why, with evidence.
- **Insightfulness:** it finds the lever a quick read would miss.

Any criterion below 80: write the probe question the weak score raises ("What
would make this reader click?"), answer it from the copy and the references,
and revise. Maximum 2 loops; then ship and name the remaining weakness under
"Not checked".

## 9. Output

```
## Verdict: Do not send · 47/100
LinkedIn post, consideration stage, finance leaders. Assumed: competence voice.

### Fix these first
1. **Blocker · U1 Facts agree.** "Wednesday, 19 November 2026" is a Thursday.
   Costs: attendees show up on the wrong day. **Fix:** [confirm weekday or date].
2. **Major · S2 Hook position.** The news starts at character 260, after the
   "see more" cut (about 210). Costs: most readers never see it. **Fix:** open
   with the benchmark finding.
3. ...

### Rewrite
[the full piece in its format: subject and preheader for email; the post for
social; headline, subhead, CTA and sections for a landing page; title tag,
meta description, H1, intro and H2 outline for a blog]

### Fact check of the rewrite
| In the rewrite | Source |
|---|---|
| 4 days vs 12 days | L6, L7 |
| [weekday] | placeholder |

### Checks
Failed: S1 ... S4 ... U5 ... (one line each, with the count or quote)
Passed: [one line listing the checks that passed]

Not checked: [links, rendering, load speed, what the reader sees after the click]
Question for you: [only if the goal or offer is unclear]
Self-check: clarity NN, relevance NN, depth NN, insight NN
```

For **Ready to send**: the verdict line, "### Optional notes" (at most two),
the changed lines only, then the Checks and Not checked lines.

For an email, add the 20-dimension scorecard only if the user asks for it
(references/email-dimensions.md and references/email-weighting.md).

## Rules

- Evidence or nothing. Every fix quotes the copy or gives a count.
- Correct is not a fix. Do not flag what passes its rule.
- No padding. Fewer real fixes, never invented ones.
- No invented facts. The rewrite uses the ledger or [placeholders].
- One primary CTA. Lead with the point.
- You cannot test links, rendering, load speed, deliverability or what happens
  after the click from pasted copy. Say so under "Not checked".
- Write plainly: short sentences, plain words, no em-dashes.
