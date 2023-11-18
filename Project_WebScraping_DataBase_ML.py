import requests
from bs4 import BeautifulSoup
import mariadb
import re
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


# Connect to Mariadb
try:
    conn = mariadb.connect(
        user='root',
        password='Water111@',
        host='127.0.0.1',
        port=3306,
        database='truecar'
    )
except mariadb.Error as e:
    print(e)
    exit(1)

# Create cursor from Connection
cur = conn.cursor()

# Create Table Schema
query = ("CREATE TABLE IF NOT EXISTS usedcar "
         "(brand varchar(20), model varchar(20), "
         "year int, mileage int, price int,"
         "CONSTRAINT UC_Car UNIQUE (mileage,price))")
cur.execute(query)
conn.commit()


# input data for request
brand = input("Brand: ")
model = input("Model: ")
min_year = input("Min year: ")
max_year = input("Max year: ")
mileage_low = input("Low Mileage: ")
mileage_high = input("High Mileage: ")
min_price = input("Min price: ")
max_price = input("Max price: ")
max_page = int(input("Max page: "))


def scrape_savedb(page):
    # send Request and get Response
    result = requests.get(f"https://www.truecar.com/used-cars-for-sale/listings"
                          f"/{brand}/{model}/year-{min_year}-{max_year}/price-{min_price}-{max_price}"
                          f"/?mileageHigh={mileage_high}&mileageLow={mileage_low}&page={page}")

    # Create soup
    soup = BeautifulSoup(result.text, 'html.parser')

    # Find data in soup
    years = soup.find_all("span", {"class": "vehicle-card-year"})
    prices = soup.find_all("span", {"data-test": "vehicleListingPriceAmount"})
    miles = soup.find_all('div', {'data-test': 'vehicleMileage'})

    # Insert Data to Table
    for j in range(len(prices)):
        query = ("INSERT IGNORE INTO usedcar "
                 "(brand, model, year, mileage, price) "
                 "VALUES (%s, %s, %s, %s, %s)")
        data = (brand, model, int(years[j].text),
                int(miles[j].text.replace(' miles', '').replace(',', '')),
                int(prices[j].text.replace(',', '').replace('$', '')))
        cur.execute(query, data)
        conn.commit()


for i in range(max_page):
    scrape_savedb(i)


# Show Table
query = "SELECT * FROM usedcar"
cur.execute(query)
for brand, model, year, mileage, price in cur:
    print(brand, model, year, mileage, price)
conn.commit()


# Predict Price with ML
x = []
y = []
query = "SELECT * FROM usedcar"
cur.execute(query)
conn.commit()
for row in cur:
    x.append(row[2:4])
    y.append(row[-1])
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
model = DecisionTreeClassifier()
model.fit(x_train, y_train)
predictions = model.predict(x_test)
score = accuracy_score(y_test, predictions)

print("Y: ", y_test)
print("P: ", predictions)
print(score)
