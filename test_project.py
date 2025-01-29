from project import function_1, function_2, function_3
import pytest

def main():
    """runs various pytests"""
    test_function_1()
    test_function_2()
    test_function_3()

def test_function_1():
    """tests number format to pull menu options from menu.csv"""
    with pytest.raises(ValueError):
        function_1(0)
    with pytest.raises(ValueError):
        function_1(5)
    with pytest.raises(ValueError):
        function_1("one")
    assert function_1(1) != ValueError
    assert function_1(2) != ValueError
    assert function_1(3) != ValueError
    assert function_1(4) != ValueError

def test_function_2():
    """tests input for game command using function_1(1)"""
    assert function_2(function_1(1), "new game") == "New game"
    assert function_2(function_1(1), "help") == "Type command from menu into input as seen"
    assert function_2(function_1(1), "anything else") == "InputError: Type command from menu into input as seen"
    with pytest.raises(SystemExit) as sample:
        function_2(function_1(1), "quit")
        assert sample.type == SystemExit
        assert sample.value.code == 1
    """tests input for game command using function_1(2)"""
    assert function_2(function_1(2), "new game") == "New game"
    assert function_2(function_1(2), "continue") == "Continue"
    assert function_2(function_1(2), "help") == "Type command from menu into input as seen"
    assert function_2(function_1(2), "anything else") == "InputError: Type command from menu into input as seen"
    with pytest.raises(SystemExit) as sample:
        function_2(function_1(2), "quit")
        assert sample.type == SystemExit
        assert sample.value.code == 1
    """tests input for game command using function_1(3)"""
    assert function_2(function_1(3), "fight") == "Fight"
    assert function_2(function_1(3), "help") == "Type command from menu into input as seen"
    assert function_2(function_1(3), "anything else") == "InputError: Type command from menu into input as seen"
    with pytest.raises(SystemExit) as sample:
        function_2(function_1(3), "quit")
        assert sample.type == SystemExit
        assert sample.value.code == 1
    """tests input for game command using function_1(4)"""
    assert function_2(function_1(4), "attack") == "Attack"
    assert function_2(function_1(4), "run") == "Run"
    assert function_2(function_1(4), "help") == "Type command from menu into input as seen"
    assert function_2(function_1(4), "anything else") == "InputError: Type command from menu into input as seen"
    with pytest.raises(SystemExit) as sample:
        function_2(function_1(4), "quit")
        assert sample.type == SystemExit
        assert sample.value.code == 1




def test_function_3():
    """tests name format for Player Name to be entered into saved_game.csv"""
    assert function_3("BoB the Builder") == "BoB the Builder"
    with pytest.raises(OSError):
        function_3("123")

if __name__ == "__main__":
    main()
