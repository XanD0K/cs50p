import random

def main():
    level = get_level()
    rand_num = random.randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))
            if not guess > 0:
                continue
            if guess > rand_num:
                print("Too large!")
                continue
            elif guess < rand_num:
                print("Too small!")
                continue
            print("Just right!")
            break
        except ValueError:
            print("Provide a positive integer!")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if not level > 0:
                print("Enter a positive number!")
                continue
            return level
        except ValueError:
            print("Provide a positive integer!")


if __name__ == "__main__":
    main()
