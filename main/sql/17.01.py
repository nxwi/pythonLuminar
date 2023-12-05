# Create a database employees

# employee_details : id, firstname, lastname, salary, job_title, mail, dept_id
# employee qualification : id, firstname, lastname, qualification, maths, chem, eng

import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="", database="employees")

myCursor = mydb.cursor()

# sql = f"create database employees"
# sql = ("create table employee_details(id int auto_increment,firstname varchar(20),lastname varchar(20),salary int(9),"
#        "job_title varchar(20), mail varchar(25), dept_id int(3), primary key(id))")
# sql = ("create table employee_qualification(id int auto_increment,firstname varchar(20),lastname varchar(20), "
#        "qualification varchar(20), maths int(3), chem int(3), eng int(3), primary key(id))")

# myCursor.execute(sql)

# s_num = int(input("Enter the number of employees: "))
# for i in range(s_num):
#     firstname = input("Enter1: ")
#     lastname = input("Enter2: ")
#     qualification = input("Enter3: ")
#     maths = int(input("Enter4: "))
#     chem = int(input("Enter5: "))
#     eng = int(input("Enter6: "))
#     sql = (f"Insert into employee_qualification(firstname,lastname,qualification,maths,chem,eng)"
#            f"values('{firstname}','{lastname}','{qualification}',{maths},{chem},{eng})")
#     myCursor.execute(sql)

sql = "alter table employee_qualification add total int as (maths + chem + eng)"
myCursor.execute(sql)
mydb.commit()

print("success")

