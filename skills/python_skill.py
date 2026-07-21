"""
Universal Code Skill.
Wraps code analysis and polyglot test execution.
"""

import os
import subprocess
from pathlib import Path
from analyzers.universal_analyzer import UniversalAnalyzer


class PythonSkill:
    def __init__(self, root: str):
        self.root = root
        self.analyzer = UniversalAnalyzer()

    def analyze_symbols(self, relative_path: str) -> list:
        file_path = Path(self.root) / relative_path
        if not file_path.exists():
            raise ValueError("File not found.")

        knowledge = self.analyzer.analyze(file_path)
        return knowledge.all()

    def run_tests(self) -> str:
        def has_file(f):
            return os.path.exists(os.path.join(self.root, f))

        try:
            if has_file("pom.xml"):
                cmd = ["mvn", "test"]
            elif has_file("build.gradle") or has_file("build.gradle.kts"):
                cmd = ["gradle", "test"]
            elif has_file("package.json"):
                cmd = ["npm", "test"]
            elif has_file("go.mod"):
                cmd = ["go", "test", "./..."]
            elif (
                has_file("requirements.txt")
                or has_file("pytest.ini")
                or has_file("pyproject.toml")
            ):
                cmd = ["pytest", "-q"]
            else:
                return "Error: Could not detect project type (Maven, Gradle, npm, Go, or Python)."

            result = subprocess.run(
                cmd, cwd=self.root, capture_output=True, text=True, check=False
            )

            output = result.stdout.strip() if result.stdout else ""
            error = result.stderr.strip() if result.stderr else ""

            if result.returncode == 0:
                return f"Tests passed successfully.\n\n{output}"
            else:
                return f"Tests failed.\n\n{output}\n{error}"
        except FileNotFoundError:
            return f"Error: Test runner command '{cmd[0]}' not found or not in PATH."
        except Exception as ex:
            return f"Error executing tests: {ex}"
