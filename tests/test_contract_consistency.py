"""Cross-check the contracts against every surface that restates them.

The other suites install into a temporary directory and validate that, so drift between
this repository's own checked-in wrappers and its contracts stayed invisible. These tests
validate the repository itself.
"""

from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path
from xml.etree import ElementTree

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))

from devspec_lite.definitions import COMMANDS, LIFECYCLE_ORDER, PROTOCOLS, lifecycle_commands  # noqa: E402
from devspec_lite.framework import FRAMEWORK_OWNED, doctor, managed_payload  # noqa: E402

CONTRACTS = REPO / "devspec/contracts"
# Live project state and this project's own work products are deliberately not installed.
UNINSTALLED = ("foundation/repository-state.md", "architecture/overview.md", "architecture/artifact-queue.md")


def contract_text(name: str) -> str:
    return (CONTRACTS / f"devspec.{name}.md").read_text(encoding="utf-8")


def workflow(name: str) -> ElementTree.Element:
    text = contract_text(name)
    return ElementTree.fromstring(text[text.index("<workflow"):text.index("</workflow>") + len("</workflow>")])


def table_rows(text: str, header_starts: str) -> list[list[str]]:
    rows = []
    seen_header = False
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            seen_header = False
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if cells[0].startswith(header_starts):
            seen_header = True
            continue
        if seen_header and not set("".join(cells)) <= set("-: "):
            rows.append(cells)
    return rows


class RepositoryIsCurrentTests(unittest.TestCase):
    def test_checked_in_wrappers_match_the_contracts(self) -> None:
        drift = []
        for item in managed_payload("all", "existing"):
            if item.ownership != FRAMEWORK_OWNED:
                continue
            target = REPO / item.path
            if target.is_file() and target.read_text(encoding="utf-8") != item.content:
                drift.append(item.path.as_posix())
        self.assertEqual([], drift, "run the installer to regenerate these from devspec/contracts")

    def test_doctor_passes_against_this_repository(self) -> None:
        self.assertEqual([], doctor(REPO, "all"))

    def test_install_manifest_covers_every_canonical_file(self) -> None:
        from devspec_lite.definitions import canonical_root, install_files

        root = canonical_root()
        installed = {p.relative_to(root).as_posix() for p in install_files()}
        for path in sorted(root.rglob("*")):
            if not path.is_file():
                continue
            relative = path.relative_to(root).as_posix()
            if relative in UNINSTALLED or relative.startswith("quickfixes/QF-") or relative.startswith("work-items/") and "_template" not in relative:
                continue
            self.assertIn(relative, installed, f"{relative} is not covered by install-manifest.txt")


class ContractSchemaTests(unittest.TestCase):
    def test_every_command_has_a_lifecycle_position(self) -> None:
        self.assertEqual(sorted(LIFECYCLE_ORDER), sorted(c.name for c in COMMANDS))

    def test_heading_summary_matches_purpose(self) -> None:
        for command in COMMANDS:
            with self.subTest(command.name):
                summary = contract_text(command.name).split("\n")[2].strip()
                self.assertEqual(command.purpose, summary)

    def test_derivable_elements_are_not_restated(self) -> None:
        # <artifact> restated <outputs>, <handoff> restated <transitions>, <actions> restated <rules>.
        for command in COMMANDS:
            with self.subTest(command.name):
                present = {child.tag for child in workflow(command.name)}
                self.assertEqual(set(), present & {"artifact", "handoff", "actions"})

    def test_every_contract_scopes_itself(self) -> None:
        for command in COMMANDS:
            with self.subTest(command.name):
                scope = workflow(command.name).findtext("scope", default="").strip()
                self.assertTrue(scope, "contract must state when to use it and what to use instead")

    def test_protocol_refs_resolve(self) -> None:
        for command in COMMANDS:
            for ref in workflow(command.name).find("protocols"):
                with self.subTest(command=command.name, ref=ref.attrib.get("ref")):
                    self.assertIn(ref.attrib.get("ref"), PROTOCOLS)

    def test_every_protocol_is_loaded_by_a_contract(self) -> None:
        used = {ref.attrib.get("ref") for c in COMMANDS for ref in workflow(c.name).find("protocols")}
        self.assertEqual(set(PROTOCOLS), used, "an unreferenced protocol never reaches the agent")

    def test_shared_vocabulary_reaches_every_command(self) -> None:
        for command in COMMANDS:
            with self.subTest(command.name):
                refs = {ref.attrib.get("ref") for ref in workflow(command.name).find("protocols")}
                self.assertIn("state", refs)
                self.assertIn("run", refs)


