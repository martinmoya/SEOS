## Sprint 08 - Technical Log

## Architecture Decisions (ADRs)
ADR-015: AST-based Code Analysis. SEOS uses Python's native ast module to parse source files rather than regex. This guarantees 100% accurate symbol extraction (Classes, Methods, Functions) regardless of formatting.

ADR-016: Subprocess Testing. PythonSkill invokes pytest via subprocess to ensure test execution is isolated from the main SEOS process.

## Files Created
analyzers/python_analyzer.py
skills/python_skill.py
agents/symbols_agent.py
agents/test_agent.py

## Files Modified
core/kernel.py: Registered SymbolsAgent and TestAgent.
