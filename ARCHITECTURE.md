# SEOS Architecture Guide

SEOS is built on strict **Clean Architecture** and **SOLID** principles. The primary goal is to keep the core business logic isolated from external tools, LLMs, and the file system.

---

# 1. Architectural Flow

All requests in SEOS follow a strict unidirectional flow:

```text
User Input -> Agent -> Service -> Skill/Analyzer -> Provider
```

### Agents (`agents/`)

The entry point.

Their only job is to parse the user's input and call a Service.

They contain **zero business logic**.

---

### Services (`services/`)

Where the business logic lives.

Services use Skills and Providers to get work done (e.g., `DocumentProcessingService`, `RefactoringEngine`).

---

### Skills (`skills/`)

Reusable system operations (e.g., `GitSkill`, `PythonSkill`).

They interact directly with the OS or external CLIs.

---

### Analyzers (`analyzers/`)

Parsers that extract structured data from unstructured sources (e.g., `PythonAnalyzer` using `ast`).

---

### Providers (`providers/`)

External connections (e.g., `LMStudioProvider`, `OllamaProvider`).

---

# 2. Core Components

## Kernel (`core/kernel.py`)

The Kernel is the orchestrator.

It does **not** contain business logic.

Its responsibilities are:

- Initializing the application.
- Connecting to the LLM Provider.
- Loading the Knowledge Base.
- Registering Agents and Skills.
- Running the CLI loop.

---

## AgentContext (`core/agent_context.py`)

To prevent agents from knowing about the Kernel or the LLM Provider, we use **Dependency Injection** via `AgentContext`.

Every agent receives this context, which provides access to shared services like:

- `llm`
- `workspace_service`
- `knowledge_service`
- `agent_service`

---

## Agent Manager & Delegation (`managers/agent_manager.py`)

Agents are registered in an `AgentManager`.

This enables **Multi-Agent Collaboration**.

The `ChatAgent` can recognize user intent and delegate tasks to other agents (e.g., asking to create code triggers the `CreateAgent`) using the `AgentService`.

---

# 3. Design Patterns Used

## Factory Pattern

`LLMFactory` creates the correct LLM provider based on `.env` configuration without exposing the instantiation logic.

---

## Strategy Pattern

`DocumentProcessingService` accepts any `BaseTextProcessor` (Translation, Summary, Rewrite), allowing new AI operations without changing the document pipeline.

---

## Dependency Injection

Services are injected into Agents via `AgentContext`, making the system highly modular and testable.

---

# 4. Directory Structure

```text
seos/
├── core/           # Kernel, Context, Settings, Workspace
├── agents/         # CLI Command handlers (orchestration only)
├── managers/       # Agent discovery and registration
├── services/       # Business logic (Document Processing, LLM, Code Gen, etc.)
├── skills/         # Reusable system operations (Git, Python, GitHub)
├── analyzers/      # Code parsing logic (AST)
├── providers/      # LLM implementations (LM Studio, Ollama)
├── processors/     # Text transformations (Translation, Summary)
├── knowledge/      # Markdown files defining SEOS behavior and expertise
├── api/            # FastAPI REST API implementation
└── tests/          # Pytest unit tests
```
