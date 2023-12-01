import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="", database="luminar")

myCursor = mydb.cursor()

sql = "select min(fee),max(fee),avg(fee),sum(fee) from student_details"
myCursor.execute(sql)
a = myCursor.fetchone()

print("The minimum value =", a[0], "\nThe maximum value =", a[1],
      "\nThe average value =", a[2], "\nThe total sum =", a[3])
