import pytest
import project
from io import IOBase


def test_test_input():
    with pytest.raises(SystemExit):
        project.test_input("none.txt", None)
        project.test_input(None, None)


def test_get_output_file():
    assert isinstance(project.get_output_file("test.txt"), IOBase) == True


def test_getInput():
    with pytest.raises(SystemExit):
        project.get_input(None, "test.com", False)
