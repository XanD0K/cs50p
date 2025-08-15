MENU = {    
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    total = get_food("Item: ")
    if total == 0:
        print("Come back when you get hungry!")
    else:
        print(f"Total: ${total:.2f}")


def get_food(prompt):
    total_cost = 0
    while True:
        try:
            item = input(prompt).title().strip()
            if item not in MENU:
                print("Item not available!")
                continue
            total_cost += MENU[item]
            print(f"Total: ${total_cost:.2f}")
        except (EOFError, KeyboardInterrupt):
            print()
            return total_cost


if __name__ == "__main__":
    main()