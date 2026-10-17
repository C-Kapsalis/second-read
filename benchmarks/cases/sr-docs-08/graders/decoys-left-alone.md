---
type: llm
weight: 2
focus: { source: file, path: report.md }
---

These parts of the page are correct and must NOT be reported as problems:
- D8.1: "If you prefer to script the export, use the Windrose command-line interface (CLI)." (An alternative path in a how-to is fine; M1 applies to tutorials only)
- D8.2: "for example to hand it to an external auditor" and the sample output "for example: Saved audit-log-ws_4821-2026-04-02.csv" (Plain English, not "e.g."; an example output labelled as an example)
- D8.3: "up to 365 days", `2026-01-01` (Digits for 10 and up; ISO dates inside code are values, not prose dates (S6))
Asking for a source or a link for one of them is fine; only presenting it as an error or a mistake to remove counts as flagging it.

PASS if report.md does not present any of them as an error or a fix to make (mentioning them neutrally or as strengths is fine).
FAIL if any of them is presented as an error or a fix.
