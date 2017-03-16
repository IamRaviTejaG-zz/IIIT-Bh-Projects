from Tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

g = Tk()
g.title("Rosei Automation Tool")
g.geometry("300x75")

titles = ["", "BRF", "LUN", "DIN"]
mon1 = ["MON", "111", "112", "113"]
tue1 = ["TUE", "121", "122", "123"]
wed1 = ["WED", "131", "132", "133"]
thu1 = ["THU", "141", "142", "143"]
fri1 = ["FRI", "151", "152", "153"]
sat1 = ["SAT", "161", "162", "163"]
sun1 = ["SUN", "171", "172", "173"]
mon2 = ["MON", "211", "212", "213"]
tue2 = ["TUE", "221", "222", "223"]
wed2 = ["WED", "231", "232", "233"]
thu2 = ["THU", "241", "242", "243"]
fri2 = ["FRI", "251", "252", "253"]
sat2 = ["SAT", "261", "262", "263"]
sun2 = ["SUN", "271", "272", "273"]
foodcodes1 = [titles, mon1, tue1, wed1, thu1, fri1, sat1, sun1]
foodcodes2 = [titles, mon2, tue2, wed2, thu2, fri2, sat2, sun2]
d1 = {111:"mess1b1", 121:"mess1b2", 131:"mess1b3", 141:"mess1b4", 151:"mess1b5", 161:"mess1b6", 171:"mess1b7"\
	,112:"mess1l1", 122:"mess1l2", 132:"mess1l3", 142:"mess1l4", 152:"mess1l5", 162:"mess1l6", 172:"mess1l7"\
	,113:"mess1d1", 123:"mess1d2", 133:"mess1d3", 143:"mess1d4", 153:"mess1d5", 163:"mess1d6", 173:"mess1d7"}

def booking():
        workingLabel = Label(text="Working!").pack()
	with open("roseidata.dat", "r") as f:
		a = f.readlines()
	a = [x.strip() for x in a]
	f.close()
	username = a[0]
	paword = a[1]
	ufc1 = a[2].split()
	ufc2 = a[3].split()
	browser = webdriver.Chrome("chromedriver.exe")
	browser.get("http://172.16.2.200:8081/rosei/login.jsp")
	uname = browser.find_element_by_name('un')
	pword = browser.find_element_by_name('pw')
	uname.send_keys(username)
	pword.send_keys(paword)
	browser.find_element_by_name('submit').click()
	if (len(ufc1) != 0):
		browser.get("http://172.16.2.200:8081/rosei/selectmess.jsp")
		browser.find_element_by_xpath('//*[@id="p1"]').click()
		for j in ufc1:
			r = j[1:len(j)]
			g = int(r)
			xp = "//*[@id=\"" + d1[g] + "\"]"
			if (j[0] == "V" or j[0] == "v"):
				for i in range(2):
					browser.find_element_by_xpath(xp).click()
			elif (j[0] == "N" or j[0] == "n"):
				for i in range(1):
					browser.find_element_by_xpath(xp).click()
		browser.find_element_by_xpath('//*[@id="submit"]').click()
		sleep(2)
		if (len(ufc2) !=0):
			browser.get("http://172.16.2.200:8081/rosei/selectmess.jsp")
			browser.find_element_by_xpath('//*[@id="p2"]').click()
			for j in ufc2:
				r = j[1:len(j)]
				g = int(r) - 100
				xp = "//*[@id=\"" + d1[g] + "\"]"
				if (j[0] == "V" or j[0] == "v"):
					for i in range(2):
						browser.find_element_by_xpath(xp).click()
				elif (j[0] == "N" or j[0] == "n"):
					for i in range(1):
						browser.find_element_by_xpath(xp).click()
			browser.find_element_by_xpath('//*[@id="submit"]').click()
			sleep(2)
			browser.close()
	elif (len(ufc1) == 0 and len(ufc2) != 0):
		browser.get("http://172.16.2.200:8081/rosei/selectmess.jsp")
		browser.find_element_by_xpath('//*[@id="p2"]').click()
		for j in ufc2:
			r = j[1:len(j)]
			g = int(r) - 100
			xp = "//*[@id=\"" + d1[g] + "\"]"
			if (j[0] == "V" or j[0] == "v"):
				for i in range(2):
					browser.find_element_by_xpath(xp).click()
			elif (j[0] == "N" or j[0] == "n"):
				for i in range(1):
					browser.find_element_by_xpath(xp).click()
		browser.find_element_by_xpath('//*[@id="submit"]').click()
		sleep(3)
		browser.close()
	binLabel = Label(text="Booking Complete!").pack()

submit = Button(text="Register Coupons", command = booking).pack()

g.mainloop()
