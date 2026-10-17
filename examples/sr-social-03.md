# sr-social-03: a paid skincare caption

A synthetic benchmark fixture, written for this benchmark with four flaws
planted on purpose. The case is in
[../benchmarks/cases/sr-social-03/](../benchmarks/cases/sr-social-03/); the
answer sheet is in
[../benchmarks/builder/second-read-benchmark.md](../benchmarks/builder/second-read-benchmark.md).

Both reports below are from the run of 2026-10-17 behind the numbers in the
README: run 1 of 3 in each arm, Claude Haiku in Claude Code, the same prompt
and the same file. They are copied from the `report.md` each run wrote,
unedited. Run folders: `e-Un862E` (without) and `e-vVT2Cb` (with), as listed
in [../benchmarks/eval.log](../benchmarks/eval.log).

## The scores

| Grader | Without | With |
|---|---|---|
| Planted flaws found (3 of 4 needed) | FAIL (votes FAIL FAIL FAIL) | PASS |
| Blocking flaws first, "do not post" verdict | PASS | PASS |
| Correct details left alone | PASS | PASS |
| No invented facts (Haiku judge) | FAIL (votes FAIL FAIL FAIL) | PASS |
| Run score | 0.38 | 1.00 |

The other two runs in each arm: without scored 0.75 and 0.38, with scored
1.00 and 1.00.

## The four planted flaws

1. The paid partnership is not disclosed up front: `#ad` is the last of 12
   hashtags, after the cut, and the in-app label is off.
2. A medical claim for a cosmetic: "it cleared my eczema in 3 days".
3. A URL in an Instagram caption is not clickable.
4. The product is not named in the first 125 characters, the part people
   see before "more"; the opening is about the move.

The decoys, correct details a careless reviewer flags: the discount code
details (JUNI15, 15% off, until 30 November 23:59 GMT) and emojis in a
creator's casual voice.

## What each run did

| | Without Second Read | With Second Read |
|---|---|---|
| Buried `#ad`, label off | Found | Found (Blocker) |
| Eczema claim | Found | Found (Blocker) |
| URL not clickable | Missed; the rewrite keeps the URL in the caption | Found; the rewrite says "Link in bio" |
| Product after the cut | Missed; the rewrite first names the balm at character 284 | Found; the rewrite names the balm at character 58 |
| New claim in the rewrite | "my skin feels so much calmer and more comfortable" | None; her experience is a placeholder |

The new claim has no number, link or code in it, so `check_facts.py` (which
counts only those) does not flag this rewrite. The Haiku judge failed it on
all three votes. I show it because it is the kind of invention a creator
would have to defend.

## The original

The prompt, as both arms saw it:

~~~text
resources/post.txt is the post. This is the caption from our creator partner for Thursday. Can you give it a second read before she posts it?

Context: Instagram caption by creator Juniper Hale (@juniperhale). This is a paid partnership: Dewlight Skin paid for the post and the code is an affiliate code. The paid-partnership label in the app is not switched on. Audience: her followers, UK.

If it needs changes, send me a fixed version too, as one fenced code block I can paste.

Save report.md in the current working directory, not inside resources/.
~~~

`resources/post.txt`:

~~~text
Okay so you guys know I've been SO busy lately with the move and everything and honestly my skin has been paying for it 😩 between the stress and the new flat's dry air it's been a lot. Enter the Dewlight Barrier Balm. I've used it every night for two weeks and it cleared my eczema in 3 days. Like, actually gone. 🙌

Shop it at https://dewlightskin.com/balm and use my code JUNI15 for 15% off until 30 November, 23:59 GMT.

#skincare #skincareroutine #eczema #barrierrepair #selfcare #glowup #cleanbeauty #skintok #dryskin #nightroutine #skincarecommunity #ad
~~~

## Without Second Read (run 1, score 0.38)

~~~~markdown
# Review: Juniper Hale Instagram caption (Dewlight Skin paid partnership)

