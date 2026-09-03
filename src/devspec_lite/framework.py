"""Render and validate the compact framework tree."""

from __future__ import annotations

from pathlib import Path
from xml.etree import ElementTree

from .definitions import COMMANDS, PROTOCOLS, canonical_root, install_files

PROFILES = ("all", "copilot", "codex", "claude", "cursor", "gemini", "antigravity")
ADAPTERS = PROFILES[1:]


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding="utf-8") != content:
        raise ValueError(f"Refusing to overwrite changed managed file: {path}")
    path.write_text(content, encoding="utf-8", newline="\n")


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
            write_file(root / "AGENTS.md", "# Devspec Lite\n\nUse Git-tracked `devspec/` artifacts as canonical state. For a clear work-item continuation, resolve the per-worktree current context and run only its saved next action; ask before switching among multiple stories.\n\n" + command_lines + "\n")
        elif adapter == "cursor":
            commands = ", ".join(f"`devspec.{c.name}`" for c in COMMANDS)
            write_file(root / ".cursor/rules/devspec-workflow.mdc", f"---\ndescription: Devspec Lite workflow\nalwaysApply: false\n---\nFor {commands}, read the matching `devspec/contracts/` file and listed protocols. For a clear continuation, resolve per-worktree current context and run only the saved next action; ask before switching stories.\n")
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
    source_root = canonical_root()
    for source in install_files():
        target = root / "devspec" / source.relative_to(source_root)
        write_file(target, source.read_text(encoding="utf-8"))
    route = "devspec.extract" if repo_state == "existing" else "devspec.projectcontext"
    write_file(root / "devspec/foundation/repository-state.md", f"# Repository State\n\n- State: {repo_state}\n- Start with: `{route}`\n")
    install_adapters(root, profile)

def xml_block(text: str) -> str:
    start = text.index("<workflow")
    end = text.index("</workflow>") + len("</workflow>")
    return text[start:end]


def expected_paths(profile: str) -> list[Path]:
    source_root = canonical_root()
    paths = [Path("devspec") / source.relative_to(source_root) for source in install_files()]
    paths.append(Path("devspec/foundation/repository-state.md"))
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
    if (root / "devspec/work-items/current.md").exists():
        issues.append("tracked current-story artifact is not allowed: devspec/work-items/current.md")
    valid_stages = {"foundation", "intake", "grooming", "finalization", "tasks", "implementation", "review", "complete", "triage", "routed", "caller", "origin"}
    valid_runs = {"active", "blocked", "complete"}
    valid_next = {f"devspec.{command.name}" for command in COMMANDS} | {"none", "return-to-caller", "resume-origin"}
    lifecycle_templates = {
        "devspec/work-items/_template/meta.md": ("scope_revision:", "finalized_revision:", "planned_revision:", "implemented_revision:", "reviewed_revision:"), "devspec/work-items/_template/tasks.md": ("Scope revision:", "Source justification", "Done condition"), "devspec/work-items/_template/implement.md": ("Scope revision:", "Changed-work baseline:"), "devspec/work-items/_template/review.md": ("Scope revision:", "Changed-work baseline:"),
    }
    current_context_commands = {"story", "grooming", "finalize", "tasks", "implement", "review", "clarify", "changerequest"}
    protocol_text_requirements = {
        "run": {"preflight": ("Before every command", "single-repository or multi-repository scope", "current workspace as proposed", "do not inspect or change source")},
        "current-work-item": {
            "location": ("git rev-parse --git-path devspec/current-work-item.json", "Never create or commit"),
            "record": ("work-item ID", "current branch", "selection source", "timestamp", "never committed or pushed"),
            "selection": ("validated explicit ID", "exactly one eligible non-terminal"),
            "validation": ("branch changed", "stage and next action"),
            "continuation": ("saved meta.md next action", "devspec.clarify", "terminal item is not resumed"),
            "clear": ("accepted review",),
        },
    }
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
                    "run": ("preflight", "checkpoint", "context", "resume", "blocked", "closure"),
                    "work": ("scope", "evidence", "change", "artifacts"),
                    "repo-access": ("when", "validate", "respect"),
                    "current-work-item": ("when", "location", "record", "selection", "validation", "recovery", "continuation", "update", "clear"),
                }[name]
                present = {child.tag for child in ElementTree.fromstring(path.read_text(encoding="utf-8"))}
                missing = sorted(set(required) - present)
                if missing:
                    issues.append(f"missing protocol tags: {path}: {', '.join(missing)}")
                protocol = ElementTree.fromstring(path.read_text(encoding="utf-8"))
                for tag, phrases in protocol_text_requirements.get(name, {}).items():
                    value = protocol.findtext(tag, default="")
                    for phrase in phrases:
                        if phrase not in value:
                            issues.append(f"missing current-story resolver requirement: {path}: {tag}: {phrase}")
    for command in COMMANDS:
        path = root / f"devspec/contracts/devspec.{command.name}.md"
        if path.is_file():
            text = path.read_text(encoding="utf-8")
            try:
                workflow = ElementTree.fromstring(xml_block(text))
                if workflow.tag != "workflow" or workflow.attrib.get("command") != f"devspec.{command.name}":
                    issues.append(f"invalid contract identity: {path}")
                required = {"purpose", "protocols", "input", "rules", "entry", "outputs", "transitions", "closure", "actions", "artifact", "handoff"}
                present = {child.tag for child in workflow}
                missing = sorted(required - present)
                if missing:
                    issues.append(f"missing contract tags: {path}: {', '.join(missing)}")
                protocols = workflow.find("protocols")
                protocol_refs = {protocol.attrib.get("ref") for protocol in protocols} if protocols is not None else set()
                if command.name in current_context_commands and "current-work-item" not in protocol_refs:
                    issues.append(f"missing current-story protocol: {path}")
                if command.name != "story" and command.name in current_context_commands and "[work-item-id]" not in text:
                    issues.append(f"work-item ID is not optional: {path}")
                if command.name == "story" and "current-work-item" not in protocol_refs:
                    issues.append(f"missing current-story classification protocol: {path}")
            except (ValueError, ElementTree.ParseError) as exc:
                issues.append(f"invalid contract XML: {path}: {exc}")
                continue
            outputs = workflow.find("outputs")
            if outputs is None or not list(outputs):
                issues.append(f"missing contract outputs: {path}")
            transitions = workflow.find("transitions")
            if transitions is None or not list(transitions):
                issues.append(f"missing contract transitions: {path}")
            elif transitions is not None:
                for transition in transitions:
                    stage = transition.attrib.get("stage")
                    run = transition.attrib.get("run")
                    next_command = transition.attrib.get("next")
                    if not transition.attrib.get("outcome") or stage not in valid_stages or run not in valid_runs or next_command not in valid_next:
                        issues.append(f"invalid lifecycle transition: {path}")
                    if run == "blocked" and next_command != "devspec.clarify":
                        issues.append(f"blocked transition must clarify: {path}")
                    if next_command == "none" and run != "complete":
                        issues.append(f"terminal transition must be complete: {path}")
    registry = root / "devspec/command-registry.md"
    registry_text = registry.read_text(encoding="utf-8") if registry.is_file() else ""
    for command in COMMANDS:
        if f"devspec.{command.name}" not in registry_text:
            issues.append(f"missing registry command: devspec.{command.name}")
    for template, required_text in lifecycle_templates.items():
        text = (root / template).read_text(encoding="utf-8") if (root / template).is_file() else ""
        for expected in required_text:
            if expected not in text:
                issues.append(f"missing lifecycle template field: {template}: {expected}")
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
