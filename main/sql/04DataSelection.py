import pymysql

# mydb=pymysql.connect(host='localhost',user='root',password='',database='luminar')
# mycursor=mydb.cursor()
# sql="select * from employee_details"
# # *:is a universal symbol that is used to select all datas
# mycursor.execute(sql)
# a=mycursor.fetchall()
# print(a)
# for i in a:
#     # print(i)
# #element accessing
#     print("id=",i[0],"name=",i[1],'salary=',i[2])
# # fetchall : is a function that is used to fetch multiple datas in a database it returns a tuple of tuples
# # ((1,'alen',12000),(2,'amal',10000))
# #insert 5 datas into student details tables then select the data

mydb = pymysql.connect(host='localhost', user='root', password='', database='luminar')
myCursor = mydb.cursor()
sql = "select * from student_details"
# *:is a universal symbol that is used to select all datas
myCursor.execute(sql)
a = myCursor.fetchall()
print(a)
for i in a:
    # print(i)
    # element accessing
    print("Details of", i[1])
    print("Id =", i[0], "\nName =", i[1], '\nE-mail =', i[2], '\nQualification =', i[3], '\nFee =', i[4],
          '\nPhone Number =', i[5], '\n-------------------------')
# fetchall : is a function that is used to fetch multiple datas in a database it returns a tuple of tuples
# ((1,'alen',12000),(2,'amal',10000))

# insert 5 datas into student details tables then select the datas
