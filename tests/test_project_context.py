"""Deterministic provenance/shape checks for project context inputs."""
import copy
import importlib.util
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('project_context', ROOT / 'scripts/project_context.py')
context = importlib.util.module_from_spec(spec)
spec.loader.exec_module(context)
SAMPLE = json.loads((ROOT / 'assets/project-context.example.json').read_text())


class ProjectContextTests(unittest.TestCase):
    def check_error(self, transform, match):
        data = copy.deepcopy(SAMPLE)
        transform(data)
        with self.assertRaisesRegex(context.ContextError, match):
            context.validate_context(data)

    def test_valid_sample(self):
        result = context.validate_context(SAMPLE)
        self.assertTrue(result['valid'])
        self.assertEqual(result['source_count'], 2)
        self.assertEqual(result['rule_count'], 2)

    def test_missing_project_source(self):
        self.check_error(lambda x: x['project'].update(source_id='phantom'), 'missing source')

    def test_duplicate_source_ids(self):
        self.check_error(lambda x: x['sources'].append(copy.deepcopy(x['sources'][0])), 'duplicate source')

    def test_duplicate_rule_ids(self):
        self.check_error(lambda x: x['rules'].append(copy.deepcopy(x['rules'][0])), 'duplicate rule')

    def test_rule_source_missing(self):
        self.check_error(lambda x: x['rules'][0].update(source_id='unknown'), 'missing source')

    def test_unknown_kind(self):
        self.check_error(lambda x: x['rules'][0].update(kind='mandatory_everywhere'), 'unknown rule kind')

    def test_unknown_scope(self):
        self.check_error(lambda x: x['rules'][0].update(scope=['science_fiction_planet']), 'valid nonempty scope')

    def test_all_scope_only(self):
        self.check_error(lambda x: x['rules'][0].update(scope=['all', 'ad']), 'cannot be mixed')

    def test_empty_source_location(self):
        self.check_error(lambda x: x['sources'][0].update(location=' '), 'location must be a nonempty')

    def test_project_identity_must_be_explicit(self):
        self.check_error(lambda x: x['project'].update(name=''), 'project.name must be a nonempty')

    def test_bool_version_not_accepted(self):
        self.check_error(lambda x: x.update(schema_version=True), 'schema_version')

    def test_empty_rules_allowed(self):
        data = copy.deepcopy(SAMPLE)
        data['rules'] = []
        self.assertEqual(context.validate_context(data)['rule_count'], 0)


if __name__ == '__main__':
    unittest.main()
