import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from main import parse_command, execute_command


def test_empty_command():
    command, args = parse_command("")
    assert command is None
    assert args == []


def test_ls_command():
    command, args = parse_command("ls")
    assert command == "ls"
    assert args == []


def test_command_with_arguments():
    command, args = parse_command("ls file.txt test.txt")
    assert command == "ls"
    assert args == ["file.txt", "test.txt"]


def test_environment_variable():
    command, args = parse_command("ls $USERPROFILE")
    assert command == "ls"
    assert args[0] == os.environ.get("USERPROFILE", "$USERPROFILE")


def test_unknown_command():
    result = execute_command("unknown", [])
    assert result is True


def test_exit():
    result = execute_command("exit", [])
    assert result is False


def test_exit_with_arguments():
    result = execute_command("exit", ["test"])
    assert result is True
