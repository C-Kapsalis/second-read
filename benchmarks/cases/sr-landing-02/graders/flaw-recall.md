---
type: llm
weight: 3
focus: { source: file, path: report.md }
---

The page has 6 planted problems:
- L2.1: Marketing consent checkbox is pre-ticked (`checked`) for UK and EU visitors
- L2.2: Two H1 tags
- L2.3: Title tag is 89 characters (over 60) and there is no meta description
- L2.4: CTA button "Submit"
- L2.5: Images with no alt text (logo, cover)
- L2.6: `href="#download"` points to an id that does not exist on the page (broken in-page link)

A problem counts as found when report.md identifies the same problem with evidence (a quote, a count, or the specific element), in the fix list or the list of failed checks. Wording need not match. Vague remarks ("the hook could be stronger") do not count, and "not visible, please confirm" counts as not found when the element is in the page.

PASS if at least 5 of the 6 problems are found.
FAIL otherwise.
