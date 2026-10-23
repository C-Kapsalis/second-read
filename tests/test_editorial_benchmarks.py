"""Only fixture/matcher mechanics; do not call this a tested model success rate."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('evaluate_editorial_cases', ROOT/'scripts/evaluate_editorial_cases.py')
evalr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(evalr)
CASES = evalr.read_jsonl(ROOT/'benchmarks/editorial_cases.jsonl')


class EditorialBenchmarkTests(unittest.TestCase):
    def test_all_cases_are_grounded(self):
        self.assertEqual(len(evalr.validate_cases(CASES)), len(CASES))
        self.assertGreaterEqual(len(CASES), 30)

    def test_each_pathway_has_examples(self):
        pathways = {x['pathway'] for x in CASES}
        for path in ('essay', 'policy', 'fiction', 'docs', 'brand', 'email',
                     'ad', 'blog', 'landing_page', 'journalism'):
            self.assertIn(path, pathways)

    def test_nearby_edit_and_leave_examples(self):
        decisions = {x['decision'] for x in CASES}
        self.assertEqual(decisions, {'edit', 'leave', 'ask', 'visual'})
        self.assertGreaterEqual(sum(x['decision']=='leave' for x in CASES), 12)

    def test_routing_agreement_not_quality_claim(self):
        ex = CASES[:3]
        responses = [{'case_id':c['id'], 'decision':c['decision'], 'source_quote':c['source_quote']} for c in ex]
        report = evalr.evaluate(ex, responses)
        self.assertEqual(report['evaluated'],3)
        self.assertEqual(report['decision_matches'],3)
        self.assertIn('not editing quality', report['label'])

    def test_false_edit_is_counted(self):
        case = next(c for c in CASES if c['decision']=='leave')
        report = evalr.evaluate([case], [{'case_id':case['id'], 'decision':'edit',
                                           'source_quote':case['source_quote']}])
        self.assertEqual(report['false_edits_on_leave_cases'],1)
        self.assertEqual(report['decision_matches'],0)

    def test_ungrounded_quote_fails_source_check(self):
        case = next(c for c in CASES if c['decision']=='edit')
        report = evalr.evaluate([case], [{'case_id':case['id'], 'decision':'edit',
                                           'source_quote':'fabricated quote'}])
        self.assertEqual(report['decision_matches'],1)
        self.assertEqual(report['source_grounded'],0)

    def test_unknown_model_case_rejected(self):
        with self.assertRaises(evalr.EvaluationError):
            evalr.evaluate(CASES[:1], [{'case_id':'not-present', 'decision':'leave'}])

    def test_duplicate_fixture_id_rejected(self):
        with self.assertRaises(evalr.EvaluationError):
            evalr.validate_cases([CASES[0],CASES[0]])


if __name__ == '__main__':
    unittest.main()
