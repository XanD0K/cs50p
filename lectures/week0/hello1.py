# It is necessary to define main() to use a function that is defined later in the code
def main():
    hello()
    name = input("What's your name? ").strip().title()
    hello(name)


# Define function to say hello. Default value set to "world"
def hello(to="world"):
    print(f"hello, {to}")

# Call the main function
main()