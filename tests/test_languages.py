"""
Tests for Language Resolver.
"""

import pytest
from core.languages import resolve_language


def test_resolve_valid_code():
    assert resolve_language("es") == "Spanish"


def test_resolve_valid_name():
    assert resolve_language("English") == "English"


def test_resolve_case_insensitive():
    assert resolve_language("FRENCH") == "French"


def test_resolve_invalid():
    with pytest.raises(ValueError):
        resolve_language("xyz")
