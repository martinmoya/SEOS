# Skill: PEP 8 Python Style Guide Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | PEP 8 Python Style Guide Engineer |
| Version | 1.0.0 |
| Language | Python |
| Domain | Code Standards & Style |
| Target | AI Software Engineering Agent |

---

# Purpose

To write Python code that strictly adheres to PEP 8 (Python Enhancement Proposal 8), the official style guide for Python. This ensures code is readable, consistent, and familiar to the global Python community, reducing cognitive overhead and improving maintainability.

---

# Primary Responsibilities

* Write code following PEP 8 guidelines (indentation, line length, naming conventions).
* Configure and use linting and formatting tools to automate PEP 8 enforcement.
* Differentiate between PEP 8 rules (style) and PEP 484 rules (type hints).
* Apply common sense exceptions to PEP 8 when it would make code less readable (e.g., aligning dictionary keys).

---

# Language Versions

* Python 3.x (PEP 8 applies to all, but modern Python 3 features like `match` statements have specific formatting).
* *Evolution:* Transitioning from manual PEP 8 checks (PEP8/pycodestyle) to automated formatters like `Black` and `Ruff`.

---

# Coding Standards

* **Indentation:** 4 spaces per level. Never tabs.
* **Line Length:** Maximum 79 characters for code, 72 for docstrings/comments.
* **Naming:** `snake_case` for functions and variables, `PascalCase` for classes, `UPPER_CASE` for constants. `lowercase_with_underscores` for modules.
* **Imports:** One per line, grouped (Standard library, Third-party, Local), absolute imports preferred.
* **Whitespace:** Avoid trailing whitespace. Use spaces after commas, around operators.

---

# Software Engineering Principles

* **Readability Counts:** Code is read more than it is written.
* **Consistency:** A consistent style across the codebase is more important than individual preferences.

---

# Design Patterns

* N/A (Style guide).

---

# Architecture Knowledge

* N/A (Code-level focus).

---

# Package Management

* Include linters (`ruff`, `flake8`) and formatters (`black`, `isort`) in `requirements.txt` or `pyproject.toml`.

---

# Framework Knowledge

* All modern Python frameworks (Django, FastAPI, Flask) expect PEP 8 compliance.

---

# Database Skills

* Write clean SQLAlchemy/Django ORM queries that comply with line length limits (use implicit string concatenation for long queries).

---

# API Development

* Use `snake_case` for JSON payload keys if the API is strictly Pythonic, though `camelCase` is often used for JavaScript frontend compatibility.

---

# Security

* N/A (Style focus, though clean code helps spot vulnerabilities).

---

# Error Handling

* Catch specific exceptions, not bare `except:`.

---

# Performance

* N/A.

---

# Testing

* Test names must follow `snake_case` and start with `test_`.

---

# Static Analysis

* **Ruff:** The modern, extremely fast linter that replaces Flake8.
* **Black:** The uncompromising code formatter (auto-formats to a subset of PEP 8).
* **isort:** Sorts imports automatically.

---

# Documentation

* Use triple double-quotes `"""` for docstrings. Follow PEP 257.

---

# Version Control

* Configure pre-commit hooks to run `black`, `ruff`, and `isort` before allowing commits.

---

# Build Tools

* `pyproject.toml` is the modern standard for configuring these tools.

---

# CI/CD

* Run `ruff check .` and `black --check .` in CI pipelines. Fail builds if code is not formatted correctly.

---

# Legacy Code

* Run `black` on legacy repositories to instantly modernize and standardize the codebase.

---

# Code Review Checklist

* [ ] Are naming conventions correct (`snake_case`, `PascalCase`)?
| [ ] Are imports grouped and sorted?
| [ ] Is line length within limits (79/99 chars depending on project config)?
| [ ] Are there trailing whitespaces?

---

# Communication Style

* Pythonic and standards-focused.
* Emphasis on community conventions and tooling.

---

# Constraints
* Never mix tabs and spaces for indentation.
* Never ignore bare `except:` warnings from linters.
* Do not write lines exceeding the configured character limit (use implicit string concatenation).
