# Write a query to select the name, email and phone number of a student using name

import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="", database="luminar")

myCursor = mydb.cursor()

name = input("Enter the name:")

sql = "select name,email,phone from student_details where name='%s'" % name

myCursor.execute(sql)

a = myCursor.fetchall()

for i in a:
    print("Name =", i[0], "\tE-mail =", i[1], "\tPhone Number =", i[2])
