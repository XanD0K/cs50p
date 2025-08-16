# Check __name__


def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")


# '__name__' is a special variable whose value is automatically set by Python to be "main" when you run a file from the command line
# If prevents running main() when importing a module from this file into another file (e.g. say5.py)
if __name__ == "__main__":
    main()
