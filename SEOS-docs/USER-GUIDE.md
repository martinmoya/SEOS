# SEOS User Guide

## For Beginners

Welcome to **SEOS**!

If you've never used an AI tool for software development before, don't worry. This guide will walk you through everything step by step, as if you had just unboxed a brand-new product.

---

# What is SEOS?

**SEOS** (**Software Engineering Operating System**) is like having a highly intelligent software engineer working alongside you.

Unlike a traditional chatbot, SEOS can:

- Read your project files
- Understand your codebase
- Generate new code
- Review code for bugs and security issues
- Translate documents
- Summarize documentation
- Help you throughout the entire software development lifecycle

One of SEOS's biggest advantages is that it is **Local First**.

When using local Large Language Models (LLMs) such as **LM Studio** or **Ollama**, **your source code never leaves your computer**.

---

# Getting Started

Using SEOS is simple.

## Step 1 — Open a Terminal

Open your preferred terminal application:

- Windows Command Prompt
- PowerShell
- Windows Terminal
- Linux Terminal
- macOS Terminal

---

## Step 2 — Start Your LLM

Before launching SEOS, make sure your preferred LLM provider is already running.

Examples:

- LM Studio
- Ollama

---

## Step 3 — Launch SEOS

Simply type:

```bash
seos
```

---

## Step 4 — You're Ready!

After a few seconds you'll see the SEOS banner followed by the command prompt.

```text
>
```

From here you can start entering commands.

---

# Everyday Scenarios

The following examples demonstrate common tasks you'll perform with SEOS.

---

# Scenario 1 — Understand an Existing File

Imagine you've opened a project and found a file like:

```text
core/kernel.py
```

but you have no idea what it does.

### Step 1

Open a terminal inside your project folder.

---

### Step 2

Ask SEOS:

```text
/chat Explain what the file core/kernel.py does
```

---

### Result

SEOS will:

- Read the file
- Analyze its contents
- Explain its purpose in plain English

---

# Scenario 2 — Translate a Word Document

Suppose you have:

```text
manual.docx
```

and you'd like to translate it into Spanish.

### Step 1

Place the document inside your project folder.

---

### Step 2

Run:

```text
/translate manual.docx es
```

---

### Result

SEOS creates:

```text
manual.es.docx
```

while preserving:

- Tables
- Images
- Bold text
- Formatting
- Styles

---

# Scenario 3 — Generate a Python Class

Need a new class called **User**?

Instead of writing everything manually, type:

```text
/create class User
```

---

### Result

SEOS automatically generates:

```text
user.py
```

including the basic class structure.

---

# Command Reference

Commands always begin with a slash (`/`).

Example:

```text
/help
```

---

# 1. Help & Chat

## `/help`

Displays all available commands.

```text
/help
```

---

## `/help <command>`

Shows detailed help for a specific command.

Example:

```text
/help translate
```

---

## `/chat <message>`

Talk to the AI.

You can:

- Ask questions
- Request explanations
- Brainstorm ideas
- Analyze code

SEOS remembers the current conversation context.

Example:

```text
/chat How do I connect to a database?
```

---

# 2. Project Navigation

## `/info`

Displays information about the current project.

---

## `/tree`

Shows the directory tree.

---

## `/find <text>`

Searches files by name.

Example:

```text
/find kernel
```

---

# 3. Documents & AI Processing

## `/translate <file> <language>`

Translate a document.

Example:

```text
/translate readme.md es
```

---

## `/summarize <file>`

Generate a concise summary of a document.

---

## `/rewrite <file>`

Improve grammar, wording, and readability.

---

# 4. Software Factory

These commands help you create or improve software automatically.

---

## Generate Python Code

```text
/create <type> <Name>
```

Example:

```text
/create class Invoice
```

---

## Generate FastAPI Endpoints

```text
/create_api <description>
```

Example:

```text
/create_api endpoint to list users
```

---

## Generate Database Models

```text
/create_db <description>
```

Example:

```text
/create_db models for Customer and Order
```

---

## Generate Dockerfiles

```text
/create_docker <entrypoint>
```

Example:

```text
/create_docker main.py
```

---

## Generate Mermaid Diagrams

```text
/create_diagram <description>
```

Example:

```text
/create_diagram user login flow
```

---

## Generate Python Examples

```text
/create_example <concept>
```

Example:

```text
/create_example how to use asyncio
```

---

## Review Code

```text
/review <file>
```

Example:

```text
/review core/kernel.py
```

SEOS reviews your code looking for:

- Bugs
- Security vulnerabilities
- Code smells
- Best practice improvements

---

## Refactor Existing Code

```text
/refactor <file> <instruction>
```

Example:

```text
/refactor agents/chat_agent.py add type hints
```

---

## Generate Unit Tests

```text
/gentest <file>
```

Example:

```text
/gentest agents/chat_agent.py
```

---

# 5. Developer Tools

## Git Integration

```text
/git <command> [arguments]
```

Example:

```text
/git status
```

---

## Analyze Python Symbols

```text
/symbols <file>
```

Lists:

- Classes
- Methods
- Functions

---

## Run Tests

```text
/test
```

Runs your project's pytest suite.

---

## Change SEOS Role

```text
/role <name>
```

Example:

```text
/role software_architect
```

SEOS will respond according to the selected professional role.

---

# 6. Advanced Features

## REST API

```text
/serve
```

Starts the built-in REST API server on port **8080**.

---

## GitHub Integration

```text
/github <issue|pr> <owner/repository> <title>
```

Example:

```text
/ github issue martinmoya/seos "Found a bug"
```

Allows SEOS to create:

- GitHub Issues
- Pull Requests

---

## Exit SEOS

Close the application safely.

```text
/exit
```

Alternative commands:

```text
/quit
```

```text
/bye
```

---

# Tips

✔ Keep your LLM running before starting SEOS.

✔ Open SEOS from inside your project directory.

✔ Use `/help` whenever you're unsure about a command.

✔ Don't hesitate to ask questions using `/chat`—SEOS is designed to assist throughout your development workflow.

✔ Explore different roles with `/role` to receive responses from various professional perspectives.

---

# Next Steps

Now that you're familiar with the basics, you may want to explore:

- **Developer Guide** — Learn how to extend SEOS with your own Agents and Skills.
- **Architecture Guide** — Understand how SEOS is organized internally.
- **API Documentation** — Integrate SEOS into your own tools and workflows.

Happy coding with **SEOS**! 🚀
