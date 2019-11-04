#-------- DAY 75 "exercise2" --------
import mysql.connector

# 2. Dealing with database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "MyEmployee"
)
mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE MyEmployee")
# sql = "CREATE TABLE Employee \
#     (id INT AUTO_INCREMENT PRIMARY KEY, firstName VARCHAR(255), lastName VARCHAR(255), age INT, gender VARCHAR(255), salary VARCHAR(255))"
# mycursor.execute(sql)
# sql = "INSERT INTO Employee (firstName, lastName, age, gender, salary) VALUES (%s, %s, %s, %s, %s)"
# val = [
#     ('Ahmed', 'Ali', 30, 'Male', '10000'),
#     ('Khalid', 'Muhammad', 34, 'Male', '7000'),
#     ('Norah', 'Saleh', 29, 'Female', '7000')
# ]
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record(s) was inserted.")
# print('Successfully')
print('The Main Employee Table:') # a
mycursor.execute("SELECT * FROM Employee")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
print('---------------------\nTable with 3 columns:') # b
mycursor.execute("SELECT firstName, gender, salary FROM Employee")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
print('---------------------\nTable as descending order:') # c
mycursor.execute("SELECT * FROM Employee ORDER BY firstName DESC")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
mycursor.execute("DELETE FROM Employee WHERE age = 34")
mydb.commit()
print('---------------------\nThe table after delete a record:') # d
mycursor.execute("SELECT * FROM Employee")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
