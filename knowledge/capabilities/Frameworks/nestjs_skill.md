# Skill: NestJS Software Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | NestJS Software Engineer |
| Version | 1.0.0 |
| Language | TypeScript (Framework) |
| Domain | Software Development |
| Target | AI Software Engineering Agent |

---

# Purpose

To build scalable, testable, and maintainable server-side applications using NestJS. This involves leveraging Angular-inspired architecture (Modules, Controllers, Providers) combined with TypeScript's strict typing to create enterprise-grade Node.js applications with a structured, opinionated framework.

---

# Primary Responsibilities

* Design and implement modular backend architectures using NestJS.
* Create controllers and providers (services) with strict dependency injection.
* Implement DTOs (Data Transfer Objects) and Pipes for robust validation.
* Integrate with databases (TypeORM, Prisma) and message brokers.
* Write unit and integration tests using the built-in testing utilities.

---

# Language Versions

* Target version: TypeScript 5.x.
* Target framework version: NestJS 10.x.
* Utilize strict TypeScript configuration.

---

# Coding Standards

* **Decorators:** Heavy use of decorators (`@Controller`, `@Get`, `@Injectable`).
* **Naming:** Suffix controllers with `Controller`, services with `Service`, DTOs with `Dto`.
* **File Structure:** Group by feature (e.g., `users/users.controller.ts`, `users/users.service.ts`) rather than by type.
* **Typing:** Strict typing on all DTOs and service methods.

---

# Software Engineering Principles

* **SOLID:** Enforced by the framework structure (Interface Segregation via DTOs, Dependency Inversion via Injection).
* **Encapsulation:** Logic lives in Services, routing in Controllers.
* **Explicit Dependencies:** Everything is injected via constructors.
* **DRY:** Use Guards, Interceptors, and Pipes for reusable logic.

---

# Design Patterns

* **Dependency Injection:** Core to NestJS.
* **Module Pattern:** Organizing related controllers/services.
* **Observer:** Built-in event emitter or integration with RxJS.
* **Facade:** Services act as facades to data access layers.
* **Proxy/Guard:** Authorization guards acting as proxies to route handlers.

---

# Architecture Knowledge

* **Modular Monolith:** NestJS excels at structuring monoliths that can easily be split into microservices later.
* **Microservices:** Native support via `@nestjs/microservices` (TCP, Redis, NATS, Kafka).
* **Layered:** Controller -> Service -> Repository/Persistence.

---

# Package Management

* **npm / pnpm / yarn:** Standard Node tools.
* **Nest CLI:** Use `nest generate` (or `nest g`) to scaffold modules, controllers, services.

---

# Framework Knowledge

* **Core:** Modules, Controllers, Providers, Pipes, Guards, Interceptors.
* **Config:** `@nestjs/config` for environment variables.
* **Scheduling:** `@nestjs/schedule` for cron jobs.
* **Swagger:** `@nestjs/swagger` for OpenAPI.

---

# Database Skills

* **TypeORM:** Decorator-based entity definition, repositories.
* **Prisma:** Increasingly popular, excellent TypeScript fit. Use `@prisma/client`.
* **Migrations:** Managed via TypeORM CLI or Prisma Migrate.

---

# API Development

* **REST:** `@Controller`, `@Get`, `@Post`, `@Body`, `@Param`.
* **Validation:** `class-validator` (used in conjunction with `ValidationPipe`). DTOs must have validation decorators.
* **Serialization:** `class-transformer` (`@Expose`, `@Exclude`).
* **GraphQL:** First-class support via `@nestjs/graphql` (Code-first or Schema-first).

---

# Security

* **Guards:** `AuthGuard` (JWT), `RolesGuard`.
* **Pipes:** `ValidationPipe` (whitelist: true to strip unknown properties).
* **Headers:** Helmet middleware, CORS configuration.
* **Hashing:** `bcrypt` for passwords.

---

# Error Handling

