---
type: llm
weight: 2
focus: { source: file, path: report.md }
---

These problems are severe enough that the email should not go out until they are fixed:
- 6.4: Subject promises a 15% gift; the body gives no code, link or terms

PASS if report.md gives a "do not send" verdict (or "do not post", "do not publish", "not ready", "fix before sending/posting/publishing") AND each listed problem appears among its top-ranked fixes (the first five fixes).
FAIL if the verdict says it is ready to go, or any listed problem is missing from the top fixes.
