while True:
    try:
        n = int(input("How many 'meows'? "))
        if n <= 0:
            print("Please enter a positive number!")
            continue
        break
    except ValueError:
        print("Provide a valid number!")

# Used just for the 'while' loop
while_i = n

while while_i != 0 :
    print("meow!")
    while_i -= 1

print()

for _ in range(n):
    print("meow!")

print()

print("meow!\n" * n, end="")