import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="", database="luminar")

myCursor = mydb.cursor()

limit = int(input("Enter the limit: "))
sql = "select * from student_details limit %d" % limit

myCursor.execute(sql)

data = myCursor.fetchall()
for i in data:
    print(i[0], "-", i[1], "-", i[2], "-", i[3], "-", i[4], "-", i[5])
