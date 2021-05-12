import pytest
from Calculator import Calculator


def test_add():
    assert Calculator.add(5, 5) == 10
    assert Calculator.add(-2, 5) == 3
    assert Calculator.add(0, 5) == 5
    x = 5
    assert Calculator.add(x, x) == 10
    assert Calculator.add(10.5, 5) == 15.5
    with pytest.raises(TypeError):
        Calculator.add("sda", 5)
        Calculator.add("4", 5)
        Calculator.add(None, 5)
        Calculator.add({}, 5)
        Calculator.add([1, 2], 5)


def test_subtract():
    assert Calculator.subtract(5, 5) == 0
    assert Calculator.subtract(-2, 5) == -7
    assert Calculator.subtract(0, 5) == -5
    x = 5
    assert Calculator.subtract(x, x) == 0
    assert Calculator.subtract(10.5, 5) == 5.5
    with pytest.raises(TypeError):
        Calculator.subtract("sda", 5)
        Calculator.subtract("4", 5)
        Calculator.subtract(None, 5)
        Calculator.subtract({}, 5)
        Calculator.subtract([1, 2], 5)


def test_multiply():
    assert Calculator.multiply(3, 5) == 15
    assert Calculator.multiply(-2, 5) == -10
    assert Calculator.multiply(0, 5) == 0
    x = 5
    assert Calculator.multiply(x, x) == 25
    assert Calculator.multiply(10.5, 5) == 52.5
    assert Calculator.multiply("sda", 5) == "sdasdasdasdasda"
    assert Calculator.multiply("4", 5) == "44444"
    assert Calculator.multiply([1, 2], 5) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
    with pytest.raises(TypeError):
        Calculator.multiply(None, 5)
        Calculator.multiply({}, 5)


def test_divide():
    assert Calculator.divide(10, 5) == 2
    assert Calculator.divide(-10, 5) == -2
    assert Calculator.divide(0, 5) == 0
    x = 5
    assert Calculator.divide(x, x) == 1
    assert Calculator.divide(10, 0.5) == 20
    with pytest.raises(ValueError):
        Calculator.divide(10, 0)
    with pytest.raises(TypeError):
        Calculator.divide("sda", 5)
        Calculator.divide("4", 5)
        Calculator.divide([1, 2], 5)
        Calculator.divide(None, 5)
        Calculator.divide({}, 5)