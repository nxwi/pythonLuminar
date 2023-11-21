import datetime

year = 2002
month = 2
date = 4

myDate = datetime.date(year, month, date)
print(myDate)
print(type(myDate))

today = datetime.date.today()

# print(today)
print(datetime.date.today())

# print(today.month)
print(datetime.date.today().month)

print(datetime.datetime.now())

d = datetime.date.today()

# d += datetime.timedelta(days=100)
# print(d)
print(d + datetime.timedelta(days=100))

