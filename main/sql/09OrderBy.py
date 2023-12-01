import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="", database="luminar")

myCursor = mydb.cursor()

sql = "select * from student_details order by fee desc"
myCursor.execute(sql)

data = myCursor.fetchall()
for i in data:
    print(i[0], "-", i[1], "-", i[2], "-", i[3], "-", i[4], "-", i[5])
