# Inserts 3000 hashes into the table.

from random import randint
import MySQLdb

db = MySQLdb.connect("localhost", "root", "raviteja", "new_schema")
cursor = db.cursor()
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
count = 1
while (count < 3001):
        for i in range(62):
                for j in range(62):
                        for k in range(62):
                                for l in range(62):
                                        b = "'" + charset[i] + charset[j] + charset[k] + charset[l] + "'"
                                        print (b + "\t" + str(count))
                                        sql = "INSERT INTO urllist (sl, hash, longurl) VALUES (%d, %s, '');" % (count, b)
                                        cursor.execute(sql)
                                        db.commit()
                                        count+=1
db.close()
