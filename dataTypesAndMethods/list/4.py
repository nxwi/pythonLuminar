# Program to remove duplicate elements from the given list

li = ['a', 'b', 'c', 'a', 'c']
li2 = []

for i in li:
    if i not in li2:
        li2.append(i)

print(li2)
