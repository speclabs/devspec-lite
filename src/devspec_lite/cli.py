"""Command-line interface for installing and checking Devspec Lite."""

from __future__ import annotations

import argparse
from pathlib import Path

from . import __version__
from .framework import PROFILES, doctor, install_framework


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(prog="devspec-lite")
    root.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = root.add_subparsers(dest="command", required=True)
    for name in ("init", "doctor"):
        cmd = sub.add_parser(name)
        cmd.add_argument("--target", default=".", help="Repository to initialize or validate")
        cmd.add_argument("--profile", choices=PROFILES, default="all")
        if name == "init":
            cmd.add_argument("--repo-state", choices=("new", "existing"), required=True)
    return root


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    target = Path(args.target).resolve()
    if not target.is_dir():
        parser().error(f"target is not a directory: {target}")
    if args.command == "init":
        try:
            install_framework(target, args.profile, args.repo_state)
        except ValueError as exc:
            print(f"init failed: {exc}")
            return 2
        print(f"Initialized Devspec Lite ({args.profile}) in {target}")
        return 0
    issues = doctor(target, args.profile)
    if issues:
        print("Devspec Lite doctor found issues:")
        print("\n".join(f"- {issue}" for issue in issues))
        return 1
    print(f"Devspec Lite doctor passed for {target} ({args.profile})")
    return 0
