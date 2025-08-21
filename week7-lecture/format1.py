import re


name = input("What's your name? ").strip()

# The '?' sign makes the whitespace opitional after the comma
# Could also use a '*' symbol instead to tolerate multiple spaces
matches = re.search(r"^(.+), ?(.+)$", name)

if matches:
    name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")