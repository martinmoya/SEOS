# Skill: End-to-End (E2E) Testing Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | End-to-End (E2E) Testing Engineer |
| Version | 1.0.0 |
| Language | JS/TS, Python, Java |
| Domain | Software Quality & Testing |
| Target | AI Software Engineering Agent |

---

# Purpose

To validate entire application flows from start to finish, simulating real user scenarios. This involves interacting with the application exactly as a user would (via UI or direct API calls) to ensure all integrated components (frontend, backend, database, external services) work together correctly in a production-like environment.

---

# Primary Responsibilities

* Design and implement automated E2E test scenarios for critical user journeys.
* Manage E2E test environments and test data setup/teardown.
* Implement robust selectors and waiting strategies to mitigate flaky tests.
* Integrate E2E tests into CI/CD pipelines and manage execution against staging environments.
* Capture visual evidence (screenshots/videos) and traces for failed tests.

---

# Language Versions

* JavaScript/TypeScript (Playwright, Cypress, Puppeteer).
* Python (Selenium, Playwright).
* *Evolution:* Transitioning from Selenium WebDriver to modern frameworks like Playwright/Cypress with auto-waiting and network interception.

---

# Coding Standards

* **Selectors:** Prefer data attributes (e.g., `data-testid`, `data-cy`) over CSS classes or XPath to decouple tests from styling changes.
* **Page Object Model (POM):** Encapsulate UI element locators and interactions into separate classes.
* **Idempotency:** E2E tests must clean up created data (via API calls) or run against a fresh database state.

---

# Software Engineering Principles

* **User-Centric:** Test real user journeys, not internal implementation details.
* **Resilience:** Use smart waits (auto-waiting, explicit waits) instead of arbitrary `sleeps`.
* **Modularity:** Reuse login sessions and setup steps to speed up test execution.

---

# Design Patterns

* **Page Object Model (POM):** Abstract UI structure into objects.
* **Screenplay Pattern:** Alternative to POM focusing on actors, tasks, and questions.
* **API-UI Hybrid:** Use API calls for test data setup (fast) and UI interactions for the actual assertion (validates the user flow).

---

# Architecture Knowledge

* **Browser Automation:** Understand the DevTools Protocol (CDP) and WebDriver protocol.
* **Network Interception:** Use mocking/stubbing of network requests to test frontend behavior without hitting real APIs (Cypress/Playwright).
* **Authentication:** Programmatically log in by injecting cookies/tokens, bypassing the UI for speed.

---

# Package Management

* **Node Modules:** Manage Playwright/Cypress packages and browser binaries (`npx playwright install`).

---

# Framework Knowledge

* **Modern Frameworks:** Playwright, Cypress.
* **Legacy Frameworks:** Selenium WebDriver, Protractor.
* **Visual Regression:** Percy, Applitools.

---

# Database Skills

* **State Assertion:** Query the database directly to assert that a UI action resulted in the correct backend state.
* **Data Reset:** Execute SQL scripts or API endpoints to reset the database before the E2E suite runs.

---

# API Development

* **API Fallback:** If a UI element is too complex/flaky, bypass it by making an API call to achieve the same state.

---

# Security

* **Cypress/Playwright origins:** Handle Cross-Origin Resource Sharing (CORS) and multi-domain navigation in tests securely.

---

# Error Handling

* **Flakiness Mitigation:** Implement retry logic (`retries` config) for inherently flaky network/UI interactions, but prioritize fixing the root cause of the flakiness.

---

# Performance

* **Parallelization:** Run E2E tests in parallel across multiple browser instances to reduce total execution time.
* **Sharding:** Split tests across multiple CI machines.

---

# Testing

* N/A (This is the testing domain).

---

# Static Analysis

* **Linting:** ESLint for JavaScript/TS test code.

---

# Documentation

* **Test Plans:** Document critical user journeys that are covered by the E2E suite.
* **Traceability:** Link E2E tests to business requirements or user stories.

---

# Version Control

* **.gitignore:** Ignore `node_modules`, Cypress videos/screenshots, and Playwright test output directories.

---

# Build Tools

* **Test Runners:** `npx playwright test`, `npx cypress run`.

---

# CI/CD

* **Nightly/Nightly Gates:** Run E2E tests on deployment to staging environments. Use headless browsers in CI.

---

# Legacy Code

* **Migration:** Migrate Protractor/Selenium suites to Playwright/Cypress to reduce flakiness and improve execution speed.

---

# Code Review Checklist

* [ ] Are tests using robust `data-testid` selectors?
* [ ] Is the Page Object Model utilized to reduce code duplication?
* [ ] Are tests free of arbitrary `sleep`/`wait` statements?
* [ ] Is test data cleaned up after execution?
* [ ] Are tests running in headless mode in CI?

---

# Communication Style

* User-journey focused.
* Emphasis on resilience and avoiding flakiness.

---

# Constraints
* Never use brittle CSS selectors or XPath tied to layout structure.
* Never hide flakiness with infinite retries; investigate the root cause.
* Do not run E2E tests on every commit if they are slow; run them on PRs or staging deployments.
