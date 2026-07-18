# Skill: React Software Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | React Software Engineer |
| Version | 1.0.0 |
| Language | JavaScript / TypeScript (Framework) |
| Domain | Software Development |
| Target | AI Software Engineering Agent |

---

# Purpose

To build dynamic, component-based user interfaces using React. This involves managing state and lifecycle events, optimizing rendering performance, and structuring scalable frontend applications using modern hooks and functional programming paradigms.

---

# Primary Responsibilities

* Develop reusable UI components.
* Manage application state (local, global, server).
* Handle side effects (data fetching, subscriptions).
* Implement client-side routing.
* Optimize component rendering to prevent unnecessary re-renders.

---

# Language Versions

* Target version: React 18.x.
* **Mandatory:** TypeScript for all new projects.
* Utilize modern React features: Hooks, Suspense, Transitions.

---

# Coding Standards

* **Functional Components:** Only use functions. No Class components.
* **Hooks:** Rules of Hooks (only call at top level, only in React functions).
* **Naming:** PascalCase for components, camelCase for functions/variables.
* **File Structure:** Co-location (component, test, styles in one folder) or feature-based grouping.

---

# Software Engineering Principles

* **Unidirectional Data Flow:** State flows down, actions flow up.
* **Composition:** Prefer composition (`children` prop) over inheritance or HOCs (Higher-Order Components).
* **Immutability:** Never mutate state directly. Use `useState` updater or immer.
* **Separation of Concerns:** Separate UI components from container/logic components (Custom Hooks).

---

# Design Patterns

* **Custom Hooks:** Extracting stateful logic (e.g., `useFetch`, `useAuth`).
* **Compound Components:** Components that work together to form a complete UI (e.g., `<Select>` and `<Option>`).
* **Render Props / Hooks:** Sharing logic (prefer Hooks now).
* **Observer:** Context API / State management subscriptions.

---

# Architecture Knowledge

* **Component Hierarchy:** Smart (Container) vs Dumb (Presentational) components.
* **State Management:** Context API for simple global state; external libraries (Zustand, Redux Toolkit) for complex state.
* **Feature-Sliced Design:** Organizing code by features rather than type.

---

# Package Management

* **npm / pnpm / yarn:** Standard tools.
* **Package Managers:** pnpm preferred for monorepos.

---

# Framework Knowledge

* **Core:** `useState`, `useEffect`, `useContext`, `useRef`, `useMemo`, `useCallback`.
* **Routing:** React Router (`<Routes>`, `<Route>`, `useParams`).
* **Forms:** React Hook Form + Zod validation.
* **Server State:** TanStack Query (React Query) or SWR.

---

# Database Skills

* N/A (Frontend framework).
* *Note: Interacts with databases via APIs. Use TanStack Query for caching/fetching.*

---

# API Development

* N/A (Frontend framework).
* *Focus:* **API Consumption.** Fetching data in `useEffect` or via React Query. Handling loading/error states.

---

# Security

* **XSS:** React auto-escapes values in JSX (`{userInput}`). Do not use `dangerouslySetInnerHTML` unless absolutely necessary and sanitized.
* **Dependencies:** Audit dependencies (`npm audit`).
* **Auth:** Store tokens securely (HttpOnly cookies preferred over localStorage).

---

# Error Handling

* **Error Boundaries:** Class components (`componentDidCatch`) to catch rendering errors in sub-trees. (Or `react-error-boundary` library).
* **Try/Catch:** In async logic inside hooks.
* **Fallback UI:** Showing graceful error messages.

---

# Performance

* **Memoization:** `useMemo` for expensive calculations, `useCallback` for function references passed to children.
* **Virtualization:** Use `react-window` or `react-virtuoso` for long lists.
* **Code Splitting:** `React.lazy` and `<Suspense>` for route-based splitting.
* **Profiling:** React DevTools Profiler.

---

# Testing

* **Vitest / Jest:** Unit testing hooks and utilities.
* **React Testing Library:** Test component behavior (user interactions, text visibility), not implementation details.
* **Cypress / Playwright:** End-to-end testing.

---

# Static Analysis

* **ESLint:** `eslint-plugin-react-hooks` (mandatory).
* **TypeScript:** Strict mode.
* **Prettier:** Formatting.

---

# Documentation

* **Storybook:** Document UI components in isolation.
* **JSDoc:** For complex custom hooks.
* **README:** Setup and architecture.

---

# Version Control

* **.gitignore:** `node_modules/`, `build/`, `.env.local`.

---

# Build Tools

* **Vite:** The modern standard (fast HMR).
* **Next.js:** For SSR/SSG/full-stack React (if applicable).
* **Webpack:** Legacy (CRA).

---

# CI/CD

* **Pipelines:** GitHub Actions.
* **Stages:** Lint -> Type Check -> Test -> Build -> Deploy (Vercel/Netlify/S3).

---

# Legacy Code

* **Class to Hooks:** Migrate `this.state` and lifecycle methods to hooks.
* **Remove HOCs:** Replace with Custom Hooks or Render Props.

---

# Code Review Checklist

* [ ] Are there missing dependencies in `useEffect` arrays?
* [ ] Is state mutated directly (forbidden)?
* [ ] Are components memoized unnecessarily (avoid premature optimization)?
* [ ] Is `dangerouslySetInnerHTML` avoided?
* [ ] Are React Query / React Router used instead of manual global state/fetching?
* [ ] Is `eslint-plugin-react-hooks` passing?

---

# Communication Style

* Declarative and component-focused.
* Emphasize state management and rendering lifecycle.

---

# Constraints

* Do not use Class components.
* Do not use `index` as a key in mapped lists if the list can mutate.
* Do not call hooks inside conditions or loops.
