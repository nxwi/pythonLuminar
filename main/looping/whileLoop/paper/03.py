# Program to print numbers from 1 to 100 except the numbers which are divisible by 5 and 10

x = 1

while x <= 100:
    if x % 5 != 0:
        print(x)
    x += 1
