"""Tests only the read-only Markdown discovery helper; no live Notion connection."""
import importlib.util
import json
import os
import pathlib
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
FILE = ROOT / 'scripts' / 'knowledge_context.py'
spec = importlib.util.spec_from_file_location('knowledge_context', FILE)
mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)


class VaultContextTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = pathlib.Path(self.tmp.name) / 'vault'
        (self.root / 'Projects' / 'Launch').mkdir(parents=True)
        (self.root / 'Notes').mkdir()
        (self.root / '.obsidian').mkdir()
        self.target = self.root / 'Projects' / 'Launch' / 'draft.md'
        self.target.write_text('---\nproject: Alpha\ncampaign: autumn\n---\nWe announce Alpha. [[Brief]]\n')
        (self.root / 'Projects' / 'Launch' / 'Brief.md').write_text('---\nproject: Alpha\nstatus: approved\n---\nDo not claim a launch date.\n')
        (self.root / 'Notes' / 'feedback.md').write_text('---\nproject: Alpha\n---\nComments on [[Projects/Launch/draft]].\n')
        (self.root / 'Notes' / 'unrelated.md').write_text('Here is unrelated personal material and TOKEN_SECRET_42810.\n')
        (self.root / '.obsidian' / 'private.md').write_text('project: Alpha\nSUPER_SECRET\n')

    def test_frontmatter_parsing_handles_lists_and_whitelisted_keys(self):
        m = mod.parse_metadata('---\nproject: Alpha\ntags:\n  - draft\n  - second-read\nsecret: pw\n---\nBody')
        self.assertEqual(m['tags'], ['draft', 'second-read'])
        self.assertNotIn('secret', m)

    def test_related_returns_linked_notes_and_omits_unrelated_bodies(self):
        output = mod.related(self.root, pathlib.Path('Projects/Launch/draft.md'))
        paths = [v['path'] for v in output['candidates']]
        self.assertIn('Projects/Launch/Brief.md', paths)
        self.assertIn('Notes/feedback.md', paths)
        self.assertNotIn('Notes/unrelated.md', paths)
        self.assertNotIn('.obsidian/private.md', paths)
        self.assertTrue(output['read_only'])
        self.assertNotIn('TOKEN_SECRET_42810', json.dumps(output))
        self.assertIn('campaign', output['target_metadata'])

    def test_read_only_after_cli_run(self):
        before = {p.as_posix():p.read_bytes() for p in self.root.rglob('*.md')}
        ret = subprocess.run([sys.executable,str(FILE),'--root',str(self.root),'--target','Projects/Launch/draft.md'],
                             capture_output=True,text=True,check=False)
        self.assertEqual(ret.returncode,0,ret.stderr)
        self.assertTrue(json.loads(ret.stdout)['candidates'])
        after = {p.as_posix():p.read_bytes() for p in self.root.rglob('*.md')}
        self.assertEqual(before,after)

    def test_max_files_truncation_is_reported(self):
        result = mod.related(self.root, self.target, max_files=1)
        self.assertTrue(result['scan_truncated'])
        self.assertEqual(result['target'], 'Projects/Launch/draft.md')

    def test_target_outside_root_rejected(self):
        outside = pathlib.Path(self.tmp.name) / 'unrelated.md'
        outside.write_text('Unrelated.')
        with self.assertRaises(mod.ContextError):
            mod.related(self.root, outside)

    def test_symlinks_outside_root_never_included(self):
        outside = pathlib.Path(self.tmp.name) / 'external.md'
        outside.write_text('secret confidential')
        linked = self.root / 'Projects' / 'Launch' / 'external.md'
        try:
            linked.symlink_to(outside)
        except (NotImplementedError, OSError):
            self.skipTest('symlinks unavailable')
        result = mod.related(self.root,self.target)
        self.assertNotIn('Projects/Launch/external.md',[x['path'] for x in result['candidates']])
        with self.assertRaises(mod.ContextError):
            mod.related(self.root,linked)

    def test_markdown_links_and_wikilink_headers(self):
        links = mod.link_targets('[[Page#Heading|alias]] and [guide](../Guides/Guide%20A.md#setup) and [url](https://example.com)')
        self.assertEqual(links,['Page','../Guides/Guide A.md'])

    def test_ambiguous_global_wikilink_not_arbitrarily_resolved(self):
        for branch in ('A','B'):
            (self.root / branch).mkdir()
            (self.root / branch / 'Same.md').write_text('Contents')
        note = mod.read_note(self.target, self.root, 10000)
        notes = {}
        for branch in ('A','B'):
            p = self.root / branch / 'Same.md'
            notes[p.relative_to(self.root).as_posix()] = mod.read_note(p,self.root,10000)
        by_stem={'same':['A/Same.md','B/Same.md']}
        self.assertIsNone(mod.resolve_link('Same',note,notes,by_stem))


if __name__=='__main__':
    unittest.main()
