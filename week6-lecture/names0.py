names = []

for _ in range(3):
    names.append(input("What's your name? ").strip().title())


for name in sorted(names):
    print(f"hello, {name}")


# Problem with this approach is that all names will be lost when program ends