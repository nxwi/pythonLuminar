import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="", database="luminar")

myCursor = mydb.cursor()

sql = "alter table student_details add total_mark float(5)"

sql = "alter table student_details add (age int(2), gender varchar(50))"

sql = "alter table student_details add last_name varchar(20) after id"

sql = "alter table student_details drop column gender"

sql = "alter table student_details drop column age, drop column last_name,drop column total_mark"

myCursor.execute(sql)
mydb.commit()
print("Database Updated...")
