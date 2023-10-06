# Program to check a number is armstrong or not

n = int(input("Enter the number:"))
temp = n
s = 0

while n != 0:
    r = n % 10
    s += r ** len(str(temp))
    n //= 10
if s == temp:
    print(s, "It's an armstrong number")
else:
    print(s, "It's not an armstrong number")
