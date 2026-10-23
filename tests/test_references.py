"""Packaging/ref-routing checks; not a replacement for qualitative model evaluation."""
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
        self.assertGreaterEqual(len(refs), 12)
        for name in refs:
            with self.subTest(name=name):
                self.assertTrue((ROOT / 'references' / name).is_file(), name)

    def test_all_specializations_routed(self):
        route = (ROOT / 'references/PATHWAYS.md').read_text()
        for name in ['EMAIL-MARKETING', 'SEO-CONTENT', 'LANDING-PAGES', 'AD-COPY',
                     'JOURNALISM', 'DATA-STORYTELLING', 'CANONICAL-DOCS',
                     'PROJECT-CONTEXT', 'AUTHOR-RULESETS']:
            with self.subTest(name=name):
                self.assertIn(name, route)

    def test_canonical_is_scoped(self):
        self.assertIn('only when', (ROOT/'references/PATHWAYS.md').read_text())
        self.assertIn('US English', (ROOT/'references/CANONICAL-DOCS.md').read_text())

    def test_editing_stays_primary(self):
        self.assertIn('Show editable changes first', SKILL)
        self.assertIn('provisional, not-yet-approved revised draft', SKILL)

    def test_ordinary_chat_questions_stay_positioned(self):
        self.assertIn('Questions to yourself after reading this once', SKILL)
        self.assertIn('immediately after', SKILL)

    def test_no_blanket_ai_diagnosis(self):
        guide = (ROOT / 'references/NATURAL-VOICE.md').read_text()
        self.assertIn('not AI-authorship detection', guide)
        self.assertIn('leave', guide.lower())

    def test_external_style_guides_are_linked(self):
        self.assertIn('https://documentation.ubuntu.com/style-guide/', (ROOT/'references/CANONICAL-DOCS.md').read_text())
        self.assertIn('https://www.ox.ac.uk/about/the-university/brand/style-guide', (ROOT/'references/JOURNALISM.md').read_text())
        self.assertIn('https://developers.google.com/search/docs/fundamentals/creating-helpful-content', (ROOT/'references/SEO-CONTENT.md').read_text())

    def test_script_still_exists(self):
        self.assertTrue((ROOT / 'scripts/edit_review.py').is_file())
        self.assertTrue((ROOT / 'scripts/product_verify.py').is_file())
        self.assertTrue((ROOT / 'scripts/editor_template.html').is_file())


if __name__ == '__main__':
    unittest.main()
