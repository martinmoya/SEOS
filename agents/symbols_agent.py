"""
Symbols Agent.
Displays code symbols found in a source file using UniversalAnalyzer.
"""

from agents.base_project_agent import BaseProjectAgent
from skills.python_skill import PythonSkill


class SymbolsAgent(BaseProjectAgent):
    description = (
        "Display classes and functions in any code file. Usage: /symbols <file>"
    )

    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
        except RuntimeError as ex:
            return str(ex)

        filename = argument.strip()
        if not filename:
            return "Usage: /symbols <file>"

        skill = PythonSkill(project.root)

        try:
            symbols = skill.analyze_symbols(filename)

            if not symbols:
                return f"No symbols found in {filename}. (Is the language supported?)"

            lines = [f"Symbols in {filename}:"]

            classes = [s for s in symbols if s["type"] == "class"]
            functions = [s for s in symbols if s["type"] == "function"]

            if classes:
                lines.append("\nClasses:")
                for c in classes:
                    lines.append(f"  - {c['name']} (Line {c['line']})")

            if functions:
                lines.append("\nFunctions/Methods:")
                for f in functions:
                    lines.append(f"  - {f['name']} (Line {f['line']})")

            return "\n".join(lines)
        except ValueError as ex:
            return str(ex)
        except Exception as ex:
            return f"Error analyzing file: {ex}"
