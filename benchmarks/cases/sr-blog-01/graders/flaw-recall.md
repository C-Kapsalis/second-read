---
type: llm
weight: 3
focus: { source: file, path: report.md }
---

The article has 5 planted problems:
- B1.1: Title tag is 69 characters (over 60)
- B1.2: The target keyword "abandoned cart email" is missing from the title tag, the H1 and the first 100 words (it first appears in Step 2)
- B1.3: Throat-clearing intro: about 95 words of generic scene-setting ("In today's fast-paced digital landscape") before the point
- B1.4: Unsourced statistic: "Emails with emojis in the subject line get 56% more opens"
- B1.5: A paragraph of about 125 words in Step 1, mostly one long sentence

A problem counts as found when report.md identifies the same problem with evidence (a quote, a count, or the specific element), in the fix list or the list of failed checks. Wording need not match. Vague remarks ("the hook could be stronger") do not count, and "not visible, please confirm" counts as not found when the element is in the article.

PASS if at least 4 of the 5 problems are found.
FAIL otherwise.
