## Contributing to SEOS
First off, thank you for taking the time to contribute! 🚀

The following is a set of guidelines for contributing to SEOS. These are mostly guidelines, not rules. Use your best judgment, and propose changes to this document in a pull request.

## Code of Conduct
This project and everyone participating in it is governed by the Code of Conduct. By participating, you are expected to uphold this code.

## Development Process
Fork the repo and create your branch from master.
If you've added code that should be tested, add tests in the tests/ folder.
Ensure the test suite passes (pytest).
Make sure your code lints (PEP 8).
Issue that pull request!

## Architecture Guidelines
SEOS follows a strict Clean Architecture. Please adhere to these rules:

agents/: CLI Command handlers (orchestration only, no business logic).
services/: Business logic and use cases.
skills/: Reusable system operations.
providers/: LLM implementations.
core/: Fundamental infrastructure (Kernel, Workspace, Settings).

## Code Style
All code, comments, logs, and documentation must be in English.
Use type hints in all Python functions.

## CODE_OF_CONDUCT.md (NUEVO)

## Contributor Covenant Code of Conduct

## Our Pledge
We as members, contributors, and leaders pledge to make participation in ourcommunity a harassment-free experience for everyone, regardless of age, bodysize, visible or invisible disability, ethnicity, sex characteristics, genderidentity and expression, level of experience, education, socio-economic status,nationality, personal appearance, race, religion, or sexual identityand orientation.

## Our Standards
Examples of behavior that contributes to a positive environment for ourcommunity include:

Demonstrating empathy and kindness toward other people
Being respectful of differing opinions, viewpoints, and experiences
Giving and gracefully accepting constructive feedback

Examples of unacceptable behavior include:

The use of sexualized language or imagery, and sexual attention or advances
Trolling, insulting or derogatory comments, and personal or political attacks
Public or private harassment

## Enforcement Responsibilities
Community leaders are responsible for clarifying and enforcing our standards ofacceptable behavior.

## Scope
This Code of Conduct applies within all community spaces, and also applies whenan individual is officially representing the community in public spaces.

## Enforcement
Instances of abusive, harassing, or otherwise unacceptable behavior may bereported to the community leaders responsible for enforcement atmartinmoya@example.com. All complaints will be reviewed and investigated promptly and fairly.

## Attribution
This Code of Conduct is adapted from the Contributor Covenant.
