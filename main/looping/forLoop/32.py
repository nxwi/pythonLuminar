# Program to find the sum of even numbers of range 100,200

x = 0

for i in range(100, 200):
    if i % 2 == 0:
        x += i
print(x)
