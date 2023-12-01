import pymysql
# mydb=pymysql.connect(host="localhost",user="root",password="",database="luminar")
# mycursor=mydb.cursor()
# sql="insert into employee_details(name,salary)values('alez',12000)"
# mycursor.execute(sql)
# mydb.commit()
# print("data added successfully")
#
#
# mydb=pymysql.connect(host="localhost",user="root",password="",database="luminar")
# mycursor=mydb.cursor()
# name=input("enter the name")
# salary=int(input("enter the salary"))
# sql="insert into employee_details(name,salary)values('%s',%d)"%(name,salary)
# mycursor.execute(sql)
# mydb.commit()
# print("data added successfully")
# import pymysql
#
# mydb=pymysql.connect(host="localhost",user="root",password="",database="luminar")
# mycursor=mydb.cursor()
# e_num=int(input("enter the number of employees"))
# for i in range(e_num):
#     name=input("enter the name")
#     salary=int(input("enter the salary"))
#     sql="insert into employee_details(name,salary)values('%s',%d)"%(name,salary)
#     mycursor.execute(sql)
# mydb.commit()
# print(e_num,"data added successfully")

# insert 5 datas into student details tables then select the datas
import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="", database="luminar")
myCursor = mydb.cursor()
s_num = int(input("Enter the number of students: "))
for i in range(s_num):
    name = input("Enter the name: ")
    email = input("Enter the email: ")
    qualification = input("Enter student qualification: ")
    fee = int(input("Enter student fee detail: "))
    phone = int(input("Enter the phone number: "))
    sql = "Insert into student_details1(name,email,qualification,fee,phone)values('%s','%s','%s',%d,%d)" % (
        name, email, qualification, fee, phone)
    myCursor.execute(sql)
mydb.commit()
print(s_num, "Data added successfully")
