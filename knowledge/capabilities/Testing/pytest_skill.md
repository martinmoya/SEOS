# Skill: pytest Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | pytest Engineer |
| Version | 1.0.0 |
| Language | Python |
| Domain | Software Testing Framework |
| Target | AI Software Engineering Agent |

---

# Purpose

To write scalable, readable, and maintainable automated tests in Python using the pytest framework. This involves leveraging pytest's powerful fixtures, parametrization, and plugin ecosystem to handle unit, integration, and E2E testing efficiently.

---

# Primary Responsibilities

* Write expressive test functions using standard `assert` statements.
* Manage test setup and teardown using robust fixture injection.
* Implement parametrized tests to run the same test logic against multiple inputs.
* Utilize marks to skip tests or categorize them (e.g., `@pytest.mark.integration`).
* Integrate pytest with mocking libraries (unittest.mock) and external tools (Testcontainers, Playwright).

---

# Language Versions

* Python 3.8+ (Recommended 3.10+).
* pytest 7.x+ / 8.x+.
* *Evolution:* Transitioning from `unittest` (class-based, boilerplate) to `pytest` (function-based, fixtures, concise assertions).

---

# Coding Standards

* **Naming Conventions:** Test files must be named `test_*.py` or `*_test.py`. Test functions must start with `test_`.
* **Fixtures over setUp/tearDown:** Use `@pytest.fixture` for setup/teardown logic rather than class-based xUnit patterns.
* **Native Asserts:** Use standard Python `assert` statements instead of `self.assertEqual`; pytest provides rich failure introspection.

---

# Software Engineering Principles

* **Dependency Injection:** pytest fixtures use dependency injection; tests request what they need via function arguments.
* **DRY:** Use parametrization and fixture scopes to avoid repeating setup code.
* **Modularity:** Group related fixtures in `conftest.py` files to share them across multiple test modules.

---

# Design Patterns

* **Fixtures:** Reusable pieces of setup code returning data or resources.
* **Conftest.py:** Directory-scoped fixture repositories.
* **Parametrization:** `@pytest.mark.parametrize` to feed multiple datasets into a single test.
* **Yield Fixtures:** Use `yield` instead of `return` in fixtures to handle teardown cleanly.

---

# Architecture Knowledge

* **Fixture Scopes:** Understand `function`, `class`, `module`, `package`, and `session` scopes to optimize resource usage (e.g., DB connections).
* **Plugin Architecture:** Understand how pytest discovers plugins and hooks (e.g., `pytest-html`, `pytest-xdist`, `pytest-asyncio`).

---

# Package Management

* **Pip / Poetry / uv:** Include `pytest` and related plugins in `devDependencies` or `test` groups.

---

# Framework Knowledge

* **Core Framework:** pytest.
* **Mocking:** `unittest.mock` (built-in) or `pytest-mock` (mocker fixture wrapper).
* **Async:** `pytest-asyncio` for testing `asyncio` code.
* **Parallel:** `pytest-xdist` for running tests across multiple CPUs.

---

# Database Skills

* **Integration Testing:** Use fixtures to spin up Testcontainers databases, provide session-scoped connections, and transactional rollbacks per test function.

---

# API Development

* **FastAPI/Flask:** Use `TestClient` fixtures to test API endpoints in-process without starting a real server.

---

# Security

* **Secrets in Tests:** Load test secrets via `.env` files using `pytest-dotenv` or inject them via CI/CD environment variables, never hardcoded.

---

# Error Handling

* **Exception Testing:** Use `with pytest.raises(ExceptionType):` to assert that specific exceptions are raised.

---

# Performance

* **Parallel Execution:** Run tests in parallel using `pytest -n auto` (pytest-xdist) to drastically reduce suite execution time.
* **Scopes:** Use `session` scoped fixtures for expensive operations (like Docker container startup) to run them only once.

---

# Testing

* N/A (This is the testing framework).

---

# Static Analysis

* **Coverage:** Use `pytest-cov` to generate coverage reports and enforce thresholds.
* **Linting:** Run `flake8` or `ruff` alongside pytest.

---

# Documentation

* **Docstrings:** Document complex fixtures to explain their scope and what they yield.

---

# Version Control

* **.gitignore:** Ignore `.pytest_cache/`, `.coverage`, and `htmlcov/`.

---

# Build Tools

* `pytest` command-line interface with various flags (`-v`, `--ff`, `--cov`).
* `tox` or `nox` for testing across multiple Python environments.

---

# CI/CD

* Run `pytest` in CI pipelines. Generate JUnit XML (`--junitxml=report.xml`) for CI systems to parse test results and `pytest-html` for human-readable reports.

---

# Legacy Code

* Migrate `unittest` classes to pytest functions incrementally; pytest can run `unittest` tests natively, allowing a gradual transition.

---

# Code Review Checklist

* [ ] Are tests using standard `assert` statements?
* [ ] Are fixtures used for setup/teardown instead of duplicate code?
* [ ] Are expensive resources (DBs) using `session` or `module` scope?
* [ ] Are tests parametrized where multiple inputs are tested?
* [ ] Is `conftest.py` used logically to share fixtures without bloating it?

---

# Communication Style

* Pythonic and concise.
* Focus on fixture dependency injection and test readability.

---

# Constraints
* Never use `print()` for debugging in tests; use `--capture=no` or the `capsys` fixture.
* Never rely on test execution order; tests must be independent.
* Do not put test logic in `conftest.py` that should be in actual test functions.
