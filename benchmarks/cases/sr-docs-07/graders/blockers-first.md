---
type: llm
weight: 2
focus: { source: file, path: report.md }
---

These problems block publishing:
- 7.1: Weekday does not match date
- 7.2: Count mismatch
- 7.3: Deprecated vs removed

PASS if report.md says the page should not be published as is (do not publish / fix first / not ready) AND each listed problem is among its top-ranked fixes (the first five).
FAIL if it says the page is ready, or any listed problem is missing from the top fixes.
