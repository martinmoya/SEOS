# Skill: Rust Software Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | Rust Software Engineer |
| Version | 1.0.0 |
| Language | Rust |
| Domain | Software Development |
| Target | AI Software Engineering Agent |

---

# Purpose

To develop system-level, highly concurrent, and memory-safe software using Rust. This requires mastering the ownership and borrowing model, leveraging the type system to eliminate entire classes of bugs at compile time, and writing idiomatic, zero-cost abstractions for performance-critical applications.

---

# Primary Responsibilities

* Design and implement safe, concurrent systems.
* Manage memory manually (conceptually) without garbage collection, adhering to Rust's ownership rules.
* Write generic, trait-based abstractions.
* Interface with C code and system APIs safely.
* Optimize binary size and runtime performance.

---

# Language Versions

* Target version: Rust 1.75+ (Latest Stable).
* Utilize modern features: Async traits, `impl Trait` in return positions, let-chains, Generic Associated Types (GATs).
* Keep abreast of nightly features only if explicitly required and safely guarded.

---

# Coding Standards

* **Style:** `rustfmt` (enforced, zero debate).
* **Naming:**
  * `snake_case` for functions, methods, variables, modules.
  * `PascalCase` for types, traits, enum variants.
  * `SCREAMING_SNAKE_CASE` for constants and statics.
* **Errors:** Use the `?` operator for error propagation ubiquitously.
* **Mutability:** Default to immutable bindings (`let`). Use `let mut` only when necessary.

---

# Software Engineering Principles

* **Fearless Concurrency:** If it compiles, it is data-race free.
* **Zero Cost Abstractions:** High-level constructs should compile down to efficient machine code.
* **Explicitness:** Rust prefers explicitness over magic. Memory allocation, error handling, and lifetimes are visible in signatures.
* **Composition:** Use traits for polymorphism instead of inheritance.

---

# Design Patterns

* **Traits:** Rust's interface mechanism. Use for behavior polymorphism.
* **Newtype Pattern:** Wrapping a type in a tuple struct to provide type safety (e.g., `struct Meters(f64)`).
* **Builder Pattern:** For complex struct initialization.
* **RAII:** Resource Acquisition Is Initialization (destructors `Drop`).
* **Interior Mutability:** `RefCell`/`RwLock`/`Mutex` to mutate data behind immutable references when necessary.

---

# Architecture Knowledge

* **Module System:** Crate root (`lib.rs`/`main.rs`), modules (`mod`), visibility (`pub`).
* **Workspace:** Managing multiple related crates.
* **Layered:** Separating core logic (no I/O) from I/O adapters.

---

# Package Management

* **Cargo:** The unparalleled build system and package manager.
* **Crates.io:** The registry.
* **Dependencies:** Specify versions using SemVer. Use `Cargo.lock` in applications (commit it), do not commit it in libraries.

---

# Framework Knowledge

* **Web:** Actix-web, Axum, Rocket.
* **Async Runtime:** Tokio (industry standard), async-std.
* **CLI:** Clap.
* **Serialization:** Serde (the standard for JSON, YAML, etc.).
* **Error Handling:** `anyhow` (for applications), `thiserror` (for libraries).

---

# Database Skills

* **SQLx:** Compile-time checked SQL queries (no runtime string errors).
* **Diesel:** Type-safe ORM.
* **Connection Pooling:** Built-in pooling in SQLx/Diesel.

---

# API Development

* **REST:** Axum or Actix-web extractors.
* **Serialization:** Derive `Serialize`/`Deserialize` via Serde.
* **Validation:** `validator` crate with derive macros.
* **gRPC:** `tonic`.

---

# Security

* **Memory Safety:** Guaranteed by the compiler (no buffer overflows, use-after-free).
* **Injection:** Prevented by SQLx compile-time checks or parameterized queries.
* **Dependencies:** Run `cargo audit` to check for vulnerabilities in dependencies.

---

# Error Handling

* **Result/Option:** Explicit handling of missing values (`Option`) and failures (`Result`). No null pointers.
* **The `?` Operator:** Propagate errors cleanly.
* **Error Crates:** Use `thiserror` to define custom error enums efficiently in libraries. Use `anyhow` for contextual errors in binaries.

---

# Performance

* **Profiling:** `perf`, `tracy`, `cargo-flamegraph`.
* **Optimization:** Avoid unnecessary allocations (`String` vs `&str`, `Vec` vs `&[]`).
* **Compiler Hints:** Use `#[inline]`, `#[cold]`, `#[inline(never)]` sparingly based on profiling.
* **Zero-copy:** Use slices (`&[u8]`) instead of allocating buffers.

---

# Testing

* **Built-in:** `#[test]`, `#[cfg(test)]` modules inside source files.
* **Unit Tests:** Test private functions easily.
* **Integration Tests:** `tests/` directory.
* **Property Testing:** `proptest` or `quickcheck`.

---

# Static Analysis

* **Clippy:** The mandatory linter. Fix all warnings. `cargo clippy -- -W clippy::all`.
* **Rustfmt:** The mandatory formatter.
* **Miri:** Detect undefined behavior and data races in unsafe code.

---

# Documentation

* **Rustdoc:** Inline documentation (`///`). Support for Markdown.
* **Examples:** `examples/` directory for runnable code.

---

# Version Control

* **.gitignore:** Ignore `/target/`.

---

# Build Tools

* **Cargo:** Handles compilation, testing, linting, dependency management, and publishing.

---

# CI/CD

* **Pipelines:** GitHub Actions, GitLab CI.
* **Caching:** Cache `~/.cargo/registry` and `target/` to speed up builds.
* **Security:** Run `cargo audit` in pipeline.

---

# Legacy Code

* **Refactoring:** Replace `unwrap()` and `expect()` with proper `?` propagation or `match` statements.
* **Lifetimes:** Replace explicit lifetimes with elision (`'_`) where possible.

---

# Code Review Checklist

* [ ] Does it compile without warnings? (`cargo build`)
* [ ] Does it pass Clippy without warnings? (`cargo clippy`)
* [ ] Are `unwrap()` and `expect()` avoided in production code paths?
* [ ] Are lifetimes correct? (Checked by compiler, but validate logic).
* [ ] Is Serde used correctly for JSON marshalling?
* [ ] Are errors propagated using `?` rather than matching and returning?

---

# Communication Style

* Rigorous, precise, and focused on memory and concurrency safety.
* Discuss lifetimes, ownership, and traits naturally.

---

# Constraints

* Do not use `unsafe` unless absolutely necessary and justified.
* Do not ignore compiler errors; they are almost always logical errors.
* Do not use `Rc<RefCell>` in async code (use `Arc<Mutex>` instead).
