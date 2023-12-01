# Select details of student using qualification by using limit clause

import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="", database="luminar")

myCursor = mydb.cursor()

limit = int(input("Enter the limit: "))
condition = input("Enter the limit: ")
sql = f"select * from student_details where qualification = '{condition}' limit {limit}"

myCursor.execute(sql)

data = myCursor.fetchall()
for i in data:
    print(i[0], "-", i[1], "-", i[2], "-", i[3], "-", i[4], "-", i[5])
