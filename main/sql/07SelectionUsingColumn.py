import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="", database="luminar")

myCursor = mydb.cursor()

sql = "select name,qualification from student_details"

myCursor.execute(sql)

a = myCursor.fetchall()

for i in a:
    print("Name =", i[0], "\tQualification =", i[1])

