"""Render and validate the compact framework tree."""

from __future__ import annotations

from pathlib import Path
from xml.etree import ElementTree
from xml.sax.saxutils import escape

from .definitions import ARCHITECTURE_TEMPLATES, COMMANDS, COMMAND_DETAILS, FOUNDATION_TEMPLATES, PROTOCOLS, WORK_ITEM_TEMPLATES

PROFILES = ("all", "copilot", "codex", "claude", "cursor", "gemini", "antigravity")
ADAPTERS = PROFILES[1:]


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding="utf-8") != content:
        raise ValueError(f"Refusing to overwrite changed managed file: {path}")
    path.write_text(content, encoding="utf-8", newline="\n")


def command_contract(command) -> str:
    protocols = "\n".join(f'    <protocol ref="{name}" />' for name in command.protocols)
    command_input, local_rules = COMMAND_DETAILS[command.name]
    rules = "\n".join(f"    <rule>{escape(rule)}</rule>" for rule in local_rules)
    purpose = escape(command.purpose)
    command_input = escape(command_input)
    actions = escape(command.actions)
    artifact = escape(f"devspec/{command.artifact}")
    handoff = escape(command.handoff)
    return f"""# devspec.{command.name}

{command.purpose}

Invocation: `{command.example}`

<workflow command="devspec.{command.name}">
  <purpose>{purpose}</purpose>
  <protocols>
{protocols}
  </protocols>
  <input>{command_input}</input>
  <rules>
{rules}
  </rules>
  <actions>{actions}</actions>
  <artifact>{artifact}</artifact>
  <handoff>{handoff}</handoff>
</workflow>
"""


def registry() -> str:
    rows = "\n".join(f"| `devspec.{c.name}` | {c.purpose} | `{c.handoff}` |" for c in COMMANDS)
    return f"# Command Registry\n\n| Command | Purpose | Next route |\n|---|---|---|\n{rows}\n"


def wrapper_text(adapter: str, command) -> tuple[str, str]:
    contract = f"devspec/contracts/devspec.{command.name}.md"
    if adapter == "copilot":
        prompt = f"# devspec.{command.name}\n\nExecute `{contract}`. Use only its listed protocols.\n"
        agent = f"---\nname: devspec.{command.name}\ndescription: {command.purpose}\nuser-invocable: true\n---\nExecute `{contract}`.\n"
        return f".github/prompts/devspec.{command.name}.prompt.md", prompt + "\n---AGENT---\n" + agent
    if adapter == "claude":
        return f".claude/skills/devspec-{command.name}/SKILL.md", f"---\nname: devspec-{command.name}\ndescription: {command.purpose}\n---\nRead and execute `{contract}`.\n"
    if adapter == "gemini":
        return f".gemini/commands/devspec/{command.name}.toml", f"description = \"{command.purpose}\"\nprompt = \"Read and execute {contract}\"\n"
    if adapter == "antigravity":
        return f".agents/skills/devspec-{command.name}.md", f"---\nname: devspec-{command.name}\ndescription: {command.purpose}\n---\nRead and execute `{contract}`.\n"
    raise ValueError(adapter)


def install_adapters(root: Path, profile: str) -> None:
    adapters = ADAPTERS if profile == "all" else (profile,)
    for adapter in adapters:
        if adapter == "codex":
            command_lines = "\n".join(f"- `devspec.{c.name}`: read `devspec/contracts/devspec.{c.name}.md`." for c in COMMANDS)
            write_file(root / "AGENTS.md", "# Devspec Lite\n\nUse Git-tracked `devspec/` artifacts as canonical state.\n\n" + command_lines + "\n")
        elif adapter == "cursor":
            commands = ", ".join(f"`devspec.{c.name}`" for c in COMMANDS)
            write_file(root / ".cursor/rules/devspec-workflow.mdc", f"---\ndescription: Devspec Lite workflow\nalwaysApply: false\n---\nFor {commands}, read the matching `devspec/contracts/` file and listed protocols.\n")
        elif adapter == "copilot":
            for command in COMMANDS:
                path, combined = wrapper_text(adapter, command)
                prompt, agent = combined.split("\n---AGENT---\n", 1)
                write_file(root / path, prompt)
                write_file(root / f".github/agents/devspec.{command.name}.agent.md", agent)
        else:
            for command in COMMANDS:
                path, content = wrapper_text(adapter, command)
                write_file(root / path, content)


