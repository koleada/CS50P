import fuel
import pytest


#
#
def test_convert():
    assert fuel.convert("1/2") == 50
    assert fuel.convert("1/3") == 33
    assert fuel.convert("1/4") == 25
    with pytest.raises(ValueError):
        fuel.convert("5/1")
        fuel.convert("one/four")
    with pytest.raises(ZeroDivisionError):
        fuel.convert("2/0")


def test_gauge():
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(75) == "75%"
    assert fuel.gauge(25) == "25%"
