---
type: llm
weight: 3
focus: { source: file, path: report.md }
---

The article has 4 planted problems:
- B4.1: Medical claim: "ashwagandha cures anxiety for many people within weeks"
- B4.2: Affiliate links with no disclosure
- B4.3: Keyword stuffing: "ashwagandha" 7 times in the first paragraph of 56 words
- B4.4: No H2 subheadings in the body

A problem counts as found when report.md identifies the same problem with evidence (a quote, a count, or the specific element), in the fix list or the list of failed checks. Wording need not match. Vague remarks ("the hook could be stronger") do not count, and "not visible, please confirm" counts as not found when the element is in the article.

PASS if at least 3 of the 4 problems are found.
FAIL otherwise.
