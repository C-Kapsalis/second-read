# Style rules S1-S14

Sources, paraphrased (not copied):

- Canonical's Documentation Style Guide,
  https://documentation.ubuntu.com/style-guide/ (CC BY-SA). Its rules on
  spelling, headings, dates, numbers, code, placeholders, images, video,
  Latin, admonitions, UI elements, links, lists, contractions and product
  names are the house baseline here.
- The Google developer documentation style guide and the Microsoft Writing
  Style Guide, as summarized in the writer's notes: voice, person, tense,
  inclusive language, abbreviations, scannability.
- The writer's own docs approach: markup carries meaning; no positional
  directions; admonition weight matches the message; one definition in one
  place.

If the user names a house style guide, it wins over this file. Say which one
you applied.

Style problems are Minor unless the rule says otherwise. Merge repeats of
one rule into one problem and quote up to three examples.

## S1 Voice, person, tense

- Address the reader as "you". Instructions use the imperative: "Run",
  "Select", "Open". Fails: "you should click", "you can now run", "the user
  must enter" in a step.
- Active voice when it says who acts: "The server sends a token", not "A
  token is sent". Passive is fine when the actor does not matter.
- Present tense for how things behave: "The command returns", not "will
  return". Tutorials may use future for expectations ("You will see").
- No "I". "We" for the tutor in a tutorial, or sparingly for the product
  team elsewhere.
- Common contractions (don't, isn't, you're) are fine in tutorials and
  explanation. Strict Canonical style keeps them out of reference and
  how-to: flag only if the user asks for that style. Always flag the
  regional or colloquial ones: ain't, gonna, gotta, how'd, how'll, I'd,
  'twas, something's, mayn't, may've, mightn't, might've.

## S2 Headings

- Sentence case: capitalize the first word and proper nouns only (product,
  company, personal and place names, brands). "Configure the cache", not
  "Configure The Cache". Never capitalize ordinary technical terms.
- No full stop at the end. Avoid other heavy punctuation.
- No links inside headings. Code font in headings only for command or
  option names in reference.
- No skipped levels (H1 then H3). A heading is never followed directly by a
  subheading with no text between.
- Task headings name what the reader does ("Rotate a key"), not the
  feature ("Key management").

## S3 US English

Flag the UK form; the US form is the fix.

| UK | US |
|---|---|
| colour, behaviour, favour, honour, labour | color, behavior, favor, honor, labor |
| organise, organisation, authorise, authorisation | organize, organization, authorize, authorization |
| customise, optimise, initialise, serialise, normalise, prioritise, recognise, summarise, utilise | customize, optimize, initialize, serialize, normalize, prioritize, recognize, summarize, use |
| analyse, catalogue, dialogue (UI), analogue | analyze, catalog, dialog, analog |
| centre, metre, litre | center, meter, liter |
| licence (noun), defence, offence | license, defense, offense |
| cancelled, labelled, modelling, travelling, signalled | canceled, labeled, modeling, traveling, signaled |
| grey, programme (software), cheque, artefact | gray, program, check, artifact |
| enrol, fulfil, instalment | enroll, fulfill, installment |
| judgement, acknowledgement | judgment, acknowledgment |

Code, file names, API fields and quoted UI labels keep their exact spelling.

## S4 Inclusive and accessible (Major)

| Avoid | Use |
|---|---|
| master/slave | primary/replica, leader/follower, main/secondary |
| whitelist/blacklist | allowlist/denylist, allow list/block list |
| sanity check | quick check, smoke test |
| dummy value | placeholder, sample value |
| man-hours, manpower | person-hours, staff |
| guys | everyone, folks, all |
| he or she, he (for the user) | they |
| crippled, lame, blind to, cripple | limited, broken, unaware of, disable |

- No direction by position, color or shape alone: "the button on the
  right", "the green icon", "the menu below". Name the control.
- Images need alt text. Meaning never lives only in a color.
- "Simply", "just", "easy", "obviously", "of course": cut them (Minor).
  They make a stuck reader feel slow.

## S5 Abbreviations and Latin

- Spell out an abbreviation on first use, then use it: "write-ahead log
  (WAL)". Skip this for terms every reader of this page knows (API, URL,
  HTML for a developer page).
- Replace Latin with plain English:

