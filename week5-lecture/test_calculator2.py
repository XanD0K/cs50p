# Problem with all those tests, is that they end up being overkill to test a 2 line function
# To solve this problem, we can use third party programs that will do a "unit test", an automated testing units/functions of a code
# We'll focus on "pytest"

from calculator import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0

# On terminal, just run 'pytest test_calculator2.py'
# It will automate the process of try-except and catch and print errors
# It will stops on the first fail