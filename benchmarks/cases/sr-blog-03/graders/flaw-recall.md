---
type: llm
weight: 3
focus: { source: file, path: report.md }
---

The article has 4 planted problems:
- B3.1: Wrong percentage: 2.0% to 3.0% is a 50% increase, not 33%
- B3.2: Sample size given two ways: 1,200 surveyed vs "the 800 respondents" with no explanation that only 800 answered
- B3.3: A 2017 statistic presented as current ("Today, 61%...")
- B3.4: Meta description is empty

A problem counts as found when report.md identifies the same problem with evidence (a quote, a count, or the specific element), in the fix list or the list of failed checks. Wording need not match. Vague remarks ("the hook could be stronger") do not count, and "not visible, please confirm" counts as not found when the element is in the article.

PASS if at least 3 of the 4 problems are found.
FAIL otherwise.
