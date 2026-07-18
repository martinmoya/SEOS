# Skill: Large Language Model (LLM) Integration Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | Large Language Model (LLM) Integration Engineer |
| Version | 1.0.0 |
| Language | Python / TypeScript / JSON |
| Domain | Artificial Intelligence & NLP |
| Target | AI Software Engineering Agent |

---

# Purpose

To integrate pre-trained Large Language Models (LLMs) into software applications for tasks such as text generation, summarization, translation, and code generation. This involves managing API interactions, optimizing token usage, enforcing context windows, and ensuring reliable, safe, and deterministic outputs from non-deterministic models.

---

# Primary Responsibilities

* Integrate with commercial and open-source LLM APIs (OpenAI, Anthropic, HuggingFace, vLLM).
* Design robust system prompts and manage conversation histories.
* Implement token counting and context window truncation strategies.
* Enforce structured output generation (JSON mode, Function Calling).
* Mitigate hallucinations and handle API rate limits/timeouts gracefully.

---

# Language Versions

* Python 3.10+ / TypeScript 5+.
* JSON (for API payloads and structured outputs).
* *Evolution:* Transitioning from raw REST API calls to standardized SDKs, and from pure text completion to ChatML and instruction-tuned models.

---

# Coding Standards

* **Decoupling:** Abstract the LLM provider behind an interface (e.g., `BaseLLMClient`) to allow swapping models (e.g., GPT-4 to Claude 3) without rewriting application logic.
* **Token Awareness:** Always estimate token counts before sending requests to prevent `ContextWindowExceeded` errors.
* **Configuration:** Parameterize `temperature`, `top_p`, and `max_tokens` via environment variables or configuration files, not hardcoded.

---

# Software Engineering Principles

* **Determinism over Randomness:** Set `temperature=0` or use deterministic decoding strategies for analytical or data-extraction tasks.
* **Graceful Degradation:** Implement fallback models if the primary LLM provider is unavailable.
* **Statelessness:** Design API endpoints to be stateless; manage conversation state in the application database, not in the LLM memory.

---

# Design Patterns

* **Facade Pattern:** Wrap complex LLM SDK calls behind a simplified application-specific interface.
* **Chain of Responsibility:** Pass LLM output through validation filters (e.g., JSON schema validation, safety filters) before returning to the user.
* **Retry with Exponential Backoff:** Handle `429 Too Many Requests` and `5xx` server errors automatically.

---

# Architecture Knowledge

* **Context Window:** Understand the maximum token limit (input + output) of the target model.
* **Instruction Tuning:** Understand how system prompts guide model behavior compared to user prompts.
* **Tokenizer:** Understand that LLMs process text in tokens, not characters, affecting cost and length limits.

---

# Package Management

* **SDKs:** `openai`, `anthropic`, `huggingface_hub`, `langchain`, `litellm`.
* **Tokenizers:** `tiktoken` (OpenAI), `transformers` (HuggingFace).

---

# Framework Knowledge

* **Commercial APIs:** OpenAI, Anthropic, Google Gemini.
* **Open-Source Serving:** vLLM, Ollama, Text Generation Inference (TGI) for self-hosted models.
* **Structured Output:** Instructor, Marvin, or native function calling APIs.

---

# Database Skills

* Store conversation history and LLM metadata (model used, token counts, latency) in a relational DB or NoSQL store for auditing and analytics.

---

# API Development

* **Asynchronous Processing:** Expose LLM endpoints as asynchronous tasks (Webhooks or Server-Sent Events) if generation takes >3 seconds.
* **Streaming:** Implement streaming responses (`stream=True`) to improve perceived latency for end-users.

---

# Security

* **Prompt Injection:** Sanitize user input to prevent override of system prompts. Use delimiters (e.g., `<user_input>`) to separate instructions from data.
* **Data Privacy:** Prevent sending PII to third-party LLM APIs by implementing redaction pipelines prior to inference.
* **API Key Management:** Store LLM API keys in Secrets Manager, never in frontend code.

---

# Error Handling

* **JSON Parsing:** LLMs may output malformed JSON. Use `json_repair` libraries or strict structured output modes.
* **Timeouts:** Enforce strict timeouts (e.g., 30s) to prevent hanging requests.

---

# Performance

* **Prompt Caching:** Cache identical prompt responses (e.g., using Redis) to reduce latency and costs.
* **Model Selection:** Route simple tasks to smaller, faster, cheaper models (e.g., GPT-3.5/Llama 8B) and complex reasoning to larger models (GPT-4/Claude Opus).

---

# Testing

* **Evaluation Frameworks:** Use frameworks like `promptfoo` or `Ragas` to run regression tests on prompts against datasets.
* **Assertion Testing:** Assert that LLM outputs match expected JSON schemas or contain specific key phrases.

---

# Static Analysis

* Lint Python/TS code.
* Validate JSON schemas of expected LLM outputs.

---

# Documentation

* Document system prompts in version control, explaining the intent and constraints of each prompt.
* Maintain a catalog of supported models and their context windows.

---

# Version Control

* Version control all prompts (`.txt` or `.py` files) alongside application code.

---

# Build Tools

* `poetry`, `npm`, `docker`.

---

# CI/CD

* Run automated prompt regression tests in CI to catch regressions when updating prompts or changing models.

---

# Legacy Code

* Migrate from deprecated completion APIs (`text-davinci-003`) to Chat Completion APIs (`gpt-4o`, `gpt-3.5-turbo`).

---

# Code Review Checklist

* [ ] Is the LLM provider abstracted behind an interface?
* [ ] Are token counts monitored to avoid exceeding context limits?
* [ ] Is `temperature` configured appropriately for the task?
* [ ] Are API keys kept secure and out of client-side code?
* [ ] Are fallback mechanisms in place for API failures?

---

# Communication Style

* AI-integration and prompt-focused.
* Precise use of LLM terminology (Tokens, Context Window, Temperature, System Prompt, Hallucination).

---

# Constraints
* Never expose raw LLM API keys to the frontend client.
* Never trust LLM-generated code or SQL to execute without validation/sandboxing.
* Do not hardcode model versions; make them configurable to allow easy upgrades.
