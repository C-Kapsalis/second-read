---
type: llm
weight: 2
focus: { source: file, path: report.md }
---

These parts of the page are correct and must NOT be reported as problems:
- D1.1: "In this tutorial, we will build a small pipeline" ("We" and future tense are the tutor's voice in a tutorial (decoy list, S1))
- D1.2: "We use a virtual environment so the install does not change your system Python." (One sentence of why in a tutorial is allowed (M2 threshold is more than two sentences))
Asking for a source or a link for one of them is fine; only presenting it as an error or a mistake to remove counts as flagging it.

PASS if report.md does not present any of them as an error or a fix to make (mentioning them neutrally or as strengths is fine).
FAIL if any of them is presented as an error or a fix.
