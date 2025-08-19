with open("names2.txt", "r") as file: # And reading, "r" method is opitional
    # readlines() method reads all lines of the file at once, returning them as a list
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip()) # .rstrip() eliminates the new line at the end

print()

# Another way to do this:
with open("names2.txt") as file:
    for line in file:
        print("hello,", line.strip())
# Downside: it doesn't allow to sort the elements before printing

print()

# To do that, we first need to load all names into memory:
# It also allows to make changes to that data before printing
names = []

with open("names2.txt") as file:
    for line in file:
        names.append(line.strip())

for name in sorted(names):
    print(f"hello, {name}")

print()

# Another simpler way to do that:
with open("names2.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())

print()

# Reverse sorted
with open("names2.txt") as file:
    for line in sorted(file, reverse=True):
        print("hello,", line.rstrip())