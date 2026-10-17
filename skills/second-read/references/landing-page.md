# Landing pages: hard checks

A landing page has one job: turn the visitor the ad, email or search result
sent into the one action. Read it as the visitor does: first screen, then the
scroll. The page may arrive as Markdown, HTML or a description. If you only
have a description, mark visual checks "not visible, confirm".

**The first screen** is everything before the first section break or about the
first 100 words, whichever comes first. In HTML, the content before the
second heading.

## Conversion checks

| # | Check | Fails when | Severity |
|---|---|---|---|
| L1 | Message match | The page contradicts or drops what the traffic source promised (the ad says 30 days and no card; the page says 14 days and asks for a card). Compare offer, terms, product name and price | Blocker when the promise is contradicted; Major when it is dropped |
| L2 | Headline | The H1 does not say what it is and what the visitor gets ("Welcome to the future of work", "Smile!") | Major |
| L3 | First screen | Missing any of: a headline with the benefit, a supporting line, the primary CTA, one proof or trust element | Major when the CTA is missing; Minor otherwise |
| L4 | One goal | More than one primary CTA to different goals in the hero; more than 3 different actions on the page | Major |
| L5 | CTA label | Vague: "Submit", "Click here", "Learn more", "Go" | Major |
| L6 | Form friction | More fields than the offer needs: over 3 for a download or newsletter, over 5 for a trial or demo; a phone, budget or card field the offer does not need | Major |
| L7 | Price and terms | The offer is announced but its price, length, deadline, or what happens after the click is missing; two different prices for the same thing | Major. Blocker for two different prices |
| L8 | Proof | Testimonial with no name and role; a rating with no count; "#1", "best", "guaranteed" with no source | Major |
| L9 | Honest urgency | A countdown or "today only" that contradicts another date on the page, or has no reason | Major |
| L10 | Consistency | The same fact differs in two places (hours, price, subscriber count, phone number, product spec) | Blocker for price, dates and claims; Major for contact details |
| L11 | Consent and privacy | Marketing consent box pre-ticked; no privacy note near a form that collects personal data | Blocker for pre-ticked consent; Minor for a missing note |
| L12 | Health, money, safety claims | "Painless", "permanent", "guaranteed results", returns promised | Blocker |
| L13 | Finished | "Lorem ipsum", "[INSERT ...]", "TK", a raw token, or an in-page link (`href="#x"`) with no element `id="x"` | Blocker |
| L14 | Scannable | A paragraph over 80 words; no subheads in a page over 300 words; key facts only inside images | Minor (Major when the CTA or offer is buried) |

## SEO checks (pages meant to rank in search)

Skip this block for pages that only receive paid or email traffic, and say
so. The target keyword is the one the user names; otherwise infer it from the
H1 and say it is assumed.

| # | Check | Fails when | Severity |
|---|---|---|---|
| L15 | Title tag | Missing; over 60 characters; target keyword missing; keyword repeated 3 or more times | Major (Minor for length alone) |
| L16 | Meta description | Missing; over 160 characters; does not say what the visitor gets | Minor (Major when missing) |
| L17 | One H1 | No H1, or more than one H1 (count `#` marks; a page title written as `## ` is an H2) | Major |
| L18 | Keyword placement | The target keyword is missing from the URL slug, the H1, or every H2 | Major for H1 or URL; Minor for H2 |
| L19 | Intent match | The page type does not fit the query's stage: a hard sell for a "what is" or "how to" query; a definition page for a "discount code" or "buy" query | Major |
| L20 | Images | No alt text; file names like IMG_4532.jpg instead of descriptive names | Minor |
| L21 | Anchor text | Internal links reading "click here" or "learn more" instead of describing the destination | Minor |
| L22 | Stuffing | The keyword more than about 3 times in a 50-word stretch, or over 10% of words; a forced, unnatural phrase | Major |
| L23 | Cannibalisation | The user says another page already targets the same keyword | Major |
| L24 | Thin or duplicate | Under about 150 words of real content for a page meant to rank; copied sections | Major |

Search intent by stage: awareness queries ("what is", "how to", "tips")
want definitions and help; consideration ("best X for Y", "A vs B",
"reviews") wants comparison and differentiation; action ("X discount", "X
sale", "X same-day delivery") wants the deal and a reason to act now. One
primary keyword per page; broad terms on top-level pages, specific long-tail
terms on deeper pages.

## Rewrite rules for landing pages

Give the rewrite as: title tag (with count), meta description (with count),
H1, supporting line, primary CTA label, then each section in order (proof,
what you get, price and terms, form fields, FAQ). Keep every price and term
from the ledger; where two conflict, write [confirm: X or Y].

## Usually fine on a landing page (do not flag)

A pricing table whose annual price is a correct multiple of the monthly one;
a privacy note under the form; a 3-field form; a sourced statistic; a stated
refund policy; a venue address; a review count with a rating; a "no
obligation" free consultation; a single-field email form; navigation links on
a product page that is not a campaign page.

## You cannot check from pasted copy

Load speed, mobile layout and tap targets, HTTPS, what the form does on
submit, analytics tags, search ranking and engagement. Name them under "Not
checked".
