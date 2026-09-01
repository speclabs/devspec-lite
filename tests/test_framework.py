from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from xml.etree import ElementTree

from devspec_lite.cli import main
from devspec_lite.definitions import COMMANDS
from devspec_lite.framework import PROFILES, doctor, install_framework, xml_block


class FrameworkTests(unittest.TestCase):
    def test_version_flag(self) -> None:
        with self.assertRaises(SystemExit) as result:
            main(["--version"])
        self.assertEqual(0, result.exception.code)

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

    def test_init_and_doctor_every_profile(self) -> None:
        for profile in PROFILES:
            with self.subTest(profile=profile), tempfile.TemporaryDirectory() as raw:
                target = Path(raw)
                install_framework(target, profile, "existing")
                self.assertEqual([], doctor(target, profile))

    def test_doctor_checks_required_xml_tags_and_templates(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            install_framework(target, "codex", "existing")
            (target / "devspec/protocols/run.xml").write_text('<protocol id="run" />\n', encoding="utf-8")
            (target / "devspec/work-items/_template/tasks.md").unlink()
            issues = doctor(target, "codex")
            self.assertTrue(any("missing protocol tags" in issue for issue in issues))
            self.assertIn("missing: devspec/work-items/_template/tasks.md", [issue.replace("\\", "/") for issue in issues])

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
            self.assertIn("every unresolved question", root.findtext("trigger"))
            self.assertIn("exactly one unanswered question", root.findtext("sequence"))
            self.assertIn("every question is answered or skipped", root.findtext("completion"))
            self.assertIn("skip an invalid or inapplicable question", root.findtext("completion"))
            work = ElementTree.fromstring((target / "devspec/protocols/work.xml").read_text(encoding="utf-8"))
            self.assertIn("including meta.md", work.findtext("initialize"))
            self.assertTrue((target / "devspec/foundation/template-map.md").is_file())
            self.assertTrue((target / "AGENTS.md").is_file())
            self.assertFalse((target / ".github").exists())

    def test_contract_xml_and_quickfix_routing_are_present(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "copilot", "--repo-state", "existing"])
            quickfix = (target / "devspec/contracts/devspec.quickfix.md").read_text(encoding="utf-8")
            self.assertIn("route risky work", quickfix)
            self.assertIn("database schema or migration", quickfix)
            self.assertIn("<rules>", quickfix)
            self.assertIn('<protocol ref="ask" />', quickfix)
            self.assertIn("devspec/contracts/devspec.quickfix.md", (target / ".github/prompts/devspec.quickfix.prompt.md").read_text(encoding="utf-8"))
            self.assertEqual([], doctor(target, "copilot"))

    def test_extract_completes_existing_system_baseline(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "codex", "--repo-state", "existing"])
            extract = ElementTree.fromstring(xml_block((target / "devspec/contracts/devspec.extract.md").read_text(encoding="utf-8")))
            refs = {protocol.attrib["ref"] for protocol in extract.find("protocols")}
            self.assertTrue({"ask", "run", "work", "repo-access"}.issubset(refs))
            outputs = {artifact.attrib["path"] for artifact in extract.find("outputs")}
            self.assertIn("devspec/foundation/workflows.md", outputs)
            self.assertIn("devspec/foundation/workflow-rules.md", outputs)
            self.assertIn("devspec/architecture/artifact-queue.md", outputs)
            self.assertTrue((target / "devspec/foundation/_template/technical-baseline.md").is_file())
            self.assertTrue((target / "devspec/foundation/_template/extraction-coverage.md").is_file())
            diagram_types = (target / "devspec/architecture/_template/diagram-types.md").read_text(encoding="utf-8")
            self.assertIn("Infrastructure topology", diagram_types)
            self.assertIn("Application landscape", diagram_types)
    def test_installs_complete_compact_artifact_structure(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "all", "--repo-state", "new"])
            self.assertTrue((target / "devspec/README.md").is_file())
            self.assertTrue((target / "devspec/glossary.md").is_file())
            self.assertTrue((target / "devspec/architecture/_template/artifact-queue.md").is_file())
            self.assertTrue((target / "devspec/architecture/artifact-queue.md").is_file())
            sample = (target / "devspec/architecture/_template/diagram-sample.md").read_text(encoding="utf-8")
            self.assertIn("DIA-001", sample)
            self.assertTrue((target / "devspec/architecture/_template/diagram-sample.svg").is_file())
            sample_svg = ElementTree.parse(target / "devspec/architecture/_template/diagram-sample.svg").getroot()
            self.assertIsNotNone(sample_svg.find("{http://www.w3.org/2000/svg}title"))
            self.assertIsNotNone(sample_svg.find("{http://www.w3.org/2000/svg}desc"))
            self.assertTrue((target / "devspec/foundation/_template/exploration-state.md").is_file())
            meta = (target / "devspec/work-items/_template/meta.md").read_text(encoding="utf-8")
            self.assertIn("stage:", meta)
            self.assertIn("run:", meta)
            self.assertIn("last:", meta)

    def test_diagram_contract_preserves_traceability_and_svg_quality(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            main(["init", "--target", str(target), "--profile", "codex", "--repo-state", "new"])
            diagram = (target / "devspec/contracts/devspec.diagram.md").read_text(encoding="utf-8")
            self.assertIn("non-duplicate diagrams", diagram)
            self.assertIn("index completed output in the overview", diagram)
            self.assertIn("title and description", diagram)
            self.assertIn("validate its XML", diagram)
            self.assertIn("Mermaid or HTML", diagram)
            self.assertTrue((target / "devspec/architecture/artifact-queue.md").is_file())
            self.assertTrue((target / "devspec/architecture/overview.md").is_file())
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
