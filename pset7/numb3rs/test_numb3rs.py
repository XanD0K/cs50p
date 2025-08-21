from numb3rs import validate
import pytest


# Check for numbers outside of the range (0-255)
def test_range():
    assert validate("0.0.0.-1") == False
    assert validate("-255.-255.-255.-255") == False
    assert validate("256.0.0.0") == False
    assert validate("0.0.0.999") == False
    assert validate("275.3.6.28") == False


# Check for alphabetical characters
def test_str():
    assert validate("pen.pineapple.apple.pen") == False
    assert validate("cs50.0.0.0") == False


# Check for leading zeros
def test_zero():
    assert validate("001.0.0.0") == False
    assert validate("0.1.01.001") == False


# Check invalid format
def test_format():
    assert validate("0") == False
    assert validate("0.0") == False
    assert validate("0.0.0") == False
    assert validate("0,0,0,0") == False
    assert validate("0.0.0.0.") == False
    assert validate("0.0.0.0.0") == False