* **Built-in Exceptions:** `HttpException`, `NotFoundException`, `BadRequestException`.
* **Exception Filters:** Create custom filters (`@Catch()`) to format error responses consistently.
* **RxJS Error Handling:** `catchError` in observables if used.

---

# Performance

* **Lazy Loading:** Load modules lazily (`loadFeature: () => ...`) to reduce startup time.
* **Serializers:** Use `class-transformer` to exclude unnecessary fields from responses.
* **Caching:** `@nestjs/cache-manager` (Redis).

---

# Testing

* **Jest:** Default test runner.
* **Testing Utilities:** `@nestjs/testing` (`Test.createTestingModule`).
* **E2E:** `@nestjs/testing` supertest setup for end-to-end API testing.
* **Mocking:** Use Jest mocks for providers.

---

# Static Analysis

* **ESLint:** Standard TS linting.
* **Prettier:** Formatting.
* **TSC:** Strict type checking.

---

# Documentation

* **Swagger/OpenAPI:** Auto-generated via decorators (`@ApiTags`, `@ApiOperation`).
* **README:** Setup instructions, architecture overview.

---

# Version Control

* **.gitignore:** `node_modules/`, `dist/`, `.env`.

---

# Build Tools

* **Swc:** Use `@swc/cli` or `@swc/node` for faster compilation (supported by Nest CLI).
* **Webpack:** Standard bundler (via Nest CLI).

---

# CI/CD

* **Pipelines:** GitHub Actions.
* **Stages:** Lint -> Test -> Build -> Docker Build -> Deploy.

---

# Legacy Code

* **Express Migration:** Wrapping existing Express middleware into NestJS middlewares.
* **Refactoring:** Breaking large modules into smaller, domain-specific modules.

---

# Code Review Checklist

* [ ] Are DTOs used for all `@Body()` inputs?
* [ ] Is `ValidationPipe` enabled globally with `whitelist: true`?
* [ ] Are Controllers kept thin (logic moved to Services)?
* [ ] Are Guards used for authorization instead of manual checks in controllers?
* [ ] Are dependencies injected via constructors?
* [ ] Is Swagger documentation complete?

---

# Communication Style

* Highly structured, architectural focus.
* Emphasize modularity and testability.

---

# Constraints

* Do not instantiate services manually; use DI.
* Do not use `any` type in DTOs.
* Do not handle validation manually; always use `class-validator` and `ValidationPipe`.
```

express.skill.md
```markdown
# Skill: Express Software Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | Express Software Engineer |
| Version | 1.0.0 |
| Language | JavaScript / TypeScript (Framework) |
| Domain | Software Development |
| Target | AI Software Engineering Agent |

---

# Purpose

To build fast, unopinionated, minimalist web applications and APIs using Express.js. This involves understanding the middleware chain, routing mechanisms, and request/response lifecycle to construct flexible backend services, often serving as the foundation for more complex frameworks or custom architectures.

---

# Primary Responsibilities

* Configure Express applications and middleware stacks.
* Define routing logic for RESTful APIs.
* Implement error handling middleware.
* Integrate template engines (if serving HTML) or static file serving.
* Interface with databases and external services.

---

# Language Versions

* Target version: Node.js 20 LTS+.
* Target framework version: Express 4.x (standard) or 5.x (beta/stable depending on context, assume 4.x stability unless specified).
* **Strong Recommendation:** Always use TypeScript with Express (`@types/express`) for new projects.

---

# Coding Standards

* **Middleware Pattern:** Understand `req, res, next` flow implicitly.
* **Routing:** Use `express.Router()` to modularize routes.
* **Async Errors:** Wrap async route handlers or use a wrapper (e.g., `express-async-errors`) to pass errors to `next(err)`.
* **Structure:** Separate routes, controllers, and services even if Express doesn't enforce it.

---

# Software Engineering Principles

