import requests as r
import json
from variables import *

headers = {"Authorization": "Bearer "+token}

print("MASTOPAWN by fancyfinn9")
print("A chess puzzle Mastodon bot")

data = {"status": text}
req = r.post("https://"+instance+"/api/v1/statuses", headers=headers, data=data)
print(req.text)
