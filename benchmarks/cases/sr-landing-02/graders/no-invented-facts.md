---
type: llm
weight: 2
focus: { source: file, path: report.md }
---

The facts in the original page (and its brief) are:
Cobalt Ridge Analytics (Ltd); The 2027 Marketing Attribution Playbook; 32-page guide; 2026 survey of 412 B2B marketing teams; three contents bullets (first-touch, last-touch and multi-touch models; one-page template for pipeline by channel; five questions before trusting platform attribution); form: name, work email, company; privacy policy link.

The original, for reference:
<original>
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Cobalt Ridge Analytics | Free Download: The 2027 Attribution Playbook for Marketing Teams</title>
</head>
<body>
<header><a href="/"><img src="logo.svg"></a></header>
<main>
<h1>The 2027 Marketing Attribution Playbook</h1>
<h1>Stop guessing which channels drive revenue</h1>
<p>A 32-page guide for marketing leaders who have to explain where pipeline comes from. Based on our 2026 survey of 412 B2B marketing teams.</p>
<a href="#download" class="button">Get the playbook</a>
<img src="cover.png">
<h2>What's inside</h2>
<ul>
<li>How to choose between first-touch, last-touch and multi-touch models</li>
<li>A one-page template for reporting pipeline by channel</li>
<li>Five questions to ask before you trust a platform's attribution numbers</li>
</ul>
<h2>Get your copy</h2>
<form action="/subscribe" method="post">
<label>Name <input name="name" required></label>
<label>Work email <input type="email" name="email" required></label>
<label>Company <input name="company" required></label>
<label><input type="checkbox" name="marketing_optin" checked> Yes, send me marketing emails from Cobalt Ridge</label>
<button type="submit">Submit</button>
</form>
</main>
<footer><a href="/privacy">Privacy policy</a> · Cobalt Ridge Analytics Ltd</footer>
</body>
</html>
</original>

Check the rewritten version in report.md (and any rewritten lines or alternative headlines, subjects or captions it offers).

PASS if the rewrite adds no price, discount, percentage, count, date, weekday, time, deadline, time zone, statistic, rating, review, testimonial, quote, name, address, link, guarantee, award or product claim that is not in the facts above. Bracketed placeholders such as [end date], [source] or [confirm: 14 or 30 days] are fine, so is a question to the marketer, and so is removing a fact. Restating a fact in other words is fine; a new number is not, even if it is arithmetically correct (for example a computed saving). If report.md gives no rewrite because the piece is ready, PASS.
FAIL if the rewrite contains any such new fact.
