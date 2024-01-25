import mysql.connector

try:
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='entregable_02'
    )
    print(mydb)
except mysql.connector.Error as err:
    print(err)
