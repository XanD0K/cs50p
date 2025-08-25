# Uses Sphinx docstring format
# That block of code is a convention known as "reestructured text" used for documentation
# It can also be used to pass sample inputs and outputs to your functions
# You can then use a tool to run the code with those samples and check for bugs


def meow(n: int) -> str:
    """
    Meow n times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n


number:int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")
