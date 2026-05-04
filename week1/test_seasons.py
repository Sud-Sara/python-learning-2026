from seasons import get_DOB
from datetime import date
import pytest

def test_get_DOB1():
    assert get_DOB("2000-12-31") == date(2000, 12, 31)

def test_get_DOB2():
    with pytest.raises(SystemExit):
        get_DOB("9-5")








