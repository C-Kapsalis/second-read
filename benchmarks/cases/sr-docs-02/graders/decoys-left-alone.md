---
type: llm
weight: 2
focus: { source: file, path: report.md }
---

These parts of the page are correct and must NOT be reported as problems:
- D2.1: "If your services read the key from Kestrel Vault, skip this step" (Conditional branches belong in how-to guides (decoy list; H5))
- D2.2: "For the full list of flags, see the [keys command reference](...)" (A how-to links to reference instead of listing every option; descriptive link text)
Asking for a source or a link for one of them is fine; only presenting it as an error or a mistake to remove counts as flagging it.

PASS if report.md does not present any of them as an error or a fix to make (mentioning them neutrally or as strengths is fine).
FAIL if any of them is presented as an error or a fix.
