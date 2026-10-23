# Editorial regression cases — not a benchmark result

The fixtures in `editorial_cases.jsonl` are **original synthetic examples** of editing decisions for five existing pathways and the specialized additions. Each represents a decision the agent should *consider* under the supplied brief: `edit`, `leave`, `ask`, or `visual` (a textual suggestion that a graphic would be useful if data are verified). The `safe_edit` field gives **one defensible option**, not the sole correct phrasing.

## How to run a real evaluation

1. Run the same fixed fixtures, including briefs, against each candidate model in a fresh, controlled session. Ask the model to read the installed skill and return JSONL objects: `{ "case_id": "...", "decision": "edit|leave|ask|visual", "source_quote": "..." }`. A `leave` result can omit `source_quote`; others need a verbatim source span.
2. Save responses to `responses.jsonl`, recording model version, temperature/reasoning settings, input context, permissioned references loaded, and date. Human review is required for each proposed replacement and evidence claim.
3. Run `python3 scripts/evaluate_editorial_cases.py --cases benchmarks/editorial_cases.jsonl --predictions responses.jsonl --json report.json`.
4. The deterministic result measures **decision routing and source anchoring**, nothing more. Separately score: meaning preservation, project rule alignment, improvement after revision, proof quality, no invented claims, false positives, and author preference. Blind independent reviewers to model identity and compare with the no-skill baseline.
5. Add real author-supplied cases under appropriate consent, remove personal data, and maintain a fixed holdout set. Record disagreement, not simply average away editorial nuance.

Do not say “Second Read achieved X% editorial accuracy” based solely on this script. A model that writes terrible replacements could still receive 100% decision agreement. Strong prose that the model does not change is a **positive outcome**.

## Maintaining cases

Pair errors with near-neighbor leave cases. Examples: vague generic marketing language versus effective compressed slogan; unsupported numerical guarantee versus clear metaphor; Canonical project conventions versus unrelated organization; legitimate data visualization need versus two-number comparison; accidental plot inconsistency versus literary suspense. Source quotes are exact excerpts of their `draft` fields. Cases should state author intention or house rules when required to disambiguate an edit.
