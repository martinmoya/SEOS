# Skill: Selenium Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | Selenium Engineer |
| Version | 1.0.0 |
| Language | Java, Python, C#, JS |
| Domain | E2E & Web Testing Automation |
| Target | AI Software Engineering Agent |

---

# Purpose

To automate web browsers for E2E testing using the Selenium WebDriver protocol. This involves writing robust, cross-browser test suites that simulate user interactions, manage dynamic page elements, and integrate with distributed testing grids to validate complex web applications.

---

# Primary Responsibilities

* Write automated tests using Selenium WebDriver APIs.
* Implement explicit and fluent waits to handle dynamic web elements.
* Utilize the Page Object Model (POM) pattern for maintainable code.
* Configure and execute tests on Selenium Grid or cloud providers (Sauce Labs, BrowserStack).
* Capture screenshots and logs for failed tests.

---

# Language Versions

* Java (Maven/Gradle, TestNG/JUnit), Python (pytest), C# (NUnit), JS (Mocha/Jest).
* Selenium 4.x.
* *Evolution:* Transitioning from Selenium 3 (JSON Wire Protocol) to Selenium 4 (W3C WebDriver Protocol) and gradually being superseded by Playwright/Cypress for modern apps.

---

# Coding Standards

* **Locators:** Prioritize `By.id` or `By.cssSelector`. Avoid absolute XPath.
* **Waits:** Always use Explicit Waits (`WebDriverWait`). Never use `Thread.sleep()` or Implicit Waits mixed with Explicit Waits.
* **POM:** Strictly use the Page Object Model to separate UI locators from test logic.

---

# Software Engineering Principles

* **Isolation:** Tests should not depend on each other.
* **Resilience:** Handle dynamic elements and asynchronous JavaScript loading using proper waits.
* **Modularity:** Reuse page components and navigation flows.

---

# Design Patterns

* **Page Object Model (POM):** Core pattern for Selenium.
* **Page Factory:** Use `@FindBy` annotations to initialize web elements lazily.
* **Fluent Waits:** Polling intervals to handle intermittent element visibility.

---

# Architecture Knowledge

* **WebDriver Protocol:** W3C standard protocol controlling browser behavior via HTTP requests.
* **Selenium Grid:** Hub and Node architecture for parallel cross-browser execution.
* **Driver Binaries:** Understand the need for driver executables (ChromeDriver, GeckoDriver) matching browser versions (mostly automated via WebDriverManager in modern setups).

---

# Package Management

* `selenium-java`, `selenium-webdriver`, `WebDriverManager`.

---

# Framework Knowledge

* **Selenium WebDriver:** Core API.
* **Test Runners:** TestNG, JUnit, pytest, NUnit.
* **WebDriverManager:** Automates driver binary management.

---

# Database Skills

* Integrate JDBC or ORM tools in test setup to verify backend state after UI interactions.

---

# API Development

* Selenium is purely UI; hybrid tests often combine Selenium with REST Assured/Requests for data setup.

---

# Security

* Handle browser cookies and profiles to maintain session state securely across tests.

---

# Error Handling

* **Exceptions:** Catch `NoSuchElementException` and `TimeoutException` explicitly to provide better test failure messages.

---

# Performance

* **Grid Execution:** Run tests in parallel on a Selenium Grid to reduce suite execution time.
* **Headless Mode:** Run browsers headlessly in CI (`--headless=new`).

---

# Testing

* N/A (This is the testing framework).

---

# Static Analysis

* Linters for the chosen language (e.g., SonarQube for Java).

---

# Documentation

* Document Selenium Grid infrastructure and how to run tests locally against it.

---

# Version Control

* **.gitignore:** Ignore driver binaries if not managed by WebDriverManager, and test output folders.

---

# Build Tools

* Maven Surefire/Failsafe, pytest, or NUnit console runner.

---

# CI/CD

* Provision Dockerized Selenium Grid (`selenium/standalone-chrome`) in CI. Run tests against it. Archive screenshots of failures.

---

# Legacy Code

* **Modernization:** Upgrade Selenium 3 to 4. Replace manual driver management with WebDriverManager. Consider migrating critical paths to Playwright.

---

# Code Review Checklist

* [ ] Are explicit waits used instead of `Thread.sleep()`?
* [ ] Is the Page Object Model strictly enforced?
* [ ] Are locators robust (CSS/ID) rather than brittle (link text/absolute XPath)?
* [ ] Are screenshots captured on test failure?
* [ ] Is the WebDriver instance properly quit in `@AfterTest`/teardown?

---

# Communication Style

* Standard, enterprise automation-focused.
* Emphasis on explicit waits and DOM interaction strategy.

---

# Constraints
* Never use `Thread.sleep()` to handle dynamic elements.
* Never mix Implicit and Explicit waits; behavior becomes unpredictable.
* Never leave WebDriver instances open; always call `driver.quit()` to free resources.
