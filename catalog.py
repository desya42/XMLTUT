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
	print("Opened database successfully")
	return conn

def XMLtoDB(file_name,cursor):
	tree = et.ElementTree(file=file_name)
	catalog = tree.getroot()
	if(catalog.tag != "Catalog"):
		print("Expecting Catalog as root tag")
		return

	mobiles = list(catalog)
	for mobile in mobiles:
		mobile_specs = list(mobile)
		outline=""
		values =""
		for spec in mobile_specs:
			outline+='"'+spec.tag+'",'
			values+='"'+spec.text+'",'
		outline = outline.rstrip(',')
		values = values.rstrip(',')
		sqlstatement= "INSERT INTO Mobile ("+outline+") VALUES ("+values+");"
		cursor.execute(sqlstatement)
		print("Adding row: "+values)


if __name__ == "__main__":
	conn = openDB(DBPATH)
	cursor = conn.cursor()
	XMLtoDB(XMLPATH,cursor)
	cursor.close()
	conn.commit()
	conn.close()

