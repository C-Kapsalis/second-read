---
type: llm
weight: 3
focus: { source: file, path: report.md }
---

The post has 4 planted problems:
- 1.1: Over X's 280-character limit for a standard account: 344 characters with the link counted as 23, so it cannot be posted as written
- 1.2: Four hashtags against X's norm of 1-2
- 1.3: Unsupported superlative: "the world's smoothest cold brew"
- 1.4: Scarcity with no number, date or reason: "Hurry, they're almost gone!" (and the code has no end date)

A problem counts as found when report.md identifies the same problem with evidence (a quote, a count, or the specific element), in the fix list or the list of failed checks. Wording need not match. Vague remarks ("the hook could be stronger") do not count, and "not visible, please confirm" counts as not found when the element is in the post.

PASS if at least 3 of the 4 problems are found.
FAIL otherwise.
