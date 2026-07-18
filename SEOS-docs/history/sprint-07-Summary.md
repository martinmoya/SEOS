## sprint 07 - Summary
Goal: Integrate basic Git operations into SEOS using the first real Skill, and fix a critical prompt leaking bug in the Prompt Engine.

## Milestone: M4 - Developer Skills

Status: ✅ Completed (v0.7.0)

Key Deliverables:

GitSkill wrapping CLI Git commands (status, add, commit, diff, log) via subprocess.
GitAgent orchestrating the skill via /git <command>.
Bugfix (Prompt Leaking): Updated LLM Providers to accept system messages. PromptService now separates Role/Rules from user input into system and user roles, preventing the LLM from reciting internal instructions.

## Next Step: Sprint 8 - Python Skills & Code Analysis (AST).