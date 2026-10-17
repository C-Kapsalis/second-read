---
type: llm
weight: 3
focus: { source: file, path: report.md }
---

The article has 4 planted problems:
- B5.1: Unfinished draft: "[link to case study]", "TK: add the bakery's before and after numbers", and an empty final section
- B5.2: Undefined acronyms for a non-marketer audience: CDP, MMM, MTA
- B5.3: Template phrasing: "It's important to note", "navigate the ever-changing marketing landscape", "delve"
- B5.4: A first sentence of about 64 words in "Why measurement feels hard"

A problem counts as found when report.md identifies the same problem with evidence (a quote, a count, or the specific element), in the fix list or the list of failed checks. Wording need not match. Vague remarks ("the hook could be stronger") do not count, and "not visible, please confirm" counts as not found when the element is in the article.

PASS if at least 3 of the 4 problems are found.
FAIL otherwise.
