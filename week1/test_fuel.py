import fuel
import pytest

def test_convert():
    assert fuel.convert("1/2")== 50
    assert fuel.convert("1/1")== 100
    with pytest.raises(ZeroDivisionError):
        fuel.convert("0/0")
    with pytest.raises(ValueError):
        fuel.convert("2/1")
    with pytest.raises(ValueError):
        fuel.convert("-1/1")

def test_gauge():
    assert fuel.gauge(1)== "E"
    assert fuel.gauge(99)== "F"
    assert fuel.gauge(10)== "10%"
    