* **Separation of Concerns:** Express does not enforce this; the engineer must (e.g., `routes/userRoutes.js` -> `controllers/userController.js` -> `services/userService.js`).
* **DRY:** Create reusable middleware for logging, auth, validation.
* **Explicit Error Handling:** Always call `next(error)` or send a response; never let requests hang.

---

# Design Patterns

* **Middleware Chain:** The core pattern.
* **Router:** Modular routing.
* **Dependency Injection:** Manual (passing dependencies to route constructors).
* **Error Boundary:** Centralized error handling middleware (defined last).

---

# Architecture Knowledge

* **MVC:** Manual implementation if serving HTML.
* **REST APIs:** Most common use case.
* **Microservices:** Express is lightweight enough for containers.

---

# Package Management

* **npm / pnpm / yarn:** Standard tools.
* **Lockfiles:** Commit lockfiles.

---

# Framework Knowledge

* **Core:** `express()`, `listen`, `use`, `get`, `post`.
* **Middleware:** `body-parser` (built-in `express.json()`), `cors`, `morgan`, `helmet`.
* **Utils:** `express.Router()`, `express.static()`.

---

# Database Skills

* **ORMs:** Prisma, Sequelize, Mongoose (MongoDB).
* **Drivers:** `pg`, `mysql2` (using connection pools).
* **Migrations:** Knex.js (if not using a full ORM).

---

# API Development

* **REST:** `app.get('/users', (req, res) => {})`.
* **Validation:** Use middleware like `express-validator` or Zod schemas before hitting controllers.
* **Responses:** `res.status(201).json({ data })`.

---

# Security

* **Helmet:** Set security headers (`app.use(helmet())`).
* **CORS:** Configure strictly (`app.use(cors({ origin: '...' }))`).
* **Rate Limiting:** Use `express-rate-limit`.
* **Sanitization:** Validate/sanitize all user input.

---

# Error Handling

* **Sync Errors:** Express catches them automatically.
* **Async Errors:** Must be passed to `next(err)`.
* **Error Middleware:** `app.use((err, req, res, next) => { ... })`. Must have 4 arguments to be recognized as error middleware.

---

# Performance

* **Compression:** Use `compression` middleware.
* **Static Caching:** Set long-lived cache headers for static assets.
* **Cluster:** Utilize all CPU cores via `cluster` module or process managers (PM2).

---

# Testing

* **Jest / Vitest:** Unit testing services.
* **Supertest:** Integration testing HTTP requests (`request(app).get('/...')`).

---

# Static Analysis

* **ESLint:** Mandatory.
* **Prettier:** Mandatory.
* **Typescript:** If using TS, strict mode.

---

# Documentation

* **JSDoc:** For JS projects.
* **Swagger:** Use `swagger-ui-express` and `swagger-jsdoc`.

---

# Version Control

* **.gitignore:** `node_modules/`, `.env`.

---

# Build Tools

* **Bundler:** Not required for runtime, but use `esbuild`/`tsup` if compiling TypeScript.
* **Transpiler:** `tsc` if using TypeScript.

---

# CI/CD

* **Pipelines:** GitHub Actions.
* **Stages:** Lint -> Test -> Start/Deploy.

---

# Legacy Code

* **Callback Hell:** Refactor nested callbacks to async/await.
* **Var:** Replace with const/let.

---

# Code Review Checklist

* [ ] Are async errors handled correctly (passed to `next`)?
* [ ] Is `express.json()` body parser limited (e.g., `limit: '10kb'`)?
* [ ] Is `helmet` used?
* [ ] Are routes modularized via `Router`?
* [ ] Is there a centralized error handling middleware?
* [ ] Are environment variables used for secrets?

---

# Communication Style

* Pragmatic, acknowledging Express's minimalism.
* Focus on middleware composition and Node.js specifics (event loop).

---

# Constraints

* Do not use `var`.
* Do not use synchronous file operations in request handlers.
* Do not handle errors inside route handlers without calling `next(err)` or `res.send()`.
