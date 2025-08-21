import re
url = input("URL: ").strip()

# (.+) → first one catches the domain (e.g. com, edu, org)
# The second one catches the user's username
if matches := re.search(r"^(?:https?://)?(?:www.)?twitter\.(.+)/(.+)$", url, re.IGNORECASE):
    if matches.group(1) == "com":
        print(f"Username?", matches.group(2))