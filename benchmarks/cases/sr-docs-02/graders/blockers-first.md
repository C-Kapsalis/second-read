---
type: llm
weight: 2
focus: { source: file, path: report.md }
---

These problems block publishing:
- 2.1: Expiry conflict
- 2.2: Steps out of order

PASS if report.md says the page should not be published as is (do not publish / fix first / not ready) AND each listed problem is among its top-ranked fixes (the first five).
FAIL if it says the page is ready, or any listed problem is missing from the top fixes.
