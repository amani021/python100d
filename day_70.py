#-------- DAY 70 "mysql1" --------
import mysql.connector

print("Lesson 70: MySQL 1")
# 1. Connect with database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "pythonDB" #After created, you can connect with it from here
)
# print(mydb)
mycursor = mydb.cursor()
# 2. Create a new database
# mycursor.execute("CREATE DATABASE pythonDB")
# 3. List all your databases
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
# 4. Create a new table with primary key
# mycursor.execute("CREATE TABLE informations (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
# 5. List all tables you have
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
# print('Successfully')
