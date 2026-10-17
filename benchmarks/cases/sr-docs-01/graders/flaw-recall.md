---
type: llm
weight: 3
focus: { source: file, path: report.md }
---

The page has 6 planted problems:
- 1.1: File name changes
- 1.2: Python version conflict, stated after install
- 1.3: Mode mix: tutorial offers choices
- 1.4: Mode mix: theory inside a tutorial
- 1.5: Style: title case heading
- 1.6: Style: non-descriptive link text

A problem counts as found when report.md identifies the same problem with evidence (a quote or the specific element). Wording need not match; vague remarks do not count.

PASS if at least 5 of the 6 problems are found.
FAIL otherwise.
