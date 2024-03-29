#-------- DAY 73 "mysql4" --------
import mysql.connector

print("Lesson 73: MySQL 4")
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "pythonDB"
)
mycursor = mydb.cursor()
# print("Informations Table:")
# mycursor.execute("SELECT * FROM informations")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)
# # 1. Update table
# print("---------------------\nInformations Table After Update:")
# sql = "UPDATE informations SET address = 'Canyon 123' WHERE address = 'Mountain 21'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) affected")
# mycursor.execute("SELECT * FROM informations")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)
# # 2. Limit the result & start with another position
# print("---------------------\nLimiting the result:")
# mycursor.execute("SELECT * FROM informations LIMIT 2 OFFSET 3")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)
#Creating tables
def createTable():
    # mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), fav VARCHAR(255))")
    # sql = "INSERT INTO users (name, fav) VALUES (%s, %s)"
    # val = [
    #     ('Peter', '166'),
    #     ('Hannah', '156'),
    #     ('Betty', ''),
    #     ('Susan', '166'),
    #     ('Viola', '')
    # ]
    # mycursor.executemany(sql, val)
    # mydb.commit()
    # print(mycursor.rowcount, "record was inserted.")
    # mycursor.execute("CREATE TABLE products (id VARCHAR(255), name VARCHAR(255))")
    # sql = "INSERT INTO products (id, name) VALUES (%s, %s)"
    # val = [
    #     ('166', 'Chocolate Heaven'),
    #     ('156', 'Tasty Lemons'),
    #     ('146', 'Vanilla Dreams')
    # ]
    # mycursor.executemany(sql, val)
    # mydb.commit()
    # print(mycursor.rowcount, "record was inserted.")
createTable()
print('Successfully!!')
# 3. (Inner / Left / Right) Join
def innerJoin():
    print("---------------------\nInner join:")
    sql = "SELECT \
        users.name AS user, \
        products.name AS favorite \
        FROM users \
        INNER JOIN products ON users.fav = products.id"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
def leftJoin():
    print("---------------------\nLeft join:")
    sql = "SELECT \
        users.name AS user, \
        products.name AS favorite \
        FROM users \
        LEFT JOIN products ON users.fav = products.id"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
def rightJoin():
    print("---------------------\nRight join:")
    sql = "SELECT \
        users.name AS user, \
        products.name AS favorite \
        FROM users \
        RIGHT JOIN products ON users.fav = products.id"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
innerJoin()
leftJoin()
rightJoin()
