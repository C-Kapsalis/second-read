# Diátaxis: the four types and their checks

Source: Daniele Procida, Diátaxis, https://diataxis.fr (CC BY-SA 4.0). This
file paraphrases it in our own words and adds review checks. It does not
copy the original text. Read the source for the full argument.

## The idea in five lines

1. There are four kinds of documentation, each answering a different need:
   tutorials, how-to guides, reference and explanation.
2. Each kind must be written differently.
3. Most documentation problems come from blurring the kinds together.
4. A reviewer classifies by what the text does, not by what it is called.
5. Improve in small steps: look at the page, find one thing that would make
   it better, do it, repeat. The framework is a tool, not a creed: use the
   parts that help.

## The map

| | Tutorial | How-to guide | Reference | Explanation |
|---|---|---|---|---|
| Job | Lead a learner through doing | Direct a competent user to a goal | Describe the product | Make a topic make sense |
| Reader's question | "Can you teach me to...?" | "How do I...?" | "What is...?" | "Why...?" |
| Oriented to | Learning | A goal | Information | Understanding |
| Shape | A lesson | A sequence of actions | Austere description | Discussion |
| Kitchen analogy | Cooking with a child | A recipe | The label on the packet | A book on the history of food |

The two axes:

- **Action vs cognition.** Tutorials and how-to guides are about doing.
  Reference and explanation are about knowing.
- **Study vs work.** Tutorials and explanation serve learning. How-to guides
  and reference serve the reader at work.

Neighbors on the map share one axis, so they blur most easily:

| Blur | Shared trait | What goes wrong |
|---|---|---|
| Tutorial and how-to | Both guide action | Beginners get expert task lists; experts get hand-holding. The worst and most common collapse |
| How-to and reference | Both serve work | Guides swell into option lists; reference starts giving directions |
| Reference and explanation | Both hold knowledge | Reference grows opinions and history; explanation dumps tables |
| Explanation and tutorial | Both serve study | Lessons stall in theory |

## The compass

Ask of the page, then of each section, then of a suspect sentence:

1. Action or cognition? (practical steps, or facts and ideas)
2. Acquisition or application? (study, or work)

| Informs | Serves | Type |
|---|---|---|
| Action | Acquisition | Tutorial |
| Action | Application | How-to guide |
| Cognition | Application | Reference |
| Cognition | Acquisition | Explanation |

Use the words loosely while you find your bearings. The compass is most
useful when a page feels wrong and you cannot say why.

## Formats that are not types

| Format | Treat as |
|---|---|
| Getting started, quickstart, "Hello world" | Tutorial (one guaranteed path, a visible success, a next step) |
| README | A front door with sections of different types: what it is (explanation, one paragraph), install and quickstart (tutorial), usage (how-to or reference), links onward. Check each section against its own type. Also RM# in audit-checklist.md |
| API reference | Reference. Also AP# in audit-checklist.md |
| Release notes | A reference record of one version. Also RN# in audit-checklist.md |
| Troubleshooting | How-to (problem, then actions) |
| Glossary | Reference |
| Migration or upgrade guide | How-to |

## Mode-mix signals

These words are signals to look closer, not failures by themselves. Quote the
sentence and apply the M rule in SKILL.md.

| Page type | Suspect when you see | Usually fine |
|---|---|---|
| Tutorial | "alternatively", "or you can", "optionally", "if you prefer", "advanced users", several install methods, a "Background" or "How it works" section, a paragraph of theory before the first step, "you will learn" | "we", one line of why plus a link, "you will see", "notice that" |
| How-to | "What is X?", history, a beginner explanation of basics, every option of a command listed, "let's learn" | "If you ..., then ...", a link to reference, one line of why |
| Reference | "you should", "we recommend", "the best", "first, open", "let's", numbered task steps, narrative, marketing claims | "must", "must not", "never", warnings, a short usage example |
| Explanation | numbered steps, "run", "click", "type", commands to execute, a full parameter table | opinion, "we think", alternatives, history, analogies, contractions |

## Tutorial checks (T#)

