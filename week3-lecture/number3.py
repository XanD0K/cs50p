# Adds prompt

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass # Catch the exception, but silently "ignore" it


if __name__ == "__main__":
    main()
