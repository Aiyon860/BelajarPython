import mysql.connector
from Belajar.OOP.assets.helper import FreeSpace

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="belajardb"
)

# print(mydb)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE BelajarDB")
""" mycursor.execute("SHOW DATABASES")
for i in mycursor:
    print(i) """

# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

""" mycursor.execute("SHOW TABLES")
for j in mycursor:
    print(j) """

# mycursor.execute("ALTER TABLE customers ADD COLUMN age INT")
""" mycursor.execute("SHOW COLUMNS FROM customers")
for x in mycursor:
    print(x) """

# mycursor.execute("ALTER TABLE customers DROP COLUMN age")
# mycursor.execute("ALTER TABLE customers ADD COLUMN age VARCHAR(5)")

""" dataInsert = "INSERT INTO customers (name, address, age) VALUES (%s, %s, %s)"
dataValue = [
    ("Firman", "Central Semarang Avenue 15", "20"),
    ("Ahmad", "South Semarang Brooklyn 3", "20"),
]
mycursor.executemany(dataInsert, dataValue)  """    # ('insert' syntax, the data that want to get inserted)
# mydb.commit()     INI WAJIB DIKETIK SETELAH MEGNINPUT DATA KE TABEL
# print("1 record inserted, ID:", mycursor.lastrowid)


# mycursor.execute("DELETE FROM customers WHERE id = 14")

# mydb.commit()

""" mycursor.execute("SELECT * FROM customers")
allResult = mycursor.fetchall()
for k in allResult:
    print(k) """

mycursor.execute("SELECT name, address FROM customers")
allResult = mycursor.fetchall()
for k in allResult:
    print(k)

FreeSpace()

mycursor.execute("SELECT * FROM customers")
oneResult = mycursor.fetchone()
print(oneResult)