The author owns the learner's success. The page must work for every reader,
every time.

| # | Check | Fails when | Severity |
|---|---|---|---|
| T1 | Destination shown | The opening does not say what the learner will build or reach. "In this tutorial you will learn..." alone is a weak pattern: say what they will make | Minor |
| T2 | Prerequisites up front | See A3 | (A3) |
| T3 | One path | Any choice or alternative (M1) | Major |
| T4 | Results early and often | Over three steps in a row with no visible result; the final step has no expected output (A5) | Minor; Major for the final step |
| T5 | Narrative of the expected | No "you should see", sample output or sign of going wrong anywhere in the page | Minor |
| T6 | Minimal explanation | Over two sentences of explanation in a row (M2) | Major |
| T7 | Concrete | Steps described in the abstract ("configure the source as needed") instead of exact values | Major |
| T8 | Ending | No summary of what the learner built, or no next step | Minor |

Tutorial language: "We will...", "First, do x. Now, do y.", "The output
looks like...", "Notice that...", "You have built...".

## How-to checks (H#)

Assumes a competent reader with a real goal. Action and only action.

| # | Check | Fails when | Severity |
|---|---|---|---|
| H1 | Goal title | The title is a noun or feature name ("Key rotation", "API keys") or a gerund that could mean "whether to" ("Rotating keys"), not the goal ("How to rotate API keys", "Rotate API keys") | Minor |
| H2 | States the goal | The first lines do not say what problem it solves | Minor |
| H3 | Action only | Teaching or background (M2); a full option list that belongs in reference | Major |
| H4 | Logical sequence | Steps out of order (A2); one step holds several actions | Blocker for A2; Minor for several actions |
| H5 | Real-world use | The guide works only for one hard-coded case with no hint how to adapt | Minor |
| H6 | Confirm | No way to tell it worked (A5) | Major |
| H7 | Machine-shaped | The guide narrates the tool's buttons ("To deploy, press Deploy") without the judgement the reader needs | Minor |

How-to language: "This guide shows how to...", "If you want x, do y",
"For all options, see the [x reference]".

## Reference checks (R#)

Consulted, not read. Austere, neutral, complete, shaped like the product.

| # | Check | Fails when | Severity |
|---|---|---|---|
| R1 | Describe only | Instruction or opinion (M3) | Major |
| R2 | Standard pattern | Entries of one kind differ in shape (one has a type and default, the next does not; one has an example, one has errors and the next does not) | Major |
| R3 | Complete | An item used in an example or mentioned in text has no entry (diff the examples against the tables) | Major |
| R4 | Accurate | A default, type or value differs between table, text and example (A1, A4) | Blocker |
| R5 | Mirrors the product | Entries ordered by nothing the reader can predict (not alphabetical, not by the product's structure) | Minor |
| R6 | Examples | No example anywhere on the page | Minor |
| R7 | Versions | An entry marked deprecated or new with no version | Minor |

Reference language: state facts ("X defaults to 30"), list items, give
warnings ("You must not...").

## Explanation checks (X#)

Read away from the keyboard. Answers "why", makes connections, may hold
opinion.

| # | Check | Fails when | Severity |
|---|---|---|---|
| X1 | Bounded topic | No clear topic or "why" question; the title cannot take "About" in front | Minor |
| X2 | Context | Says what without why: no design reason, history, constraint or trade-off | Minor |
| X3 | No procedure | Steps or commands to run (M4) | Major |
| X4 | No reference dump | A full option or parameter table (M4) | Major |
| X5 | Alternatives | Presents one approach as the only one when the page itself names others | Minor |
| X6 | Links out | Mentions a task or setting with no link to its how-to or reference | Minor |

Explanation language: "The reason for x is...", "x is better than y
because...", "Some teams prefer...", "An x behaves like a y, except...".

## Fixing a mix

Do not delete the misplaced content. In the corrected version:

1. Replace it with one line and a link: "For why the scheduler works this
   way, see [link to explanation page: About scheduling]."
2. List it under "Move to another page" with the target type.
3. Keep one line of why in a tutorial or how-to if the step needs it.
