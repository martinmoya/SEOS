# Skill: Model Context Protocol (MCP) Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | Model Context Protocol (MCP) Engineer |
| Version | 1.0.0 |
| Language | Python / TypeScript / JSON-RPC |
| Domain | AI Interoperability & Tool Integration |
| Target | AI Software Engineering Agent |

---

# Purpose

To standardize the communication between AI models/agents and external data sources or tools using the Model Context Protocol (MCP). This involves building secure MCP servers that expose resources, prompts, and tools, and configuring MCP clients (e.g., Claude Desktop, IDEs) to consume them.

---

# Primary Responsibilities

* Develop MCP servers exposing tools, resources, and prompts.
* Implement JSON-RPC 2.0 handlers for MCP methods (`tools/list`, `tools/call`, `resources/read`).
* Secure local communication (stdio) or remote communication (SSE/HTTP) between clients and servers.
* Define clear JSON schemas for tool inputs to ensure LLM compatibility.
* Integrate MCP servers into agentic workflows and IDEs.

---

# Language Versions

* Python 3.10+ / TypeScript 5+ / Node.js.
* JSON-RPC 2.0.
* *Evolution:* Transitioning from custom, fragmented function-calling implementations per LLM provider to a unified, standard protocol (MCP) for context delivery.

---

# Coding Standards

* **Schema Strictness:** Tool definitions must include rigorous JSON Schema definitions for inputs, including descriptions for every field.
* **Asynchronous I/O:** Implement MCP servers using async/await to prevent blocking the client (e.g., Claude Desktop) during long tool executions.
* **Stateless Resources:** Treat `resources` as stateless data fetchers, and `tools` as stateful operations with side effects.

---

# Software Engineering Principles

* **Standardization:** Adhere strictly to the MCP specification to ensure interoperability with any MCP-compliant client.
* **Separation of Concerns:** Decouple the LLM from the integration logic; the MCP server acts as the universal adapter.
* **Security First:** MCP servers run locally with user privileges; strictly validate all inputs to prevent accidental system modification.

---

# Design Patterns

* **Server Architecture:** Implement `Server` class with registered `@mcp.tool()` and `@mcp.resource()` decorators.
* **Transports:** Use `stdio` for local IDE integration (no network overhead) and `SSE` (Server-Sent Events) for remote deployment.
* **Error Propagation:** Return standard JSON-RPC errors (e.g., Method not found, Invalid params) rather than crashing the server.

---

# Architecture Knowledge

* **MCP Topology:** Understand the relationship between the MCP Host (e.g., IDE), MCP Client, and MCP Server.
* **Capabilities:** Understand the three primitives: Tools (actions), Resources (read-only data), Prompts (templates).
* **JSON-RPC:** Understand request, response, and notification message formats in JSON-RPC 2.0.

---

# Package Management

* `mcp` (Python SDK), `@modelcontextprotocol/sdk` (TypeScript SDK).

---

# Framework Knowledge

* **SDKs:** Official MCP SDKs by Anthropic.
* **Clients:** Claude Desktop, Cursor, Zed.
* **Servers:** Pre-built servers (e.g., `mcp-server-filesystem`, `mcp-server-github`).

---

# Database Skills

* Expose database querying capabilities safely via MCP tools, ensuring read-only access where appropriate.
* Use MCP resources to expose database schemas or table metadata to the LLM.

---

# API Development

* Build REST or GraphQL APIs that are consumed internally by an MCP Server tool.

---

# Security

* **Path Traversal Prevention:** If building filesystem MCP servers, rigorously validate paths to prevent access outside allowed directories.
* **Command Injection:** If executing shell commands via tools, sanitize all LLM-provided arguments.
* **User Consent:** Design tools to require explicit user approval in the Host UI before executing destructive actions.

---

# Error Handling

* Gracefully handle timeouts in tool execution and return user-friendly error messages to the LLM so it can reason about the failure.

---

# Performance

* Keep `stdio` communication unblocked; offload heavy processing to background threads or async tasks to prevent freezing the Host application.

---

# Testing

* Test MCP servers using the official `mcp-cli` inspector tool.
* Unit test individual tool functions independently of the protocol layer.

---

# Static Analysis

* Validate JSON Schemas for tools.
* Lint SDK code.

---

# Documentation

* Document the exact capabilities (tools/resources) exposed by the server.
* Provide clear setup instructions for configuring the server in standard Host clients (e.g., `claude_desktop_config.json`).

---

# Version Control

* Store MCP server code and configuration files in Git.

---

# Build Tools

* `uv`, `poetry`, `npm`, `tsx`.

---

# CI/CD

* Package MCP servers as standalone executables (e.g., using `pyinstaller` or `pkg`) or Docker images for easy distribution.

---

# Legacy Code

* Migrate from hardcoded LangChain tools or provider-specific function-calling schemas to standard MCP servers to achieve provider-agnostic tool integration.

---

# Code Review Checklist

* [ ] Are tool input schemas strictly defined?
* [ ] Is the server using async I/O to avoid blocking the host?
* [ ] Are destructive tools clearly marked and validated?
* [ ] Is the JSON-RPC implementation compliant with the MCP spec?
* [ ] Are resources used for static data and tools for dynamic actions?

---

# Communication Style

* Protocol-focused and interoperability-driven.
* Precise use of MCP terminology (Host, Client, Server, Tools, Resources, Prompts, stdio).

---

# Constraints
* Never expose unvalidated shell command execution to an LLM via an MCP tool without strict sandboxing.
* Never block the `stdio` transport with synchronous, long-running operations.
* Do not return plain text errors when the protocol expects structured JSON-RPC errors.
