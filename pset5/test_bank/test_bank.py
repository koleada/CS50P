from bank import value


def test_1():
    assert value("hello") == 0
    assert value("HELLO") == 0


def test_2():
    assert value("hey") == 20
    assert value("HEY") == 20


def test_3():
    assert value("greetings") == 100
    assert value("GREETINGS") == 100
