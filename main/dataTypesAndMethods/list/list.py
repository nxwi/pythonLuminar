li = ['a', 'b', 1, 2]
print(li)
print(type(li))
print(len(li))

li.append('f')
print(li)
li.insert(2, 'c')
print(li)
li.extend(['d', 'e', 'f',])
print(li)
li.pop(3)
print(li)
li.pop()
print(li)
li.remove(2)
print(li)
li.reverse()
print(li)
li.sort()
print(li)
li.extend(['G', 'H', 'I'])
li.sort()
print(li)
li.sort(reverse=True)
print(li)

for i in li:
    print(i, end='')
print()

# slicing
print(li[1:4])
print(li[:4])
print(li[4:])
print(li[::-1])

print(li.count('a'))
print(li.index('a'))

