import requests
from bs4 import BeautifulSoup


result = requests.get('https://divar.ir/s/tehran/car?price=500000000-800000000')
soup = BeautifulSoup(result.text, 'html.parser')
print(soup.prettify())

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print(soup.head)

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print(soup.findAll('a'))
links = soup.findAll('a')
for link in links:
    print("Link:", link.get("href"), "Text:", link.string)

# print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
# titles = soup.findAll(class_="kt-post-card__title")
# for title in titles:
#     print(title.string)
#
# print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
# tages = soup.findAll(class_="kt-post-card__info")
# for tag in tages:
#     print(tag.name + ' -> ' + tag.text.strip())

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
tages = soup.findAll(class_='kt-post-card__red-text')
for tag in tages:
    print(tag.parent.parent.text.strip())

