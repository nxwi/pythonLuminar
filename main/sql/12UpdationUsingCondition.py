import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="", database="luminar")

myCursor = mydb.cursor()

sln = int(input("Enter the ID: "))
sql = "select id from student_details"
myCursor.execute(sql)
data = myCursor.fetchall()
for i in data:
    if id == i[0]:
        name = input("Enter the new name: ")
        sql = f"update student_details set name = '{name}' where id = {sln}"
        myCursor.execute(sql)
        mydb.commit()
        print("Database Updated...")
        break

else:
    print("ID not found")
