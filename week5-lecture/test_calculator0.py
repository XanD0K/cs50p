# This code has the purpose of test calculator.py, specifically, its square() function

from calculator import square

def main():
    test_square2()


def test_square():
    if square(2) != 4:
        print("2 square was not 4")
    if square(3) != 9:
        print("3 square was not 9")


if __name__ == "__main__":
    main()