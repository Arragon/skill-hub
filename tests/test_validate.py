"""Broken registry/package fixtures must fail before a maintainer publishes them."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('hub_validate', Path(__file__).parents[1] / 'scripts/validate.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class HubValidationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.local = dict(id='sample', kind='local', entry='skills/sample/SKILL.md', status='active',
                          description='Example', requires=['text'], provenance='user-maintained', license='not-granted')
        self.entries = [self.local]
        self.write('skills/sample/SKILL.md', '---\nname: sample\ndescription: Example\n---\n\n# Sample\n')
        self.save()

    def write(self, name, text):
        p = self.root / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)

    def save(self):
        self.write('catalog.json', json.dumps(dict(schema_version=1, skills=self.entries)))

    def errors(self):
        self.save()
        return '\n'.join(module.validate(self.root))

    def test_valid_package(self):
        self.assertEqual(self.errors(), '')

    def test_duplicate_id(self):
        self.entries.append(dict(self.local))
        self.assertIn('duplicate id', self.errors())

    def test_missing_entry(self):
        (self.root / self.local['entry']).unlink()
        self.assertIn('missing entry', self.errors())

    def test_name_mismatch(self):
        self.write(self.local['entry'], '---\nname: wrong\ndescription: Example\n---\n')
        self.assertIn('name mismatch', self.errors())

    def test_entry_escape(self):
        self.local['entry'] = '../outside/SKILL.md'
        self.assertIn('unsafe entry', self.errors())

    def test_symlink_is_not_a_portable_package(self):
        (self.root / 'skills/sample/alias.md').symlink_to('SKILL.md')
        self.assertIn('symlink', self.errors())

    def test_markdown_reference_missing(self):
        with (self.root / self.local['entry']).open('a') as f:
            f.write('\n[Required](references/missing.md)\n')
        self.assertIn('broken link', self.errors())

    def test_external_requires_fixed_commit(self):
        self.entries.append(dict(id='vendor:skill', kind='external', status='active', description='External',
            requires=['text'], provenance='upstream', license='unknown', project='https://github.com/example/skills',
            ref='main', entry='skills/skill/SKILL.md', upstream_name='skill', entry_sha256='a'*64,
            verified='2026-10-13', verification='entry-content-read'))
        self.assertIn('invalid ref', self.errors())

    def test_reference_only_needs_reason(self):
        self.entries.append(dict(id='vendor:pending', kind='external', status='reference-only', description='Pending',
            requires=['text'], provenance='upstream', license='unknown', project='https://example.com'))
        self.assertIn('missing reason', self.errors())

    def test_unregistered_skill_cannot_be_published(self):
        self.write('skills/unregistered/SKILL.md', '---\nname: unregistered\n---\n')
        self.assertIn('unregistered skill', self.errors())

    def test_platform_metadata_rejected(self):
        self.write('skills/sample/agents/openai.yaml', 'interface: {}\n')
        self.assertIn('platform metadata', self.errors())

    def test_missing_composite_fallback(self):
        self.write('skills/sample/manifest.json', json.dumps({'internal_fallback_playbooks':['child']}))
        self.assertIn('missing fallback', self.errors())

    def test_invalid_registry_shape_is_reported(self):
        self.write('catalog.json', '{"schema_version":1,"skills":null}')
        self.assertIn('skills must be a list', '\n'.join(module.validate(self.root)))

if __name__ == '__main__':
    unittest.main()
