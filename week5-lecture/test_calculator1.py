# This code has the purpose of test calculator.py, specifically, its square() function

from calculator import square

def main():
    test_square()


# Use 'assert' keyword, which allows to assert that something is True. 
# If it is, nothing's gonna happen. If something is wrong, than an AssertionError will appear
def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 square was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 square was not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 square was not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 square was not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 square was not 0")
        

if __name__ == "__main__":
    main()