class RouteGraphTests(unittest.TestCase):
    def transitions(self, name: str) -> list[dict]:
        return [t.attrib for t in workflow(name).find("transitions")]

    def test_blocked_and_terminal_transitions_agree_with_lifecycle(self) -> None:
        for command in COMMANDS:
            for attrib in self.transitions(command.name):
                with self.subTest(command=command.name, outcome=attrib.get("outcome")):
                    if attrib["run"] == "blocked":
                        self.assertEqual("devspec.clarify", attrib["next"])
                    if attrib["run"] == "complete":
                        self.assertEqual("none", attrib["next"])
                    if attrib["next"] == "none":
                        self.assertEqual("complete", attrib["run"])

    def test_work_item_stages_match_the_lifecycle_table(self) -> None:
        text = (REPO / "devspec/lifecycle.md").read_text(encoding="utf-8")
        documented = {row[0].strip("`"): row[1] for row in table_rows(text, "Stage")}
        stages = {"intake", "grooming", "finalization", "tasks", "implementation", "review", "complete"}
        self.assertEqual(stages, set(documented))
        for command in COMMANDS:
            for attrib in self.transitions(command.name):
                stage, nxt = attrib["stage"], attrib["next"]
                if stage in documented and nxt.startswith("devspec."):
                    with self.subTest(command=command.name, stage=stage):
                        self.assertIn(nxt, documented[stage], f"lifecycle.md does not allow {stage} -> {nxt}")

    def test_registry_restates_the_contracts_exactly(self) -> None:
        text = (REPO / "devspec/command-registry.md").read_text(encoding="utf-8")
        rows = table_rows(text, "Command")
        self.assertEqual([f"`devspec.{c.name}`" for c in lifecycle_commands()], [r[0] for r in rows])
        for command, row in zip(lifecycle_commands(), rows):
            with self.subTest(command.name):
                self.assertEqual(command.purpose, row[1])
                expected = []
                for attrib in self.transitions(command.name):
                    if attrib["next"] not in expected:
                        expected.append(attrib["next"])
                self.assertEqual(", ".join(f"`{v}`" for v in expected), row[2])


class ArtifactShapeTests(unittest.TestCase):
    def test_markdown_tables_are_well_formed(self) -> None:
        separator = re.compile(r"\|(\s*:?-+:?\s*\|)+$")
        broken = []
        for path in sorted((REPO / "devspec").rglob("*.md")):
            lines = path.read_text(encoding="utf-8").split("\n")
            for index, line in enumerate(lines[:-1]):
                nxt = lines[index + 1].strip()
                if line.strip().startswith("|") and separator.fullmatch(nxt):
                    header = line.strip().strip("|").split("|")
                    if len(header) != len(nxt.strip("|").split("|")):
                        broken.append(f"{path.relative_to(REPO).as_posix()}:{index + 1}")
        self.assertEqual([], broken)

    def test_contract_outputs_have_a_template(self) -> None:
        template_map = (REPO / "devspec/foundation/template-map.md").read_text(encoding="utf-8")
        work_item_templates = {p.name for p in (REPO / "devspec/work-items/_template").glob("*.md")}
        for command in COMMANDS:
            for artifact in workflow(command.name).find("outputs"):
                path = artifact.attrib["path"]
                with self.subTest(command=command.name, path=path):
                    name = path.rsplit("/", 1)[-1]
                    if path.startswith("devspec/work-items/"):
                        self.assertIn(name, work_item_templates)
                    elif path.startswith("devspec/foundation/"):
                        self.assertIn(f"`{name}`", template_map)
                    else:
                        self.assertTrue((REPO / path).is_file() or "###" in name, f"no home for {path}")


if __name__ == "__main__":
    unittest.main()
