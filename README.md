SEOS
Software Engineering Operating System
An AI-Orchestrated Platform for Software Engineering.

What is SEOS?
SEOS is a local-first, AI-orchestrated platform designed to support software engineers throughout the entire software development lifecycle.

It is not just a chatbot. It is not just a coding assistant. SEOS understands your project's structure, analyzes code, translates documents, and coordinates specialized AI agents to act as a virtual software team.

Current Features (v0.19.0)
Local LLM Support: Connects seamlessly with LM Studio and Ollama.
Workspace Management: Open and explore multiple projects.
File Navigation: Understands your project tree, finds files, and shows stats.
Document Engine (Format Preserving):
Translate, Summarize, and Rewrite documents.
Supports TXT, MD, PDF.
Preserves formatting (tables, styles, bold) for DOCX, XLSX, and PPTX using In-Place Translation.
Knowledge Core:
Hierarchical knowledge base (Roles, Rules, Capabilities).
Loads 19 roles and 110 capabilities at startup.
Prompt Engine:
Dynamic prompt composition using System Messages.
Switch SEOS personality on the fly using /role <name>.
Developer Skills:
Git Integration: Run /git status, /git add, /git commit directly from SEOS.
Python Analysis: Extract symbols (classes, methods) using AST /symbols.
Testing: Run pytest directly via /test.
Software Factory:
Code Scaffolding: Generate Python boilerplate files /create class <Name>.
API Generation: Generate FastAPI endpoints /create_api <description>.
Database Generation: Generate SQLAlchemy models /create_db <description>.
Refactoring: Modify existing code safely with AST validation /refactor <file> <instruction>.
Test Generation: Generate pytest unit tests /gentest <file>.
Quality Gate: Review code for bugs and vulnerabilities /review <file>.
Deployment: Generate Dockerfiles /create_docker <entrypoint>.
CLI Experience:
Dynamic /help system: Type /help for a list of commands, or /help <command> for detailed usage.
Rich Terminal UI: Colored outputs and panels using rich.
Integrations:
REST API: Run SEOS as a headless service using /serve.
VS Code Extension (MVP): Explain code from the editor context menu.
GitHub API: Create Issues and PRs directly via /github.
Multi-Agent Collaboration:
Intent Recognition: The ChatAgent can understand user requests and automatically delegate tasks to specialized agents (e.g., asking to create code triggers /create).
Conversational Memory: SEOS remembers the context of the current session to provide continuous and natural interactions.
Quality Assurance:
Unit Testing: Core components (Parser, Analyzer, Languages) are covered by pytest unit tests.
Packaging & Distribution:
Installable as a Python package via pip install ..
seos CLI command globally available.
Docker support for containerized deployment.
Architecture
SEOS is built on Clean Architecture principles:

core/: Kernel, Workspace, Context, Settings.
agents/: CLI Command handlers (orchestration only).
managers/: Agent discovery and registration.
services/: Business logic (Document Processing, LLM, Workspace, Knowledge, Prompt, Code Gen, Refactoring, Review, Deployment, Agent Comms, Memory).
skills/: Reusable system operations (Git, Python, GitHub).
analyzers/: Code parsing logic (AST).
providers/: LLM implementations (LM Studio, Ollama).
processors/: Text transformations (Translation, Summary, Rewrite).
api/: FastAPI REST API implementation.
vscode-extension/: TypeScript source for the VS Code integration.
knowledge/: Markdown files defining SEOS behavior and expertise.
tests/: Pytest unit tests for core components.
Installation & Setup
Clone the repository.
Create a virtual environment:
python -m venv .venv.venv\Scripts\activate
Install the package (editable mode recommended for development):
bash

pip install -e .
Configure your environment:
Copy .env.example to .env
Set your LLM_PROVIDER, LMSTUDIO_URL, and MODEL.
(Optional) Set GITHUB_TOKEN to enable GitHub integration.
Setup VS Code Extension (Optional):
cd vscode-extension
npm install
npm run compile
Usage
Run the application (from anywhere in your terminal):

bash

seos
Or run it directly:

bash

python main.py
Available CLI commands:

/help [command]: List all commands or show detailed help for a specific command.
/chat <message>: Talk to the LLM (remembers context, can delegate tasks).
/info: Show current project information.
/tree: Display the project directory tree.
/find <text>: Find files by name.
/translate <file> <lang>: Translate a document (e.g., /translate manual.docx es).
/summarize <file>: Generate a summary of a document.
/rewrite <file>: Improve text clarity and grammar.
/role <name>: Activate a specific role (e.g., /role software_architect).
/role clear: Remove the active role.
/git <command> [args]: Execute Git commands (status, add, commit, diff, log).
/symbols <file>: Display Python classes, methods, and functions in a file.
/test: Run pytest in the current project.
/create <type> <Name>: Generate a Python boilerplate file (e.g., /create class UserDTO).
/create_api <description>: Generate a FastAPI endpoint file.
/create_db <description>: Generate a SQLAlchemy model file.
/refactor <file> <instruction>: Refactor an existing Python file safely.
/gentest <file>: Generate pytest unit tests for a Python file.
/review <file>: Review a Python file for bugs and vulnerabilities.
/create_docker <entrypoint>: Generate a production-ready Dockerfile.
/serve: Start the SEOS REST API server on port 8080.
/github <issue|pr> <owner/repo> <title> [head:base]: Create an Issue or PR on GitHub.
/exit, /quit, /bye: Shut down SEOS.

License
This project is licensed under the MIT License - see the LICENSE file for details.
