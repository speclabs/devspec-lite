from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from xml.etree import ElementTree

from devspec_lite.cli import main
from devspec_lite.definitions import COMMANDS
from devspec_lite.framework import doctor


class FrameworkTests(unittest.TestCase):
    def test_init_all_and_doctor(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            self.assertEqual(0, main(["init", "--target", str(target), "--profile", "all", "--repo-state", "existing"]))
            self.assertEqual([], doctor(target, "all"))
            self.assertEqual(0, main(["doctor", "--target", str(target), "--profile", "all"]))
            self.assertEqual(len(COMMANDS), len(list((target / "devspec/contracts").glob("*.md"))))
            self.assertTrue((target / ".github/agents/devspec.quickfix.agent.md").is_file())
            self.assertTrue((target / ".claude/skills/devspec-grooming/SKILL.md").is_file())
            self.assertIn("devspec.extract", (target / "devspec/foundation/repository-state.md").read_text(encoding="utf-8"))

    def test_ask_protocol_requires_interactive_choices(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "codex", "--repo-state", "new"])
            root = ElementTree.fromstring((target / "devspec/protocols/ask.xml").read_text(encoding="utf-8"))
            interaction = root.find("interaction")
            self.assertIsNotNone(interaction)
            self.assertEqual("interactive", interaction.attrib["mode"])
            self.assertEqual("true", interaction.find("recommendation").attrib["required"])
            self.assertEqual("true", interaction.find("custom-answer").attrib["required"])
            self.assertTrue((target / "AGENTS.md").is_file())
            self.assertFalse((target / ".github").exists())

    def test_contract_xml_and_quickfix_routing_are_present(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "copilot", "--repo-state", "existing"])
            quickfix = (target / "devspec/contracts/devspec.quickfix.md").read_text(encoding="utf-8")
            self.assertIn("route risky work", quickfix)
            self.assertIn('<protocol ref="ask" />', quickfix)
            self.assertIn("devspec/contracts/devspec.quickfix.md", (target / ".github/prompts/devspec.quickfix.prompt.md").read_text(encoding="utf-8"))
            self.assertEqual([], doctor(target, "copilot"))

    def test_init_refuses_changed_managed_file(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "codex", "--repo-state", "new"])
            contract = target / "devspec/contracts/devspec.story.md"
            contract.write_text("user change", encoding="utf-8")
            self.assertEqual(2, main(["init", "--target", str(target), "--profile", "codex", "--repo-state", "new"]))

    def test_doctor_reports_missing_contract(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "gemini", "--repo-state", "new"])
            (target / "devspec/contracts/devspec.rules.md").unlink()
            issues = doctor(target, "gemini")
            self.assertTrue(any("devspec.rules.md" in issue for issue in issues))

    def test_doctor_rejects_wrapper_logic_or_missing_reference(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "claude", "--repo-state", "new"])
            wrapper = target / ".claude/skills/devspec-story/SKILL.md"
            wrapper.write_text("<workflow />", encoding="utf-8")
            issues = doctor(target, "claude")
            self.assertTrue(any("does not reference contract" in issue for issue in issues))
            self.assertTrue(any("duplicates workflow logic" in issue for issue in issues))


if __name__ == "__main__":
    unittest.main()
