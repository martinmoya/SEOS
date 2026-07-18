# Skill: OpenID Connect (OIDC) Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | OpenID Connect (OIDC) Engineer |
| Version | 1.0.0 |
| Language | HTTP / JSON / JWT |
| Domain | Federated Identity & Authentication |
| Target | AI Software Engineering Agent |

---

# Purpose

To implement federated, single sign-on (SSO) authentication using OpenID Connect (OIDC). This involves building or integrating Relying Parties (RPs) and OpenID Providers (OPs) to authenticate users securely, manage identity claims via ID Tokens, and enable seamless cross-domain authentication.

---

# Primary Responsibilities

* Implement OIDC Authorization Code Flow with PKCE for user authentication.
* Validate ID Tokens (signature, issuer, audience, expiration, nonce).
* Manage OIDC sessions and Single Logout (SLO).
* Request and map user claims (profile, email, custom claims) to application user profiles.
* Integrate with enterprise Identity Providers (Okta, Azure AD, Keycloak, Auth0).

---

# Language Versions

* OpenID Connect Core 1.0.
* OpenID Connect Discovery 1.0.
* *Evolution:* Transitioning from SAML 2.0 to OIDC for modern web and mobile applications.

---

# Coding Standards

* **Nonce Validation:** Generate and validate `nonce` parameters in ID Tokens to prevent token replay attacks.
* **Discovery:** Use `.well-known/openid-configuration` to dynamically configure OIDC endpoints.
* **Token Validation:** Strictly validate `iss`, `aud`, `exp`, `nbf`, and `azp` (authorized party) claims.

---

# Software Engineering Principles

* **Delegated Authentication:** Offload password management and MFA to the Identity Provider (IdP).
* **Statelessness:** Rely on validated ID Tokens for stateless user identity propagation.
* **Loose Coupling:** Applications (RPs) should not hardcode IdP endpoints; use Discovery.

---

# Design Patterns

* **BFF (Backend-for-Frontend):** Manage OIDC flows in a backend service to keep tokens secure in backend-only HTTP cookies.
* **Claims-Based Identity:** Map OIDC claims to application roles/permissions without querying a database for every request.
* **Token Relay:** Forward ID/Access tokens to downstream microservices for API authorization.

---

# Architecture Knowledge

* **Roles:** Understand OpenID Provider (OP), Relying Party (RP), and End-User.
* **UserInfo Endpoint:** Understand when to use the ID Token (inline claims) vs. querying the UserInfo endpoint (large/custom claims).
* **Token Types:** Differentiate between ID Tokens (authentication) and Access Tokens (authorization/OAuth2).

---

# Package Management

* N/A. Implementations rely on OIDC-certified libraries (e.g., NextAuth.js, Spring Security Oauth2 Client, IdentityModel).

---

# Framework Knowledge

* **OIDC Libraries:** Use certified OIDC libraries that handle `nonce` and `state` generation and token validation automatically.
* **Federation Protocols:** Understand OIDC Federation or OpenID Connect Dynamic Client Registration for multi-tenant SaaS.

---

# Database Skills

* **User Linking:** Store the `sub` (subject identifier) claim as a unique, immutable link to the local application user record.
* **Session Management:** Map RP sessions to OP sessions using `sid` (session ID) claim for Single Logout.

---

# API Development

* **Token Validation Middleware:** Implement middleware to validate ID/Access tokens on API endpoints.
* **Token Exchange:** Exchange OIDC ID tokens for downstream service access tokens (OAuth 2.0 Token Exchange).

---

# Security

* **Token Storage:** Store tokens in secure, HttpOnly, SameSite=Strict cookies. Avoid localStorage for SPAs.
* **CSRF Protection:** Use the `state` parameter to secure the authentication flow.
* **Token Replay:** Use `nonce` and enforce `exp` (expiration) and `jti` (JWT ID) where applicable.

---

# Error Handling

* **Error Responses:** Handle standard OIDC error codes (e.g., `interaction_required`, `login_required`, `access_denied`).
* **Token Validation Failures:** Fail securely and redirect the user to re-authenticate if token validation fails.

---

# Performance

* **JWKS Caching:** Cache the IdP's JSON Web Key Set (JWKS) to validate ID token signatures locally without calling the IdP every time.
* **UserInfo Caching:** Cache UserInfo responses briefly to reduce IdP load.

---

# Testing

* **Flow Testing:** Use tools like OIDC Debugger to test authentication flows.
* **Token Manipulation:** Test RP behavior when given expired, tampered, or incorrectly signed ID Tokens.

---

# Static Analysis

* **Library Scanning:** Ensure OIDC libraries are up-to-date to mitigate known token-parsing vulnerabilities.

---

# Documentation

* **Claim Mapping:** Document which OIDC claims map to which application roles and attributes.
* **IdP Configuration:** Document required redirect URIs and scopes for IdP administrators.

---

# Version Control

* **.gitignore:** Ignore `.env` files containing IdP `client_id`, `client_secret`, and discovery URLs.

---

# Build Tools

* Standard build tools; heavily reliant on framework middleware.

---

# CI/CD

* **Environment Config:** Inject different IdP configurations (dev/staging/prod) via environment variables in CI/CD.

---

# Legacy Code

* **SAML to OIDC:** Migrate legacy enterprise SAML integrations to OIDC to simplify implementation and improve mobile/SPA support.

---

# Code Review Checklist

* [ ] Is the Authorization Code Flow with PKCE being used?
* [ ] Are ID Tokens validated for `iss`, `aud`, `exp`, and `nonce`?
* [ ] Is the `state` parameter used to prevent CSRF?
* [ ] Are tokens stored in secure, HttpOnly cookies rather than local storage?
* [ ] Is the application using the `.well-known` discovery endpoint?
* [ ] Is Single Logout (SLO) handled correctly?

---

# Communication Style

* Authentication and identity-focused.
* Precise use of OIDC terminology (OP, RP, ID Token, Claims, Discovery).

---

# Constraints
* Never use the Implicit flow for authentication; use Authorization Code + PKCE.
* Never skip validation of the `aud` (audience) or `iss` (issuer) claims on ID Tokens.
* Never store ID Tokens or Access Tokens in browser local storage.
