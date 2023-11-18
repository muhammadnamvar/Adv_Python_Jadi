import requests
from bs4 import BeautifulSoup



# res = requests.get("https://nextoffice.ir/")
res = requests.get("https://divar.ir/s/tehran/car/?price=800000000-1000000000")
print(res)
print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')

# val1 = soup.find('h2')
# print(val1)

# val2 = soup.findAll('h2')
# print(val2)

val3 = soup.find_all('h2')
print(val3)

# valn = soup.find('class="kt-post-card__info')
# print(valn)
