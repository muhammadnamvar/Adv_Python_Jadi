import requests

res = requests.get('https://api.apis.guru/v2/providers.json')
print(res)
# print(res.json())
print(res.text)
