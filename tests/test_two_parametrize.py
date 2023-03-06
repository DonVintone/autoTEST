# test_expectation.py Передача значений аргументов тесту декоратором.
import pytest


@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [(0, 5, 0), (1, 5, 5), (2, 5, 10), (-1, 5, -15), (-4, -5, 25) ]
)
def test_multiplication(a, b, expected):
    assert a * b == expected
