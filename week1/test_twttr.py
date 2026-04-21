from twttr import shorten

def test_shorten():
    assert shorten("Hi")==("H")
    assert shorten("who")==("wh")
    assert shorten("Oh, you")==("h, y")
    assert shorten("1 world")==("1 wrld")


