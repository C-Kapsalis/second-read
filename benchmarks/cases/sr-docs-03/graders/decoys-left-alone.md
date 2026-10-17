---
type: llm
weight: 2
focus: { source: file, path: report.md }
---

These parts of the page are correct and must NOT be reported as problems:
- D3.1: "You must not set `workers` above the number of CPU cores on the host." (Warnings belong in reference (decoy list; Diátaxis reference language))
- D3.2: `8080`, `10000` without commas (Code values and ports take no commas (S6))
Asking for a source or a link for one of them is fine; only presenting it as an error or a mistake to remove counts as flagging it.

PASS if report.md does not present any of them as an error or a fix to make (mentioning them neutrally or as strengths is fine).
FAIL if any of them is presented as an error or a fix.
