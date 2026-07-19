## Sprint 15 - Technical Log
Architecture Decisions (ADRs)
ADR-030: Optional API Tokens. Settings now supports a get_optional method for environment variables that are not strictly required for the core application to run (like GITHUB_TOKEN).

ADR-031: Graceful API Error Handling. GithubSkill catches GithubException and returns the API error message directly to the user, preventing the application from crashing due to external API failures (e.g., 403 Forbidden or 404 Not Found).

## Files Created
skills/github_skill.py
agents/github_agent.py

## Files Modified
config/settings.py: Added GITHUB_TOKEN reading.
core/kernel.py: Registered GithubAgent.
requirements.txt: Added PyGithub.
