"""Routing and packaging checks; qualitative model evaluation remains separate."""
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SKILL = (ROOT / 'SKILL.md').read_text(encoding='utf-8')


class ReferenceTests(unittest.TestCase):
    def test_root_skill_frontmatter(self):
        self.assertTrue(SKILL.startswith('---\nname: second-read\n'))

    def test_every_named_reference_exists(self):
        refs = set(re.findall(r'references/([A-Z][A-Z-]+\.md)', SKILL))
        self.assertGreaterEqual(len(refs), 8)
        for name in refs:
            with self.subTest(name=name):
                self.assertTrue((ROOT / 'references' / name).is_file(), name)

    def test_all_specializations_routed(self):
        route = (ROOT / 'references/PATHWAYS.md').read_text()
        for name in ('EMAIL-MARKETING', 'SEO-CONTENT', 'LANDING-PAGES', 'AD-COPY',
                     'JOURNALISM', 'DATA-STORYTELLING', 'PR-AND-MEDIA-RELATIONS',
                     'DOCUMENTATION', 'KNOWLEDGE-BASES', 'PROJECT-CONTEXT',
                     'BRAND-POSITIONING', 'AUTHOR-RULESETS'):
            with self.subTest(name=name):
                self.assertIn(name, route)

    def test_canonical_is_docs_only(self):
        docs = (ROOT / 'references/DOCUMENTATION.md').read_text()
        self.assertIn('sole house', docs)
        self.assertIn('US English', docs)
        self.assertIn('Do not use Canonical', docs)

    def test_editing_stays_primary(self):
        self.assertIn('Deliver edits, not a diagnosis', SKILL)
        self.assertIn('not approved edits', SKILL)
        self.assertIn('two consequential proposals', SKILL)

    def test_ordinary_chat_questions_stay_positioned(self):
        self.assertIn('Questions to yourself after reading this once', SKILL)
        self.assertIn('immediately after', SKILL)

    def test_no_blanket_ai_diagnosis(self):
        guide = (ROOT / 'references/ANTI-FORMULAIC-PROSE.md').read_text()
        self.assertIn('Never infer', guide)
        self.assertIn('leave', guide.lower())

    def test_external_primary_style_guides_linked(self):
        self.assertIn('https://documentation.ubuntu.com/style-guide/', (ROOT/'references/DOCUMENTATION.md').read_text())
        self.assertIn('https://reutersagency.com/about/standards-values/', (ROOT/'references/JOURNALISM.md').read_text())
        self.assertIn('https://www.prsa.org/professional-development/prsa-resources/ethics',
                      (ROOT/'references/PR-AND-MEDIA-RELATIONS.md').read_text())
        self.assertIn('https://developers.google.com/search/docs/fundamentals/creating-helpful-content',
                      (ROOT/'references/SEO-CONTENT.md').read_text())

    def test_existing_executables_preserved(self):
        for name in ('edit_review.py','product_verify.py','editor_template.html','project_context.py'):
            self.assertTrue((ROOT/'scripts'/name).is_file(),name)


if __name__ == '__main__':
    unittest.main()
