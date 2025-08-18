def main():
    name = input("What's your name? ").strip().title()
    print (hello(name))


# Define function to say hello. Default value set to "world"
def hello(to="world"):
    return f"hello, {to}"


if __name__ == "__main__":
    main()