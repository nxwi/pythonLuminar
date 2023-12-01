import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="", database="luminar")

myCursor = mydb.cursor()

sql = "truncate table student_details1"

myCursor.execute(sql)
mydb.commit()
print("Database Updated...")
