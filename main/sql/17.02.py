# employee_details : id, firstname, lastname, salary,pf, job_title, mail, dept_id
# employee qualification : id, firstname, lastname, qualification, maths, chem, eng, total

# 1.Display firstname,lastname, dept id, total mark of employees
# 2.create a new column PF in employee details. Pf : 15% of salary
# 3.Print the total salary
# 4.Print the min, max, avg (salary)
# 5.Print employee name in desc order

import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="", database="employees")
myCursor = mydb.cursor()

x = int(input("1.Display firstname,lastname, dept id, total mark of employees"
              "\n2.create a new column PF in employee details. Pf: 15% of salary"
              "\n3.Print the total salary"
              "\n4.Print the min, max, avg (salary)"
              "\n5.Print employee name in desc order"
              "\nSelect an option:"))

if x == 1:
    sql = ("SELECT employee_details.firstname, employee_details.lastname, employee_qualification.qualification, "
           "employee_qualification.total FROM employee_details INNER JOIN employee_qualification ON "
           "employee_details.firstname = employee_qualification.firstname")
    myCursor.execute(sql)
    data = myCursor.fetchall()
    for i in data:
        print(i[0], "-", i[1], "-", i[2], "-", i[3])

elif x == 2:
    sql = "ALTER TABLE employee_details ADD pf float as (salary * 0.15) AFTER salary;"
    myCursor.execute(sql)
    mydb.commit()
    print("PR created successfully")

elif x == 3:
    sql = "SELECT firstname, lastname, salary + pf AS total_salary FROM employee_details"
    myCursor.execute(sql)
    data = myCursor.fetchall()
    for row in data:
        firstname, lastname, total_salary = row
        print(f"{firstname} {lastname}: Total Salary = {total_salary}")


elif x == 4:
    sql = "SELECT MIN(salary), MAX(salary), AVG(salary) FROM employee_details"
    myCursor.execute(sql)
    data = myCursor.fetchone()
    print(f"Minimum Salary: {data[0]}")
    print(f"Maximum Salary: {data[1]}")
    print(f"Average Salary: {data[2]}")

elif x == 5:
    sql = "SELECT firstname, lastname FROM employee_details ORDER BY firstname DESC"
    myCursor.execute(sql)
    data = myCursor.fetchall()
    for i in data:
        print(i[0], i[1])

else:
    print("Wrong input")
