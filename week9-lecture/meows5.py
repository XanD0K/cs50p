# Adds docstring to function
# It standardizes how to document your functions and other aspects of your code
# In Python's ecosystem there are a lot of tools to analyze the code,
# extract these docstrings and generate webpages/pdfs for your own functions


def meow(n: int) -> str:
    """Meow n times."""
    return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")
