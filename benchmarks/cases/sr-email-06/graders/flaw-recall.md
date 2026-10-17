---
type: llm
weight: 3
focus: { source: file, path: report.md }
---

The email has 4 planted problems:
- 6.1: Brand misspelled in the body: "Lumin Botanicals" vs "Lumen Botanics"
- 6.2: Unsupported superlative claims: "clinically proven", "#1 serum in the world"
- 6.3: Health claim and spam trigger: "cure your acne in just 7 days"
- 6.4: Subject promises a 15% gift; the body gives no code, link or terms

A problem counts as found when report.md identifies the same problem with evidence (a quote, a count, or the specific element), in the fix list or the list of failed checks. Wording need not match. Vague remarks ("the hook could be stronger") do not count, and "not visible, please confirm" counts as not found when the element is in the email.

PASS if at least 3 of the 4 problems are found.
FAIL otherwise.
