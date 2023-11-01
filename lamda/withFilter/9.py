# Filter the numbers which are divisible by 2 and not by 3 [1,2,3,4,5,6,7,8]

li = [1,2,3,4,5,6,7,8]

x = list(filter(lambda i: i % 2 == 0 and i % 3 != 0, li))

print(x)
