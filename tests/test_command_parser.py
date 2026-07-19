"""
Tests for CommandParser.
"""

from core.command_parser import CommandParser


def test_parse_slash_command():
    parser = CommandParser()
    assert parser.parse("/chat hello") == ("chat", "hello")


def test_parse_no_slash():
    parser = CommandParser()
    assert parser.parse("hello") == ("chat", "hello")


def test_parse_with_spaces():
    parser = CommandParser()
    assert parser.parse("  /review core/kernel.py  ") == ("review", "core/kernel.py")


def test_parse_no_argument():
    parser = CommandParser()
    assert parser.parse("/info") == ("info", "")
