# Create a table student details: id, name, email, qualification, fee, phone number(bigint)

import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="", database="luminar")

myCursor = mydb.cursor()

sql = ("create table employee_details02(id int auto_increment, name varchar(20),email varchar(25),"
       "qualification varchar(15), fee int(6),phone bigint, primary key(id))")

myCursor.execute(sql)

mydb.commit()  # used to save database

print("Table created successfully")
