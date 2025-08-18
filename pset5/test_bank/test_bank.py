# This code has the purpose of testing value() function from "bank.py" file

from bank import value

# Test words that start with 'hello', lower and upper case
def test_hello():
    assert value("hello, how are you?") == 0
    assert value("Hello my friend!") == 0
    assert value("HeLlOoOoOoO") == 0
    assert value("heLLo, HEllO") == 0


# Test words that start with the letter 'h besides 'hello', lower and upper case
def test_h():
    assert value("Hi! How are you?") == 20
    assert value("Hey my friend!") == 20
    assert value("Hola!") == 20
    assert value("How you doing?") == 20


# Test words that start with any letter besides 'h', lower and uppercase
    assert value("What's happening?") == 100
    assert value("I'm at a place called Vertigo!") == 100
    assert value("I'm not in a good mood today!") == 100
