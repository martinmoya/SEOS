Sprint 02 - Technical Log
Architecture Decisions (ADRs)
ADR-003 (Implicit): Workspace as Root Context. The Workspace object manages opened projects, and WorkspaceService handles the use cases. AgentContext exposes the active project via workspace_service.

ADR-004 (Implicit): BaseProjectAgent Pattern. Agents that require file system access must inherit from BaseProjectAgent and call require_project() to ensure a workspace is open.

Files Created
core/project.py
core/workspace.py
services/workspace_service.py
agents/base_project_agent.py
agents/open_agent.py, agents/info_agent.py, agents/tree_agent.py, agents/find_agent.py

Files Modified
core/agent_context.py: Injected WorkspaceService and added project property.
core/kernel.py: Initialized WorkspaceService, opened Path.cwd() by default, and registered new agents.

Key Implementations
Directory Exclusion: /tree and /find automatically ignore .git, .venv, __pycache__, and logs.
Graceful Degradation: BaseProjectAgent catches missing project contexts and returns a user-friendly message instead of crashing.
