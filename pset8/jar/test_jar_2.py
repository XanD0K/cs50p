# Tests using pytest

import pytest

from jar import Jar


def test_init_default_capacity():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_init_custom_capacity():
    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0


def test_init_negative_capacity():
    with pytest.raises(ValueError):
        Jar(-1)


def test_str_empty():
    jar = Jar()
    assert str(jar) == ""


def test_str_with_cookies():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪" * 3


def test_deposit_valid():
    jar = Jar(5)
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(3)
    assert jar.size == 5


def test_deposit_negative():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(-1)


def test_deposit_over_capacity():
    jar = Jar(5)
    jar.deposit(3)
    with pytest.raises(ValueError):
        jar.deposit(3)


def test_withdraw_valid():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3


def test_withdraw_negative():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(-1)


def test_withdraw_too_many():
    jar = Jar()
    jar.deposit(2)
    with pytest.raises(ValueError):
        jar.withdraw(3)


def test_capacity_read_only():
    jar = Jar()
    with pytest.raises(AttributeError):
        jar.capacity = 20
        

def test_size_read_only():
    jar = Jar()
    with pytest.raises(AttributeError):
        jar.size = 5