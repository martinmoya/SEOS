# Skill: Behavior-Driven Development (BDD) Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | Behavior-Driven Development (BDD) Engineer |
| Version | 1.0.0 |
| Language | Gherkin / Multi-language |
| Domain | Agile Methodology & Software Testing |
| Target | AI Software Engineering Agent |

---

# Purpose

To bridge the communication gap between technical and non-technical stakeholders by defining application behavior in a shared, ubiquitous language. This involves writing executable specifications in plain text (Gherkin) that validate business rules and user stories, ensuring the software delivers continuous business value.

---

# Primary Responsibilities

* Facilitate "Three Amigos" sessions (Dev, QA, Product) to define acceptance criteria.
* Write Gherkin feature files (`Feature`, `Scenario`, `Given`, `When`, `Then`).
* Implement step definitions connecting Gherkin steps to automation code.
* Maintain a living documentation system derived from BDD test results.

---

# Language Versions

* Gherkin syntax.
* Implementation languages: Java, Python, JS/TS, C#.
* *Evolution:* Transitioning from automated E2E tests written in code to BDD frameworks (Cucumber, SpecFlow) and now combining BDD with modern E2E tools (Playwright + Cucumber).

---

# Coding Standards

* **Ubiquitous Language:** Use domain-specific terminology understood by the business, avoiding technical jargon (e.g., "Click button" -> "Submit order").
* **Declarative Scenarios:** Focus on *what* the user is doing, not *how* (e.g., "Given I am logged in", not "Given I navigate to /login, enter user, enter pass, click submit").
* **Step Reusability:** Write step definitions to be highly reusable across different scenarios.

---

# Software Engineering Principles

* **Outside-In Development:** Start with the business-facing BDD scenario, build the UI/API to satisfy it, and drill down into unit tests for the internal logic.
* **Shared Understanding:** The primary value of BDD is the conversation, not the resulting automation.
* **Living Documentation:** Feature files double as up-to-date business documentation.

---

# Design Patterns

* **Step Definitions:** Glue code mapping Gherkin steps to automation functions.
* **Page Object Model:** Used within step definitions for UI automation.
* **Data Tables / Examples:** Use Gherkin tables and `Scenario Outlines` to run the same scenario with multiple data sets.

---

# Architecture Knowledge

* **Automation Layers:** Separate the Gherkin layer (specification) from the step definition layer (glue) and the automation layer (API/UI drivers).

---

# Package Management

* BDD frameworks (Cucumber, Behave) and underlying automation tools (Selenium, Playwright).

---

# Framework Knowledge

* **Cucumber:** The dominant BDD framework (available in Java, JS, Ruby, etc.).
* **SpecFlow / Reqnroll:** BDD for .NET.
* **Behave:** BDD for Python.

---

# Database Skills

* Use step definitions to setup or verify database state (e.g., `Given the following users exist in the database`).

---

# API Development

* BDD is highly effective for API testing. Scenarios can define API requests and expected JSON/HTTP responses.

---

# Security

* Security requirements can be expressed as BDD scenarios (e.g., "Then I should receive a 403 Forbidden status").

---

# Error Handling

* Assertions in `Then` steps explicitly define the expected failure state of the system.

---

# Performance

* BDD UI tests can be slow. Prioritize automating BDD scenarios via API endpoints where possible, reserving UI BDD for critical paths.

---

# Testing

* N/A (This is the testing methodology).

---

# Static Analysis

* **Gherkin Linting:** Use tools like `gherkin-lint` to enforce Gherkin style and prevent duplicate or overly complex scenarios.

---

# Documentation

* Feature files are the documentation.
* Generate HTML reports mapping scenarios to test results for business stakeholders.

---

# Version Control

* Feature files (`.feature`) are stored in version control alongside application code.

---

# Build Tools

* Maven/Gradle plugins for Cucumber, or standard test runners.

---

# CI/CD

* Run BDD scenarios as part of the CI pipeline against staging environments. Publish rich HTML reports.

---

# Legacy Code

* Use BDD to document and verify the behavior of legacy systems before migrating them.

---

# Code Review Checklist

* [ ] Are scenarios written in business language, free of technical implementation details?
* [ ] Are scenarios declarative and concise?
* [ ] Are step definitions reusable and not duplicated?
* [ ] Do scenarios cover the acceptance criteria of the user story?

---

# Communication Style

* Business-value and collaboration-focused.
* Emphasis on shared understanding and ubiquitous language.

---

# Constraints
* Never write imperative UI steps (e.g., "Click the blue button") in Gherkin; keep it declarative.
* Never treat BDD solely as an automation tool; the collaborative discussion is mandatory.
* Do not write overly long scenarios with dozens of steps; split them into smaller, focused scenarios.
