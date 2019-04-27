
# Establishing a connection to DB
import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='tgif2019!', db='users')

# Getting a cursor from Database
cursor = conn.cursor()

# Getting all data from table “users”
cursor.execute("SELECT * FROM users.all_users;")
#cursor.execute("INSERT into users.all_users(name,id)VALUES('Eithan',2)")
#cursor.execute("DELETE FROM users.all_users WHERE id=2")
cursor.execute("UPDATE users.all_users SET id ='17' where name='elad'")
conn.commit() # for INSERT and for DELETE we must add it
cursor.close()

cursor = conn.cursor()
cursor.execute("SELECT * FROM users.all_users;")
# Iterating table and printing all users
for row in cursor:
    print(row)

cursor.close()
conn.close()