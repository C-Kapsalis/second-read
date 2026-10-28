# Second Read 0.3.1 — portable plugin package

Adds a skills-only portable plugin package with listing metadata and icon for
ChatGPT/Codex directory review. Adds packaging and publishing instructions for
the standalone skill, Claude plugin and portable package. Existing editing
behavior is unchanged.

# Second Read 0.3.0 — editorial architecture and context update

One skill, same optional offline editor, no forced output or UI change.

Changes: leaner `SKILL.md`; unified semantic/reader/restraint decisions; branch-specific PR, journalism, brand, email, ads, SEO, landing pages, documentation and data-storytelling references; Canonical documentation style enforced only for documentation; targeted Obsidian/Notion/Markdown context retrieval with no assumption of connector access; `README.md` with *optional* knowledge-base organization links; a tested read-only Markdown navigator.

**Evidence limits:** no live-model editorial benchmark is claimed; user-supplied marketing scores/benchmarks are diagnostic proposals, not ground-truth performance guarantees. External standards should be consulted in their current editions; no complete copyrighted style guide is reproduced here.

**Compatibility:** previous JSON editing and verification scripts and offline editor template remain untouched.

**Portability fixes:** normalize vault and product-checkout paths before containment checks so the read-only helpers and regression suite behave consistently on macOS paths that resolve through `/var` to `/private/var`.
