# Install PyMySQL package -> pip install pymysql

import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="")

myCursor = mydb.cursor()

dbname = input("Enter the Database name: ")

sql = f"create database {dbname}"  # create database database_name

myCursor.execute(sql)

print("Database created successfully")
