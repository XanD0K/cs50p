import re


name = input("What's your name? ").strip()

# (.+) → The parentheses are being used for capturing purpose
# Everything inside the parentheses will be returned from re.search as a return value and will be assigned to a variable (in this case, 'matches')
matches = re.search(r"^(.+), (.+)$", name)

if matches:
    last = matches.group(1)
    first = matches.group(2)

    name = f"{first} {last}"

    # Another way of getting the returned values:
    # last, first = matches.groups()

 

print(f"hello, {name}")