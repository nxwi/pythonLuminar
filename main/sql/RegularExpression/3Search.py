import re

data = input("Input: ")

find = "hi"

search = re.search(find, data)

if search:
    print(1)
else:
    print(0)
