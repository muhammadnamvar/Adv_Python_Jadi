# import modules
import mariadb
import sys

# Connect to mariadb
try:
    conn = mariadb.connect(
        user="root",
        password="Water111@",
        host="127.0.0.1",
        port=3306,
        database="nextoffice"
    )
except mariadb.Error as e:
    print(f"Error connectiong to mariadb platform is: {e}")
    sys.exit(1)

# Get cursor
cur = conn.cursor()


# Create Table
try:
    cur.execute(
        "CREATE TABLE task2 (taskid INTEGER, name VARCHAR(20), descr VARCHAR(20))"
    )
except mariadb.Error as e:
    print(e)
    sys.exit(1)

cur.execute(
    "INSERT INTO task2 (taskid, name) VALUES (102, 'ali')"
)
conn.commit()


# Retrieving data
cur.execute(
    "SELECT taskid, name FROM task2"
)
for taskid, name in cur:
    print(taskid, name)

