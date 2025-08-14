# Permanently prompts the user for a valid input
while True:
    try:
        camel_variable = input("camelCase: ")
        if camel_variable.strip() == "":
            print("Enter a text before submitting")
            continue
        break
    except ValueError:
        print("Enter a valid text")


# Use list comprehension to search any uppercase character and replace it with the newer version
snake_variable = "".join(f"_{c.lower()}" if c.isupper() else c for c in camel_variable)

print(snake_variable)


# Another way (more explicit) of doing that for loop
"""
for character in camel_variable:
    if character.isupper():
        character = character.replace(character, f"_{character.lower()}")
    snake_variable += character
"""
