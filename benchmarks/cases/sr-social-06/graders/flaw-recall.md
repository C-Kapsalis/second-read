---
type: llm
weight: 3
focus: { source: file, path: report.md }
---

The post has 4 planted problems:
- 6.1: "Guaranteed 8% returns every year and zero risk" on an investment product, contradicting the post's own "Capital at risk" line
- 6.2: Unsourced comparison: "Most high-street banks pay 0.1%" with no source or date
- 6.3: The product is not named in the first 125 characters; the opening is pleasantries
- 6.4: Three links competing and a vague "Learn more" label

A problem counts as found when report.md identifies the same problem with evidence (a quote, a count, or the specific element), in the fix list or the list of failed checks. Wording need not match. Vague remarks ("the hook could be stronger") do not count, and "not visible, please confirm" counts as not found when the element is in the post.

PASS if at least 3 of the 4 problems are found.
FAIL otherwise.
