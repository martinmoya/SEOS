"""
Write Agent.
Extracts code blocks from the last AI response and writes them to disk.
"""

import re
from pathlib import Path
from agents.base_project_agent import BaseProjectAgent


class WriteAgent(BaseProjectAgent):
    description = (
        "Extract code from the last AI response and write to disk. Usage: /write"
    )

    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
        except RuntimeError as ex:
            return str(ex)

        history = self.context.conversation_service.get_history()
        if not history:
            return "No recent AI response to extract code from."

        last_response = history[-1].get("content", "")

        # Regex magico: Encuentra bloques ```python, ```java, etc.
        # y captura el lenguaje y el código.
        pattern = (
            r"```([a-zA-Z0-9_+#]+)?\s*(?:([a-zA-Z0-9_./-]+\.[a-zA-Z0-9]+))?\n(.*?)```"
        )
        matches = re.findall(pattern, last_response, re.DOTALL)

        if not matches:
            return "No code blocks found in the last AI response."

        ext_map = {
            "python": "py",
            "py": "py",
            "java": "java",
            "javascript": "js",
            "js": "js",
            "typescript": "ts",
            "ts": "ts",
            "html": "html",
            "css": "css",
            "json": "json",
            "yaml": "yaml",
            "yml": "yml",
            "bash": "sh",
            "shell": "sh",
            "sql": "sql",
            "csharp": "cs",
            "cpp": "cpp",
            "c": "c",
            "go": "go",
            "rust": "rs",
        }

        target_dir = Path(project.root) / "projects"
        target_dir.mkdir(parents=True, exist_ok=True)

        saved_files = []
        for i, match in enumerate(matches):
            lang, filename, code = match

            if filename:
                fname = filename.strip()
            else:
                ext = ext_map.get(lang.lower(), "txt") if lang else "txt"
                fname = f"generated_{i + 1}.{ext}"

            filepath = target_dir / fname
            filepath.write_text(code.strip() + "\n", encoding="utf-8")
            saved_files.append(str(filepath))

        return (
            f"✅ Successfully extracted and saved {len(saved_files)} file(s):\n"
            + "\n".join(saved_files)
        )
