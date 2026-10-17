---
type: llm
weight: 3
focus: { source: file, path: report.md }
---

The page has 5 planted problems:
- L5.1: Health claims: "100% painless", "permanent results, guaranteed"
- L5.2: Phone numbers disagree: 0113 496 0721 in the hero, 0113 496 0712 in the footer
- L5.3: H1 "Smile!" says neither the service, the offer nor the place, and lacks the target keyword; the price only appears far down
- L5.4: CTA "Click here"
- L5.5: URL slug "page?id=4471" carries no keyword

A problem counts as found when report.md identifies the same problem with evidence (a quote, a count, or the specific element), in the fix list or the list of failed checks. Wording need not match. Vague remarks ("the hook could be stronger") do not count, and "not visible, please confirm" counts as not found when the element is in the page.

PASS if at least 4 of the 5 problems are found.
FAIL otherwise.
