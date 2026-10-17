# Coverage: sources to the docs skill

Where each section of each source lives in the docs skill. One row per
section heading.

Status:

- **Applied:** the skill acts on it every run (SKILL.md checks, decoy guard,
  output, or a reference the skill always opens).
- **Reference:** in a reference file, used when the page type or the
  question needs it.
- **Not applied:** deliberately left out, with the reason.

Paths are relative to `skills/docs/`. "SKILL §4" means section 4 of
SKILL.md. Diátaxis (CC BY-SA 4.0) and the Canonical style guide (CC BY-SA)
are paraphrased and cited, never copied; word lists are reproduced as lists.

## 1. Technical Writing Brain Knowledge notes

| # | Note and section | Where it lives | Status |
|---|---|---|---|
| N1 | api-reference-docs: reference is consulted, optimize for lookup, completeness, accuracy | references/diataxis.md "Reference checks" intro; SKILL §2 table | Applied |
| N2 | api-reference-docs: what good reference has (one entry per thing, coverage, parameter tables, runnable examples, returns and errors, versioning, mirrors product) | references/diataxis.md R2-R7; references/audit-checklist.md AP2, AP3, AP5 | Applied |
| N3 | api-reference-docs: API-specific (auth, base URL, rate limits, pagination once; per-endpoint shape; generate SDK reference from source) | references/audit-checklist.md AP1, AP2, AP6 | Applied. "Generate from source" not applied: a review of pasted text cannot change the build |
| N4 | api-reference-docs: audit signals (undocumented surface, broken examples, inconsistent entries, no errors, prose that instructs, stale) | SKILL §4 A4, M3; references/diataxis.md R2, R3; references/audit-checklist.md AP5, "Not checked" for staleness against the live API | Applied |
| N5 | api-reference-docs: tools audited (Sphinx, scikit-learn, DuckDB, smolagents, PyMC-Marketing) | none | Not applied: names the writer's audit targets, no rule |
| N6 | diataxis-framework: two axes and the four-type table | SKILL §2 compass table; references/diataxis.md "The map", "The compass" | Applied |
| N7 | diataxis-framework: the rules that matter (tutorial no options; how-to goal-titled, tolerant of variation; reference austere; explanation discursive) | SKILL §4 M1-M4; references/diataxis.md T3, H1, H5, R1, X1-X2 | Applied |
| N8 | diataxis-framework: why it is the audit backbone (map pages, name gaps and conflations) | SKILL §2; references/audit-checklist.md "Whole doc set" item 1 | Applied |
| N9 | documentation-audit-checklist: 1 doc-type coverage | SKILL §2; references/audit-checklist.md doc-set item 1 | Applied |
| N10 | documentation-audit-checklist: 2 getting started (minutes, steps, stuck points; prerequisites; it-worked moment; next step) | references/audit-checklist.md G1-G6; SKILL A3, A5 | Applied. Minutes to first success: Not applied, needs a real run; step count is reported instead (G3) |
| N11 | documentation-audit-checklist: 3 information architecture (two clicks, intent structure, dead ends, orphans, broken links) | references/audit-checklist.md "Single-page findability" and doc-set item 3 | Applied for one page (dead ends, in-page links); site-level items listed as Not checked |
| N12 | documentation-audit-checklist: 4 task orientation | references/diataxis.md H1-H7 | Applied |
| N13 | documentation-audit-checklist: 5 reference quality | references/diataxis.md R1-R7; AP# | Applied |
| N14 | documentation-audit-checklist: 6 examples and code | SKILL A2, A4; references/style.md S7 | Applied. "Run on the current version": Not checked |
| N15 | documentation-audit-checklist: 7 style | SKILL S1-S14; references/style.md | Applied |
| N16 | documentation-audit-checklist: 8 accessibility and inclusion | SKILL S4 (Major); references/style.md S4, S14 | Applied |
| N17 | documentation-audit-checklist: 9 freshness and maintenance | references/audit-checklist.md doc-set item 9; RN1 | Reference (doc-set mode); single page: Not checked |
| N18 | documentation-audit-checklist: output shape (scorecard, 3-5 fixes, worked example, contribution plan) | SKILL §6-§8 (score, ranked fixes, corrected version = worked example); references/audit-checklist.md "Whole doc set" | Applied |
| N19 | getting-started-and-onboarding: what a great getting started does | references/audit-checklist.md G1-G6; references/diataxis.md "Formats" (getting started = tutorial) | Applied |
| N20 | getting-started-and-onboarding: common failures (install reference, no checkpoint, late prerequisites, too long, broken copy-paste) | G5, A5, A3, G3, S7 | Applied |
| N21 | getting-started-and-onboarding: the audit metric | G3 (step and concept count) | Applied in part: minutes need a real run |
| N22 | google-style-guide: voice and grammar (second person, present, active, imperative, sentence case, serial comma, expand acronyms, global audience) | references/style.md S1, S2, S5, S13 | Applied |
| N23 | google-style-guide: structure (task headings, inverted pyramid, one idea per paragraph, numbered steps with results, descriptive links) | references/style.md S2, S9, S10, S13; references/diataxis.md T4, H6 | Applied |
| N24 | google-style-guide: code and formatting (working examples, consistent font treatment, say the outcome) | references/style.md S7, S8; SKILL A5 | Applied |
| N25 | google-style-guide: accessibility (alt text, no color or position alone, inclusive) | references/style.md S4, S14 | Applied |
| N26 | information-architecture: what good IA looks like | references/audit-checklist.md doc-set item 3; "Single-page findability" | Reference |
| N27 | information-architecture: audit signals | references/audit-checklist.md; site-level items under Not checked | Reference |
| N28 | microsoft-style-guide: voice (warm, crisp, ready to help) | SKILL persona paragraph; references/style.md S1 (contractions allowed in conversational text), S13 | Applied |
| N29 | microsoft-style-guide: concrete rules (write like you talk, get to the point, be brief, scannable, "you", bias-free, sentence case, numerals, one term per thing) | references/style.md S1, S2, S4, S6, S12, S13 | Applied |
| N30 | microsoft-style-guide: how it differs from Google | references/style.md opening (house guide wins; Canonical as baseline) | Applied as a tie-break rule. Register choice by audience: Not applied as a check, it is a judgment the writer owns |
| N31 | writethedocs-principles: write for your audience, meet their level | SKILL §1 reader and need | Applied |
| N32 | writethedocs-principles: documentation is a product | references/audit-checklist.md doc-set closing line | Reference |
| N33 | writethedocs-principles: ARID | SKILL §5 decoy list (repeated command); BENCHMARK D5.1 | Applied |
| N34 | writethedocs-principles: docs as code | none | Not applied: a workflow practice, not visible in a page |
| N35 | writethedocs-principles: the arrange step, plan IA first | references/audit-checklist.md doc-set mode | Reference |
| N36 | writethedocs-principles: lower the barrier to contribution | references/audit-checklist.md RM5, doc-set item 9 | Reference |
| N37 | writethedocs-principles: README is the front door; examples are documentation; stale docs worse than missing | references/audit-checklist.md RM1-RM6; SKILL A4; Not checked (freshness) | Applied |
| N38 | powerbi-doc-tools.md | none | Not read, by instruction |

