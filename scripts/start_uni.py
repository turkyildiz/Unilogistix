#!/usr/bin/env python3
"""Launch a local Codex session with an ephemeral GitHub token."""
import getpass
import os
from pathlib import Path
import shutil
import sys


def main():
    executable = shutil.which("codex")
    if not executable:
        raise SystemExit("Codex CLI is required.")
    if not sys.stdin.isatty():
        raise SystemExit("Run in your own interactive terminal; do not send credentials through chat.")
    token = os.environ.get("UNI_GITHUB_TOKEN")
    if not token:
        token = getpass.getpass("Repository-scoped GitHub token (hidden; held only for this session): ").strip()
    if not token:
        raise SystemExit("No credential supplied; no session started.")
    environment = os.environ.copy()
    environment["UNI_GITHUB_TOKEN"] = token
    os.chdir(Path(__file__).resolve().parents[1])
    os.execve(executable, [executable], environment)


if __name__ == "__main__":
    main()
