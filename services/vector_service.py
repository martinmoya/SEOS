"""
Vector Service.
Manages ChromaDB for local semantic search (RAG).
"""

import chromadb
from pathlib import Path
from core.logger import logger


class VectorService:
    def __init__(self, root: Path):
        self.root = root
        # PersistentClient guarda los vectores en disco para que persistan entre sesiones
        self.client = chromadb.PersistentClient(path=str(root / ".seos_vector_db"))
        self.collection = self.client.get_or_create_collection(name="seos_project")

    def index_project(self):
        """Scans the project for Python files and indexes them."""
        files = []
        for f in self.root.rglob("*.py"):
            if any(
                part
                in {".venv", "node_modules", "__pycache__", ".git", ".seos_vector_db"}
                for part in f.parts
            ):
                continue
            files.append(f)

        if not files:
            return

        # Limpiar índice anterior para evitar duplicados
        self.collection.delete(where={"source": "project"})

        docs = []
        metadatas = []
        ids = []

        for f in files:
            try:
                content = f.read_text(encoding="utf-8")
                if content.strip():
                    docs.append(content)
                    metadatas.append(
                        {"source": "project", "file": str(f.relative_to(self.root))}
                    )
                    ids.append(str(f))
            except Exception:
                continue

        if docs:
            self.collection.add(documents=docs, metadatas=metadatas, ids=ids)
            logger.info(f"Vector DB indexed {len(docs)} files.")

    def query(self, text: str, n_results: int = 2) -> str:
        """Searches the vector DB for code relevant to the user's question."""
        if self.collection.count() == 0:
            return ""

        results = self.collection.query(query_texts=[text], n_results=n_results)

        context = []
        for i, doc in enumerate(results["documents"][0]):
            meta = results["metadatas"][0][i]
            # Truncar el documento para no llenar el prompt de tokens
            snippet = doc[:800]
            context.append(f"File: {meta['file']}\n```\n{snippet}\n```")

        return "\n\n---\n\n".join(context)
