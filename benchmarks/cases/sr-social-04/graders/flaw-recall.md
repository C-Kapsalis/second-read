---
type: llm
weight: 3
focus: { source: file, path: report.md }
---

The post has 4 planted problems:
- 4.1: Wrong arithmetic: £45 to £30 is a third off (about 33%), not 50%
- 4.2: Engagement bait: "Comment YES and tag 3 friends" (Facebook demotes it)
- 4.3: Vague deadline: "For a limited time only", no end date
- 4.4: Four ways to act (call, DM, app, walk in) and no primary action or link

A problem counts as found when report.md identifies the same problem with evidence (a quote, a count, or the specific element), in the fix list or the list of failed checks. Wording need not match. Vague remarks ("the hook could be stronger") do not count, and "not visible, please confirm" counts as not found when the element is in the post.

PASS if at least 3 of the 4 problems are found.
FAIL otherwise.
