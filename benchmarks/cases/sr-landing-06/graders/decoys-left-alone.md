---
type: llm
weight: 1
focus: { source: file, path: report.md }
---

These aspects of the page are correct and must NOT be reported as problems: a single email field is right for a newsletter; "Free. Unsubscribe in one click."
Asking for a source, a date or a link for one of them is fine and does not count as flagging it; only presenting it as an error or a mistake to remove does.

PASS if report.md does not flag any of these as a problem in its fix list or failed checks (mentioning them neutrally or as a strength is fine).
FAIL if any of them is presented as an error or a fix to make.
