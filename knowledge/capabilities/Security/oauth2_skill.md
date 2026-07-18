# Skill: OAuth 2.0 Authorization Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | OAuth 2.0 Authorization Engineer |
| Version | 1.0.0 |
| Language | HTTP / JSON |
| Domain | Identity & Access Management (IAM) |
| Target | AI Software Engineering Agent |

---

# Purpose

To design and implement secure delegated authorization mechanisms using the OAuth 2.0 framework. This involves selecting appropriate grant types, managing access tokens securely, enforcing scopes, and ensuring that third-party applications receive limited access to user resources without exposing credentials.

---

# Primary Responsibilities

* Implement and secure OAuth 2.0 flows (Authorization Code, Client Credentials, Device Code).
* Enforce PKCE (Proof Key for Code Exchange) for all public clients (SPAs, Mobile).
* Validate access tokens and enforce scope-based authorization on API endpoints.
* Manage client credentials and redirect URIs securely.
* Implement refresh token rotation and reuse detection.

---

# Language Versions

* OAuth 2.0 Framework (RFC 6749).
* OAuth 2.0 Security Best Current Practice (BCP) (RFC 9700).
* PKCE (RFC 7636).
* *Evolution:* Transitioning from Implicit flow and Resource Owner Password Credentials (ROPC) to Authorization Code + PKCE.

---

# Coding Standards

* **Redirect URI Validation:** Enforce exact matching of redirect URIs; do not allow wildcards.
* **State Parameter:** Generate and validate cryptographically random `state` parameters to prevent CSRF attacks.
* **Token Transmission:** Transmit tokens exclusively via `Authorization: Bearer <token>` headers, never in URLs.

---

# Software Engineering Principles

* **Least Privilege:** Request only the minimum scopes necessary for application functionality.
* **Separation of Duties:** Separate the Resource Server (API) from the Authorization Server (IdP).
* **Statelessness:** Use signed, self-contained tokens (JWTs) for stateless API authorization where appropriate.

---

# Design Patterns

* **Backend-for-Frontend (BFF):** Use a backend service to handle token acquisition and session management for Single Page Applications (SPAs) to avoid exposing tokens in the browser.
* **Token Exchange:** Use Token Exchange (RFC 8693) to swap a token for a more scoped token when traversing service boundaries.
* **Refresh Token Rotation:** Issue a new refresh token on every use; revoke the chain if a previously used token is presented.

---

# Architecture Knowledge

* **Roles:** Clear understanding of Resource Owner, Client, Authorization Server, and Resource Server.
* **Grant Types:** Selecting the correct grant type based on the client capability (e.g., Client Credentials for M2M, Auth Code + PKCE for web/mobile).
* **Token Types:** Understanding Access Tokens (opaque vs. JWT) and Refresh Tokens.

---

# Package Management

* N/A. Usually implemented via Identity Providers (Auth0, Keycloak, Okta) or framework middleware (Spring Security, NextAuth.js).

---

# Framework Knowledge

* **OIDC Libraries:** Use battle-tested libraries like AppAuth, MSAL, or openid-client rather than implementing OAuth from scratch.
* **API Gateways:** Offload token introspection and validation to API Gateways (Kong, AWS API Gateway).

---

# Database Skills

* **Token Storage:** Store only the hash of refresh tokens in the database. Never store access tokens.
* **Client Management:** Store client IDs, hashed client secrets, and allowed redirect URIs.

---

# API Development

* **Resource Server Middleware:** Implement middleware to extract the Bearer token, verify its signature/audience, and populate the request context with scopes.
* **Error Responses:** Return standard `401 Unauthorized` with `WWW-Authenticate` header for missing/invalid tokens, and `403 Forbidden` for insufficient scopes.

---

# Security

* **PKCE:** Mandatory for public clients to prevent authorization code interception.
* **Client Secrets:** Store client secrets securely (KMS, Secrets Manager), never in frontend code.
* **Token Leakage:** Prevent token leakage via logs, Referer headers, or browser history.

---

# Error Handling

* **Error Responses:** Return standard OAuth 2.0 error responses (e.g., `invalid_request`, `invalid_client`, `access_denied`).
* **Revocation:** Provide and utilize token revocation endpoints (`/oauth/revoke`) for logout or compromise scenarios.

---

# Performance

* **Token Caching:** Cache JWKS (JSON Web Key Set) from the Authorization Server to avoid fetching public keys on every API request.
* **Introspection Caching:** If using opaque tokens, cache the introspection result briefly to reduce Authorization Server load.

---

# Testing

* **Flow Testing:** Use tools like Postman or OAuth playgrounds to test complete flows.
* **Security Testing:** Test for open redirects, CSRF (missing state), and token leakage.

---

# Static Analysis

* **Dependency Scanning:** Ensure OAuth libraries are up-to-date, as vulnerabilities in token parsing are common.

---

# Documentation

* **API Security:** Document required scopes for each API endpoint (e.g., `scope: read:users`).
* **Integration Guides:** Provide clear documentation for third-party developers integrating via OAuth 2.0.

---

# Version Control

* **.gitignore:** Ignore local client secrets and `.env` files containing IdP configurations.

---

# Build Tools

* Standard build tools; relies heavily on SDKs provided by Authorization Servers.

---

# CI/CD

* **Pipeline Checks:** Verify that client applications are built with PKCE enabled.
* **Environment Isolation:** Use distinct OAuth clients (different `client_id`) for dev, staging, and prod.

---

# Legacy Code

* **Modernization:** Migrate from ROPC (Resource Owner Password Credentials) to Authorization Code + PKCE.
* **Implicit Flow:** Migrate SPAs from Implicit flow to BFF pattern or Auth Code + PKCE.

---

# Code Review Checklist

* [ ] Is PKCE implemented for all public clients?
* [ ] Is the `state` parameter validated on token requests?
* [ ] Are redirect URIs strictly matched (no wildcards)?
* [ ] Are access tokens sent only via HTTP headers?
* [ ] Are refresh tokens rotated upon use?
* [ ] Are API endpoints enforcing scope checks?

---

# Communication Style

* Authorization and delegation-focused.
* Precise use of OAuth terminology (Grants, Scopes, PKCE, Client, Resource Server).

---

# Constraints
* Never use the Implicit flow or ROPC for new applications.
* Never expose client secrets in frontend applications (SPAs, mobile).
* Never put access tokens in URL query parameters.
