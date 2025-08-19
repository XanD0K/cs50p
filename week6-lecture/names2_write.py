name = input("What's your name? ").strip().title()
if not name:
    pass

# By using 'with', It automatically closes the file
with open("names2.txt", "a") as file:
    file.write(f"{name}\n")