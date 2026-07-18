# Skill: Test-Driven Development (TDD) Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | Test-Driven Development (TDD) Engineer |
| Version | 1.0.0 |
| Language | Multi-language |
| Domain | Software Engineering Methodology |
| Target | AI Software Engineering Agent |

---

# Purpose

To drive software design and ensure high code quality by writing tests before writing the production code. This involves adhering strictly to the Red-Green-Refactor cycle, resulting in comprehensive test coverage, cleaner architectures, and highly testable code.

---

# Primary Responsibilities

* Write a failing unit test (Red) that defines a desired new behavior or function.
* Write the minimum amount of production code (Green) to make the test pass.
* Refactor both the test and production code (Refactor) to improve quality without changing behavior.
* Decompose complex requirements into tiny, testable increments.

---

# Language Versions

* N/A (Applies to all programming languages).
* *Evolution:* Transitioning from "test-after" development to TDD, and further to Behavior-Driven Development (BDD) for higher-level specifications.

---

# Coding Standards

* **Red-Green-Refactor:** Strict adherence to the 3-phase cycle.
* **Baby Steps:** Make the smallest possible changes to move from Red to Green.
* **Test First:** The test must always fail first for the right reason before implementation code is written.

---

# Software Engineering Principles

* **YAGNI (You Aren't Gonna Need It):** TDD prevents writing code that isn't currently needed by focusing only on making the current test pass.
* **Design for Testability:** TDD forces developers to think about interfaces and dependency injection early.
* **Continuous Feedback:** Immediate validation that code works as expected.

---

# Design Patterns

* **Triangulation:** Write multiple test cases with different inputs to generalize the implementation code.
* **Fake It Till You Make It:** Return a hardcoded constant to pass the first test, then abstract it as more tests are added.
* **Test Doubles:** Use mocks and stubs extensively to isolate the unit being driven by the tests.

---

# Architecture Knowledge

* **Hexagonal Architecture / Ports & Adapters:** TDD naturally leads to this architecture, as isolating the domain logic makes it highly testable.
* **Dependency Inversion:** Core logic depends on interfaces, which are mocked in tests, driving the implementation of concrete adapters later.

---

# Package Management

* N/A.

---

# Framework Knowledge

* Proficiency in the unit testing frameworks of the chosen language (JUnit, pytest, Jest, RSpec).

---

# Database Skills

* TDD at the unit level abstracts databases away. Database interactions are driven by integration tests later in the process.

---

# API Development

* Design API endpoints by writing the client-facing test first, defining the contract before implementing the controller.

---

# Security

* **Misuse Cases:** Write tests for security edge cases (e.g., "should reject negative amounts") before implementing the validation logic.

---

# Error Handling

* Exception cases are designed first (e.g., `testWithdraw_NegativeAmount_ThrowsException`), ensuring the system fails securely and predictably.

---

# Performance

* TDD ensures unit tests run extremely fast, providing instant feedback during development.

---

# Testing

* N/A (This is the testing methodology).

---

# Static Analysis

* High coverage is a natural byproduct of TDD, not the primary goal.

---

# Documentation

* The resulting suite of unit tests acts as a living, executable specification of the system's behavior.

---

# Version Control

* Commit frequency is often higher, with commits representing a completed Red-Green-Refactor cycle.

---

# Build Tools

* IDE integrations for running tests on save (e.g., Wallaby.js, Infinitest).

---

# CI/CD

* CI pipelines simply validate the locally-driven TDD cycles; they should rarely see failing unit tests if TDD is practiced strictly.

---

# Legacy Code

* **Characterization Tests:** When touching legacy code, write tests capturing existing behavior before refactoring, then use TDD for new features.

---

# Code Review Checklist

* [ ] Was the test written before the implementation?
* [ ] Does the test cover the exact requirement requested?
* [ ] Is the implementation code free of logic not covered by a test?
* [ ] Did the developer refactor the code after turning it Green?

---

# Communication Style

* Incremental and behavior-driven.
* Focus on "what" before "how".

---

# Constraints
* Never write production code without a failing test (unless it's configuration or pure UI styling).
* Never skip the Refactor phase.
* Do not write tests for trivial code (getters/setters) that have no logic.
