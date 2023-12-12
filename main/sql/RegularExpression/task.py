import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="", database="luminar")
myCursor = mydb.cursor()

# Table creation
'''
sql = ("create table movie(id int auto_increment,language varchar(10),name varchar(25),rating int(1), year int(4), "
       "genre varchar(10),primary key(id))")
myCursor.execute(sql)
'''

# Data insertion
'''
language = input("Enter the language: ")
name = input("Enter the name: ")
rating = int(input("Enter the rating: "))
year = int(input("Enter the year: "))
genre = input("Enter the genre: ")
sql = f"insert into movie(language, name, rating, year, genre)values('{language}','{name}',{rating},{year},'{genre}')"
myCursor.execute(sql)
mydb.commit()
print("Done")
'''

# All Movies
sql = "select * from movie"
myCursor.execute(sql)
data = myCursor.fetchall()
print("All Movies")
for i in data:
    print('Id:', i[0], ' Language:', i[1], ' Name:', i[2], ' Rating:', i[3], ' Year:', i[4], ' Genre:', i[5])

# Adventure Movies
sql = "select * from movie where genre = 'Adventure'"
myCursor.execute(sql)
data = myCursor.fetchall()
print("\nAdventure Movies")
for i in data:
    print('Id:', i[0], ' Language:', i[1], ' Name:', i[2], ' Rating:', i[3], ' Year:', i[4], ' Genre:', i[5])

# Top Rated Movie
sql = "select * from movie order by rating desc"
myCursor.execute(sql)
data = myCursor.fetchall()
print("\nTop Rated Movies")
top = data[0][3]
for i in data:
    if i[3] == top:
        print('Id:', i[0], ' Language:', i[1], ' Name:', i[2], ' Rating:', i[3], ' Year:', i[4], ' Genre:', i[5])

# Movie From Year 2001
sql = "select * from movie where year = '2001'"
myCursor.execute(sql)
data = myCursor.fetchall()
print("\nMovie From Year 2023")
for i in data:
    print('Id:', i[0], ' Language:', i[1], ' Name:', i[2], ' Rating:', i[3], ' Year:', i[4], ' Genre:', i[5])

# Movie by Rating
sql = "select * from movie order by rating desc"
myCursor.execute(sql)
data = myCursor.fetchall()
print("\nTop Rated Movies")
for i in data:
    print('Id:', i[0], ' Language:', i[1], ' Name:', i[2], ' Rating:', i[3], ' Year:', i[4], ' Genre:', i[5])

# Malayalam Movies
sql = "select * from movie where language = 'Malayalam'"
myCursor.execute(sql)
data = myCursor.fetchall()
print("\nAdventure Movies")
for i in data:
    print('Id:', i[0], ' Language:', i[1], ' Name:', i[2], ' Rating:', i[3], ' Year:', i[4], ' Genre:', i[5])
