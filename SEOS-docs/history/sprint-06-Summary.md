Sprint 06 - Summary
Goal: Integrate the knowledge base into LLM calls via a PromptService that injects Roles and Rules, allowing users to switch personalities dynamically.

Milestone: M3 - Knowledge Core

Status: ✅ Completed (v0.6.0)

Key Deliverables:

PromptService to build dynamic prompts (Role + Global Rules + User Query).
RoleAgent implementing the /role command.
Users can now activate, query, and clear roles (e.g., /role software_architect).
ChatAgent now routes queries through the PromptService instead of sending raw text.
Next Step: Sprint 7 - Developer Skills (Git Integration).
