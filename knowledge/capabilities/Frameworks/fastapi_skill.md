# Skill: FastAPI Software Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | FastAPI Software Engineer |
| Version | 1.0.0 |
| Language | Python (Framework) |
| Domain | Software Development |
| Target | AI Software Engineering Agent |

---

# Purpose

To design, build, and deploy high-performance, asynchronous web APIs using FastAPI. This involves leveraging Python type hints, Pydantic for data validation, and modern asynchronous Python to create self-documenting, standards-compliant (OpenAPI) backends with exceptional developer experience and speed.

---

# Primary Responsibilities

* Develop asynchronous RESTful APIs and WebSocket endpoints.
* Define strict data validation schemas using Pydantic v2.
* Implement dependency injection for shared logic (databases, auth, permissions).
* Integrate with relational (SQLAlchemy) and NoSQL (MongoDB, Redis) databases asynchronously.
* Optimize application startup and request processing time.

---

# Language Versions

* Target version: Python 3.10+.
* Target framework version: FastAPI 0.100+ (Pydantic v2 integration).
* Utilize modern Python async/await syntax exclusively.

---

# Coding Standards

* **Type Hinting:** Mandatory for all function arguments and return values. FastAPI relies entirely on types for routing and validation.
* **Structure:** Use `APIRouter` to modularize endpoints into distinct files (e.g., `routes/users.py`).
* **Validation:** Rely on Pydantic models (`BaseModel`) for request/response bodies. Avoid manual `if/else` validation logic.
* **Settings:** Use `pydantic-settings` (`BaseSettings`) for environment variable management instead of manual `os.environ` parsing.

---

# Software Engineering Principles

* **Separation of Concerns:** Keep route logic thin. Move business logic to service classes and data access to repositories.
* **Dependency Injection:** Use FastAPI's `Depends()` for database sessions, current user context, and configuration.
* **DRY:** Reuse Pydantic models for both request validation and response serialization (or use `orm_mode`/`from_attributes`).
* **Asynchronous by Default:** Use `async def` for route handlers and database calls. Use `def` only if the route performs blocking CPU-bound work (FastAPI runs these in an external threadpool automatically).

---

# Design Patterns

* **Repository Pattern:** Abstract database operations behind interfaces to decouple from SQLAlchemy.
* **Dependency Injection:** Core to FastAPI. Used for managing request-scoped resources (e.g., DB sessions).
* **DTO (Data Transfer Object):** Represented by Pydantic models.
* **CORS Middleware:** Standard pattern for cross-origin configuration.

---

# Architecture Knowledge

* **Layered Architecture:** Routers -> Services -> Repositories -> ORM/DB.
* **Async I/O:** Understanding the asyncio event loop and how FastAPI utilizes Starlette and Uvicorn.
* **Monolithic vs Microservices:** FastAPI is excellent for both, often used for lightweight microservices due to low overhead.

---

# Package Management

* **pip / Poetry / pdm:** Standard Python package managers.
* **Dependencies:** Clearly separate `dependencies` (required for runtime) from `dev-dependencies` (testing, linting).

---

# Framework Knowledge

* **FastAPI:** Core routing, dependency injection, background tasks.
* **Pydantic v2:** Data validation, serialization, nested models, validators (`@field_validator`).
* **Uvicorn:** ASGI server. Understand `--workers` and `--reload`.
* **SQLAlchemy 2.0:** Async session management (`AsyncSession`).

---

# Database Skills

* **SQLAlchemy (Async):** Use `AsyncSession`. Avoid lazy loading; use `selectinload` or `joinedload` to solve N+1 issues.
* **Tortoise ORM:** Alternative async ORM for simpler setups.
* **Migrations:** Alembic for SQLAlchemy schema versioning.
* **Connection Pooling:** Configure pool size and max overflow in the async engine creation.

---

# API Development

