---
type: llm
weight: 2
focus: { source: file, path: report.md }
---

These problems are severe enough that the post should not go out until they are fixed:
- 3.1: Paid partnership not disclosed up front: "#ad" is the last of 12 hashtags at the end, after the cut, and the label is off
- 3.2: Medical claim for a cosmetic: "it cleared my eczema in 3 days"

PASS if report.md gives a "do not send" verdict (or "do not post", "do not publish", "not ready", "fix before sending/posting/publishing") AND each listed problem appears among its top-ranked fixes (the first five fixes).
FAIL if the verdict says it is ready to go, or any listed problem is missing from the top fixes.
