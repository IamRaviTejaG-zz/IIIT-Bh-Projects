# Short URL Redirector
# By Ravi Teja Gannavarapu

import MySQLdb
from selenium import webdriver

def main():
	db = MySQLdb.connect("localhost", "root", "raviteja", "new_schema")
	cursor = db.cursor()
	x = raw_input("Enter the short url:\n\n")
	d = x[len(x)-4:]
	sql = "SELECT longurl FROM urllist WHERE hash = '" + str(d) + "';"
	cursor.execute(sql)
	a = cursor.fetchone()
	b = str(a[0])
	print ("\nRedirecting to the original URL:\n")
	browser = webdriver.Chrome("chromedriver.exe")
	browser.get(b)
	print (b)
	db.close()

main()
