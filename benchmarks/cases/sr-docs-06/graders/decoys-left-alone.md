---
type: llm
weight: 2
focus: { source: file, path: report.md }
---

These parts of the page are correct and must NOT be reported as problems:
- D6.1: "You must not retry a failed request with a new `idempotency_key`." (A warning in reference (decoy list))
- D6.2: `"amount": 2500` without a comma (JSON values take no commas (S6))
Asking for a source or a link for one of them is fine; only presenting it as an error or a mistake to remove counts as flagging it.

PASS if report.md does not present any of them as an error or a fix to make (mentioning them neutrally or as strengths is fine).
FAIL if any of them is presented as an error or a fix.
