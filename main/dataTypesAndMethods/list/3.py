# Reverse the list without using slicing and reverse method

li = ['a', 'b', 'c']
li2 = []

for i in range(len(li)-1, -1, -1):
    li2.append(li[i])

print(li2)
