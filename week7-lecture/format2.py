import re


name = input("What's your name? ").strip()

# := is known as the 'walrus operator'
# Besides assigning the result of 're.search()' to 'matches', it also asks a boolean question (if/elif/while)
if matches := re.search(r"^(.+), (.+)$", name):
    name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")