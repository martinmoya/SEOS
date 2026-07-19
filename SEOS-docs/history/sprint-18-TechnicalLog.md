## Sprint 18 - Technical Log
Architecture Decisions (ADRs)
## ADR-036: Isolated Test Suite. pytest.ini sets testpaths = tests to prevent pytest from accidentally trying to collect SEOS agents (like TestAgent) as unit tests, keeping the test execution clean and fast.

## Files Created
tests/__init__.py
tests/test_command_parser.py
tests/test_languages.py
tests/test_python_analyzer.py
pytest.ini

## Files Modified
requirements.txt: Added pytest.
