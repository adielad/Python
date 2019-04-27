import pymysql
conn = pymysql.connect(host='remotemysql.com', port=3306, user='Ms5N4TL8g6', passwd='gIgmkPhiAP', db='Ms5N4TL8g6')
cursor = conn.cursor()

#2.
cursor.execute("INSERT into Ms5N4TL8g6.Dogs(name, age, breed)VALUES('Jack', 12, 'Pincher');")
cursor.execute("INSERT into Ms5N4TL8g6.Dogs(name, age, breed)VALUES('john', 7, 'Pudel');")
cursor.execute("INSERT into Ms5N4TL8g6.Dogs(name, age, breed)VALUES('Jim', 3, 'Hasky');")

#3.
cursor.execute("UPDATE Ms5N4TL8g6.Dogs SET name='john' where age='12';")

#4.
cursor.execute("DELETE from Ms5N4TL8g6.Dogs where name='Jim';")
conn.commit()
#5.
cursor.execute("SELECT * FROM Dogs;")

for r in cursor:
    print(r)

conn.close()