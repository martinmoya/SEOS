"""
Metrics Service.
Tracks usage statistics during the SEOS session.
"""


class MetricsService:
    def __init__(self):
        self.llm_calls = 0
        self.total_tokens = 0
        self.files_created = 0
        self.files_modified = 0

    def add_llm_call(self, tokens: int = 0):
        self.llm_calls += 1
        self.total_tokens += tokens

    def add_file_created(self):
        self.files_created += 1

    def add_file_modified(self):
        self.files_modified += 1

    def get_stats(self) -> str:
        return (
            f"LLM Calls: {self.llm_calls}\n"
            f"Total Tokens Used: {self.total_tokens}\n"
            f"Files Created: {self.files_created}\n"
            f"Files Modified: {self.files_modified}"
        )
