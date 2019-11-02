#-------- DAY 72 "mysql3" --------
import mysql.connector

print("Lesson 72: MySQL 3")
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "pythonDB"
)
mycursor = mydb.cursor()
# 1. Sorting the result, by default is ascending
sql = "SELECT name, address FROM informations ORDER BY name DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
# 2. Delete record
#If we don't write (WHERE), it will delete all records
sql = "DELETE FROM informations WHERE address = 'One way 98'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")
# 3. Drop table with condition if exist
sql = "DROP TABLE IF EXISTS customers"
mycursor.execute(sql)
