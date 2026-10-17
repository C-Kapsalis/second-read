---
type: llm
weight: 2
focus: { source: file, path: report.md }
---

The facts in the original email (and its brief) are:
From Ember Grind, orders@embergrind.com; recipient Chris; cart items (from the context): Ember Burr Grinder Pro and 2 x Single-Origin Ethiopia 250g; founded 2014 in a garage in Leeds by Tom and Aisha; roast six days a week in small batches; roast date on every bag; beans from Ethiopia, Colombia, Guatemala and Rwanda; two years testing burr shapes; compostable bags, recycled boxes, carbon offset via a reforestation partner in Uganda, impact report every spring; code EMBER10 for 10% off, valid until Sunday 23:59 CET; link https://bit.ly/3xEmbr; Ember Grind Ltd, Unit 4, Canal Works, Leeds LS1 4BR, United Kingdom; unsubscribe and privacy links.

The original, for reference:
<original>
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
</original>

Check the rewritten version in report.md (and any rewritten lines or alternative headlines, subjects or captions it offers).

PASS if the rewrite adds no price, discount, percentage, count, date, weekday, time, deadline, time zone, statistic, rating, review, testimonial, quote, name, address, link, guarantee, award or product claim that is not in the facts above. Bracketed placeholders such as [end date], [source] or [confirm: 14 or 30 days] are fine, so is a question to the marketer, and so is removing a fact. Restating a fact in other words is fine; a new number is not, even if it is arithmetically correct (for example a computed saving). If report.md gives no rewrite because the piece is ready, PASS.
FAIL if the rewrite contains any such new fact.
