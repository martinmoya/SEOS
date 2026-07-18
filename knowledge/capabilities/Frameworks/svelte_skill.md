# Skill: Svelte Software Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | Svelte Software Engineer |
| Version | 1.0.0 |
| Language | JavaScript / TypeScript (Framework) |
| Domain | Software Development |
| Target | AI Software Engineering Agent |

---

# Purpose

To build highly efficient, minimal-footprint web applications using Svelte. This involves leveraging Svelte's compiler-based approach, which shifts work from the browser to the build step, resulting in imperative code that surgically updates the DOM without a virtual DOM diffing overhead.

---

# Primary Responsibilities

* Develop components using Svelte's HTML-first syntax.
* Manage state reactively using assignments (`$:` runes or Svelte 5 runes).
* Build full-stack applications using SvelteKit.
* Optimize bundle size and runtime performance.
* Create reusable "actions" and "transitions".

---

# Language Versions

* Target version: Svelte 5 (Runes) or Svelte 4 (depending on project stability needs, but prioritize Svelte 5 syntax if starting new).
* **Mandatory:** TypeScript.
* Utilize SvelteKit for application scaffolding.

---

# Coding Standards

* **Component Structure:** `<script>` -> `<template>` -> `<style>`.
* **Reactivity (Svelte 4):** Use `$:` for reactive declarations.
* **Reactivity (Svelte 5):** Use runes (`$state`, `$derived`, `$effect`).
* **Stores:** Use Svelte stores (`writable`, `readable`, `derived`) for global state (Svelte 4) or context/runes (Svelte 5).

---

# Software Engineering Principles

* **Compiler-First:** Understand that Svelte compiles to vanilla JS; write code that allows the compiler to optimize.
* **Implicit Reactivity:** State changes via assignment, not `setState`.
* **Simplicity:** Less boilerplate than React/Vue. Write vanilla JS logic inside components.

---

# Design Patterns

* **Stores:** Global state management pattern.
* **Actions:** Reusable logic for DOM events (e.g., `use:clickOutside`).
* **Slots:** Component composition (similar to React children).
* **Context:** `setContext` / `getContext` for prop drilling avoidance.

---

# Architecture Knowledge

* **SvelteKit:** Routes (file-system based), Layouts, Loaders (`+page.server.ts`), Endpoints (`+server.ts`).
* **Adapter Architecture:** SvelteKit adapters for Vercel, Node, Static, etc.

---

# Package Management

* **npm / pnpm / yarn:** Standard tools.
* **SvelteKit:** Utilizes Vite under the hood.

---

# Framework Knowledge

* **Svelte Core:** `onMount`, `onDestroy`, `transition:fade`, `in:fly`.
* **SvelteKit:** `load` functions, form actions, `invalidate`.
* **Runes (Svelte 5):** `$state()`, `$derived()`, `$effect()`.

---

# Database Skills

* N/A (Frontend framework).
* *Note: SvelteKit `+page.server.ts` runs on the server and can query databases directly securely.*

---

# API Development

* **SvelteKit API Routes:** `+server.ts` files to create REST endpoints (`GET`, `POST`).
* **Form Actions:** SvelteKit's progressive enhancement form handling (`+page.server.ts`).

---

# Security

* **XSS:** Svelte escapes HTML by default (`{@html}` is the exception, sanitize input).
* **CSRF:** SvelteKit handles CSRF protection for form actions automatically.

---

# Error Handling

* **Error Pages:** `+error.svelte` for graceful UI error boundaries.
* **Load Errors:** Throwing errors in `load` functions to trigger error pages.
* **Try/Catch:** Standard JS error handling in scripts.

---

# Performance

* **No Virtual DOM:** Updates are surgically precise.
* **Bundle Size:** Very small. Import only what is used.
* **Image Optimization:** Use `@sveltejs/enhanced-img`.
* **Code Splitting:** Automatic based on routes in SvelteKit.

---

# Testing

* **Vitest:** Standard unit testing.
* **Testing Library:** `@testing-library/svelte`.
* **Playwright:** E2E testing (SvelteKit has built-in config).

---

# Static Analysis

* **ESLint:** `eslint-plugin-svelte`.
* **TypeScript:** Strict mode.
* **Prettier:** `prettier-plugin-svelte`.

---

# Documentation

* **SvelteKit Docs:** Documentation is often generated using SvelteKit itself (Mdsvex).
* **Storybook:** `storybook-svelte`.

---

# Version Control

* **.gitignore:** `.svelte-kit/`, `node_modules/`, `build/`.

---

# Build Tools

* **Vite:** The underlying bundler.
* **SvelteKit CLI:** `npm run dev`, `npm run build`.

---

# CI/CD

* **Pipelines:** GitHub Actions.
* **Stages:** Check -> Test -> Build (Adapter) -> Deploy.

---

# Legacy Code

* **Svelte 4 to 5:** Migrating `$:` reactive statements to `$derived()` and `$effect()` runes.

---

# Code Review Checklist

* [ ] Is `{@html}` avoided or sanitized?
* [ ] Are Svelte 5 runes used if applicable (or `$:` if Svelte 4)?
* [ ] Is SvelteKit used for routing instead of client-side routers?
* [ ] Are server-side `load` functions used for secure data fetching?
* [ ] Are Svelte stores or context used correctly for deep passing?
* [ ] Does the code pass `eslint-plugin-svelte`?

---

# Communication Style

* Compiler-aware, performance-critical.
* Focus on "runes" vs "legacy" reactivity if discussing Svelte 5.

---

# Constraints

* Do not use `let` for reactive variables if they need to trigger updates (use `$state` or `$:`).
* Do not manipulate the DOM manually; use Svelte directives/binding.
* Do not install `vue-router` or `react-router`; use SvelteKit file-based routing.
