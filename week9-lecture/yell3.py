# Uses map → it applies a function to every element of a sequence


def main():
    yell("This", "is", "CS50")


def yell(*words): # Variable number of words being passed in
    uppercased = map(str.upper, words)
    print(*uppercased)


if __name__ == "__main__":
    main()
