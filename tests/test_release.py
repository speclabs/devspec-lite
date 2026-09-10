from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

from devspec import __version__


ROOT = Path(__file__).resolve().parents[1]


class ReleaseMetadataTests(unittest.TestCase):
    def test_pyproject_reads_the_single_cli_version(self) -> None:
        pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
        self.assertIn('dynamic = ["version"]', pyproject)
        self.assertIn('version = {attr = "devspec.__version__"}', pyproject)
        self.assertNotIn('\nversion = "', pyproject)

    def test_release_tag_must_match_package_version(self) -> None:
        command = [sys.executable, str(ROOT / "scripts" / "verify_release_version.py")]
        matching = subprocess.run([*command, "--tag", f"v{__version__}"], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(0, matching.returncode, matching.stderr)
        mismatched = subprocess.run([*command, "--tag", "v9.9.9"], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(2, mismatched.returncode)
        self.assertIn("does not match package version", mismatched.stderr)

    def test_release_templates_are_parameterized(self) -> None:
        winget = (ROOT / "packaging" / "winget" / "Devspec.installer.yaml").read_text(encoding="utf-8")
        homebrew = (ROOT / "packaging" / "homebrew" / "devspec.rb").read_text(encoding="utf-8")
        self.assertIn("REPLACE_WITH_VERSION", winget)
        self.assertIn("REPLACE_WITH_RELEASE_URL", winget)
        self.assertIn("REPLACE_WITH_RELEASE_SHA256", winget)
        self.assertIn("REPLACE_WITH_VERSION", homebrew)
        self.assertIn("REPLACE_WITH_RELEASE_SHA256", homebrew)

    def test_release_workflows_generate_and_publish_artifacts(self) -> None:
        python_publish = (ROOT / ".github" / "workflows" / "python-package-publish.yml").read_text(encoding="utf-8")
        winget_publish = (ROOT / ".github" / "workflows" / "winget-package-publish.yml").read_text(encoding="utf-8")
        homebrew_publish = (ROOT / ".github" / "workflows" / "homebrew-package-publish.yml").read_text(encoding="utf-8")
        self.assertIn("verify_release_version.py", python_publish)
        self.assertIn("devspec-python-package-checksums.txt", python_publish)
        self.assertIn("pypa/gh-action-pypi-publish", python_publish)
        self.assertIn("Get-FileHash", winget_publish)
        self.assertIn("devspec.exe.sha256", winget_publish)
        self.assertIn("REPLACE_WITH_RELEASE_SHA256", winget_publish)
        self.assertIn("curl -fsSL", homebrew_publish)
        self.assertIn("REPLACE_WITH_RELEASE_SHA256", homebrew_publish)


if __name__ == "__main__":
    unittest.main()