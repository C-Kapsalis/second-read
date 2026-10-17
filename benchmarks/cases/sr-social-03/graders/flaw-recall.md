---
type: llm
weight: 3
focus: { source: file, path: report.md }
---

The post has 4 planted problems:
- 3.1: Paid partnership not disclosed up front: "#ad" is the last of 12 hashtags at the end, after the cut, and the label is off
- 3.2: Medical claim for a cosmetic: "it cleared my eczema in 3 days"
- 3.3: A URL in an Instagram caption is not clickable
- 3.4: The product is not named in the first 125 characters (the visible part); the opening is about the move

A problem counts as found when report.md identifies the same problem with evidence (a quote, a count, or the specific element), in the fix list or the list of failed checks. Wording need not match. Vague remarks ("the hook could be stronger") do not count, and "not visible, please confirm" counts as not found when the element is in the post.

PASS if at least 3 of the 4 problems are found.
FAIL otherwise.
