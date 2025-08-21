# Pupose of prompting users for the URL of their Twitter profile, and extract from it the user's username

url = input("URL: ").strip()

username = url.removeprefix("https://twitter.com/")

print(f"Username: {username}")

# Even though that approach works, it has some downsides:
# User might use 'http', or he could use 'www', or he could write a whole sentence like "My username is (...)"
# So, let's use regex to specify the pattern of the URL to correctly extract user's username
