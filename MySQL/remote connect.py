
# Establishing a connection to DB
import pymysql

conn = pymysql.connect(host='remotemysql.com', port=3306, user='Ms5N4TL8g6', passwd='gIgmkPhiAP', db='Ms5N4TL8g6')

# Getting a cursor from Database
cursor = conn.cursor()

cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# Getting all data from table “users”


cursor = conn.cursor()

cursor.close()
conn.close()