Source: `resources/post.txt`
Posting: Thursday, UK audience, paid by Dewlight Skin, affiliate code JUNI15.

**Verdict: do not post as written.** Two issues need fixing before it goes live. Both are the kind the UK ASA/CAP Code and CMA consumer-law rules target. This is a compliance read, not legal advice.

## Issues

### 1. Disclosure is buried and the platform label is off (high)

- The only disclosure is `#ad`, the last of 12 hashtags at the bottom of the caption. Under the ASA/CAP influencer guidance, a disclosure has to be clear and upfront, before the reader has to decide whether to keep reading. A tag at the end of a hashtag block does not meet that bar.
- The caption does not say the post is paid, or that the code is an affiliate code that earns her a commission. Affiliate codes should be disclosed as well.
- Instagram's "Paid partnership" label is not switched on. Turn it on. It is a separate requirement from the in-caption disclosure, and both should be used.

**Fix:** put the disclosure on the first line of the caption and turn on the Paid partnership label.

### 2. Medicinal claim: a cosmetic is said to cure eczema (high)

- "it cleared my eczema in 3 days. Like, actually gone." An eczema claim is a medical condition claim. Cosmetics cannot be advertised as treating, curing, or clearing medical conditions. This is one of the most common reasons ASA rulings go against skincare ads.
- A testimonial does not get around this. A personal account of a cure is still the claim, and the brand would be responsible for it.
- The "3 days" detail is a specific result. It needs evidence, and it is the kind of result a reader would take as typical.
- The hashtag `#eczema` makes the same medical claim and should go too.

**Fix:** describe her own experience in general terms (skin feels calmer and more comfortable), not as a treatment outcome. Remove `#eczema`.

### 3. Smaller points (lower)

- `#cleanbeauty`: "clean" has no fixed legal meaning, so it is hard to substantiate. Keep it only if Dewlight can back it up. The fixed version drops it.
- `#barrierrepair`: "repair" is a functional claim. It is acceptable if Dewlight holds evidence for it (for example, moisturisation or barrier-support data). Otherwise, soften it to `#barriercare` or drop it.
- The "two weeks, every night" usage detail is fine only if it is true. Confirm with her before posting.
- Discount terms (15% off, JUNI15, until 30 November 23:59 GMT) are clear. Confirm with Dewlight that the code is live and the end date is right.

## Before she posts

1. Turn on Instagram's Paid partnership label, with Dewlight Skin tagged as the partner.
2. Use the fixed version below, or have her rewrite the first line in her own voice. Keep the disclosure at the top.
3. Confirm with her that every statement in the caption is true for her. That includes the two-week timeline and the calmer-skin experience.
4. Check that Dewlight has substantiation for any product claim she keeps.

## Suggested fixed version

```
#ad Paid partnership with Dewlight Skin. I earn a commission when you use my code.

Okay so you guys know I've been SO busy lately with the move and everything, and honestly my skin has been feeling it 😩 between the stress and the dry air in the new flat, it's been a lot. Enter the Dewlight Barrier Balm. I've been using it every night for two weeks and my skin feels so much calmer and more comfortable. 🙌

Shop it at https://dewlightskin.com/balm and use my code JUNI15 for 15% off until 30 November, 23:59 GMT.

#skincare #skincareroutine #barrierrepair #selfcare #glowup #skintok #dryskin #nightroutine #skincarecommunity
```

Changes from the original:
- Disclosure moved to the first line and states the affiliate commission.
- "cleared my eczema in 3 days / actually gone" replaced with a general, subjective description of her experience.
- Removed `#eczema`, `#cleanbeauty`, and the trailing `#ad`, which now sits at the top.
- Everything else (story, usage, link, code, deadline) is kept.
~~~~

## With Second Read (run 1, score 1.00)

