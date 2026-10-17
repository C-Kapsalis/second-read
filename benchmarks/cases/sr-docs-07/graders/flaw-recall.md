---
type: llm
weight: 3
focus: { source: file, path: report.md }
---

The page has 5 planted problems:
- 7.1: Weekday does not match date
- 7.2: Count mismatch
- 7.3: Deprecated vs removed
- 7.4: Mode mix: tutorial and explanation inside release notes
- 7.5: Numeric date

A problem counts as found when report.md identifies the same problem with evidence (a quote or the specific element). Wording need not match; vague remarks do not count.

PASS if at least 4 of the 5 problems are found.
FAIL otherwise.
