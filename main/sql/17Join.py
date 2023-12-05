import pymysql
mydb = pymysql.connect(host="localhost", user="root", password="", database="employees")
myCursor = mydb.cursor()

sql = ("select employee_details.firstname, employee_details.lastname, employee_qualification.qualification "
       "from employee_details inner join employee_qualification "
       "on employee_details.firstname = employee_qualification.firstname")

myCursor.execute(sql)

data = myCursor.fetchall()
for i in data:
    print(i)
