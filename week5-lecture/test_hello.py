# This code has the purpose of test hello.py, specifically the hello() function

from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    for name in ["Hermione", "Harry", "Ron", "Draco"]:
        assert hello(name) == f"hello, {name}"
