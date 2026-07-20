"""
Audit Service.
Maintains an append-only, immutable log of all file modifications and LLM calls made by SEOS.
"""

import json
from datetime import datetime
from pathlib import Path


class AuditService:
    def __init__(self):
        self.log_file = Path("logs/audit.jsonl")
        self.log_file.parent.mkdir(exist_ok=True)

    def log_action(self, action: str, file_path: str = "N/A", tokens: int = 0):
        """Logs an action to the JSONL file. Actions: CREATE, MODIFY, DELETE, LLM_CALL."""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "file": str(file_path),
        }
        if tokens > 0:
            entry["tokens"] = tokens

        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
