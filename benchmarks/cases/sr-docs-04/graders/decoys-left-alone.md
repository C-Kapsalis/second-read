---
type: llm
weight: 2
focus: { source: file, path: report.md }
---

These parts of the page are correct and must NOT be reported as problems:
- D4.1: "We think asynchronous replication is the better default for most teams, because..." (Opinion with reasons is what explanation is for (decoy list; X5))
- D4.2: "you can't lose", "that's a sound choice" (Contractions are fine in explanation (S1))
Asking for a source or a link for one of them is fine; only presenting it as an error or a mistake to remove counts as flagging it.

PASS if report.md does not present any of them as an error or a fix to make (mentioning them neutrally or as strengths is fine).
FAIL if any of them is presented as an error or a fix.
