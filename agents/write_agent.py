"""
Write Agent.
Extracts code blocks from the last AI response and writes them to disk.
Respects file paths specified in markdown blocks or user arguments.
"""

import re
from pathlib import Path
from agents.base_project_agent import BaseProjectAgent


class WriteAgent(BaseProjectAgent):
    description = (
        "Extract code from last AI response to disk. Usage: /write [optional/path.ext]"
    )

    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
        except RuntimeError as ex:
            return str(ex)

        history = self.context.conversation_service.get_history()
        if not history:
            return "No recent AI response to extract code from."

        # Buscar hacia atrás en el historial el último mensaje con bloques de código
        last_response = ""
        for msg in reversed(history):
            if msg.get("role") == "assistant":
                content = msg.get("content", "")
                if "```" in content:
                    last_response = content
                    break

        if not last_response:
            return "No code blocks found in recent AI responses."

        # Regex magico: Encuentra bloques ```python, ```java, etc.
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
            "perl": "pl",
        }

        saved_files = []
        forced_filename = argument.strip() if argument else None

        for i, match in enumerate(matches):
            lang, filename, code = match

            # Si el usuario forzó un nombre de archivo, SOLO guardamos el primer bloque
            # e ignoramos los demás para no crear archivos basura.
            if forced_filename and i > 0:
                continue

            if forced_filename and i == 0:
                fname = forced_filename
            elif filename:
                fname = filename.strip()
            else:
                ext = ext_map.get(lang.lower(), "txt") if lang else "txt"
                fname = f"projects/generated_{i + 1}.{ext}"

            # Seguridad: Prevenir path traversal fuera del proyecto
            clean_fname = fname.replace("\\", "/").lstrip("./").lstrip("/")
            if ".." in clean_fname.split("/"):
                clean_fname = clean_fname.replace("..", "")

            filepath = Path(project.root) / clean_fname

            # Crear directorios padre si no existen (Ej: src/models/)
            filepath.parent.mkdir(parents=True, exist_ok=True)

            filepath.write_text(code.strip() + "\n", encoding="utf-8")

            # Auditoría y Métricas
            self.context.audit_service.log_action("CREATE", filepath)
            self.context.metrics_service.add_file_created()

            saved_files.append(str(filepath.relative_to(project.root)))

        return (
            f"✅ Successfully extracted and saved {len(saved_files)} file(s):\n"
            + "\n".join(saved_files)
        )
