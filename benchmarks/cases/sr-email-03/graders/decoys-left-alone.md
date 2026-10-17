---
type: llm
weight: 1
focus: { source: file, path: report.md }
---

These aspects of the email are correct and must NOT be reported as problems: **D3.a** the discount has a clear code, amount and expiry with time zone (EMBER10, 10%, Sunday 23:59 CET). **D3.b** the footer is complete (address and unsubscribe).
Asking for a source, a date or a link for one of them is fine and does not count as flagging it; only presenting it as an error or a mistake to remove does.

PASS if report.md does not flag any of these as a problem in its fix list or failed checks (mentioning them neutrally or as a strength is fine).
FAIL if any of them is presented as an error or a fix to make.