def install_framework(root: Path, profile: str, repo_state: str) -> None:
    for name, xml in PROTOCOLS.items():
        write_file(root / f"devspec/protocols/{name}.xml", xml + "\n")
    for command in COMMANDS:
        write_file(root / f"devspec/contracts/devspec.{command.name}.md", command_contract(command))
    write_file(root / "devspec/command-registry.md", registry())
    write_file(root / "devspec/README.md", "# Devspec Lite\n\nFoundation: `projectcontext → techstack → codebase-structure → coding-standards → rules`.\n\nWork item: `story → grooming` when needed `→ finalize → tasks → implement → review`.\n\nUse `clarify` only for an active blocker and `quickfix` only for localized, low-risk changes.\n")
    write_file(root / "devspec/glossary.md", "# Glossary\n\n- Stages: intake, grooming, finalization, tasks, implementation, review, complete.\n- Quickfix stages: triage, implementation, validation, complete, routed.\n- Run states: active, paused, blocked, stopped, complete.\n- Evidence: confirmed, observed, inferred, blocked.\n")
    for name, content in FOUNDATION_TEMPLATES.items():
        write_file(root / f"devspec/foundation/_template/{name}", content)
    for name, content in ARCHITECTURE_TEMPLATES.items():
        write_file(root / f"devspec/architecture/_template/{name}", content)
    route = "devspec.extract → devspec.projectcontext" if repo_state == "existing" else "devspec.projectcontext"
    write_file(root / "devspec/foundation/repository-state.md", f"# Repository State\n\n- State: {repo_state}\n- Start with: `{route}`\n")
    for name, content in WORK_ITEM_TEMPLATES.items():
        write_file(root / f"devspec/work-items/_template/{name}", content)
    write_file(root / "devspec/quickfixes/README.md", "# Quickfix Records\n\nEach accepted quickfix uses `QF-###-slug.md` and preserves scope, checkpoint, validation, and outcome.\n")
    write_file(root / "devspec/quickfixes/_template.md", "---\nid: QF-###-slug\ntype: bug\nstage: triage\nrun: active\nscope: []\nresume: none\nnext: select scope\nupdated: <yyyy-mm-dd>\n---\n\n# Quickfix\n\n- Request:\n- Evidence:\n- Changed areas:\n- Validation:\n- Outcome:\n")
    install_adapters(root, profile)


def xml_block(text: str) -> str:
    start = text.index("<workflow")
    end = text.index("</workflow>") + len("</workflow>")
    return text[start:end]


def expected_paths(profile: str) -> list[Path]:
    paths = [Path("devspec/command-registry.md"), Path("devspec/README.md"), Path("devspec/glossary.md"), Path("devspec/foundation/repository-state.md")]
    paths.extend(Path(f"devspec/protocols/{name}.xml") for name in PROTOCOLS)
    paths.extend(Path(f"devspec/contracts/devspec.{c.name}.md") for c in COMMANDS)
    paths.extend(Path(f"devspec/foundation/_template/{name}") for name in FOUNDATION_TEMPLATES)
    paths.extend(Path(f"devspec/work-items/_template/{name}") for name in WORK_ITEM_TEMPLATES)
    paths.extend((Path("devspec/quickfixes/README.md"), Path("devspec/quickfixes/_template.md")))
    paths.extend(Path(f"devspec/architecture/_template/{name}") for name in ARCHITECTURE_TEMPLATES)
    adapters = ADAPTERS if profile == "all" else (profile,)
    for adapter in adapters:
        if adapter == "codex":
            paths.append(Path("AGENTS.md"))
        elif adapter == "cursor":
            paths.append(Path(".cursor/rules/devspec-workflow.mdc"))
        elif adapter == "copilot":
            for c in COMMANDS:
                paths.extend((Path(f".github/prompts/devspec.{c.name}.prompt.md"), Path(f".github/agents/devspec.{c.name}.agent.md")))
        elif adapter == "claude":
            paths.extend(Path(f".claude/skills/devspec-{c.name}/SKILL.md") for c in COMMANDS)
        elif adapter == "gemini":
            paths.extend(Path(f".gemini/commands/devspec/{c.name}.toml") for c in COMMANDS)
        elif adapter == "antigravity":
            paths.extend(Path(f".agents/skills/devspec-{c.name}.md") for c in COMMANDS)
    return paths


