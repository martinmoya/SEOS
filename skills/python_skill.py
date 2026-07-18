"""
Python Skill.
Wraps Python specific operations like AST analysis and testing.
"""

import subprocess
from pathlib import Path
from analyzers.python_analyzer import PythonAnalyzer


class PythonSkill:
    def __init__(self, root: str):
        self.root = root
        self.analyzer = PythonAnalyzer()

    def analyze_symbols(self, relative_path: str) -> dict:
        file_path = Path(self.root) / relative_path
        if not file_path.exists() or file_path.suffix != ".py":
            raise ValueError("File not found or not a Python file.")
        return self.analyzer.analyze(file_path)

    def run_tests(self) -> str:
        try:
            result = subprocess.run(
                ["pytest", "-q"],
                cwd=self.root,
                capture_output=True,
                text=True,
                check=False,
            )
            output = result.stdout.strip() if result.stdout else ""
            error = result.stderr.strip() if result.stderr else ""

            if result.returncode == 0:
                return f"Tests passed successfully.\n\n{output}"
            else:
                return f"Tests failed.\n\n{output}\n{error}"
        except FileNotFoundError:
            return "Error: pytest is not installed or not in PATH."
        except Exception as ex:
            return f"Error executing pytest: {ex}"
