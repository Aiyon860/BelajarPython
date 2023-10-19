mycursor.execute("SELECT * FROM customers")
allResult = mycursor.fetchall()
for k in allResult:
    print(k)