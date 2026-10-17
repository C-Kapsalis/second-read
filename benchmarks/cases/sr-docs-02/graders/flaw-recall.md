---
type: llm
weight: 3
focus: { source: file, path: report.md }
---

The page has 6 planted problems:
- 2.1: Expiry conflict
- 2.2: Steps out of order
- 2.3: Mode mix: how-to teaches basics
- 2.4: Title is a feature noun, in title case
- 2.5: Position and color-only direction
- 2.6: UK spelling

A problem counts as found when report.md identifies the same problem with evidence (a quote or the specific element). Wording need not match; vague remarks do not count.

PASS if at least 5 of the 6 problems are found.
FAIL otherwise.
