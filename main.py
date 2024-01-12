import requests as r
import json

token = "<put token here>"
headers = {"Authorization": "Bearer "+token}

print("MASTOPAWN by fancyfinn9")
print("A chess puzzle Mastodon bot")

data = {"status": text}
req = r.post("https://botsin.space/api/v1/statuses", headers=headers, data=data)
print(req.text)
