import re


email = input("What's your email? ").strip()

# 'r' → tells Python to interpret that string as a raw string, so that the backslash ('\') isn't misinterpreted
# The outers '^' and '$' sings determ the start and the end of the string
if re.search(r"^.+@.+\.edu$", email):
    print("Valid 1")
else:
    print("Invalid 1")

# [^@]+ → One or more of any characters except the '@' sign
if re.search(r"^[^@]+@[^@]+\.edu$", email):
    print("Valid 2")
else:
    print("Invalid 2")

# [a-zA-Z0-9_] → specifies a set of characters to be typed in
if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print("Valid 3")
else:
    print("Invalid 3")

# Some of those patterns are so common that there are built-in shortcuts for representing its iformation
# \w → represents a "word character", which include alphanumeric charaters and the underscore
# (com|edu|gov|net|org) → 'com' OR 'edu' OR 'gov' OR 'net' OR 'org'
if re.search(r"^\w+@\w+\.(com|edu|gov|net|org)$", email):
    print("Valid 4")
else:
    print("Invalid 4")

# 're.IGNORECASE' → makes re.search() be case insensitive
# Could achieve the same result by adding .lower() to the input or to the 'email' parameter of the re.search() function
if re.search(r"^\w+@\w+\.edu$", email, flags=re.IGNORECASE):
    print("Valid 5")
else:
    print("Invalid 5")

# The '?' sign makes the block on the left opitional (0 or 1 times)
# Or add a '*' sign, which means 0 or more times
# (\w|\.)+ → besides alphanumeric characters and underscore, now you are also allowing the '.' sign
if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$", email, flags=re.IGNORECASE):
    print("Valid 6")
else:
    print("Invalid 6")


# That's a simplified version of a regular expression for email validation:
if re.search(r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", email, flags=re.IGNORECASE):
    print("Valid 7")
else:
    print("Invalid 7")


# Since it's overwhemingly confusing, which could lead to typos if you are manually coding it, and to avoid copy paste, there are libraries that do that work of email validation
