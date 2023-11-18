import requests
from bs4 import BeautifulSoup


car_name = input("Please enter your car name: ")
result = requests.get(f"https://www.truecar.com/used-cars-for-sale/listings/hyundai/{car_name}/")
soup = BeautifulSoup(result.text, 'html.parser')


# prices = soup.find_all("span", {"data-test": "vehicleListingPriceAmount"})
# for price in prices:
#     print(price.text)
#
#
# miles = soup.find_all('div', {'data-test': 'vehicleMileage'})
# for mile in miles:
#     print(mile.text)


prices = soup.find_all("span", {"data-test": "vehicleListingPriceAmount"})
miles = soup.find_all('div', {'data-test': 'vehicleMileage'})
for i in range(len(prices)):
    print(f"{car_name}: price: {prices[i].text}, {miles[i].text}")


# tags = soup.find_all(attrs={'data-test': 'vehicleMileage'})
# for tag in tags:
#     print(tag.text)


# tags = soup.find_all(attrs={'data-test': 'vehicleMileage', "data-test": "vehicleListingPriceAmount"})
# for tag in tags:
#     print(tag.text)
