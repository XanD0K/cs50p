# Demonstrates iterating over JSON

import json
import sys
import requests

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&term=" + sys.argv[1]
)
# There's no 'limit' anymore, so it will get all songs

object = response.json()
for result in object["results"]:
    print(result["trackName"])
