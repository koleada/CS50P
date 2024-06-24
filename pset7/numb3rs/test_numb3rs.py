from numb3rs import validate
import pytest


def test_1():
    assert validate("cat") == False
    assert validate("dog") == False


def test_2():
    assert validate("1.2.3.1000") == False
    assert validate("512.512.512.512") == False
    assert validate("255.255.255.255") == True
    assert validate("75.456.76.65") == False
