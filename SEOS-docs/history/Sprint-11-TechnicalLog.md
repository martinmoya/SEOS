## Sprint 11 - Technical Log
Architecture Decisions (ADRs)
ADR-022: Safe Refactoring. RefactoringEngine uses ast.parse() to validate LLM output before overwriting any files. If the LLM returns broken Python, the operation is aborted, protecting the user's codebase.

ADR-023: Test File Naming Convention. Generated tests are saved with a test_ prefix in the same directory as the source file (e.g., test_chat_agent.py).

## Files Created
services/refactoring_engine.py
services/test_generator.py
agents/refactor_agent.py
agents/gentest_agent.py

## Files Modified
core/kernel.py: Registered RefactorAgent and GenTestAgent.
