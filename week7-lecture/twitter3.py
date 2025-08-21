import re
url = input("URL: ").strip()

# Twitter only supporst letters, numbers and underscore
# instead of [a-z0-9_], I could use '\w'
# Removed the '$' sign at the end to allow more stuff after the username
if matches := re.search(r"^(?:https?://)?(?:www.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username?", matches.group(1))