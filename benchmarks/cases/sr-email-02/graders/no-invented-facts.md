---
type: llm
weight: 2
focus: { source: file, path: report.md }
---

The facts in the original email (and its brief) are:
From Dana Whitfield, Head of Finance Ops at Tallyhawk, dana@tallyhawk.io; webinar Thursday 12 November at 4 PM (no time zone given); two controllers from mid-size companies; close cut from 10 days to 3, 70%; automated reconciliations; their checklist and a template; 2026 Close Benchmark ebook; 1:1 demo; LinkedIn; Tallyhawk Inc., 410 Harbor Street, Suite 900, Boston, MA 02110; unsubscribe and manage preferences links; sent Tuesday 10:00 local.

The original, for reference:
<original>
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
</original>

Check the rewritten version in report.md (and any rewritten lines or alternative headlines, subjects or captions it offers).

PASS if the rewrite adds no price, discount, percentage, count, date, weekday, time, deadline, time zone, statistic, rating, review, testimonial, quote, name, address, link, guarantee, award or product claim that is not in the facts above. Bracketed placeholders such as [end date], [source] or [confirm: 14 or 30 days] are fine, so is a question to the marketer, and so is removing a fact. Restating a fact in other words is fine; a new number is not, even if it is arithmetically correct (for example a computed saving). If report.md gives no rewrite because the piece is ready, PASS.
FAIL if the rewrite contains any such new fact.
