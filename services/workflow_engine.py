"""
Workflow Engine.
Orchestrates multi-agent execution for high-level requirements.
"""

import json
import re
from rich.console import Console
from services.llm_service import LLMService
from services.agent_service import AgentService


class WorkflowEngine:
    def __init__(self, llm: LLMService, agent_service: AgentService):
        self.llm = llm
        self.agent_service = agent_service
        self.console = Console()

    def execute_sprint(self, requirement: str) -> str:
        self.console.print(
            f"\n[bold blue]🚀 Starting Autonomous Sprint: {requirement}[/bold blue]\n"
        )

        # Step 1: Architect Agent plans the files
        self.console.print(
            "[bold yellow]1. Architect Agent: Planning files...[/bold yellow]"
        )
        plan_prompt = (
            f"Requirement: {requirement}\n"
            "List the exact Python files and classes needed to fulfill this requirement. "
            "Return STRICTLY a valid JSON list of objects with 'type' and 'name'. "
            "Do not include any markdown formatting or conversational text. "
            'Example: [{"type": "class", "name": "User"}, {"type": "class", "name": "LoginService"}]'
        )
        plan_response = self.llm.generate(plan_prompt)

        # Robust JSON Extraction
        # 1. Eliminar bloques de markdown si existen (```json ... ```)
        if "```json" in plan_response:
            plan_response = plan_response.split("```json")[1].split("```")[0]
        elif "```" in plan_response:
            plan_response = plan_response.split("```")[1].split("```")[0]

        # 2. Buscar el primer '[' y el último ']' para aislar el array JSON
        start = plan_response.find("[")
        end = plan_response.rfind("]")

        if start == -1 or end == -1:
            return "Sprint failed: Architect did not return a valid JSON list."

        json_str = plan_response[start : end + 1]

        try:
            plan = json.loads(json_str)
        except json.JSONDecodeError:
            return (
                "Sprint failed: Architect returned malformed JSON even after cleanup."
            )

        if not plan:
            return "Sprint failed: Architect returned an empty plan."

        created_files = []

        # Step 2: Coder Agent creates the files
        self.console.print(
            f"[bold yellow]2. Coder Agent: Generating {len(plan)} files...[/bold yellow]"
        )
        for item in plan:
            name = item.get("name")
            type_ = item.get("type", "class")
            if name:
                self.console.print(f"   -> Generating {name}...")
                result = self.agent_service.delegate("create", f"{type_} {name}")

                # Extract filename from result
                if "Successfully created:" in result:
                    # The CreateAgent converts CamelCase to snake_case.py
                    filename = (
                        "".join(
                            ["_" + c.lower() if c.isupper() else c for c in name]
                        ).lstrip("_")
                        + ".py"
                    )
                    created_files.append(filename)

        # Step 3: Tester Agent generates unit tests
        if created_files:
            self.console.print(
                f"[bold yellow]3. Tester Agent: Generating tests for {len(created_files)} files...[/bold yellow]"
            )
            for filename in created_files:
                self.console.print(f"   -> Generating tests for {filename}...")
                self.agent_service.delegate("gentest", filename)

        self.console.print("[bold green]✅ Autonomous Sprint Completed![/bold green]\n")
        return f"Sprint executed successfully. Created {len(created_files)} modules and their tests."
