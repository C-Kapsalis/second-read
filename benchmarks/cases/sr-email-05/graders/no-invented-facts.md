---
type: llm
weight: 2
focus: { source: file, path: report.md }
---

The facts in the original email (and its brief) are:
From Fork & Field, hi@forkandfield.com; recipient Sam; inactive 4 months; 14 boxes together; autumn menu with 22 new recipes; miso squash bowl Sam rated five stars in March; 'a special discount' with no amount; account deletion in 24 hours (claim); Fork & Field, 88 Mercer Lane, Portland, OR 97209.

The original, for reference:
<original>
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
</original>

Check the rewritten version in report.md (and any rewritten lines or alternative headlines, subjects or captions it offers).

PASS if the rewrite adds no price, discount, percentage, count, date, weekday, time, deadline, time zone, statistic, rating, review, testimonial, quote, name, address, link, guarantee, award or product claim that is not in the facts above. Bracketed placeholders such as [end date], [source] or [confirm: 14 or 30 days] are fine, so is a question to the marketer, and so is removing a fact. Restating a fact in other words is fine; a new number is not, even if it is arithmetically correct (for example a computed saving). If report.md gives no rewrite because the piece is ready, PASS.
FAIL if the rewrite contains any such new fact.
