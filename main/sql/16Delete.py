import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="")

myCursor = mydb.cursor()
# table
# sql = "drop table student_details"

# Database
sql = "drop database employee"

myCursor.execute(sql)
mydb.commit()
print("Database Updated...")
