import sqlite3

userPrice = input("What is your Phone Budget? ")

#Connecting to sqlite
conn = sqlite3.connect('catalog.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Retrieving data
cursor.execute(
    "SELECT brand,description,price from mobile where price <=" + userPrice + ";")
#Fetching 1st row from the table
rows = cursor.fetchall()

for row in rows:

    print("Brand:", row[0])
    print("Description:", row[1])
    print("Price: $", row[2])
    print("----------------------")

#Closing the connection
conn.close()
