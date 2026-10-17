---
type: llm
weight: 3
focus: { source: file, path: report.md }
---

The page has 5 planted problems:
- 3.1: Mode mix: reference instructs and opines
- 3.2: Default conflict
- 3.3: Undocumented option
- 3.4: Latin abbreviation
- 3.5: Skipped heading level

A problem counts as found when report.md identifies the same problem with evidence (a quote or the specific element). Wording need not match; vague remarks do not count.

PASS if at least 4 of the 5 problems are found.
FAIL otherwise.
