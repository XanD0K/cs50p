# Modified that pset to allow multiple operations (addition, subtraction, multiplication and division)

import random
import operator

def main():
    total_questions = 10
    correct_answers = 0
    level = get_level()
    op = get_operator()

    for _ in range(total_questions):
        x, y, expected_answer = generate_integer(level, op)
        wrong_count = 0
        while wrong_count < 3:
            try:
                answer = int(input (f"{x} {op} {y} = "))
                if answer == expected_answer:
                    correct_answers += 1
                    break
                
                print("EEE")
                wrong_count += 1
            except ValueError:
                print("Enter a valid value!")

        if wrong_count == 3:
            print(f"{x} {op} {y} = {expected_answer}")

    print(f"Score: {correct_answers}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            print("Enter a valid level among 1, 2 and 3!")
        except ValueError:
            print("Enter a valid level among 1, 2 and 3!")


# Get operator used for the math problems
def get_operator():
    while True:    
        op = input("Operator: ")
        if op in ["+", "-", "*", "/"]:
            return op
        print("Enter a valid operator among '+', '-', '*', '/'")


# Generate problem's data based on chosen level and operator
def generate_integer(level, op):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(1 if op == "/" else 0, 9)

    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999) 

    # Change output for division to guarantee an integer as answer
    if op == "/":
        answer = random.randint(1, 10 ** level - 1)
        x = y * answer
        return x, y, answer 
    
    # Track which operation is going to be calculated, based on inputed operator
    used_op = {"+": operator.add, "-": operator.sub, "*": operator.mul}

    # Return the 2 values and the answer
    return x, y, used_op[op](x, y)

if __name__ == "__main__":
    main()