from plates import is_valid


def test_1():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False
    assert is_valid("5C") == False
    assert is_valid("C5") == False
    assert is_valid("22") == False
    assert is_valid("FF") == True


def test_2():
    assert is_valid("kole0724") == False
    assert is_valid("kol") == True
    assert is_valid("k") == False


def test_3():
    assert is_valid("AAA22A") == False
    assert is_valid("AAA222") == True
    assert is_valid("A22AA") == False
    assert is_valid("AA0AA") == False
    assert is_valid("AAAA0A") == False
    assert is_valid("A02AA") == False
    assert is_valid("A00AA") == False
    assert is_valid("AA000A") == False
    assert is_valid("AA0AA") == False
    assert is_valid("AAA0") == False


def test_4():
    assert is_valid("kole!") == False
    assert is_valid("kole.") == False
    assert is_valid(".kole.") == False
