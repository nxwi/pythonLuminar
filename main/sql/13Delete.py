import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="", database="luminar")

myCursor = mydb.cursor()

sln = int(input("Enter the ID to be deleted: "))
sql = "select id from student_details"
myCursor.execute(sql)
data = myCursor.fetchall()

for j in data:
    if sln == j[0]:
        sql = f"delete from student_details where id = {sln}"
        myCursor.execute(sql)
        mydb.commit()
        print("Database Updated...")
        break

else:
    print("ID not found")
