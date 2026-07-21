# SEOS

### Software Engineering Operating System

> **An AI-Orchestrated Autonomous Platform for Software Engineering**
>
> **Analyze • Design • Build • Refactor • Document • Test • Deploy • Execute**

---

![Version](https://img.shields.io/badge/Version-v3.0.0-blue)

![License](https://img.shields.io/badge/License-MIT-green)

![Python](https://img.shields.io/badge/Python-3.10+-yellow)

![Status](https://img.shields.io/badge/Status-Stable-success)

---

**🇪🇸 [Leer en Español](README.es.md)**

---

# 🚀 What is SEOS?

SEOS (**Software Engineering Operating System**) is a **local-first**, AI-orchestrated platform designed to support software engineers throughout the entire software development lifecycle.

Unlike traditional coding assistants, SEOS executes complete engineering workflows autonomously.

---

# ⚡ The Paradigm Shift (v3.0.0)

SEOS is no longer just an AI chat.

It is an **Autonomous Engineering Engine**.

Instead of printing generated code to the terminal for manual copy & paste, SEOS writes engineering artifacts directly to your project, respecting its architecture and conventions.

---

# ✨ Current Features (v3.0.0)

## 🤖 Autonomous Execution

- Autonomous file generation
- Automatic JSON extraction
- Automatic Markdown extraction
- Direct file writing

---

## 🧠 Multi-Provider AI

Supports both local and cloud providers with token tracking.

### Local

- LM Studio
- Ollama

### Cloud

- OpenAI
- Claude
- Gemini

---

## 📁 Workspace Intelligence

- Multi-project management
- Workspace navigation
- Context awareness
- AST analysis

Supported languages:

- Python
- Java
- JavaScript
- C#
- Rust
- Perl

---

## 📄 Document Engine

- Batch translation
- Summarization
- Rewriting
- Format preservation

---

## 🏗 Software Factory

- Code scaffolding
- API generation
- Database generation
- Safe refactoring
- Automatic test generation

---

## 🤝 Multi-Agent Workflows

Autonomous engineering workflows coordinated through specialized agents.

Example:

```text
User

 │

 ▼

Architect

 │

 ▼

Developer

 │

 ▼

Reviewer

 │

 ▼

Tester

 │

 ▼

Documentation

 │

 ▼

Completed Sprint
```

---

## 🧠 RAG & Memory

- ChromaDB integration
- Semantic code search
- Conversational memory

---

## 🔍 Project Intelligence

- Cross-reference dependency graphs
- Impact analysis
- Dead code detection
- Sequence diagram generation

---

## 🔌 Integrations

- REST API
- GitHub API
- VS Code Extension
- MCP Client

---

## 🧩 Plugin System

- Dynamic plugin loading
- Install plugins directly from Git repositories

---

# ⚡ Quick Start

Clone the repository.

```bash
git clone https://github.com/your-org/seos.git

cd seos
```

---

## Create a Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## Install

```bash
pip install -e .
```

---

## Configuration

Copy the environment template.

```text
.env.example → .env
```

Configure:

- `LLM_PROVIDER`
- Provider API Keys
- `SEOS_API_KEY`

---

# ▶ Usage

## Interactive Mode

```bash
seos
```

---

## Headless Mode

```bash
seos --headless
```

---

# 💬 Main Commands

| Command | Description |
|----------|-------------|
| `/chat <message>` | Talk to SEOS. Generated code is written directly to disk when applicable. |
| `/sprint <requirement>` | Execute an autonomous multi-agent development workflow. |
| `/write [path/file.ext]` | Extract generated code from the last AI response into a file. |
| `/sequence <file>` | Generate a Mermaid sequence diagram from execution flow. |
| `/impact <file>` | Analyze dependency impact. |
| `/translate <folder> <language>` | Batch translate documents. |
| `/help [command]` | Display detailed command help. |

---

# 📄 License

Distributed under the **MIT License**.

See the **LICENSE** file for additional information.
