from twttr import shorten


def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("WORD") == "WRD"
    assert shorten("kole") == "kl"
    assert shorten("kole1") == "kl1"
    assert shorten("test!") == "tst!"
