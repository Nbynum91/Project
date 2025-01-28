from project import function_1, function_2, function_3
import pytest


def main():
    """runs various pytests"""
    test_function_1()
    test_function_2()
    test_function_3()


def test_function_1():
    """tests number format for menu options"""
    with pytest.raises(ValueError):
        function_1(0)
    with pytest.raises(ValueError):
        function_1(5)
    with pytest.raises(ValueError):
        function_1("one")


def test_function_2():
    """tests number format for input options"""
    with pytest.raises(ValueError):
        function_1(0)
    with pytest.raises(ValueError):
        function_1(5)
    with pytest.raises(ValueError):
        function_1("one")



def test_function_3():
    """tests name format for csv dictionary"""
    assert function_3("BoB ") == "BoB "
    assert function_3("BoB") == "BoB"
    assert function_3("bob") == "bob"
    with pytest.raises(OSError):
        function_3("123")


if __name__ == "__main__":
    main()
