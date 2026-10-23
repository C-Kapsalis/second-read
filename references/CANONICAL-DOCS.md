# Canonical documentation style — conditional project guide

**Primary authority:** https://documentation.ubuntu.com/style-guide/ (consult current version when possible; verified 2026-10-23). **Do not apply to unrelated projects** merely because the content is technical. Apply when the documentation project follows Canonical conventions or the author explicitly selects this guide. These conventions complement, not replace, Diátaxis (https://diataxis.fr/).

## Checks worth making

- **Documentation type:** Determine whether the reader is learning (tutorial), performing a task (how-to), looking up a contract (reference), or understanding a concept (explanation). Propose moving content to the right page when it interrupts the task; not every mixture merits a new page.
- **Spelling:** Canonical's current guide specifies **US English** (the organization formerly used UK English). Do not impose British spelling from an older assumption.
- **Headings:** use **sentence case**, retain actual product names, do not skip levels, do not finish headings with periods, avoid hyperlinks and excess code formatting in headings; give each heading substantive content.
- **Branding:** maintain official capitalisation and version notation; e.g. “Ubuntu 24.04 LTS” (not “ubuntu 24.04 lts”). Verify product naming in a current product source rather than guessing.
- **Dates:** the documented example for a single day is “January 1, 2013”; follow the guide when the publication uses it, not as a universal news convention.
- **Links:** make text descriptive, preferably match the destination's topic/title, avoid “click here” and naked URLs. Use permalinks for links to versioned code where useful.
- **Commands:** clearly distinguish copyable command input from output. Explain the first occurrence of a placeholder; use consistent delimiters, or variables when repeated placeholder editing would be error-prone. Never invent command outputs or product flags.
- **Interface:** use real UI labels, bold the clickable item when the house style requires it, and keep menu navigation concise. Verify labels against the target product version.
- **Accessibility:** meaningful screenshots need alt text or equivalent accessible content; do not pretend an unprovided image was checked.
- **Lists:** numbered lists for true order-sensitive steps; use bullets when sequence does not matter.

## Before/after judgment

**Edit — house style and accessibility**
- Original heading: “How To Setup Your LXD Server”.
- Suggested: “Set up your LXD server” if the article's actual task is setup and this is its title. Sentence case, action wording and precise task help a reader. Verify LXD product naming; don't rewrite every title to start with a verb.

**Edit — placeholder safety**
- Draft: `lxc delete <instance>` with no explanation of `<instance>` anywhere.
- Suggested source-adjacent sentence: “Replace `<instance>` with the instance name you want to delete.” Also check that the operation, preconditions and warnings are verified; don't imply deletion is reversible.

**Leave — appropriate short reference heading**
- “Command-line options” is valid sentence case and adequate for a reference section; do not force an action verb as though it were a tutorial.

**Do not invent success criteria**
- If a setup procedure lacks an observable result, request product-authorized output or a tested verification command. Do not manufacture example output.

## Primary sources

- Canonical documentation style: https://documentation.ubuntu.com/style-guide/
- Diátaxis guidance: https://diataxis.fr/
- Product docs for the actual target/version supplied by the author (otherwise status unknown).