~~~~markdown
## Verdict: Do not send · 30/100
Instagram caption, paid partnership with Dewlight Skin, affiliate code, UK followers, creator Juniper Hale (@juniperhale). Consideration/decision stage. Assumed: creator voice (sincere, casual, first person).

### Fix these first
1. **Blocker · S10 Health claim (merged with #eczema hashtag).** "it cleared my eczema in 3 days. Like, actually gone." A cosmetic is presented as curing a skin condition, based on one person's two weeks of use. Costs: the ASA and CAP code treat this as a medical claim the product cannot support; the post can be taken down and the partner and creator are both exposed. **Fix:** delete the eczema outcome and the #eczema hashtag. Keep her own experience in her own words, with no cure, treatment or medical outcome.
2. **Blocker · S5 Paid partnership (U7).** The paid partnership is real, the platform label is off, and the only disclosure is "#ad" as the 12th hashtag at the end. Costs: this is a clear breach of UK ad disclosure rules, and the platform label is the one that tells followers and the brand. **Fix:** switch on the platform's Paid partnership label before posting, and open the caption with "Paid partnership with Dewlight Skin".
3. **Major · S2 Hook position.** "Enter the Dewlight Barrier Balm" starts after the "more" cut (about 125 characters). The visible part is backstory: "Okay so you guys know I've been SO busy lately with the move…". Costs: most followers scroll past without seeing what is being sold. **Fix:** put the product in the first line.
4. **Major · S4 Link placement.** "Shop it at https://dewlightskin.com/balm" is a URL in an Instagram caption, which is not clickable. Costs: the CTA cannot be acted on from the post. **Fix:** "Link in bio" (and a link sticker in Stories), with the URL kept as text for anyone who copies it.

### Rewrite
```
Paid partnership with Dewlight Skin. I've been using the Dewlight Barrier Balm every night for two weeks.

Okay so you guys know I've been SO busy lately with the move and everything and honestly my skin has been paying for it 😩 between the stress and the new flat's dry air it's been a lot.

[Your honest experience with the balm, in your own words. No cure, treatment or medical claims.]

Get it with my code JUNI15 for 15% off until 30 November, 23:59 GMT. Link in bio: [confirm bio link goes to https://dewlightskin.com/balm].

#ad #skincare #skincareroutine #barrierrepair #selfcare #glowup #cleanbeauty #skintok #dryskin #nightroutine #skincarecommunity
```

### Fact check of the rewrite
| In the rewrite | Source |
|---|---|
| Paid partnership with Dewlight Skin | user (paid partnership, brief) |
| Dewlight Barrier Balm | L4 |
| every night for two weeks | L5 |
| the move, the stress, the new flat's dry air | L1, L2, L3 |
| JUNI15, 15% off | L8 |
| until 30 November, 23:59 GMT | L9 |
| dewlightskin.com/balm | L7 (placed in bio: confirm) |
| [her experience] | placeholder |
| #eczema removed | removed (S10) |

### Checks
Failed: S10 ("cleared my eczema in 3 days. Like, actually gone."; #eczema); S5 (paid partnership label off; #ad at position 12 of 12 hashtags); S2 (product name after about character 125); S4 ("Shop it at https://dewlightskin.com/balm", URL in caption).
Passed: S1 (well under 2,200 characters, 11 hashtags against a 30 limit); S3 (hashtag count); S9 (code, 15%, date and time with GMT are present and consistent, no arithmetic to check); S7 (no engagement bait); S8 (one action, shop with the code); S13 (no list of emoji bullets; no image text visible).

Not checked: the image or video, the link destination, whether the platform's Paid partnership label is switched on, whether the discount code works, reach and engagement, and what the reader sees after the click. The result in "cleared my eczema" cannot be verified from copy, and the rewrite does not repeat it.

Question for you: none. The goal (sales through the code) and the offer are clear.
Self-check: clarity 90, relevance 90, depth 85, insight 85.
~~~~