## 2. Technical Writing Brain (practical brain)

| # | Section | Where it lives | Status |
|---|---|---|---|
| B1 | Purpose (craft brain, powers docs-mode audit) | The skill as a whole; references/audit-checklist.md "Whole doc set" | Applied |
| B2 | Foundations (Diátaxis, IA, getting started) | See N6-N11, N19-N27 | Applied |
| B3 | Style authorities (Google, Microsoft, Write the Docs) | See N22-N37 | Applied |
| B4 | Specialized (API reference, audit checklist) | See N1-N18 | Applied |
| B5 | Additional resources: Technical Documentation 101 course notes | Read (linked note). Used: audience questions (SKILL §1), release notes contents (RN1-RN5), quality checkpoints (complete coverage, accurate, unambiguous, findable: R3, A1, S12, findability), user-pull perspective (SKILL §1) | Applied in part. Audience catalog (evaluators, admins, contributors), usage layer and maintainability plan: Not applied as checks, they need product knowledge beyond the page |
| B6 | Additional resources: Canonical documentation style guide | Applied from the web source (section 5 below) | Applied |
| B7 | Deepen comment (tool-specific conventions) | none | Not applied: a to-do for the brain |

## 3. The writer's public pages

| # | Page and section | Where it lives | Status |
|---|---|---|---|
| P1 | approach: three jobs of documentation (users, prospects, builders) | SKILL §1 reader | Applied in part: the skill reviews for the page's reader; prospect and builder jobs matter in doc-set mode |
| P2 | approach: start from the reader, not the feature (user-pull; supply missing domain knowledge) | SKILL §1 ("what background does the page assume, does it say where to get it"); references/diataxis.md H7 (machine-shaped guides) | Applied |
| P3 | approach: Diátaxis as starting framework, including branching how-to guides | SKILL §2; decoy list (how-to branches) | Applied |
| P4 | approach: structure follows complexity (small tool needs little; complex library needs all four) | references/audit-checklist.md doc-set item 1 | Reference. Not a single-page check |
| P5 | approach: one definition, in one place | references/style.md S12; audit-checklist "one home per topic" | Applied |
| P6 | approach: markup is part of the meaning (components by meaning, mark UI labels only where the reader goes to them) | references/style.md S8, S7 (code font by meaning) | Applied. Theme-specific caption and cross-reference label conventions: Not applied, need the source markup |
| P7 | approach: a page is a set of claims; verify against the product; avoid positional descriptions; admonition weight | SKILL Rules and "Not checked"; S4 positional; S11 weight | Applied |
| P8 | approach: documentation is a product (prototype, publish, iterate) | references/audit-checklist.md doc-set closing line | Reference |
| P9 | open-source: values, docs as teacher, barrier to entry, reader to contributor to advocate | Persona tone (strict on facts, relaxed on style); RM5 contribution path | Applied in part: the essay sets motivation, not rules |

