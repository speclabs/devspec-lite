from __future__ import annotations

import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from devspec.cli import main
from devspec.framework import MANIFEST_PATH, diff_framework, read_install_manifest


class UpgradeLifecycleTests(unittest.TestCase):
    def test_adding_a_profile_preserves_project_work(self) -> None:
        # Re-running init to add a profile must not fail on, or overwrite, the developer's own
        # constitution, architecture queue, or overview. The only escape used to be --force,
        # which would have destroyed exactly those files.
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "codex", "--repo-state", "existing"])
            owned = {
                "devspec/constitution.md": "# Constitution\n\n| CP-001 | keep me |\n",
                "devspec/architecture/artifact-queue.md": "# Architecture Artifact Queue\n\n| DIA-001 | keep me |\n",
                "devspec/architecture/overview.md": "# Architecture Overview\n\nkeep me\n",
            }
            for path, content in owned.items():
                (target / path).write_text(content, encoding="utf-8")
            self.assertEqual(0, main(["init", "--target", str(target), "--profile", "claude", "--repo-state", "existing"]))
            for path, content in owned.items():
                self.assertEqual(content, (target / path).read_text(encoding="utf-8"), path)
            self.assertTrue((target / ".claude/skills/devspec-story/SKILL.md").is_file())
            self.assertTrue((target / "AGENTS.md").is_file())

    def run_cli(self, arguments: list[str]) -> tuple[int, str]:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = main(arguments)
        return result, output.getvalue()

    def test_init_writes_manifest_and_diff_is_clean(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            self.assertEqual(0, main(["init", "--target", str(target), "--profile", "codex", "--repo-state", "existing"]))
            manifest = read_install_manifest(target)
            self.assertEqual("codex", manifest["profile"])
            self.assertEqual("existing", manifest["repo_state"])
            self.assertTrue((target / MANIFEST_PATH).is_file())
            code, output = self.run_cli(["diff", "--target", str(target)])
            self.assertEqual(0, code)
            self.assertIn("Protected project-owned files", output)

    def test_sync_requires_force_for_local_framework_change_and_dry_run_is_read_only(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "codex", "--repo-state", "existing"])
            contract = target / "devspec/contracts/devspec.story.md"
            contract.write_text("local override\n", encoding="utf-8")
            self.assertIn("devspec/contracts/devspec.story.md", diff_framework(target, "codex")["modified"])
            self.assertEqual(1, main(["sync", "--target", str(target), "--profile", "codex"]))
            self.assertEqual("local override\n", contract.read_text(encoding="utf-8"))
            self.assertEqual(0, main(["sync", "--target", str(target), "--profile", "codex", "--force", "--dry-run"]))
            self.assertEqual("local override\n", contract.read_text(encoding="utf-8"))
            self.assertEqual(0, main(["sync", "--target", str(target), "--profile", "codex", "--force"]))
            self.assertNotEqual("local override\n", contract.read_text(encoding="utf-8"))

    def test_diff_reports_missing_files_and_init_force_preserves_project_owned_files(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "codex", "--repo-state", "new"])
            (target / "AGENTS.md").unlink()
            self.assertIn("AGENTS.md", diff_framework(target, "codex")["missing"])
            constitution = target / "devspec/constitution.md"
            constitution.write_text("# Constitution\n\nCP-001: protected\n", encoding="utf-8")
            # init now restores the missing wrapper instead of failing, and --force still
            # cannot reach a project-owned file.
            self.assertEqual(0, main(["init", "--target", str(target), "--profile", "codex", "--repo-state", "new", "--force"]))
            self.assertIn("CP-001: protected", constitution.read_text(encoding="utf-8"))
            self.assertTrue((target / "AGENTS.md").is_file())

    def test_sync_preserves_project_owned_constitution(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "codex", "--repo-state", "new"])
            constitution = target / "devspec/constitution.md"
            constitution.write_text("# Constitution\n\nCP-001: preserve this\n", encoding="utf-8")
            self.assertEqual(0, main(["sync", "--target", str(target), "--profile", "codex", "--force"]))
            self.assertIn("CP-001: preserve this", constitution.read_text(encoding="utf-8"))

    def test_sync_reports_obsolete_files_alongside_conflicts(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "all", "--repo-state", "existing"])
            contract = target / "devspec/contracts/devspec.story.md"
            contract.write_text("local override\n", encoding="utf-8")
            code, output = self.run_cli(["sync", "--target", str(target), "--profile", "codex"])
            self.assertEqual(1, code)
            self.assertIn("Sync conflicts", output)
            self.assertIn("Retained obsolete files", output)
            self.assertIn(".github/prompts/devspec.story.prompt.md", output)

    def test_sync_migrates_legacy_install_and_retains_obsolete_files(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "all", "--repo-state", "existing"])
            (target / MANIFEST_PATH).unlink()
            self.assertEqual(0, main(["sync", "--target", str(target), "--profile", "all"]))
            self.assertTrue((target / MANIFEST_PATH).is_file())
            code, output = self.run_cli(["sync", "--target", str(target), "--profile", "codex"])
            self.assertEqual(0, code)
            obsolete = diff_framework(target, "codex")["obsolete"]
            self.assertTrue(any(path.startswith(".github/") for path in obsolete))
            self.assertIn("Retained obsolete files", output)
            self.assertTrue((target / ".github/prompts/devspec.story.prompt.md").is_file())


if __name__ == "__main__":
    unittest.main()
