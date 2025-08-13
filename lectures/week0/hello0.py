# Ask user for their name
name = input("What's your name? ").strip().title()

# Polish 'name' variable
# .strip() → remove whitespace to the left and to right of a string 
# .capitalize() → capitalize first letter of the first word
# .title() → capitalize the first letter of each word

# Say hello to user
print("hello, " + name)
print("hello,", name) # With multiple arguments, the space is automatically added (sep=" ")
print(f"hello, {name}")

# Remove the default "new line" from print() function
print("hello, ", end="") # The default value is '\n'
print(name)

# Split user's name into first and last name
first, last = name.split(" ")

print(f"hello, {first}")
print(f"hello, {last}")