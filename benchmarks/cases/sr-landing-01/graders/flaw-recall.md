---
type: llm
weight: 3
focus: { source: file, path: report.md }
---

The page has 5 planted problems:
- L1.1: Message mismatch: the ad promises 30 days with no card; the page offers a 14-day trial and asks for a credit card
- L1.2: The H1 "Welcome to the future of work" does not say what Pipewise is or what the visitor gets
- L1.3: Nine form fields for a trial, including phone, budget and card
- L1.4: The only CTA is at the bottom, after about 220 words; nothing to act on in the first screen
- L1.5: Anonymous, vague testimonial: "This tool changed everything!" A happy customer

A problem counts as found when report.md identifies the same problem with evidence (a quote, a count, or the specific element), in the fix list or the list of failed checks. Wording need not match. Vague remarks ("the hook could be stronger") do not count, and "not visible, please confirm" counts as not found when the element is in the page.

PASS if at least 4 of the 5 problems are found.
FAIL otherwise.
