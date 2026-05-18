"""
tests/test_calculator.py — unit tests for calculator module
"""
import pytest
from calculator import add, subtract, multiply, divide


def test_add_positive():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, -4) == -5


def test_add_zero():
    assert add(0, 100) == 100


def test_subtract():
    assert subtract(10, 4) == 6


def test_subtract_negative_result():
    assert subtract(3, 7) == -4


def test_multiply():
    assert multiply(4, 5) == 20


def test_multiply_by_zero():
    assert multiply(99, 0) == 0


def test_divide():
    assert divide(10, 2) == 5.0


def test_divide_float():
    assert divide(7, 2) == 3.5


def test_divide_by_zero_raises():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)
