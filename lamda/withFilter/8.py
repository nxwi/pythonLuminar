# Filter alphabets from the given list ['a','b',1,2,3]

li = ['a', 'b', 1, 2, 3]

x = list(filter(lambda i: str(i).isalpha(), li))

print(x)