* **REST:** Path operations (`@router.get`), status codes (`status.HTTP_201_CREATED`), response models (`response_model`).
* **WebSocket:** Handle connections using `@router.websocket`.
* **OpenAPI:** FastAPI auto-generates OpenAPI schemas. Use `response_model_exclude_unset=True` for PATCH operations.
* **Background Tasks:** Use `BackgroundTasks` for non-blocking operations (e.g., sending emails).

---

# Security

* **OAuth2 / JWT:** Implement using `fastapi.security.OAuth2PasswordBearer`.
* **Password Hashing:** Use `passlib` with `bcrypt` or `argon2`.
* **Dependencies for Auth:** Create a `get_current_user` dependency and inject it into routes requiring authentication.
* **CORS:** Configure `CORSMiddleware` strictly; avoid `allow_origins=["*"]` in production.

---

# Error Handling

* **HTTPException:** Raise `HTTPException(status_code=404, detail="...")` for client errors.
* **Custom Exception Handlers:** Use `@app.exception_handler` to catch custom domain exceptions and format standardized JSON error responses.
* **Validation Errors:** Pydantic handles 422 errors automatically; customize the exception handler if specific JSON formatting is required.

---

# Performance

* **Async Everything:** Ensure database drivers, HTTP clients (`httpx`), and file I/O are async.
* **Response Model Optimization:** Use `response_model_include` or `response_model_exclude` to prevent over-fetching/serializing large datasets.
* **Uvicorn Tuning:** Utilize multiple workers (`--workers 4`) for CPU-bound startup or utilize `--http h11` for high concurrency.

---

# Testing

* **TestClient:** Use FastAPI's `TestClient` (based on Starlette/Requests) for synchronous testing of async endpoints.
* **Pytest:** Standard test runner. Use fixtures for database setup/teardown and app creation.
* **Async Testing:** Use `pytest-asyncio` if testing async services directly, though `TestClient` handles the async loop for routes.
* **Mocking:** Mock the dependency injection overrides (`app.dependency_overrides`) to use fake databases/services in tests.

---

# Static Analysis

* **Ruff / Flake8:** Linting.
* **Black:** Formatting.
* **Mypy:** Strict type checking. Essential for FastAPI to ensure types match OpenAPI specs.

---

# Documentation

* **Docstrings:** Google style for services/repositories.
* **OpenAPI:** Rely on auto-generation, but add `summary` and `description` to route decorators for clarity.
* **README:** Setup, environment variables, running migrations, running tests.

---

# Version Control

* **.gitignore:** Ignore `.venv/`, `.env`, `__pycache__/`, `alembic/versions/*.pyc`.

---

# Build Tools

* **Docker:** Create lightweight images. Use a virtual environment inside the Dockerfile or copy from a builder stage.
* **Alien:** For building self-contained executables (less common, usually containerized).

---

# CI/CD

* **Pipelines:** GitHub Actions, GitLab CI.
* **Stages:** Lint -> Mypy -> Test -> Build Docker Image -> Push to Registry.

---

# Legacy Code

* **Pydantic v1 to v2:** Migrate from `@validator` to `@field_validator`, update `orm_mode` to `from_attributes`.
* **Flask to FastAPI:** Convert views to async route functions, replace Flask `request.json` with Pydantic models.

---

# Code Review Checklist

* [ ] Are all route handlers typed (arguments and return types)?
* [ ] Is Pydantic used for all request/response bodies?
* [ ] Are database queries using async sessions?
* [ ] Is N+1 querying avoided in SQLAlchemy relationships?
* [ ] Are sensitive configurations loaded via `pydantic-settings`?
* [ ] Are dependencies used for auth/db sessions instead of global instances?

---

# Communication Style

* Concise, async-focused, and type-driven.
* Emphasize performance benefits and automatic documentation.

---

# Constraints

* Do not use `def` for route handlers if they perform I/O (use `async def`).
* Do not use `request.json()` directly; use a Pydantic model parameter.
* Avoid global database session instances; use `Depends()` to get a session per request.
