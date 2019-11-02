#-------- DAY 71 "mysql2" --------
import mysql.connector

print("Lesson 71: MySQL 2")
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "pythonDB"
)
mycursor = mydb.cursor()
# 1. Insert into table (one row)
# sql = "INSERT INTO informations (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)
# mydb.commit() #Should write it to save
# print(mycursor.rowcount, "record inserted.")
# 2. Insert into table (multiple rows)
# sql = "INSERT INTO informations (name, address) VALUES (%s, %s)"
# val = [
#     ('Peter', 'Lowstreet 4'),
#     ('Hannah', 'Mountain 21'),
#     ('Betty', 'Yellow Garden 2'),
#     ('Susan', 'One way 98'),
#     ('Viola', 'Sideway 1633')
# ]
# mycursor.executemany(sql, val) #For insert many rows
# mydb.commit()
# print(mycursor.rowcount, "record was inserted.\nLast item's ID:", mycursor.lastrowid)
# print('Successfully!!')
# 3. Select all or some columns with/without conditions from a table, use fetchall() method
# 4. Fetch only the first row
# mycursor.execute("SELECT * FROM informations")
# print(mycursor.fetchone())
# 5. Select records have that part you want
sql = "SELECT * FROM informations WHERE address Like '%low%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
