# SEOS

## Software Engineering Operating System

**An AI-Orchestrated Platform for Software Engineering.**

---

## What is SEOS?

SEOS is a local-first, AI-orchestrated platform designed to support software engineers throughout the entire software development lifecycle. 

It is not just a chatbot. It is not just a coding assistant. SEOS understands your project's structure, analyzes code, translates documents, and will eventually coordinate specialized AI agents to act as a virtual software team.

## Current Features (v0.4.0)

- **Local LLM Support:** Connects seamlessly with LM Studio and Ollama.
- **Workspace Management:** Open and explore multiple projects.
- **File Navigation:** Understands your project tree, finds files, and shows stats.
- **Document Engine (Format Preserving):** 
  - Translate, Summarize, and Rewrite documents.
  - Supports TXT, MD, PDF.
  - Preserves formatting (tables, styles, bold) for DOCX, XLSX, and PPTX using In-Place Translation.

## Architecture

SEOS is built on Clean Architecture principles:
- `core/`: Kernel, Workspace, Context, Settings.
- `agents/`: CLI Command handlers (orchestration only).
- `services/`: Business logic (Document Processing, LLM, Workspace).
- `providers/`: LLM implementations (LM Studio, Ollama).
- `processors/`: Text transformations (Translation, Summary, Rewrite).

## Installation & Setup

1. Clone the repository.
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate

## 3 Install dependencies:

bash

pip install -r requirements.txt

## 4 Configure your environment:
• Copy .env.example to .env
• Set your LLM_PROVIDER, LMSTUDIO_URL, and MODEL.

## Usage
Run the application:

bash

python main.py

Available commands:

• /chat <message>: Talk to the LLM.
• /info: Show current project information.
• /tree: Display the project directory tree.
• /find <text>: Find files by name.
• /translate <file> <lang>: Translate a document (e.g., /translate manual.docx es).
• /summarize <file>: Generate a summary of a document.
• /rewrite <file>: Improve text clarity and grammar.
• /exit, /quit, /bye: Shut down SEOS.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

