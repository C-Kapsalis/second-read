"""Guard practical invocation, source boundary and no-new-UI commitments."""
import pathlib
import re
import unittest

ROOT=pathlib.Path(__file__).resolve().parents[1]
SKILL=(ROOT/'SKILL.md').read_text()


class ArchitectureTests(unittest.TestCase):
    def test_one_skill_entrypoint(self):
        self.assertTrue(SKILL.startswith('---\nname: second-read\n'))
        self.assertEqual(len(list(ROOT.rglob('SKILL.md'))),1)

    def test_lean_root(self):
        self.assertLessEqual(len(SKILL.splitlines()),85)
        self.assertIn('author',SKILL.lower())

    def test_all_inline_references_exist(self):
        files=set(re.findall(r'\]\(references/([A-Z][A-Z-]+\.md)\)', SKILL))
        self.assertGreaterEqual(len(files),7)
        for file in files:
            with self.subTest(file=file):
                self.assertTrue((ROOT/'references'/file).is_file(),file)

    def test_paths_have_important_branches(self):
        r=(ROOT/'references/PATHWAYS.md').read_text()
        for name in ('KNOWLEDGE-BASES','PROJECT-CONTEXT','PR-AND-MEDIA-RELATIONS','DOCUMENTATION',
                     'EMAIL-MARKETING','JOURNALISM','BRAND-POSITIONING','SEO-CONTENT',
                     'LANDING-PAGES','AD-COPY','ANTI-FORMULAIC-PROSE'):
            self.assertIn(name, r)

    def test_canonical_is_doc_only(self):
        d=(ROOT/'references/DOCUMENTATION.md').read_text()
        self.assertIn('https://documentation.ubuntu.com/style-guide/',d)
        self.assertIn('sole house',d)
        self.assertIn('Do not use Canonical',d)
        self.assertNotIn('CANONICAL-DOCS.md',(ROOT/'references/PATHWAYS.md').read_text())

    def test_reader_questions_preserved(self):
        self.assertIn('Questions to yourself after reading this once',SKILL)
        self.assertIn('immediately after',SKILL)
        self.assertIn('two consequential',SKILL)

    def test_preview_not_approval_and_editor_unchanged(self):
        self.assertIn('not approved edits',SKILL)
        self.assertIn('python3 scripts/edit_review.py',SKILL)
        self.assertIn('unchanged',SKILL)

    def test_readme_links_not_prescriptive(self):
        readme=(ROOT/'README.md').read_text()
        for source in ('https://obsidian.md/help/properties','https://obsidian.md/help/links',
                       'https://www.notion.com/help/wikis-and-verified-pages',
                       'https://github.com/mattpocock/skills/tree/main/skills/productivity/writing-for-agents'):
            self.assertIn(source,readme)
        self.assertIn('do not need to change your organization',readme.lower())
        self.assertIn('knowledge_context.py',readme)


if __name__=='__main__':
    unittest.main()
