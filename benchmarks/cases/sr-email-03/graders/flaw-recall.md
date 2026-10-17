---
type: llm
weight: 3
focus: { source: file, path: report.md }
---

The email has 5 planted problems:
- 3.1: Subject "Your order has shipped" misdescribes a cart reminder
- 3.2: About 310 words against a 75-150 cart-reminder budget (twice the ceiling); the only CTA comes after ~290 words, far below the first screen
- 3.3: Shortened URL (bit.ly) as the only link
- 3.4: Cart items never named ("some items") although cart data exists
- 3.5: No button: the only CTA is a bare link with "Complete your order here" text

A problem counts as found when report.md identifies the same problem with evidence (a quote, a count, or the specific element), in the fix list or the list of failed checks. Wording need not match. Vague remarks ("the hook could be stronger") do not count, and "not visible, please confirm" counts as not found when the element is in the email.

PASS if at least 4 of the 5 problems are found.
FAIL otherwise.