## 4. Diátaxis (diataxis.fr)

| # | Page and section | Where it lives | Status |
|---|---|---|---|
| D1 | Start here: use it as a toolbox, apply it to something small | references/diataxis.md "idea in five lines" item 5 | Reference |
| D2 | Start here: the four kinds (tutorial, how-to, reference, explanation) | SKILL §2; references/diataxis.md map | Applied |
| D3 | Start here: the map, blurring causes problems | references/diataxis.md "The map" and blur table; SKILL M1-M5 | Applied |
| D4 | Start here: the compass (action/cognition, acquisition/application) | SKILL §2 table; references/diataxis.md "The compass" | Applied |
| D5 | Start here: working (look, find one improvement, do it, repeat) | references/diataxis.md item 5; SKILL §7 ranked fixes | Applied |
| D6 | Start here: do what you like, pragmatism | references/diataxis.md item 5 | Reference |
| D7 | Tutorials: tutorial as lesson; obligations of the teacher (meaningful, successful, logical, usefully complete) | references/diataxis.md T1-T8; SKILL A2, A5 | Applied |
| D8 | Tutorials: the problem of tutorials (hard, conflated with how-to, costly to maintain) | references/diataxis.md blur table | Reference |
| D9 | Tutorials: key principles (show the destination, results early, narrative of the expected, point out what to notice, minimize explanation, concrete, ignore options, reliability) | T1, T4, T5, T6, T7, T3, A1-A3; decoy list (future tense, one line of why) | Applied |
| D10 | Tutorials: feeling of doing, repetition | none | Not applied: not checkable from text |
| D11 | Tutorials: language of tutorials; cooking analogy | references/diataxis.md tutorial language; map analogy row | Reference |
| D12 | How-to: goal-oriented; addressed to problems, not machinery | H2, H7 | Applied |
| D13 | How-to: what how-to guides are not (not tutorials; not only linear procedures) | Blur table; decoy list (branches) | Applied |
| D14 | How-to: key principles (action only, real-world complexity, omit the unnecessary, instructions, logical sequence, flow) | H3, H4, H5, A2; M2 | Applied. Flow and pacing: Not applied as a check (judgment) |
| D15 | How-to: pay attention to naming | H1 | Applied |
| D16 | How-to: language; recipe analogy | references/diataxis.md how-to language | Reference |
| D17 | Reference: description of machinery, austere, consulted | R1, M3 | Applied |
| D18 | Reference: describe only; standard patterns; mirror the structure; examples | R1, R2, R5, R6; decoy (short examples) | Applied |
| D19 | Reference: language (facts, lists, warnings); food label analogy | references/diataxis.md reference language; decoy (warnings) | Applied |
| D20 | Explanation: reflection, understanding-oriented, read away from the product | X1 | Applied |
| D21 | Explanation: value and boundaries (other names, why-question as prompt) | X1 | Applied |
| D22 | Explanation: make connections, context, talk about the subject, admit opinion, keep bounded | X2, X5, X6, X3, X4; decoy (opinion) | Applied |
| D23 | Explanation: language; history-of-food analogy | references/diataxis.md explanation language | Reference |
| D24 | Map: problem of structure (feature-based structure fails) | references/audit-checklist.md doc-set item 3 | Reference |
| D25 | Map: expectations and guidance table | references/diataxis.md map table | Applied |
| D26 | Map: blur between neighbors | references/diataxis.md blur table | Applied |
| D27 | Map: the journey around the map | none | Not applied: describes reader cycles, no page check |
| D28 | Compass: truth table, two questions, use at sentence and document level | SKILL §2 ("page, then each section"); references/diataxis.md | Applied |

