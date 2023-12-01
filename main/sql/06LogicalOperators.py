import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="", database="luminar")

myCursor = mydb.cursor()

qualification = input("Enter the qualification: ")

sql = "select * from student_details"

myCursor.execute(sql)
