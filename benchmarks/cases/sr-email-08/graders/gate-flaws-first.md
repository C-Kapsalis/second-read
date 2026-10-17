---
type: llm
weight: 2
focus: { source: file, path: report.md }
---

These problems are severe enough that the email should not go out until they are fixed:
- 8.2: Weekday and date disagree: 14 November 2026 is a Saturday

PASS if report.md gives a "do not send" verdict (or "do not post", "do not publish", "not ready", "fix before sending/posting/publishing") AND each listed problem appears among its top-ranked fixes (the first five fixes).
FAIL if the verdict says it is ready to go, or any listed problem is missing from the top fixes.
