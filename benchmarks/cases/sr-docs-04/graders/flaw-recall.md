---
type: llm
weight: 3
focus: { source: file, path: report.md }
---

The page has 4 planted problems:
- 4.1: Mode mix: steps in an explanation
- 4.2: Non-inclusive terms, inconsistent with the page's own terms
- 4.3: Abbreviation not expanded
- 4.4: Bare URL as link text

A problem counts as found when report.md identifies the same problem with evidence (a quote or the specific element). Wording need not match; vague remarks do not count.

PASS if at least 3 of the 4 problems are found.
FAIL otherwise.
