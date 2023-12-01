import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="", database="luminar")

myCursor = mydb.cursor()

# Can be skipped
sql = "select * from student_details"
myCursor.execute(sql)
data = myCursor.fetchall()
for i in data:
    print(i[0], "-", i[1], "-", i[2], "-", i[3], "-", i[4], "-", i[5])
#

sln = int(input("Enter the ID: "))
name = input("Enter the new name: ")
sql = f"update student_details set name = '{name}' where id = {sln}"
myCursor.execute(sql)

# Can be skipped
sql = "select * from student_details"
myCursor.execute(sql)
data = myCursor.fetchall()
for i in data:
    print(i[0], "-", i[1], "-", i[2], "-", i[3], "-", i[4], "-", i[5])
#

mydb.commit()
print("Database Updated...")
