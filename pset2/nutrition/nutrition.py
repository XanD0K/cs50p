FRUIT = {
    "apple": "130",
    "avocado": "50",
    "banana": "110",
    "cantaloupe": "50",
    "grapefruit": "60",
    "grapes": "90",
    "honeydew melon": "50",
    "kiwifruit": "90",
    "lemon": "15",
    "lime": "20",
    "nectarine": "60",
    "orange": "80",
    "peach": "60",
    "pear": "100",
    "pineapple": "50",
    "plums": "70",
    "strawberries": "50",
    "sweet cherries": "100",
    "tangerine": "50",
    "watermelon": "80"
}


while True:
    try:
        fruit = input("Fruit: ").strip().lower()
        if fruit.strip() == "":
            print("Enter a fruit name before submitting")
            continue
        break
    except ValueError:
        print("That's not a valid name! Try again")

if not fruit in FRUIT:
    print("That's not a valid fruit name!")
else:
    print(FRUIT[fruit])