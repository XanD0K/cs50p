import random

def main():
    total_question = 10
    correct_answers = 0
    level = get_level()

    for _ in range(total_question):
        x = generate_integer(level)
        y = generate_integer(level)
        wrong_count = 0
        while wrong_count < 3:
            try:
                answer = int(input (f"{x} + {y} = "))
                if answer >= 0:
                    if answer == (x + y):
                        correct_answers += 1
                        break
                    else:
                        print("EEE")
                        wrong_count += 1
                else:
                    print("Enter a positive integer")
                    continue
            except ValueError:
                print("Enter a positive integer")

        if wrong_count == 3:
            print(f"{x} + {y} = {x + y}")

    print(f"Score: {correct_answers}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:
                print("Enter a valid level among 1, 2 and 3!")
                continue
            return level
        except ValueError:
            print("Enter a valid level among 1, 2 and 3!")


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
    elif level == 2:
         x = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
    return x


if __name__ == "__main__":
    main()