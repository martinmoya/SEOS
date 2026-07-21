"""
File Writer Service.
Intercepts LLM responses. If it detects a JSON or Markdown code block,
it writes the files to disk autonomously and returns a clean log.
"""

import json
import re
from pathlib import Path


class FileWriterService:
    def __init__(self, root: Path, audit_service=None, metrics_service=None):
        self.root = root
        self.audit = audit_service
        self.metrics = metrics_service

    def process_response(self, response_text: str, user_prompt: str = "") -> str | None:
        """
        Returns a log string if files were written, or None if it was a normal text response.
        """
        # 1. Intentar extraer JSON (la forma ideal)
        start = response_text.find("[")
        end = response_text.rfind("]")

        if start != -1 and end != -1 and end > start:
            json_str = response_text[start : end + 1]
            try:
                files = json.loads(json_str)
                if isinstance(files, list):
                    saved_files = self._write_files(files)
                    if saved_files:
                        return (
                            f"✅ Autonomous Execution Complete (JSON). Files written to disk:\n"
                            + "\n".join(saved_files)
                        )
            except json.JSONDecodeError:
                pass  # JSON inválido, pasar al fallback de Markdown

        # 2. Fallback: Extraer bloques de código Markdown (si el LLM fue terco)
        # Pattern: ```lang path/filename.ext \n code ```
        pattern = (
            r"```([a-zA-Z0-9_+#]+)?\s*(?:([a-zA-Z0-9_./-]+\.[a-zA-Z0-9]+))?\n(.*?)```"
        )
        matches = re.findall(pattern, response_text, re.DOTALL)

        if matches:
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

            files_to_write = []
            for lang, filename, code in matches:
                if filename:
                    fname = filename.strip()
                else:
                    # Si el LLM no puso nombre, intentar extraerlo del prompt del usuario (ej: "in src/models/customer.py")
                    fname_match = re.search(r"([\w./-]+\.\w+)", user_prompt)
                    if fname_match:
                        fname = fname_match.group(1)
                    else:
                        ext = ext_map.get(lang.lower(), "txt") if lang else "txt"
                        fname = f"projects/generated.{ext}"

                files_to_write.append({"path": fname, "code": code})

            saved_files = self._write_files(files_to_write)
            if saved_files:
                return (
                    f"✅ Autonomous Execution Complete (Markdown). Files written to disk:\n"
                    + "\n".join(saved_files)
                )

        return None  # No era código, dejar pasar como texto

    def _write_files(self, files: list) -> list:
        saved_files = []
        for f in files:
            path_str = f.get("path")
            code = f.get("code")

            if not path_str or code is None:
                continue

            try:
                clean_path = path_str.replace("\\", "/").lstrip("./").lstrip("/")
                if ".." in clean_path.split("/"):
                    clean_path = clean_path.replace("..", "")

                filepath = self.root / clean_path
                filepath.parent.mkdir(parents=True, exist_ok=True)

                filepath.write_text(code.strip() + "\n", encoding="utf-8")

                if self.audit:
                    self.audit.log_action("CREATE", filepath)
                if self.metrics:
                    self.metrics.add_file_created()

                saved_files.append(str(filepath.relative_to(self.root)))
            except Exception:
                continue

        return saved_files
