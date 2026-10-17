---
type: llm
weight: 3
focus: { source: file, path: report.md }
---

The article has 4 planted problems:
- B6.1: Unsourced, damaging claim about a named competitor: "Dealdesk has a history of leaking customer data"
- B6.2: Competitor price stated with no date or source ("Dealdesk costs $99 per user per month")
- B6.3: Calls itself "an unbiased review" without saying it is written by Pipewise
- B6.4: No H1: the page title is an H2

A problem counts as found when report.md identifies the same problem with evidence (a quote, a count, or the specific element), in the fix list or the list of failed checks. Wording need not match. Vague remarks ("the hook could be stronger") do not count, and "not visible, please confirm" counts as not found when the element is in the article.

PASS if at least 3 of the 4 problems are found.
FAIL otherwise.
