"""Exercise setup reruns and configuration conflicts without changing real settings."""
import contextlib
import io
import json
import os
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch
import setup_mcp
import setup_stack_mcp
import tomllib


class SetupTests(unittest.TestCase):
    def invoke(self, current, apply=False):
        calls = []

        def fake_run(args):
            calls.append(args)
            if args[2] == "list":
                return SimpleNamespace(stdout=json.dumps(current))
            if args[2] == "get":
                url = next(url for name, url, _ in setup_mcp.SERVERS if name == args[3])
                return SimpleNamespace(stdout=json.dumps({"transport": {"url": url}}))
            return SimpleNamespace(stdout="")

        with tempfile.TemporaryDirectory() as directory:
            config = Path(directory) / "config.toml"
            config.write_text("# existing configuration\n")
            with patch.dict(os.environ, {"CODEX_HOME": directory}), \
                 patch("sys.argv", ["setup_mcp.py"] + (["--apply"] if apply else [])), \
                 patch.object(setup_mcp.shutil, "which", return_value="codex"), \
                 patch.object(setup_mcp, "run", side_effect=fake_run), \
                 contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                setup_mcp.main()
            backups = list(Path(directory).glob("config.toml.uni-backup-*"))
            for backup in backups:
                self.assertEqual(backup.read_bytes(), config.read_bytes())
                self.assertEqual(backup.stat().st_mode & 0o777, 0o600)
            return calls, len(backups)

    def test_dry_run_does_not_write(self):
        calls, backups = self.invoke([])
        self.assertEqual([call[2] for call in calls], ["list"])
        self.assertEqual(backups, 0)

    def test_apply_backs_up_and_verifies(self):
        calls, backups = self.invoke([], apply=True)
        self.assertEqual([call[2] for call in calls], ["list", "add", "get", "add", "get"])
        self.assertEqual(backups, 1)

    def test_matching_rerun_is_noop(self):
        current = [{"name": name, "enabled": True,
                    "transport": {"url": url, "bearer_token_env_var": token}}
                   for name, url, token in setup_mcp.SERVERS]
        calls, backups = self.invoke(current, apply=True)
        self.assertEqual(len(calls), 1)
        self.assertEqual(backups, 0)

    def test_conflicting_server_is_not_overwritten(self):
        with self.assertRaises(SystemExit) as error:
            self.invoke([{"name": "uni-github", "transport": {"url": "https://invalid.example"}}], apply=True)
        self.assertEqual(error.exception.code, 2)


class StackSetupTests(unittest.TestCase):
    def test_preserves_existing_settings(self):
        original = b'# Keep existing settings\nmodel = "existing-model"\n[mcp_servers.existing]\nurl = "https://example.invalid/mcp"\n'
        result = setup_stack_mcp.prepare(original)
        self.assertTrue(result.startswith(original))
        parsed = tomllib.loads(result.decode())
        self.assertEqual(parsed["model"], "existing-model")
        self.assertIn("existing", parsed["mcp_servers"])
        self.assertEqual(len(parsed["mcp_servers"]), 5)

    def test_rerun_is_noop(self):
        result = setup_stack_mcp.prepare(b"")
        self.assertEqual(result, setup_stack_mcp.prepare(result))

    def test_conflict_does_not_overwrite(self):
        with self.assertRaises(ValueError):
            setup_stack_mcp.prepare(b'[mcp_servers.uni-vercel]\nurl = "https://example.invalid"\n')

    def test_supabase_does_not_enable_mutation_tools(self):
        result = tomllib.loads(setup_stack_mcp.prepare(b"").decode())
        tools = result["mcp_servers"]["uni-supabase"]["enabled_tools"]
        self.assertIn("list_projects", tools)
        self.assertNotIn("create_project", tools)
        self.assertNotIn("execute_sql", tools)


if __name__ == "__main__":
    unittest.main()