def doctor(root: Path, profile: str) -> list[str]:
    issues = [f"missing: {path}" for path in expected_paths(profile) if not (root / path).is_file()]
    for name in PROTOCOLS:
        path = root / f"devspec/protocols/{name}.xml"
        if path.is_file():
            try:
                ElementTree.fromstring(path.read_text(encoding="utf-8"))
            except ElementTree.ParseError as exc:
                issues.append(f"invalid XML: {path}: {exc}")
            else:
                required = {
                    "ask": ("trigger", "checkpoint", "interaction", "resolution"),
                    "run": ("preflight", "checkpoint", "resume", "blocked", "closure"),
                    "work": ("scope", "evidence", "change", "artifacts"),
                    "repo-access": ("when", "validate", "respect"),
                }[name]
                present = {child.tag for child in ElementTree.fromstring(path.read_text(encoding="utf-8"))}
                missing = sorted(set(required) - present)
                if missing:
                    issues.append(f"missing protocol tags: {path}: {', '.join(missing)}")
    for command in COMMANDS:
        path = root / f"devspec/contracts/devspec.{command.name}.md"
        if path.is_file():
            text = path.read_text(encoding="utf-8")
            try:
                workflow = ElementTree.fromstring(xml_block(text))
                if workflow.tag != "workflow" or workflow.attrib.get("command") != f"devspec.{command.name}":
                    issues.append(f"invalid contract identity: {path}")
                required = {"purpose", "protocols", "input", "rules", "actions", "artifact", "handoff"}
                present = {child.tag for child in workflow}
                missing = sorted(required - present)
                if missing:
                    issues.append(f"missing contract tags: {path}: {', '.join(missing)}")
            except (ValueError, ElementTree.ParseError) as exc:
                issues.append(f"invalid contract XML: {path}: {exc}")
    adapters = ADAPTERS if profile == "all" else (profile,)
    for adapter in adapters:
        if adapter == "codex":
            text = (root / "AGENTS.md").read_text(encoding="utf-8") if (root / "AGENTS.md").is_file() else ""
            for command in COMMANDS:
                if f"devspec.{command.name}" not in text:
                    issues.append(f"missing Codex command reference: devspec.{command.name}")
        elif adapter == "cursor":
            path = root / ".cursor/rules/devspec-workflow.mdc"
            text = path.read_text(encoding="utf-8") if path.is_file() else ""
            for command in COMMANDS:
                if f"devspec.{command.name}" not in text:
                    issues.append(f"missing Cursor command reference: devspec.{command.name}")
        else:
            for command in COMMANDS:
                if adapter == "copilot":
                    paths = (root / f".github/prompts/devspec.{command.name}.prompt.md", root / f".github/agents/devspec.{command.name}.agent.md")
                elif adapter == "claude":
                    paths = (root / f".claude/skills/devspec-{command.name}/SKILL.md",)
                elif adapter == "gemini":
                    paths = (root / f".gemini/commands/devspec/{command.name}.toml",)
                else:
                    paths = (root / f".agents/skills/devspec-{command.name}.md",)
                expected = f"devspec/contracts/devspec.{command.name}.md"
                for path in paths:
                    if path.is_file():
                        text = path.read_text(encoding="utf-8")
                        if expected not in text:
                            issues.append(f"wrapper does not reference contract: {path}")
                        if "<workflow" in text:
                            issues.append(f"wrapper duplicates workflow logic: {path}")
    return issues
