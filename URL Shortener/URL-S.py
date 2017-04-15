# URL Shortener
# By Ravi Teja Gannavarapu

from random import randint
import MySQLdb

def lastdig():
	with open("record.txt", "r") as f:
		a = f.readlines()
	b = int(a[0])
	b+=1
	return b

def storedig(c):
	f = open("record.txt", "w")
	f.write(str(c))
	f.close()

def main():
	db = MySQLdb.connect("localhost", "root", "raviteja", "new_schema")
	cursor = db.cursor()
	x = raw_input("Enter the long url:\n\n")
	d = lastdig()
	sql = "UPDATE urllist SET longurl = '" + x + "' WHERE sl = " + str(d) + ";"
	cursor.execute(sql)
	db.commit()
	sql = "SELECT hash FROM urllist WHERE sl = " + str(d) + ";"
	cursor.execute(sql)
	a = cursor.fetchone()
	b = "http://iiit-bh.ac.in/" + str(a[0])
	print ("\n\nHere's the short URL:\n\n")
	print (b)
	storedig(d)
	db.close()
	u = raw_input()

main()
