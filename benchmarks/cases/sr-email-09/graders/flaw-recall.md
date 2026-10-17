---
type: llm
weight: 3
focus: { source: file, path: report.md }
---

The email has 5 planted problems:
- 9.1: Deceptive sender and framing: "Security Team" and "action required" on a promo
- 9.2: Financial spam triggers: "Earn", "cash", "risk-free", "guaranteed"
- 9.3: Attachment on a marketing email
- 9.4: Insecure http:// link
- 9.5: The condition that changes the deal ($500 deposit for 90 days) hidden in a footnote, contradicting "guaranteed"

A problem counts as found when report.md identifies the same problem with evidence (a quote, a count, or the specific element), in the fix list or the list of failed checks. Wording need not match. Vague remarks ("the hook could be stronger") do not count, and "not visible, please confirm" counts as not found when the element is in the email.

PASS if at least 4 of the 5 problems are found.
FAIL otherwise.
