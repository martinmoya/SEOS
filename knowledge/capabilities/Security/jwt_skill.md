# Skill: JSON Web Token (JWT) Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | JSON Web Token (JWT) Engineer |
| Version | 1.0.0 |
| Language | JSON / Base64URL |
| Domain | Stateless Authentication & Information Security |
| Target | AI Software Engineering Agent |

---

# Purpose

To securely transmit authenticated claims and information between parties as a JSON object. This involves generating, signing, validating, and managing JWTs for stateless API authorization, ensuring that tokens are tamper-proof, correctly scoped, and impervious to common JWT attack vectors.

---

# Primary Responsibilities

* Generate and sign JWTs using secure algorithms (RS256, ES256).
* Implement robust JWT validation middleware (signature, expiration, audience, issuer).
* Manage key rotation via JWKS (JSON Web Key Set).
* Pack necessary, non-sensitive claims into JWTs for stateless authorization.
* Mitigate common JWT vulnerabilities (algorithm confusion, `alg: none`).

---

# Language Versions

* JWT (RFC 7519).
* JWS (JSON Web Signature - RFC 7515).
* JWE (JSON Web Encryption - RFC 7516).
* *Evolution:* Transitioning from symmetric signing (HS256) with shared secrets to asymmetric signing (RS256/ES256) and key rotation via JWKS.

---

# Coding Standards

* **Claim Usage:** Use standard claims (`iss`, `sub`, `aud`, `exp`, `nbf`, `iat`, `jti`) appropriately.
* **Compact Size:** Keep JWT payloads minimal; do not dump entire user profiles into the token.
* **Signing Algorithms:** Enforce specific expected algorithms during validation; do not trust the `alg` header blindly.

---

# Software Engineering Principles

* **Statelessness:** JWTs carry all necessary context, allowing APIs to authorize requests without a database lookup.
* **Expiration:** All tokens must have a strict, short `exp` (expiration) claim.
* **Immutability:** Once signed, a JWT cannot be modified; use short lifespans to handle role/permission changes.

---

# Design Patterns

* **Access & Refresh Tokens:** Use short-lived Access Tokens for API calls and long-lived Refresh Tokens to obtain new Access Tokens.
* **JWKS Endpoint:** Expose a public keys endpoint (`/.well-known/jwks.json`) for asymmetric key rotation.
* **Token Revocation:** Implement a blacklist of `jti` (JWT ID) claims for urgent token revocation (requires stateful check).

---

# Architecture Knowledge

* **Structure:** Understand the Header, Payload, and Signature components.
* **JWS vs. JWE:** Differentiate between signed tokens (JWS - integrity) and encrypted tokens (JWE - confidentiality).
* **Stateful vs. Stateless:** Understand the trade-offs; JWTs are stateless, making immediate revocation difficult.

---

# Package Management

* **Libraries:** Use mature, well-tested libraries like `jsonwebtoken` (Node), `PyJWT` (Python), or `jose` (Go/JS) rather than custom implementations.

---

# Framework Knowledge

* **Middleware:** Integrate JWT validation into API Gateway or framework middleware (Express, Spring, FastAPI).
* **OAuth2/OIDC:** Understand JWTs as the standard format for OAuth2 Access Tokens and OIDC ID Tokens.

---

# Database Skills

* **Refresh Token Storage:** Store hashes of refresh tokens in the database to validate and support rotation/revocation.
* **Blacklisting:** Store revoked `jti`s in a fast key-value store (Redis) with TTL matching the token expiration.

---

# API Development

* **Bearer Tokens:** Accept JWTs exclusively via `Authorization: Bearer <token>`.
* **Error Handling:** Return `401 Unauthorized` for missing/invalid tokens, `403 Forbidden` for valid tokens lacking permissions.

---

# Security

* **Algorithm Confusion:** Prevent attacks where an attacker alters the `alg` header to `none` or HS256, tricking the server into using the public key as an HMAC secret.
* **Key Management:** Protect signing private keys using HSMs or KMS.
* **Data Minimization:** Never put sensitive data (passwords, SSNs) in a JWT payload; it is Base64URL encoded, not encrypted.

---

# Error Handling

* **Token Expiration:** Handle `TokenExpiredError` gracefully by prompting the client to refresh.
* **Invalid Signature:** Reject tokens with invalid signatures immediately with generic 401 errors (no detailed error messages).

---

# Performance

* **Local Validation:** Use RS256/ES256 so APIs can validate tokens locally using cached public keys, avoiding database or IdP lookups per request.
* **Payload Size:** Keep payloads small to avoid large HTTP headers (especially for mobile networks).

---

# Testing

* **Token Tampering:** Test APIs by altering payload claims (e.g., changing `role` from `user` to `admin`) to ensure signature validation fails.
* **Expiration Testing:** Test API behavior with expired tokens.

---

# Static Analysis

* **Library Audits:** Regularly audit JWT libraries for known CVEs (e.g., CVE-2022-23529 in `jsonwebtoken`).

---

# Documentation

* **Claim Specifications:** Document custom claims used in the application and their types.
* **Security Policies:** Document token lifetimes and key rotation policies.

---

# Version Control

* **.gitignore:** Never commit private keys (`.pem`, `.key`) used for signing JWTs.

---

# Build Tools

* Standard build tools; signing keys injected via environment variables or Secrets Managers.

---

# CI/CD

* **Key Rotation:** Automate key rotation in CI/CD or infrastructure code, updating the JWKS endpoint and keeping old keys valid briefly for overlap.

---

# Legacy Code

* **Stateful Sessions:** Migrate from server-side opaque session cookies to stateless JWTs for distributed, microservice-based architectures.

---

# Code Review Checklist

* [ ] Is the token validated against a hardcoded expected algorithm list?
* [ ] Are `exp`, `aud`, and `iss` claims strictly validated?
* [ ] Is RS256 or ES256 used instead of HS256 for multi-service architectures?
* [ ] Are JWTs transmitted over HTTPS only?
* [ ] Are JWT payloads kept minimal and free of sensitive PII?
* [ ] Is key rotation implemented via JWKS?

---

# Communication Style

* Stateless architecture and cryptographic integrity focused.
* Precise use of JWT terminology (Claims, Header, Payload, Signature, JWS, JWKS).

---

# Constraints
* Never allow the `alg: none` algorithm during validation.
* Never put sensitive information (passwords, PII) in a JWT payload unless using JWE.
* Never use HS256 (symmetric) in distributed systems where the secret must be shared across multiple services.
