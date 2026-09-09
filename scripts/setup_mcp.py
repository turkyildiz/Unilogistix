#!/usr/bin/env python3
"""Configure the currently needed UNI MCP servers without writing token values."""
import argparse
import datetime
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

SERVERS = [
    ("uni-openai-docs", "https://developers.openai.com/mcp", None),
    ("uni-github", "https://api.githubcopilot.com/mcp/", "UNI_GITHUB_TOKEN"),
]


def run(args):
    return subprocess.run(args, check=True, capture_output=True, text=True, timeout=45)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Register missing servers in Codex user configuration")
    args = parser.parse_args()
    if not shutil.which("codex"):
        parser.exit(2, "Codex CLI is required; no configuration was changed.\n")
    current = json.loads(run(["codex", "mcp", "list", "--json"]).stdout)
    existing = {item["name"]: item for item in current}
    pending = []
    for name, url, token_var in SERVERS:
        if name in existing:
            item = existing[name]
            transport = item.get("transport", {})
            if (transport.get("url") != url or not item.get("enabled", True)
                    or transport.get("bearer_token_env_var") != token_var):
                parser.exit(2, f"Existing {name} differs from the requested configuration; left untouched.\n")
            print(f"{name}: already configured; authentication/tool use still require verification.")
            continue
        pending.append((name, url, token_var))
        print(f"{'Configure' if args.apply else 'Would configure'} {name}: {url}")
    if not args.apply:
        print("Dry run only. Run with --apply to register missing servers. No credentials are read or stored.")
        return
    config_dir = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex")))
    config = config_dir / "config.toml"
    if pending and config.exists():
        stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        backup = config.with_name(f"config.toml.uni-backup-{stamp}")
        # Backups may contain existing private configuration: create owner-only.
        with backup.open("xb") as dest:
            os.chmod(backup, 0o600)
            dest.write(config.read_bytes())
        print("Existing configuration backed up privately alongside config.toml.")
    for name, url, token_var in pending:
        command = ["codex", "mcp", "add", name, "--url", url]
        if token_var:
            command += ["--bearer-token-env-var", token_var]
        run(command)
        item = json.loads(run(["codex", "mcp", "get", name, "--json"]).stdout)
        if item.get("transport", {}).get("url") != url:
            raise RuntimeError(f"Configuration read-back failed for {name}")
        print(f"{name}: configuration verified; live MCP access not yet verified.")
    print("GitHub requires UNI_GITHUB_TOKEN in the environment of the Codex host.")
    print("No token is requested, printed, or saved by this script.")
    print("See integrations/README.md for repository-scoped authentication and verification.")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as exc:
        # Do not expose process output or user configuration: it may contain secrets.
        print(f"Setup incomplete ({type(exc).__name__}). Existing settings were not removed.\n"
              "Check configuration write permission, Codex availability, and network access; rerun after repair.", file=sys.stderr)
        sys.exit(1)
