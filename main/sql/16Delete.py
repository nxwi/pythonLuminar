import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="", database="employees")

myCursor = mydb.cursor()
# table
# sql = "drop table student_details"

# Database
# sql = "drop column employee"
sql = "ALTER TABLE employee_details DROP COLUMN pf"

myCursor.execute(sql)
mydb.commit()
print("Database Updated...")
