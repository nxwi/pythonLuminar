# Write a SQL query to update the fee of student using name and email

import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="", database="luminar")

myCursor = mydb.cursor()

name = input("Enter the name: ")
email = input("Enter the E-mail: ")
sql = "select name,email from student_details"
myCursor.execute(sql)
data = myCursor.fetchall()
for i in data:
    if name == i[0] and email == i[1]:
        fee = int(input("Enter the fee: "))
        sql = f"update student_details set fee = {fee} where name = '{name}' and email = '{email}'"
        myCursor.execute(sql)
        mydb.commit()
        print("Database Updates...")
        break
else:
    print("Name or E-mail mismatch")
