---
type: llm
weight: 2
focus: { source: file, path: report.md }
---

These parts of the page are correct and must NOT be reported as problems:
- D7.1: "more than 10,000 projects" (Comma in a prose number over 999 is the house rule (S6))
- D7.2: "see the [Saltmarsh changelog](...) on GitHub" (Descriptive link text, external source named, upstream repo link (S9))
Asking for a source or a link for one of them is fine; only presenting it as an error or a mistake to remove counts as flagging it.

PASS if report.md does not present any of them as an error or a fix to make (mentioning them neutrally or as strengths is fine).
FAIL if any of them is presented as an error or a fix.
