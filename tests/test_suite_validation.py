"""Exercise the bundled suite validator against complete and broken packages."""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

class SuiteValidationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        source = Path(__file__).parents[1] / 'skills/ui-ux-design-suite'
        self.root = Path(self.tmp.name) / source.name
        shutil.copytree(source, self.root, ignore=shutil.ignore_patterns('__pycache__'))

    def run_validator(self):
        return subprocess.run([sys.executable, str(self.root / 'scripts/validate_suite.py')], capture_output=True, text=True)

    def test_complete_suite_accepts_existing_wildcard_references(self):
        result = self.run_validator()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_missing_declared_fallback_is_rejected(self):
        manifest = json.loads((self.root / 'manifest.json').read_text())
        child = manifest['internal_fallback_playbooks'][0]
        (self.root / 'references' / f'fallback-{child}.md').unlink()
        result = self.run_validator()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('missing fallback', result.stdout)

if __name__ == '__main__':
    unittest.main()
