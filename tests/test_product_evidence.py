"""Regression tests: evidence authority is narrower than lexical/source occurrence."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('product_verify', ROOT / 'scripts/product_verify.py')
pv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pv)


class ProductEvidenceTests(unittest.TestCase):
    def test_source_file_does_not_prove_runtime(self):
        with tempfile.TemporaryDirectory() as td:
            work = Path(td)
            (work/'README.md').write_text('The widget exists here.', encoding='utf-8')
            manifest = {'schema_version':1, 'claims':[{
                'id':'widget', 'quote':'The widget exists here.',
                'section_id':'readme', 'required_authority':'runtime',
                'probe':{'type':'file_exists','path':'README.md'}}]}
            report = pv.verify_manifest(work, manifest, (work/'README.md').read_text())
            self.assertFalse(report['ready_for_product_claims'])
            self.assertEqual(report['claims'][0]['status'], 'corroborated')

    def test_execution_opt_in_returns_unknown(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root/'README.md').write_text('The widget runs locally.', encoding='utf-8')
            manifest={'schema_version':1,'claims':[{
                'id':'run', 'quote':'The widget runs locally.', 'section_id':'demo',
                'required_authority':'runtime',
                'probe':{'type':'command','argv':['python3','--version'], 'expected_exit':0}}]}
            report=pv.verify_manifest(root, manifest, (root/'README.md').read_text())
            self.assertFalse(report['ready_for_product_claims'])
            self.assertEqual(report['claims'][0]['status'], 'unknown')


if __name__ == '__main__':
    unittest.main()
