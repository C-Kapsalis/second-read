---
type: llm
weight: 2
focus: { source: file, path: report.md }
---

These problems are severe enough that the post should not go out until they are fixed:
- 1.1: Over X's 280-character limit for a standard account: 344 characters with the link counted as 23, so it cannot be posted as written

PASS if report.md gives a "do not send" verdict (or "do not post", "do not publish", "not ready", "fix before sending/posting/publishing") AND each listed problem appears among its top-ranked fixes (the first five fixes).
FAIL if the verdict says it is ready to go, or any listed problem is missing from the top fixes.