| Latin | Plain English |
|---|---|
| e.g., exempli gratia | for example, such as |
| i.e., id est | that is |
| etc., et cetera | and so on (or finish the list) |
| via | through, by, using |
| vs., versus | compared with, against |
| cf. | see, compare |
| n.b., nota bene | note |
| viz. | namely |
| per se | in itself |
| ad hoc | one-off, improvised |
| de facto | actual, established |
| a priori | assumed |
| in situ | in place |
| circa, ca. | about, around |
| ergo | so, therefore |
| vice versa | the other way around |
| verbatim | exactly, word for word |
| status quo | the current state |
| a.m., p.m. | 24-hour time (14:00) |
| per (for "each") | each, every |
| et al., ibid., sic, stet | do not use |

## S6 Numbers and dates

- One to nine in words; 10 and up in digits. Exceptions: numbered lists,
  units of measurement (5 GB, 3 ms), versions, code, and table cells.
- Commas in prose numbers over 999 (7,000). Never in code, versions, ports,
  years, IDs or JSON.
- Dates: "January 1, 2026"; ranges "January 1-2, 2026" and "January 1 -
  February 2, 2026". Flag numeric dates (04/03/2026, 15/04/2026): readers
  in different countries read them differently.

## S7 Code

- Copyable: no prompt marks ($, #, >) inside a block a reader will copy,
  unless the tool keeps them out of the copy. Flag a "$ " at line start.
- Command and output separate: a sentence between the command and what it
  prints ("The command prints:").
- Placeholders: one delimiter style used consistently (`<instance_name>`),
  and the text tells the reader to replace it at first use. In long blocks,
  set the value once as a variable.
- Short blocks: if it does not fit on a screen, split it or offer a download.
- Explain in prose, not in shell comments inside the block (Canonical
  rule; Minor).
- Code font for commands, file names, paths, flags, parameters, values and
  environment variables, consistently. A file name in plain text in one
  place and code font in another is a Minor.
- Label the block's language when the format allows it.

## S8 UI elements

- Bold the label of a control the reader acts on: Select **Save**.
- Write the label exactly as the UI shows it.
- Menu paths with ">": **Settings > API > Keys**.
- Mark a label up only where you send the reader to it, not every mention.
- Do not chain whole actions with ">" ("Go to home > click Packages > select
  all").

## S9 Links

- Link text says where it goes, ideally the target's title: "see [Configure
  the cache]". Fails: "click here", "here", "this page", "this document",
  "read more", a bare URL as text.
- Say when a link leaves the doc set ("on GitHub"). Links to the project's
  own upstream repo are fine.
- No cluster of three or more links in one sentence or step: move them to a
  "Related topics" list.
- For an action link, link the whole action: "[Download config.zip]".
- Link to a fixed revision (permalink) for specific lines of code.

## S10 Lists and steps

- Numbered lists for ordered steps, items referred to by number, and
  sequences. Bullets for everything else.
- One action per step. Two actions joined by "and then" are a Minor.
- A bulleted list is complete for what it claims; if it is a sample, say so.
- Procedures are lists, not paragraphs.

## S11 Admonitions

- Use a note, warning or caution for: a consequence of an action, useful but
  optional information, a time-saver, or a prerequisite or restriction.
- Avoid "hint" and "tip" boxes.
- Weight matches the message: a "Warning" for a cosmetic detail is a Minor;
  a destructive step with no warning is A7 (Blocker).
- Two or more admonitions in a row: merge or move into the text.

## S12 Terms and names

- One term per thing across the page ("workspace" here, "project" there,
  for the same object: Minor; Major if a reader could think they are two
  things).
- Product and feature names spelled and capitalized one way. Product name
  plus version written one way ("Saltmarsh 4.2", not also "SaltMarsh v4.2").
- Define a heavy concept once, in one place, and link to it. A page that
  restates a definition differently from the glossary is A1.

## S13 Plain and front-loaded

- The point first: the first sentence of a page or section says what it is
  for. Cut throat-clearing ("In this section we will be taking a look at").
- Short sentences (aim under 25 words), short paragraphs, one idea each.
- Use the serial comma in lists of three or more ("red, green, and blue").
- Cut filler: "in order to" (to), "it should be noted that", "please note",
  "basically", "at this point in time" (now), "utilize" (use).
- Write for a global audience: no idioms, slang or culture-bound jokes.

## S14 Media

- Screenshots only when words cannot do it; never as the only description
  of a step; alt text on each.
- Do not crop so tight the reader loses where they are.
- No images hosted on personal cloud drives (links rot and outsiders cannot
  open them).
- Avoid video in docs; prefer a text-based terminal recording. Any video is
  held to the same accuracy standard as text.
