"""Protect the existing editing implementation while expanding references."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('edit_review', ROOT / 'scripts/edit_review.py')
editor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(editor)
REVIEW = json.loads((ROOT / 'assets/review.example.json').read_text())


class ExistingEditorTests(unittest.TestCase):
    def test_original_fixture_validates(self):
        r = editor.validate(REVIEW)
        self.assertEqual(r['blocks'], 7)
        self.assertEqual(r['questions'], 3)

    def test_no_edit_preserves_original(self):
        self.assertEqual(editor.apply(REVIEW, []), REVIEW['source']['text'])

    def test_accepted_edits_apply(self):
        result = editor.apply(REVIEW, ['e1', 'e3'])
        self.assertIn('The city should test more reliable night buses', result)
        self.assertNotIn('Free fares will solve the problem for everyone.', result)

    def test_conflicting_edits_rejected(self):
        review = copy.deepcopy(REVIEW)
        duplicate = copy.deepcopy(review['suggestions'][0])
        duplicate['id'] = 'other'
        review['suggestions'].append(duplicate)
        with self.assertRaisesRegex(editor.ReviewError, 'edit conflict'):
            editor.apply(review, ['e1', 'other'])

    def test_unknown_edit_rejected(self):
        with self.assertRaisesRegex(editor.ReviewError, 'unknown edit'):
            editor.apply(REVIEW, ['made-up'])

    def test_changed_source_is_rejected(self):
        review = copy.deepcopy(REVIEW)
        review['source']['blocks'][0]['text'] += ' Changed.'
        with self.assertRaisesRegex(editor.ReviewError, 'source.text must equal'):
            editor.validate(review)

    def test_unanchored_quote_is_rejected(self):
        review = copy.deepcopy(REVIEW)
        review['suggestions'][0]['evidence']['quote'] = 'A quote not in the draft.'
        with self.assertRaisesRegex(editor.ReviewError, 'quote is not present'):
            editor.validate(review)

    def test_question_must_anchor_to_same_passage(self):
        review = copy.deepcopy(REVIEW)
        review['questions'][0]['after_block_id'] = 'p6'
        with self.assertRaisesRegex(editor.ReviewError, 'anchored to the tested passage'):
            editor.validate(review)

    def test_html_renderer_escapes_embedded_data(self):
        review = copy.deepcopy(REVIEW)
        review['context'][0]['text'] = '</script><script>alert(1)</script>'
        rendered = editor.render(review)
        self.assertNotIn('</script><script>alert(1)', rendered)
        self.assertIn('<\\/script>', rendered)


if __name__ == '__main__':
    unittest.main()
