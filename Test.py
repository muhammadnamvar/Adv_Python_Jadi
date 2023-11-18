import mariadb
import sys
import re


# Check email with Regex
email = input("Please Enter your email: ")
pattern = '^[A-Za-z0-9.%+-]+@[A-Za-z0-9+-]+\.[A-Za-z]{2,7}$'
result = re.search(pattern, email)
while not result:
    email = input("Pleas Enter Correct Fucking Email Format: ")
    result = re.search(pattern, email)
print("Your Email Registered!!!!!")


# Check password with Regex
password = input("Please Enter your password: ")
pattern = '^[A-Za-z0-9%.@$]{8,20}$'
result = re.search(pattern, password)
while not result:
    password = input("Pleas Enter Correct Fucking password Format: ")
    result = re.search(pattern, password)
print("Your password Registered!!!!!")


# connect to mariadb
try:
    conn = mariadb.connect(
        user="root",
        password="Wate111@",
        host="127.0.0.1",
        port=3306,
        database="nextoffice"
    )
except mariadb.Error as e:
    print(e)
    sys.exit(1)

# create cursor
cur = conn.cursor()


# create table schema
cur.execute(
    "CREATE TABLE IF NOT EXISTS account (username VARCHAR(20), password varchar(20))"
)


# insert data to table
query = "INSERT INTO account (username, password) VALUES (%s, %s)"
data = (email, password)
cur.execute(query, data)
conn.commit()


# retrieving data
cur.execute(
    "SELECT username, password FROM account"
)
for e, p in cur:
    print(e, p)


# Delete data
query = 'DELETE FROM employer'
cur.execute(query)
conn.commit()


conn.close()
