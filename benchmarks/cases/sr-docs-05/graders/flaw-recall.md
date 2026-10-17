---
type: llm
weight: 3
focus: { source: file, path: report.md }
---

The page has 5 planted problems:
- 5.1: Node version conflict
- 5.2: Command name typo
- 5.3: Mode mix: quickstart offers choices
- 5.4: Unfinished
- 5.5: Prompt mark breaks copying

A problem counts as found when report.md identifies the same problem with evidence (a quote or the specific element). Wording need not match; vague remarks do not count.

PASS if at least 4 of the 5 problems are found.
FAIL otherwise.
