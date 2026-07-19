# SEOS Developer Guide

Welcome, developer!

SEOS is designed to be **highly extensible**. This guide explains how to create your own **Agents**, **Skills**, and integrate them into the platform while following SEOS architectural principles.

---

# Architecture Overview

SEOS follows a strict **Clean Architecture**.

When adding new functionality, always follow this dependency flow:

```text
User Input
      │
      ▼
    Agent
      │
      ▼
   Service
      │
      ▼
Skill / Analyzer
      │
      ▼
   Provider
```

Each layer has a specific responsibility.

---

# Components

## 1. Agents (`agents/`)

Agents are the **entry point** of the application.

Their responsibilities are:

- Parse user input.
- Validate command arguments.
- Call the appropriate Service.
- Return a user-friendly response.

> **Important**
>
> Agents should contain **zero business logic**.

---

## 2. Services (`services/`)

Services contain the application's business logic.

Responsibilities include:

- Coordinating workflows.
- Calling Skills.
- Communicating with Providers.
- Returning processed results.

---

## 3. Skills (`skills/`)

Skills implement reusable system operations.

Examples:

- Git operations
- Python analysis
- File system utilities
- Encryption
- Docker interactions

Skills should be reusable by multiple Services.

---

## 4. Providers (`providers/`)

Providers connect SEOS to external systems.

Examples:

- LM Studio
- Ollama
- OpenAI
- GitHub API
- REST services

Providers should never contain business logic.

---

# Creating a New Agent

Suppose you want to implement a new command:

```text
/encrypt <text>
```

using a hypothetical `EncryptionService`.

---

## Step 1 — Create the Agent

Create a new file:

```text
agents/encrypt_agent.py
```

Example:

```python
"""
Encrypt Agent.
"""

from agents.base_agent import BaseAgent


class EncryptAgent(BaseAgent):
    description = "Encrypt a text. Usage: /encrypt <text>"

    def execute(self, argument: str) -> str:
        if not argument:
            return "Usage: /encrypt <text>"

        result = f"ENCRYPTED: {argument}"  # Mocked

        return result
```

---

### Working with Projects

If your Agent needs access to the currently opened project, inherit from:

```python
BaseProjectAgent
```

instead of:

```python
BaseAgent
```

At the beginning of `execute()`, call:

```python
self.require_project()
```

This ensures that a project is currently open before continuing.

---

## Step 2 — Register the Agent

Open:

```text
core/kernel.py
```

### Import the Agent

```python
from agents.encrypt_agent import EncryptAgent
```

---

### Register the Agent

Inside `initialize()`:

```python
self.agent_manager.register(
    "encrypt",
    EncryptAgent(context)
)
```

---

## Step 3 — Test It

Start SEOS.

```bash
seos
```

Try the new command.

```text
> /help encrypt

> /encrypt Hello World

ENCRYPTED: Hello World
```

---

# Creating a New Skill

Skills implement reusable operations that may be shared by many Services.

Examples include:

- Cryptography
- Git
- Docker
- Networking
- File operations
- Python analysis

---

## Step 1 — Create the Skill

Create a file inside:

```text
skills/
```

Example:

```text
skills/crypto_skill.py
```

Implement the desired functionality.

---

## Step 2 — Register the Skill

Open:

```text
core/kernel.py
```

Import it:

```python
from skills.crypto_skill import CryptoSkill
```

Register it during initialization.

```python
self.skill_manager.register(
    "crypto",
    CryptoSkill()
)
```

---

## Step 3 — Use the Skill

Agents and Services can retrieve the Skill through the Context.

Example:

```python
crypto = self.context.skills.get("crypto")
```

---

# Development Guidelines

Please follow these rules when contributing to SEOS.

---

## Language

All source code must be written in **English**.

This includes:

- Variable names
- Function names
- Class names
- Comments
- Docstrings
- Logs
- Error messages

---

## Type Hints

Always use Python type annotations.

Good example:

```python
def execute(self, argument: str) -> str:
    ...
```

Avoid:

```python
def execute(argument):
    ...
```

---

## Error Handling

Agents should never allow unhandled exceptions to propagate.

Always catch exceptions and return a meaningful message.

Example:

```python
try:
    ...
except Exception as ex:
    return f"Encryption failed: {ex}"
```

The application should **never crash because of an Agent**.

---

# Best Practices

✔ Keep Agents small.

✔ Put business logic into Services.

✔ Reuse Skills whenever possible.

✔ Keep Providers isolated from business logic.

✔ Use descriptive command names.

✔ Validate user input early.

✔ Return clear error messages.

✔ Keep commands deterministic whenever possible.

✔ Write unit tests for new functionality.

---

# Summary

The extension workflow can be summarized as:

```text
Create Agent
      │
      ▼
Create Service (if needed)
      │
      ▼
Create Skill (if reusable)
      │
      ▼
Register in Kernel
      │
      ▼
Test using /help and command execution
```

Following these guidelines ensures that SEOS remains modular, maintainable, and easy to extend.
