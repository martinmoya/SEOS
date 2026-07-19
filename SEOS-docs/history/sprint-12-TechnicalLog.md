## Sprint 12 - Technical Log
Architecture Decisions (ADRs)
ADR-024: Prompt-Based Code Analysis. CodeReviewer uses a strict Senior Engineer persona to evaluate code. This allows for semantic understanding of bugs rather than just regex-based static analysis.

ADR-025: Deployment Artifacts. DeploymentGenerator is designed to return raw configuration files (Dockerfiles) without markdown, ready to be saved directly to the project root.

## Files Created
services/code_reviewer.py
services/deployment_generator.py
agents/review_agent.py
agents/deploy_agent.py

## Files Modified
core/kernel.py: Registered ReviewAgent and DeployAgent.
