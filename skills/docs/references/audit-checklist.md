# Audit checklist

The order to work in, the format checks for READMEs, API reference and
release notes, what to do with a whole doc set, and what a review of pasted
text cannot check.

## One page, in order

1. Reader and need (SKILL §1). Questions to answer: who is this for, what
   background do they need, where can they get it, how will they use this
   page?
2. Classify with the compass, page then sections (SKILL §2,
   references/diataxis.md).
3. Fact ledger (SKILL §3).
4. A1-A7 against the ledger.
5. M1-M5, then the type's T#, H#, R# or X# checks.
6. Format checks below, if a README, API reference or release notes.
7. S1-S14 (references/style.md).
8. Decoy guard, score, rank, corrected version, fact check, challenge table.

## Getting started pages

The highest-leverage page in a doc set: it decides whether a newcomer keeps
going. Treat it as a tutorial (T#) and also check:

| # | Check | Fails when | Severity |
|---|---|---|---|
| G1 | Who and what | The opening does not say who it is for and what they will have at the end | Minor |
| G2 | Prerequisites | Not listed before step 1 (A3) | (A3) |
| G3 | Count the path | Report the step count and the number of new concepts. Flag over about 10 steps or any step that sends the reader off the page to finish it | Minor; report the count either way |
| G4 | It worked | No visible success moment (A5) | Major |
| G5 | Not an install reference | Every OS, flag or option listed (M1) | Major |
| G6 | Next step | No link to where to go after the first success | Minor |

## README (RM#)

The front door: what it is, who it is for, how to start, where to go next.

| # | Check | Fails when | Severity |
|---|---|---|---|
| RM1 | What and who | The first paragraph does not say what the project does and who it is for | Major |
| RM2 | Install | No install or access instructions, or no stated requirements (runtime and version) | Major |
| RM3 | Quickstart | No minimal working example; the quickstart offers several paths (M1) | Major |
| RM4 | Where next | No link to full docs, usage, or help | Minor |
| RM5 | Contribute and license | An open-source README with no license line or no contribution path | Minor |
| RM6 | Status | Badges or version text that disagree with the install text (A1) | Blocker |

Repeating the install command in Install and Quickstart is fine.

## API reference (AP#)

| # | Check | Fails when | Severity |
|---|---|---|---|
| AP1 | Shared facts once | Auth, base URL, versioning, rate limits, pagination missing or stated differently in two places (A1) | Major; Blocker if two values conflict |
| AP2 | Endpoint shape | An endpoint lacks method, path, parameters, request example, response example or status and error codes, while others have them (R2) | Major |
| AP3 | Parameters complete | A field in an example is missing from the parameter table, or a table field is never explained (R3) | Major |
| AP4 | Types agree | An example value's type or format contradicts the table (A4): a string where the table says integer, a different date format | Blocker |
| AP5 | Errors | No error documentation at all, or an error code with no meaning or fix | Major |
| AP6 | Path agrees with base URL | The endpoint path uses a version or prefix that contradicts the stated base URL (A1) | Blocker |
| AP7 | Neutral | Tutorial steps, "let's", "you should" or opinions inside entries (M3) | Major |

## Release notes (RN#)

| # | Check | Fails when | Severity |
|---|---|---|---|
| RN1 | Identity | No version number or no release date; weekday does not match date (A1) | Blocker for a mismatch; Major if missing |
| RN2 | Changes listed | New, changed and fixed items not separated; a stated count ("three fixes") differs from the list (A1) | Minor; Blocker for a count mismatch |
| RN3 | Breaking changes and deprecations | A breaking change or removal with no upgrade or migration step; a feature called "deprecated" in one place and "removed" in another (A1) | Major; Blocker for the contradiction |
| RN4 | Known issues | Missing section when the notes mention open problems elsewhere | Minor |
| RN5 | Support | No pointer to where to report problems or get help | Minor |
| RN6 | Record, not lesson | A walkthrough, tutorial or long explanation inside the notes (M2 or M5). Link to it instead | Major |
| RN7 | Plain claims | Marketing superlatives ("the best release ever") in a record | Minor |

## Single-page findability (from information architecture)

Checkable on one page:

- Task-shaped title the reader would search for.
- Headings that let a reader scan to the part they need.
- A next step or related links at the end. A page with none is a dead end
  (Minor).
- In-page links that resolve (A6).
- One home per topic: a concept defined here and also restated differently
  elsewhere on the page is A1.

Not checkable on one page: the two-clicks-or-one-search rule, orphan pages,
search quality, sidebar order. List them under "Not checked" if the user asks
about navigation.

## Whole doc set (when the user gives several pages or a site)

Score each dimension 1-5 with one headline finding and a cited page:

1. Type coverage: which of the four types exist, which are missing, which
   pages are conflated.
2. Getting started: step count, concepts, a success moment, a next step.
3. Information architecture: top level by reader intent (Get started,
   Guides, Concepts, Reference, Troubleshooting), dead ends, orphans, broken
   links.
4. Task orientation: goal-titled how-to guides that cover real tasks.
5. Reference quality: coverage, consistent entries, examples, errors.
6. Examples and code: runnable as written, on the current version.
7. Style: S1-S14.
8. Accessibility and inclusion: alt text, no color- or position-only
   meaning, inclusive terms.
9. Freshness: last-updated signal, matches the current release, versioned,
   an "edit this page" path.

Then the 3-5 fixes that matter most (page, problem, principle, rewrite), one
worked example (rewrite one weak section in full), and, for open source,
which fix to contribute first. Docs are a product: suggest shipping the
fixes and gathering reader feedback, not polishing forever.

## Not checked (say so in every review)

- Commands were not run; output, versions and defaults were not verified
  against the real product. A page is a set of claims; the writer should
  run the steps before publishing.
- Links and images were not opened.
- Rendering (admonitions, tabs, code highlighting) was not seen.
- Other pages in the doc set were not seen unless pasted.
