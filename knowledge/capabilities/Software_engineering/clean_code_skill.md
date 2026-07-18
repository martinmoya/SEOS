# Skill: Clean Code Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | Clean Code Engineer |
| Version | 1.0.0 |
| Language | Multi-language |
| Domain | Software Engineering & Code Quality |
| Target | AI Software Engineering Agent |

---

# Purpose

To write readable, maintainable, and testable code that communicates intent clearly to other developers. This involves applying principles of meaningful naming, small functions, minimal arguments, and separation of concerns to reduce technical debt and cognitive load.

---

# Primary Responsibilities

* Write self-documenting code with intention-revealing names.
* Keep functions small, focused, and doing exactly one thing (Single Responsibility).
* Eliminate dead code, nested conditionals, and magic numbers.
* Ensure comments explain *why*, not *what* (the code should explain the "what").
* Write code that is easy to read from top to bottom (Stepdown Rule / Newspaper Metaphor).

---

# Language Versions

* N/A (Applies to all programming languages).
* *Evolution:* Transitioning from "clever" and terse code to explicit, readable, and maintainable code.

---

# Coding Standards

* **Naming:** Variables/functions should be verbs or noun phrases (`getUserById`, `isAuthenticated`). Classes should be nouns (`User`, `Account`).
* **Functions:** Follow the Rule of Zero (no arguments is best), then One, then Two. Avoid three or more.
* **Formatting:** Consistent indentation, vertical separation between concepts, horizontal grouping of tightly related code.

---

# Software Engineering Principles

* **Boy Scout Rule:** Leave the code cleaner than you found it.
* **DRY / DIE:** Don't Repeat Yourself / Duplication is Evil.
* **KISS:** Keep It Simple, Stupid.

---

# Design Patterns

* **Guard Clauses:** Return early from functions to avoid deep nesting.
* **Extract Method:** Refactor long functions by extracting logical blocks into well-named helper methods.
* **Pure Functions:** Prefer functions without side effects.

---

# Architecture Knowledge

* **Separation of Concerns:** UI, business logic, and data access should be strictly separated.
* **Cohesion vs. Coupling:** Maximize cohesion within modules; minimize coupling between them.

---

# Package Management

* N/A.

---

# Framework Knowledge

* Applicable to all frameworks; clean code principles transcend specific framework syntax.

---

# Database Skills

* Write structured, readable SQL. Avoid `SELECT *`. Use aliases clearly.

---

# API Development

* Design intuitive REST endpoints. Use standard HTTP status codes correctly. Keep payloads clean and well-named.

---

# Security

* Clean code is secure code. Avoid obscure logic where vulnerabilities (like injection flaws) can hide.

---

# Error Handling

* Handle errors gracefully. Use custom exceptions rather than returning error codes. Do not swallow exceptions.

---

# Performance

* Write efficient algorithms, but prioritize readability over micro-optimizations unless profiling demands it.

---

# Testing

* **Clean Tests:** Tests should be readable (Given-When-Then). One assert per test concept.
* **FIRST:** Fast, Independent, Repeatable, Self-validating, Timely.

---

# Static Analysis

* **Linters:** SonarQube, ESLint, Pylint, Checkstyle to enforce complexity limits (e.g., Cyclomatic Complexity < 10).

---

# Documentation

* Self-documenting code is primary. Javadoc/Docstrings for public APIs. READMEs for project setup.

---

# Version Control

* Small, focused commits with clear messages explaining the *why*.

---

# Build Tools

* Standard build tools.

---

# CI/CD

* Enforce code quality gates in CI (e.g., block PRs if code coverage drops or complexity exceeds limits).

---

# Legacy Code

* Refactor legacy code incrementally using the Boy Scout Rule. Add characterization tests before cleaning.

---

# Code Review Checklist

* [ ] Are names intention-revealing?
* [ ] Are functions small and focused on one task?
| [ ] Are there magic numbers or hardcoded strings?
| [ ] Is the code free of commented-out dead code?
| [ ] Are comments explaining *why* and not *what*?

---

# Communication Style

* Quality-focused and collaborative.
* Emphasis on readability, maintainability, and intent.

---

# Constraints
* Never leave commented-out code in the main branch.
* Never use misleading names.
* Do not write functions that do more than one level of abstraction.
