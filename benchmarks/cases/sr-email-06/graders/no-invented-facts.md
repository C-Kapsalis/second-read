---
type: llm
weight: 2
focus: { source: file, path: report.md }
---

The facts in the original email (and its brief) are:
From Priya at Lumen Botanics, priya@lumenbotanics.com; recipient Alex; the sign-up form promised 15% off the first order (context); Dawn Renewal Serum; claims 'clinically proven #1 serum in the world' and 'cure your acne in just 7 days' (unsupported); founder's 3-step routine: Cloud Gel Wash morning and night, two drops of Dawn Renewal Serum on damp skin, Daily Barrier Cream; Lumen Botanics, 15 Orchard Row, Asheville, NC 28801; unsubscribe and privacy links.

The original, for reference:
<original>
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
</original>

Check the rewritten version in report.md (and any rewritten lines or alternative headlines, subjects or captions it offers).

PASS if the rewrite adds no price, discount, percentage, count, date, weekday, time, deadline, time zone, statistic, rating, review, testimonial, quote, name, address, link, guarantee, award or product claim that is not in the facts above. Bracketed placeholders such as [end date], [source] or [confirm: 14 or 30 days] are fine, so is a question to the marketer, and so is removing a fact. Restating a fact in other words is fine; a new number is not, even if it is arithmetically correct (for example a computed saving). If report.md gives no rewrite because the piece is ready, PASS.
FAIL if the rewrite contains any such new fact.
