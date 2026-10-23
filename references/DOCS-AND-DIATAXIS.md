# Documentation and Diátaxis: the reader must complete a task

Apply the actual **reader need** rather than assuming every README must contain everything. Diátaxis distinguishes **tutorial** (learning), **how-to** (accomplishing a goal), **reference** (finding accurate technical facts) and **explanation** (understanding ideas). It is often appropriate to **link** to another mode rather than cram all four into one document.

## Reader journey verification

- Identify what the intended reader is trying to achieve, what they already know, and which page/section they should visit first.
- Check prerequisites *before* use: required access, installation, environment variables, commands, files and keys.
- Check code against the actual source/version: flags, ports, values, filenames and outputs must match. Mark unexecuted instructions unverified; run only authorized probes.
- Check that a tutorial has a coherent, bounded successful path, a how-to provides a goal-oriented procedure, a reference is precise and scannable, and explanation does not demand untested actions.
- Each consequential procedure should lead to **an observable success condition** when the product makes it possible. If not supplied, ask for the actual verification result.
- Place destructive-command warnings **before** execution and never bury security-critical prerequisites.
- Prefer meaningful headings and links, actual product UI terms, and clear placeholder instructions. Do not treat a heading's tone as a technical defect.
- A README should orient and route users without copying the entire docs site.

## Conditional Canonical style

If the project follows Canonical (or the author explicitly requests the official Ubuntu documentation style), load **`CANONICAL-DOCS.md`**: US English, sentence-case headings, branding/version names, link conventions, code placeholders and accessibility. The authoritative source is https://documentation.ubuntu.com/style-guide/ . Do not automatically impose Canonical rules on every open-source project.

## Before/after decisions

**Edit — command prerequisite comes too late**
- P2: `export SERVICE_TOKEN="$TOKEN"`; P5: “Generate the token in Settings.”
- Proposed: move the supplied token-generation instruction **before** P2, or add a link to its verified setup page. Never invent the token creation procedure.

**Edit — example vs reference conflict**
- Reference lists `--config`, but tutorial uses `--configs`. Verify the exact flag in the target version and change the wrong occurrence; do not assume which without product evidence.

**Leave — reference lacks handholding**
- API parameter table accurately describes types and defaults and links to a tutorial. Do not add a 10-step walkthrough inside the reference merely for warmth.

**Leave — README as navigation**
- A short README links newcomers to “Quickstart,” “How-to guides,” “API reference” and “Architecture.” If those destinations exist and work, no need to expand all content into the README.

**Question in sequence**

After the source command block: “At this point, has the reader been told where the credential comes from?” Link to an actual proposed insertion/move if the answer matters.

## Sources

- Diátaxis: https://diataxis.fr/
- Canonical conditional style: https://documentation.ubuntu.com/style-guide/
- `PRODUCT-VERIFICATION.md` for authorized source/runtime inspection.
