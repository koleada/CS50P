from um import count
import pytest


def test_1():
    assert count("yummy") == 0
    assert count("thats yummy") == 0


def test_2():
    assert count("hello, um, world") == 1
    assert count("Hello, um...") == 1


def test_3():
    assert count("um, um, um") == 3
    assert count("Um, thanks, um...") == 2
