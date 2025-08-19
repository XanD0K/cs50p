# This file has the purpose of checking convert() and gauge() functions from 'test_fuel.py' file

from fuel import convert, gauge
import pytest

# Check for division by zero
def test_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
        convert("0/0")


# Check if nominator is higher than denominator
def test_higher_nominator():
    with pytest.raises(ValueError):
        convert("2/1")
        convert("4/3")
        convert("10/5")


# Check if any value is a negative value
def test_negative():
    with pytest.raises(ValueError):
        convert("-1/2")
        convert("-5/10")


# Check for string fractions:
def test_str():
    with pytest.raises(ValueError):
        convert("one/two")
        convert("apple/banana")


# Check for decimal values
def test_decimal():
    with pytest.raises(ValueError):
        convert("3.4/4")
        convert("1/2.5")


# Check for integers
def test_no_fraction():
    with pytest.raises(ValueError):
        convert("25")
        convert("50")
        convert("0")
        convert("100")


# Check for correct fraction input
def test_correct_fraction():
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/100") == 1
    assert convert("100/100") == 100


# Check for "E" out put
def test_low_fuel():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


# Check for "F" output
def test_high_fuel():
    assert gauge(100) == "F"
    assert gauge(99) == "F"


# Check for numeric percentage output
def test_numeric_gauge():
    assert gauge(50) == "50%"
    assert gauge(44) == "44%"
    assert gauge(19) == "19%"
    assert gauge(77) == "77%"