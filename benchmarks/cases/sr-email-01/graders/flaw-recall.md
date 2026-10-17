---
type: llm
weight: 3
focus: { source: file, path: report.md }
---

The email has 6 planted problems:
- 1.1: Subject is 77 characters, truncated on phones
- 1.2: Spam signals: 5 ALL CAPS words, "!!!", "FREE", "Act now"
- 1.3: Default preheader "View this email in your browser"
- 1.4: No end date or time zone: "ends soon"; unsupported scarcity "sizes are going fast"
- 1.5: CTA "Click here"
- 1.6: No physical postal address in footer

A problem counts as found when report.md identifies the same problem with evidence (a quote, a count, or the specific element), in the fix list or the list of failed checks. Wording need not match. Vague remarks ("the hook could be stronger") do not count, and "not visible, please confirm" counts as not found when the element is in the email.

PASS if at least 5 of the 6 problems are found.
FAIL otherwise.
