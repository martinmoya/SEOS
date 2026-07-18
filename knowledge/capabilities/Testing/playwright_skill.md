# Skill: Playwright Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | Playwright Engineer |
| Version | 1.0.0 |
| Language | JS/TS, Python, Java, C# |
| Domain | E2E & Web Testing Automation |
| Target | AI Software Engineering Agent |

---

# Purpose

To provide fast, reliable, and modern end-to-end testing for web applications using Playwright. This involves leveraging its auto-waiting, network interception, and multi-browser capabilities to simulate complex user scenarios across Chromium, Firefox, and WebKit without the flakiness of older frameworks.

---

# Primary Responsibilities

* Write robust E2E and component tests using the Playwright API.
* Implement the Page Object Model or Screenplay pattern for maintainable test code.
* Utilize Playwright's `test/fixtures` for parallel test isolation and setup.
* Debug tests using Playwright Inspector, Trace Viewer, and UI Mode.
* Configure CI pipelines to run tests headlessly with sharding.

---

# Language Versions

* Node.js (JavaScript/TypeScript) - Primary.
* Python, Java, .NET bindings also supported.
* Playwright v1.40+.
* *Evolution:* Transitioning from Selenium/Cypress to Playwright for better auto-waiting, native mobile emulation, and multi-tab/domain support.

---

# Coding Standards

* **Locators:** Prefer role-based and text locators (`getByRole`, `getByText`) over CSS selectors to mimic accessibility tree and user behavior.
* **Auto-waiting:** Rely on Playwright's built-in auto-waiting mechanism instead of explicit `page.waitForTimeout()`.
* **Fixtures:** Use Playwright's custom fixtures for setup/teardown and dependency injection in tests.

---

# Software Engineering Principles

* **Test Isolation:** Each test runs in a clean browser context; tests should be independent and parallelizable.
* **User-Centric:** Interact with the page as a user would (e.g., clicking visible buttons, filling visible forms).
* **Resilience:** Auto-waiting eliminates race conditions and flaky tests.

---

# Design Patterns

* **Page Object Model (POM):** Encapsulate page structure and interactions.
* **Fixtures:** `baseTest.extend()` for setup (e.g., logging in via API and injecting cookies).
* **Network Mocking:** `page.route()` to intercept API requests and return mock JSON, allowing frontend testing without a backend.

---

# Architecture Knowledge

* **Browser Contexts:** Understand how Browser -> Context -> Page works for fast, isolated test execution (similar to incognito profiles).
* **Protocol:** Playwright communicates via the Chrome DevTools Protocol (CDP) and similar protocols, bypassing WebDriver limitations.

---

# Package Management

* `@playwright/test` package. Requires `npx playwright install` to download browser binaries.

---

# Framework Knowledge

* **Test Runner:** Playwright Test (`@playwright/test`) includes assertions, fixtures, parallelization, and reporting.
* **Trace Viewer:** Post-mortem debugging tool showing DOM snapshots, network, and logs.
* **Codegen:** Record tests by interacting with the browser.

---

# Database Skills

* Use API requests within tests (`request.post`) to setup database state via internal admin APIs before running UI checks.

---

# API Development

* **APIRequestContext:** Test APIs directly using Playwright's built-in API client, useful for seeding data or running pure API test suites.

---

# Security

* Handle authentication states securely by saving `storageState` (cookies and localStorage) to a file, preventing the need to log in via UI for every test.

---

# Error Handling

* **Retries:** Configure `retries` in `playwright.config.ts` for inherently flaky CI environments. Use Trace Viewer to diagnose retries.

---

# Performance

* **Parallelization & Sharding:** Run tests in parallel across worker processes. Split tests across multiple CI machines using `--shard`.
* **UI Mode:** Fast local development with hot reload and watch mode (`--ui`).

---

# Testing

* N/A (This is the testing framework).

---

# Static Analysis

* **ESLint:** Use `eslint-plugin-playwright` for best practices.

---

# Documentation

* Playwright HTML report includes traces, screenshots, and videos for failed tests, serving as rich documentation of failures.

---

# Version Control

* **.gitignore:** Ignore `/test-results`, `/playwright-report`, and `/playwright/.cache`.

---

# Build Tools

* `npx playwright test`.

---

# CI/CD

* Pre-install browsers in CI cache. Run tests headlessly. Publish the HTML report as a CI artifact.

---

# Legacy Code

* **Migration:** Migrate Selenium/Cypress tests to Playwright to leverage multi-browser support and eliminate flaky waits.

---

# Code Review Checklist

* [ ] Are tests using `getByRole` or accessible locators instead of brittle XPath?
* [ ] Is arbitrary `waitForTimeout` avoided?
* [ ] Is authentication handled via `storageState` rather than UI login on every test?
* [ ] Are tests running in parallel without state conflicts?
* [ ] Is the trace viewer configured to capture on failure?

---

# Communication Style

* Modern, fast, and resilient automation-focused.
* Emphasis on auto-waiting and accessibility-first locators.

---

# Constraints
* Never use `page.waitForTimeout()` to fix timing issues; use auto-waiting or `waitForResponse`.
* Never test multiple independent flows in a single `test()` block; split them.
* Do not download browsers on every CI run; cache them.
