import mariadb
import sys


# Connect to database
try:
    conn = mariadb.connect(
        user='root',
        password='Water111@',
        host='127.0.0.1',
        port=3306,
        database='irankhodro'
    )
except mariadb.Error as e:
    print(e)
    sys.exit(1)


# Create Cursor
cur = conn.cursor()


# Create Table schema
query = 'CREATE TABLE IF NOT EXISTS employee (name varchar(20), height int, weight int)'
cur.execute(query)


# Insert data to table
query = 'INSERT INTO employee (name, height, weight) VALUES ("jala", 190, 93)'
cur.execute(query)


# perform change to db
conn.commit()


# Read Table to list
query = 'SELECT * FROM employee ORDER BY height DESC, weight'
cur.execute(query)
for name, height, weight in cur:
    print(name, height, weight)

