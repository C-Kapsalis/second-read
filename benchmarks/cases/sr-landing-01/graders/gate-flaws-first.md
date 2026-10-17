---
type: llm
weight: 2
focus: { source: file, path: report.md }
---

These problems are severe enough that the page should not go out until they are fixed:
- L1.1: Message mismatch: the ad promises 30 days with no card; the page offers a 14-day trial and asks for a credit card

PASS if report.md gives a "do not send" verdict (or "do not post", "do not publish", "not ready", "fix before sending/posting/publishing") AND each listed problem appears among its top-ranked fixes (the first five fixes).
FAIL if the verdict says it is ready to go, or any listed problem is missing from the top fixes.
