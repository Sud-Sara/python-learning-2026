import pytest
import project


def test_function_1():
    assert project.function_1("1/1")== 100
    with pytest.raises(ZeroDivisionError):
        project.function_1("0/0")


def test_function_2():
    ...


def test_function_n():
    ...