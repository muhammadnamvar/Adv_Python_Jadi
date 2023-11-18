# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="Water111@",
        host="127.0.0.1",
        port=3306,
        database="nextoffice"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
# Get Cursor
cur = conn.cursor()


cur.execute("CREATE TABLE salary (income VARCHAR(30), age INTEGER)");


cur.execute("INSERT INTO salary (income, age) VALUES ('mammad Namvar', 33), ('li momuuul', 38),('amin khare', 45)")


conn.commit()



cur.execute("SELECT income, age FROM salary")
for (income, age) in cur:
    print("Name:", {income}, "Age:", {age})
conn.close()
