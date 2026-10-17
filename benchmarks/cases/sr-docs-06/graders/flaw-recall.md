---
type: llm
weight: 3
focus: { source: file, path: report.md }
---

The page has 5 planted problems:
- 6.1: Mode mix: tutorial and opinion in reference
- 6.2: Example type contradicts the table
- 6.3: Undocumented field
- 6.4: Inconsistent endpoint shape: no errors for GET
- 6.5: Title case heading, inconsistent with the next heading

A problem counts as found when report.md identifies the same problem with evidence (a quote or the specific element). Wording need not match; vague remarks do not count.

PASS if at least 4 of the 5 problems are found.
FAIL otherwise.
