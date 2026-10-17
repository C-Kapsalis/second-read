---
type: llm
weight: 3
focus: { source: file, path: report.md }
---

The article has 4 planted problems:
- B2.1: The title promises 7 ways; the body has 5
- B2.2: Heading level skipped: an H4 ("Watch your attribution window") directly under an H2
- B2.3: Meta description is about 250 characters (over 160)
- B2.4: Hard sell and unexplained urgency in an awareness article: "Book a demo today, prices go up Friday!"

A problem counts as found when report.md identifies the same problem with evidence (a quote, a count, or the specific element), in the fix list or the list of failed checks. Wording need not match. Vague remarks ("the hook could be stronger") do not count, and "not visible, please confirm" counts as not found when the element is in the article.

PASS if at least 3 of the 4 problems are found.
FAIL otherwise.
