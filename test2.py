from calculator import Calculator, CalculatorError
import pytest

def test_multiply():
    calculator = Calculator()
    result = calculator.multiply(3,3)
    assert result == 9

def test_divide():
    calculator = Calculator()
    result = calculator.divide(9,3)
    assert result == 3

def test_add():
    calculator = Calculator()
    result = calculator.add(9,3)
    assert result == 12

def test_sub():
    calculator = Calculator()
    result = calculator.subtract(9,3)
    assert result == 6

def test_divide_by_zero():
    calculator = Calculator()
    with pytest.raises(CalculatorError):
        result = calculator.divide(9, 0)