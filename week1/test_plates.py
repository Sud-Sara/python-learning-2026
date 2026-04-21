from plates import is_valid

def test_is_valid1():
    assert is_valid("CS50")==True

def test_is_valid2():
    assert is_valid("CS-50")==False

def test_is_valid3():
    assert is_valid("5050")==False

def test_is_valid4():
    assert is_valid("CS50CS")==False

def test_is_valid5():
    assert is_valid("CS050")==False

def test_is_valid6():
    assert is_valid("C")==False

