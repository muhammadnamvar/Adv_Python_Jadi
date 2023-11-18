import requests


response = requests.get("http://api.coincap.io/v2/assets")
print(response)
data = response.json()['data']
for i in range(len(data)):
    print(data[i]['rank'], data[i]['id'], data[i]['symbol'], data[i]['priceUsd'])
