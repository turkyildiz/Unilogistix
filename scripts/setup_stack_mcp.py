#!/usr/bin/env python3
"""Register the founder's existing cloud providers without starting OAuth or workloads."""
import argparse
import datetime
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import tomllib

SERVERS = {
    "uni-cloudflare-docs": {"url": "https://docs.mcp.cloudflare.com/mcp"},
    "uni-cloudflare": {"url": "https://mcp.cloudflare.com/mcp"},
    "uni-vercel": {"url": "https://mcp.vercel.com"},
    "uni-supabase": {
        "url": "https://mcp.supabase.com/mcp?read_only=true&features=account,docs",
        "enabled_tools": ["search_docs", "list_projects", "get_project", "list_organizations", "get_organization", "get_cost"],
    },
}


def prepare(original):
    current = tomllib.loads(original.decode()).get("mcp_servers", {})
    additions = []
    for name, settings in SERVERS.items():
        if name in current:
            if any(current[name].get(k) != v for k, v in settings.items()) or current[name].get("enabled") is False:
                raise ValueError(f"Existing {name} differs; refusing to overwrite it")
            continue
        additions += ["", f"[mcp_servers.{name}]"]
        additions += [f"{key} = {json.dumps(value)}" for key, value in settings.items()]
    if not additions:
        return original
    result = original + ("\n" + "\n".join(additions) + "\n").encode()
    tomllib.loads(result.decode())
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--login", action="store_true", help="Run interactive provider OAuth after configuration")
    args = parser.parse_args()
    if args.login and not args.apply:
        parser.error("--login requires --apply")
    if not shutil.which("codex"):
        parser.exit(2, "Codex CLI is required.\n")
    directory = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex")))
    config = directory / "config.toml"
    original = config.read_bytes() if config.exists() else b""
    updated = prepare(original)
    print("Providers: Cloudflare documentation, Cloudflare API, Vercel, Supabase metadata/docs.")
    if not args.apply:
        print("Dry run passed; no configuration or account access changed.")
        return
    if updated != original:
        directory.mkdir(parents=True, exist_ok=True)
        if config.exists():
            stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
            backup = config.with_name(f"config.toml.uni-backup-{stamp}")
            fd = os.open(backup, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
            with os.fdopen(fd, "wb") as handle:
                handle.write(original)
        fd, temporary = tempfile.mkstemp(prefix=".uni-mcp-", dir=directory)
        try:
            with os.fdopen(fd, "wb") as handle:
                handle.write(updated)
            if (config.read_bytes() if config.exists() else b"") != original:
                raise RuntimeError("Configuration changed concurrently; retry without overwriting")
            os.replace(temporary, config)
        finally:
            if os.path.exists(temporary):
                os.unlink(temporary)
    verified = tomllib.loads(config.read_text())["mcp_servers"]
    for name, values in SERVERS.items():
        assert all(verified[name].get(key) == value for key, value in values.items())
        print(f"{name}: configuration verified; live access not verified.")
    if args.login:
        for name in ["uni-cloudflare", "uni-vercel", "uni-supabase"]:
            subprocess.run(["codex", "mcp", "login", name], check=True)
    else:
        print("Account authorization is pending. Use --apply --login in your terminal when ready.")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
        raise SystemExit(f"Stack setup incomplete ({type(error).__name__}); no credentials were printed.")
