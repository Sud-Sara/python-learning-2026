from bank import value

def test_value_hello():
    assert value("Hello")==(0)

def test_value_hi():
    assert value("Hi")==(20)

def test_value_who():
    assert value("Who")==(100)


