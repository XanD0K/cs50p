# Prints 'None' because line 10-11 mistakes meow() as having a return value


def meow(n: int) -> None:
    for _ in range(n):
        print("meow")


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)


# -> is a type hint used to indicate the return value of a function
# When a function doesn't return a value (e.g. meow()), it's default return is set to None