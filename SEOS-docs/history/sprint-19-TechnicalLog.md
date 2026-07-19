## Sprint 19 - Technical Log
Architecture Decisions (ADRs)

## ADR-037: PyPA Standard Packaging. The project uses pyproject.toml (setuptools backend) to define dependencies and entry points, replacing the need for setup.py.

## ADR-038: CLI Entry Point. The seos command maps directly to main:main, allowing the application to be executed from any working directory context.

## Files Created
Dockerfile
.dockerignore
pyproject.toml

## Files Modified
main.py: Ensured main() function is explicitly defined for the entry point.
