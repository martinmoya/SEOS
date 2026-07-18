"""
Git Skill.
Wraps Git CLI commands using subprocess.
"""

import subprocess
from pathlib import Path


class GitSkill:
    def __init__(self, root: str):
        self.root = str(root)

    def _run(self, args: list[str]) -> str:
        try:
            result = subprocess.run(
                ["git"] + args,
                cwd=self.root,
                capture_output=True,
                text=True,
                check=False,
            )
            if result.returncode != 0:
                return result.stderr.strip() or "Unknown Git error."
            return result.stdout.strip() or "Success."
        except FileNotFoundError:
            return "Error: Git is not installed or not in PATH."
        except Exception as ex:
            return f"Error executing git: {ex}"

    def status(self) -> str:
        return self._run(["status"])

    def add(self, files: str) -> str:
        if not files:
            files = "."
        return self._run(["add"] + files.split())

    def commit(self, message: str) -> str:
        if not message:
            return "Error: Commit message cannot be empty."
        return self._run(["commit", "-m", message])

    def diff(self) -> str:
        return self._run(["diff"])

    def log(self) -> str:
        return self._run(["log", "--oneline", "-5"])
