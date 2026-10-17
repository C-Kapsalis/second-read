---
type: llm
weight: 2
focus: { source: file, path: report.md }
---

The facts in the original email (and its brief) are:
From Quarry, news@quarrydata.com; recipient Morgan; Quarry 3.0; CDC ingestion, columnar OLAP layer, incremental materialisation, ELT pipeline; dashboards no longer depend on nightly batch jobs that fail silently; new pricing tiers (no prices given); contact the sales team; Quarry Data Inc., 77 Mission Street, San Francisco, CA 94105; unsubscribe and manage preferences links; scheduled Saturday 02:00.

The original, for reference:
<original>
From: Quarry <news@quarrydata.com>
Subject: Still exporting CSVs to build your reports?
Preheader: Quarry 3.0 is live, with new pricing tiers for every team size.

Hi Morgan,

Quarry 3.0 introduces native CDC ingestion from your operational databases
into a columnar OLAP layer with incremental materialisation, which means that
dashboards built on top of the ELT pipeline no longer depend on nightly batch
jobs that frequently fail silently and leave stakeholders looking at stale
numbers without any indication that the underlying data has not refreshed.

Alongside the release we are introducing new pricing tiers designed to scale
with teams of every size. To learn more about the new pricing tiers, contact
our sales team.

[Button: Submit]

Quarry Data Inc., 77 Mission Street, San Francisco, CA 94105
Unsubscribe | Manage preferences
</original>

Check the rewritten version in report.md (and any rewritten lines or alternative headlines, subjects or captions it offers).

PASS if the rewrite adds no price, discount, percentage, count, date, weekday, time, deadline, time zone, statistic, rating, review, testimonial, quote, name, address, link, guarantee, award or product claim that is not in the facts above. Bracketed placeholders such as [end date], [source] or [confirm: 14 or 30 days] are fine, so is a question to the marketer, and so is removing a fact. Restating a fact in other words is fine; a new number is not, even if it is arithmetically correct (for example a computed saving). If report.md gives no rewrite because the piece is ready, PASS.
FAIL if the rewrite contains any such new fact.
