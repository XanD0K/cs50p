# Returns n sheep from helper function


def main():
    n = int(input("What's n? "))
    for i in range(n):
        print(sheep(i + 1)) # The +1 skips the blank line and count up to the range number


def sheep(n):
    return "🐑" * n


if __name__ == "__main__":
    main()
