# Demonstrates requests
# Needs 'pip install requests'

import json
import sys
import requests

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    # 'entity=song' searches for songs in apple's database
    # 'limit=1' provides information about just one song
    # 'term=weezer' specifies the band (in this case, Weezer)
    "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]
)
print(response.json())
print()
print(json.dumps(response.json(), indent=2))

 # json.dumps() allows to format that outputed data more cleanly
 # indent=2 indents everything with 2 spaces