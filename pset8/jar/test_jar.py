from jar import Jar
import pytest

myjar = Jar(15)


def test_cap():

    assert myjar.capacity == 15
    assert myjar.size == 0


def test_deposit():
    myjar.deposit(2)
    assert myjar.size == 2
    myjar.deposit(10)
    assert myjar.size == 12
    with pytest.raises(ValueError):
        myjar.deposit(4)


def test_withdraw():
    newjar = Jar(10)
    newjar.deposit(3)
    newjar.withdraw(3)
    assert newjar.size == 0
    with pytest.raises(ValueError):
        newjar.withdraw(3)


def test_str():
    newjar = Jar()
    newjar.deposit(5)
    newjar.__str__() == "🍪🍪🍪🍪🍪"
    newjar.withdraw(2)
    newjar.__str__ == "🍪🍪🍪"
