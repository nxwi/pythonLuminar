import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="", database="luminar")

myCursor = mydb.cursor()

sql = "create table employee_details(id int auto_increment, name varchar(20),salary int(6),primary key(id))"

myCursor.execute(sql)

mydb.commit()  # used to save database

print("Table created successfully")

