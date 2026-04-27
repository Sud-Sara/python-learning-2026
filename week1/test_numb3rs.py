import numb3rs
import pytest

def test_convert():
    assert numb3rs.validate("255.255.255.255")== True
    assert numb3rs.validate("0.0.0.0")== True
    assert numb3rs.validate("1.11.111.2")== True
    assert numb3rs.validate("")== False
    assert numb3rs.validate("256.256.256.256")== False
    assert numb3rs.validate("255.256.255.255")== False
    assert numb3rs.validate("A.2.255.25")== False
    assert numb3rs.validate("001.2.255.25")== False
