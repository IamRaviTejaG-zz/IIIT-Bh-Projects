# RAT - Rosei Automation Tool.
# Requires Selenium and Chrome Webdriver.
# Last Update: 04-02-2017.
# Copyright (c) 2017 Ravi Teja Gannavarapu.
# Distributed under MIT License.

"""
Inspired from Hibiscus Automation by Ankit Choudhary (B216008) (b216008@iiit-bh.ac.in).
Contact Ravi Teja Gannavarapu (b216023@iiit-bh.ac.in) for further help/information.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

# ^ For os.path.exists and os.system('cls')

#Food codes data. Please note that these codes are no way related to the Roseighara platform and are useful only in this module itself.
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

#The dictionary below (d1) is Roseighara HTML ID's for use with the selenium webdriver.
d1 = {111:"mess1b1", 121:"mess1b2", 131:"mess1b3", 141:"mess1b4", 151:"mess1b5", 161:"mess1b6", 171:"mess1b7"\
	,112:"mess1l1", 122:"mess1l2", 132:"mess1l3", 142:"mess1l4", 152:"mess1l5", 162:"mess1l6", 172:"mess1l7"\
	,113:"mess1d1", 123:"mess1d2", 133:"mess1d3", 143:"mess1d4", 153:"mess1d5", 163:"mess1d6", 173:"mess1d7"}

#For printing the food codes.
def fcodes():
	print ("\nRoseighara-1 Food Codes\n")
	for i in foodcodes1:
		for j in i:
			print j + "\t",
		print "\n"
	print ("\nRoseighara-2 Food Codes\n")
	for i in foodcodes2:
		for j in i:
			print j + "\t",
		print "\n"

#For booking the coupons.
def booking():
	with open("roseidata.dat", "r") as f:
		a = f.readlines() #Reads from the files and stores each line as list item.
	a = [x.strip() for x in a] #Removes any whitespace characters from the list.
	f.close()
	username = a[0]
	paword = a[1]
	ufc1 = a[2].split()
	ufc2 = a[3].split()
	ufc = [ufc1, ufc2]
	browser = webdriver.Chrome("chromedriver.exe") #Set the path to the chromedriver executable folder.
	browser.get("http://172.16.2.200:8081/rosei/login.jsp")
	uname = browser.find_element_by_name('un')
	pword = browser.find_element_by_name('pw')
	uname.send_keys(username)
	pword.send_keys(paword)
	browser.find_element_by_name('submit').click()
	for i in ufc:
		browser.get("http://172.16.2.200:8081/rosei/selectmess.jsp")
		if (len(i) != 0 and i == ufc1):
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
		if (len(i) != 0 and i == ufc2):
			browser.find_element_by_id('//*[@id="p2"]').click()
			for j in ufc2:
				r = j[1:len(j)]
				g = int(r) - 100 #The goddamn HTML selectors used the same ID.
				xp = "//*[@id=\"" + d1[g] + "\"]"
				if (j[0] == "V" or j[0] == "v"):
					for i in range(2):
						browser.find_element_by_xpath(xp).click()
				elif (j[0] == "N" or j[0] == "n"):
					for i in range(1):
						browser.find_element_by_xpath(xp).click()
			browser.find_element_by_xpath('//*[@id="submit"]').click()
	q = cost()
	print ("\nBooking Complete.")
	print ("\nTotal Roseighara Amount: " + str(q[0] + q[1]))

#For changing the user preferences.
def setprefs():
	uname = raw_input("\nEnter your username: ")
	pwd = raw_input("\nEnter your password: ")
	fcodes()
	print ("\nNOTE: Please prefix your food code with V for Veg and N for Non-Veg.\n")
	k = raw_input ("\nEnter your Roseighara 1 food codes in the correct format separated by space in a single line: ")
	g = raw_input ("\nEnter your Roseighara 2 food codes in the correct format separated by space in a single line: ")
	f = open("roseidata.dat", "w")
	f.write(uname)
	f.write("\n")
	f.write(pwd)
	f.write("\n")
	f.write(k)
	f.write("\n")
	f.write(g)
	f.write("\n")
	f.close()
	print ("\n\nPreferences updated!")

#For viewing the user preferences.
def viewprefs():
	with open("roseidata.dat", "r") as f:
		a = f.readlines() #Reads from the files and stores each line as list item.
	a = [x.strip() for x in a] #Removes any whitespace characters from the list.
	f.close()
	username = a[0]
	paword = a[1]
	ufc1 = a[2].split()
	ufc2 = a[3].split()
	u = cost()
	print ("\nUsername: " + username)
	print ("\nPassword: " + paword)
	print ("\nRoseighara 1 Food Preferences: " + ''.join(ufc1))
	print ("\nRoseighara 2 Food Preferences: " + ' '.join(ufc2))
	print ("\nRoseighara 1 Amount: " + str(u[0]))
	print ("\nRoseighara 2 Amount: " + str(u[1]))
	print ("\nTotal Roseighara Amount: " + str(u[0] + u[1]))

#For calculating the cost.
def cost():
	with open("roseidata.dat", "r") as f:
		b = f.readlines() #Reads from the files and stores each line as list item.
	b = [x.strip() for x in b] #Removes any whitespace characters from the list.
	f.close()
	a = []
	count1 = count2 = 0
	uc1 = b[2].split()
	uc2 = b[3].split()
	for i in uc1:
		if (i[3] == '1'):
			count1+=10
		elif (i[3] == '2' or i[3] == '3'):
			count1+=25
	for j in uc2:
		if (j[3] == '1'):
			count2+=10
		elif (j[3] == '2' or j[3] == '3'):
			count2+=25
	a.append(count1)
	a.append(count2)
	return a

#The main function. Calls every other function.
def main():
	if (os.path.exists("roseidata.dat") == False):
		print ("\nPreferences/Data file wasn't found. Please set preferences.")
		setprefs()
		main()
	else:
		print ("\nPreferences file was found. Reading from file.")
		c = raw_input("\n1. Register coupons for the upcoming week.\n2. Change preferences.\n3. View present preferences.\n4. View amount to be paid.\n5. Exit.\n\nEnter your choice: ")
		if (int(c) == 1):
			os.system('cls')
			booking()
			main()
		elif (int(c) == 2):
                        os.system('cls')
			setprefs()
			main()
		elif (int(c) == 3):
                        os.system('cls')
			viewprefs()
			main()
		elif (int(c) == 4):
                        os.system('cls')
			u = cost()
			print ("\nRoseighara 1 Amount: " + str(u[0]))
			print ("\nRoseighara 2 Amount: " + str(u[1]))
			print ("\nTotal Roseighara Amount: " + str(u[0] + u[1]))
			main()
		elif (int(c) == 5):
			exit()
		else:
			main()

#And finally the main function call.
print ("Welcome to Rosei Automation Tool")
main()
