import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="", database="luminar")

myCursor = mydb.cursor()

# sql = "create table student_details(id int auto_increment, name varchar(20),salary int(6),primary key(id))"
sql = ("create table student_details(id int auto_increment,name varchar(20),email varchar(25),qualification varchar("
       "20),phone bigint,fee int(6),primary key(id))")

myCursor.execute(sql)

mydb.commit()  # used to save database

print("Table created successfully")
