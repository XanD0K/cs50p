# We can improve the design of that test function by segregating it into different categories

from calculator import square
import pytest


def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negartive():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


# Checks fro str's errors. We don't use 'assert 'for that, but pytest's raises() function
def test_str():
    with pytest.raises(TypeError): # The argument is the expected type of error
        square("cat")

# All of those functions will be run automatically
# If one of them fails, the others will be attempted