## 5. Canonical Documentation Style Guide

| # | Section | Where it lives | Status |
|---|---|---|---|
| C1 | Diátaxis | SKILL §2 | Applied |
| C2 | Spelling (US English) | references/style.md S3 word list | Applied |
| C3 | Branding: Ubuntu (name, release, LTS, codename case) | references/style.md S12 (product plus version one way) | Applied as a general rule. Canonical product list: Not applied, the skill reviews any product |
| C4 | Branding: other Canonical products | S12 | Not applied as a list (product-specific) |
| C5 | Contractions; forbidden contractions | references/style.md S1 (list); decoy (contractions in explanation) | Applied. Strict "no contractions outside conversational text" only on request |
| C6 | Headings: sentence case | S2 | Applied |
| C7 | Headings: other considerations (no end punctuation, no links, limited code, no skipped levels, no heading directly under heading) | S2 | Applied |
| C8 | Dates | S6 | Applied |
| C9 | Numbers | S6; decoys (commas, digits) | Applied |
| C10 | Code examples (prompt marks, no comments in bash, short blocks, separate command and output, terminal extension) | S7 | Applied. Sphinx-terminal extension: Not applied, tool-specific |
| C11 | Placeholders in code blocks (delimiters, tell the reader, variables in long blocks) | S7; SKILL §8 placeholder rules for the corrected version | Applied |
| C12 | Images (not over-cropped, no cloud-drive links) | S14 | Applied |
| C13 | Video (avoid, prefer text recordings, same standard) | S14 | Applied |
| C14 | Latin words and phrases (three tables) | S5 word list | Applied |
| C15 | Admonitions (four uses, avoid hint and tip) | S11 | Applied |
| C16 | UI: screenshots | S14 | Applied |
| C17 | UI: UI elements as English words | S8 | Applied in part: "click **Save**" is not flagged because the same guide's bold examples use it |
| C18 | UI: bold vs italics | S8 | Applied |
| C19 | UI: angled brackets for menus | S8 | Applied |
| C20 | Hyperlinks: general use (no clusters, permalinks) | S9 | Applied |
| C21 | Hyperlinks: formatting (text matches target, no "click here"/"this document"/bare URL, name external source, link the whole action) | S9; decoy D7.2 | Applied |
| C22 | Lists (numbered only for order; bullets complete) | S10 | Applied |

## Style areas the request named that the Canonical guide does not cover

Voice, person, tense, inclusive language and abbreviation expansion are not
sections of the Canonical guide. They come from the Google and Microsoft
notes (N22, N25, N29) and the writer's approach page (P7), and live in
references/style.md S1, S4 and S5.
