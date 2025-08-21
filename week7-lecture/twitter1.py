import re


url = input("URL: ").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

print(f"Username: {username}")

# We still need to check if the user typed a correct pattern
# He may still type https://google.com and it will be printed on screen