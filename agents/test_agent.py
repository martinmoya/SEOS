"""
Test Agent.
Runs pytest in the current project.
"""

from agents.base_project_agent import BaseProjectAgent
from skills.python_skill import PythonSkill


class TestAgent(BaseProjectAgent):
    description = "Run pytest in the current project. Usage: /test"

    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
        except RuntimeError as ex:
            return str(ex)

        skill = PythonSkill(project.root)
        print("\nRunning tests... Please wait.\n")
        return skill.run_tests()
