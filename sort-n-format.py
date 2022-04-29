#!/usr/bin/env python3
import sys
import sqlite3
import xml.etree.cElementTree as et

XMLPATH='CatalogXML.xml'
DBPATH='catalog.db'

def openDB(db):
	try:
		conn = sqlite3.connect(db)
	except:
		print("Unable to open database")
		sys.exit(1)
	#print("Opened database successfully")
	return conn

def findMobileLessThan(maxprice,cursor):
	sqlstatement= "SELECT brand,description,price FROM Mobile WHERE price <= "+str(maxprice)+ \
		" ORDER BY brand ASC, price DESC;"
	cursor.execute(sqlstatement)
	rows = cursor.fetchall()

	found=0
	brand=""
	for row in rows:
		found+=1
		newbrand=row[0]
		print("<html><head><title>Catalog</title></head><body>")
	print("<table border=1>")
	for i in range(found):
		print("<tr>")
		for j in range(found):
			print("<td>")
			print(str(i)+","+str(j))
			print("</td>")
			print("</tr>")	
	print("</table>")
	print("</body></html>")

	if(found==0):
		print("You're too broke to buy a phone these days")
	elif(found==1):
		print("There's only one option with your budget")
	else:
		print("""You have %d choices""" % found)




if __name__ == "__main__":
	try:
		budget = float(input("What is the most you are willing to pay for a phone? "))
	except:
		print("invalid input")
		sys.exit(1)

	conn = openDB(DBPATH)
	cursor = conn.cursor()
original_stdout = sys.stdout
with open('catalog.html','w') as f:
	sys.stdout = f
	print(findMobileLessThan(budget,cursor))
	sys.stdout = original_stdout
	cursor.close()
	conn.close()

