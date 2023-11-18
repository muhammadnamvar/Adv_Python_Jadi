import requests
from kavenegar import *


proxies = {
   'http': 'http://127.0.0.1:10810',
   'https': 'http://127.0.0.1:10810',
   'socks': 'socks://127.0.0.1:10810'
}
url = "https://api.coincap.io/v2/assets"
response = requests.get(url, proxies=proxies)
data = response.json()['data']
for i in range(len(data)):
    print(data[i]['rank'], data[i]['id'], data[i]['symbol'], data[i]['priceUsd'])


try:
    api = KavenegarAPI('31376F663668697162767867303147593979445374464B50664A4C6D426A795A724E5868335455764F62773D')
    params = {
        'sender': '2000500666',
        'receptor': '09382465446',
        'message': f"hi zari, bitcoin price is: {data[0]['priceUsd']}",
    }
    response = api.sms_send(params)
    print(response)
except APIException as e:
    print(e)
except HTTPException as e:
    print(e)
