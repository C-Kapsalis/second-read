---
type: llm
weight: 3
focus: { source: file, path: report.md }
---

The email has 4 planted problems:
- 7.1: Jargon and undefined acronyms (CDC, OLAP, ELT) for a non-technical audience; first sentence is 47 words
- 7.2: Announces "new pricing tiers" with no price
- 7.3: CTA "Submit", with no stated action or benefit
- 7.4: Scheduled Saturday 02:00 local for a B2B audience

A problem counts as found when report.md identifies the same problem with evidence (a quote, a count, or the specific element), in the fix list or the list of failed checks. Wording need not match. Vague remarks ("the hook could be stronger") do not count, and "not visible, please confirm" counts as not found when the element is in the email.

PASS if at least 3 of the 4 problems are found.
FAIL otherwise.
