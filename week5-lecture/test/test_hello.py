# This code has the purpose of test hello.py, specifically the hello() function
# It demonstrates that third party unit test programs also allow testing multiple files inside a folder

from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("David") == "hello, David"

# To run a pytest in a file inside a folder, inside that folde I need to create an '__init__.py' file
# That file tells Python to treat that folder not as a folder, but as a package
# A package is a Python module(s) that are organized inside of a folder

# Instead of running pytest on a file, you run it on the folder py runnig 'pytest test'