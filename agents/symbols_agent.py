"""
Symbols Agent.
Displays Python symbols found in a source file.
"""

from agents.base_project_agent import BaseProjectAgent
from skills.python_skill import PythonSkill


class SymbolsAgent(BaseProjectAgent):
    description = (
        "Display Python classes, methods, and functions. Usage: /symbols <file>"
    )

    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
        except RuntimeError as ex:
            return str(ex)

        filename = argument.strip()
        if not filename:
            return "Usage: /symbols <python_file>"

        skill = PythonSkill(project.root)

        try:
            symbols = skill.analyze_symbols(filename)

            lines = [f"Symbols in {filename}:"]

            if symbols["classes"]:
                lines.append("\nClasses:")
                for c in symbols["classes"]:
                    lines.append(f"  - {c}")

            if symbols["methods"]:
                lines.append("\nMethods:")
                for m in symbols["methods"]:
                    lines.append(f"  - {m}")

            if symbols["functions"]:
                lines.append("\nFunctions:")
                for f in symbols["functions"]:
                    lines.append(f"  - {f}")

            if not (symbols["classes"] or symbols["methods"] or symbols["functions"]):
                lines.append("  No symbols found.")

            return "\n".join(lines)
        except ValueError as ex:
            return str(ex)
        except Exception as ex:
            return f"Error analyzing file: {ex}"
