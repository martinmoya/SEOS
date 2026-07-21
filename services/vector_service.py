"""
Vector Service.
Manages ChromaDB for local semantic search (RAG) and hot-reloading.
"""

import chromadb
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from core.logger import logger
import threading

SUPPORTED_EXTENSIONS = {
    ".py",
    ".js",
    ".ts",
    ".jsx",
    ".tsx",
    ".java",
    ".cs",
    ".go",
    ".rs",
    ".cpp",
    ".c",
    ".rb",
    ".php",
    ".md",
    ".sql",
    ".html",
    ".css",
    ".txt",
}


class SEOSFileWatcher(FileSystemEventHandler):
    def __init__(self, vector_service):
        self.vs = vector_service

    def on_modified(self, event):
        if not event.is_directory:
            self.vs.index_file(Path(event.src_path))

    def on_created(self, event):
        if not event.is_directory:
            self.vs.index_file(Path(event.src_path))


class VectorService:
    def __init__(self, root: Path):
        self.root = root
        self.client = chromadb.PersistentClient(path=str(root / ".seos_vector_db"))
        self.collection = self.client.get_or_create_collection(name="seos_project")
        self.observer = Observer()
        self.last_watcher_message = "No watcher activity yet."

    def start_watcher(self):
        event_handler = SEOSFileWatcher(self)
        self.observer.schedule(event_handler, str(self.root), recursive=True)
        self.observer.start()
        logger.info("Vector DB File Watcher started.")

    def stop_watcher(self):
        if self.observer.is_alive():
            self.observer.stop()
            self.observer.join()

    def index_project(self):
        files = []
        for f in self.root.rglob("*"):
            if any(
                part
                in {
                    ".venv",
                    "node_modules",
                    "__pycache__",
                    ".git",
                    ".seos_vector_db",
                    "logs",
                    "projects",
                }
                for part in f.parts
            ):
                continue
            if f.suffix.lower() in SUPPORTED_EXTENSIONS:
                files.append(f)

        if not files:
            return

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
            self.collection.upsert(documents=docs, metadatas=metadatas, ids=ids)
            logger.info(f"Vector DB indexed {len(docs)} files.")
            self.last_watcher_message = f"Indexed {len(docs)} files."

    def index_file(self, file_path: Path):
        if file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            return
        if any(
            part
            in {
                ".venv",
                "node_modules",
                "__pycache__",
                ".git",
                ".seos_vector_db",
                "logs",
                "projects",
            }
            for part in file_path.parts
        ):
            return

        try:
            content = file_path.read_text(encoding="utf-8")
            if not content.strip():
                return

            rel_path = str(file_path.relative_to(self.root))

            self.collection.upsert(
                documents=[content],
                metadatas=[{"source": "project", "file": rel_path}],
                ids=[str(file_path)],
            )
            logger.info(f"Vector DB hot-reloaded: {rel_path}")
            self.last_watcher_message = f"Hot-reloaded: {rel_path}"
        except Exception as ex:
            logger.error(f"Error indexing file {file_path}: {ex}")
            self.last_watcher_message = f"Error indexing {file_path.name}"

    def query(self, text: str, n_results: int = 2) -> str:
        if self.collection.count() == 0:
            return ""

        try:
            results = self.collection.query(query_texts=[text], n_results=n_results)

            context = []
            for i, doc in enumerate(results["documents"][0]):
                meta = results["metadatas"][0][i]
                snippet = doc[:800]
                context.append(f"File: {meta['file']}\n```\n{snippet}\n```")

            return "\n\n---\n\n".join(context)
        except Exception as ex:
            logger.error(f"Vector query failed: {ex}")
            return ""
