# Prints square of bricks using a function with a loop and str multiplication
def main():
    while True:
        try:
            blocks = int(input("How many blocks? "))
            if blocks <= 0:
                print("Enter a positive number!")
                continue
            break
        except ValueError:
            print("Provide a valid number!")
    print_square(blocks)


def print_square(size):
    for _ in range(size):
        print_row(size)


def print_row(width):
    print("#" * width)


main()
