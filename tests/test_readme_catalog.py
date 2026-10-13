"""The visible inventory must include every record and report pending skills honestly."""
import importlib.util
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('readme_catalog', Path(__file__).parents[1] / 'scripts/readme_catalog.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class ReadmeCatalogTests(unittest.TestCase):
    def setUp(self):
        self.entries = [
            dict(id='sample', kind='local', status='active', entry='skills/sample/SKILL.md', description='Review a plan'),
            dict(id='vendor:pending', kind='external', status='reference-only', project='https://example.com', description='Collect weekly updates'),
        ]

    def test_every_record_has_a_row_and_pending_is_distinguished(self):
        table = module.render(self.entries)
        self.assertIn('共 **2** 个条目', table)
        self.assertIn('[$sample](skills/sample/SKILL.md)', table)
        self.assertIn('[$vendor:pending](https://example.com)', table)
        self.assertIn('Collect weekly updates | 仅供参考', table)

    def test_upstream_link_uses_registered_commit(self):
        entry = dict(id='vendor:tool', kind='external', status='active', project='https://github.com/example/repo',
                     ref='a'*40, entry='skills/tool/SKILL.md', description='Execute a probe')
        self.assertIn('https://github.com/example/repo/blob/'+'a'*40+'/skills/tool/SKILL.md', module.render([entry]))

    def test_table_refresh_preserves_surrounding_instructions(self):
        before = 'User instructions\n'+module.START+'\nold rows\n'+module.END+'\nMaintenance rules\n'
        after = module.update_readme(before, 'New table\n')
        self.assertEqual(after, 'User instructions\n'+module.START+'\nNew table\n'+module.END+'\nMaintenance rules\n')

    def test_missing_or_duplicated_markers_stop_refresh(self):
        for text in ['Unmarked README', module.START+'\n'+module.START+'\n'+module.END]:
            with self.subTest(text=text), self.assertRaises(ValueError):
                module.update_readme(text, 'New table\n')

if __name__ == '__main__':
    unittest.main()
