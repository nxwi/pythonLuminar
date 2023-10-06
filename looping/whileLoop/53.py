# Program to find reverse of a number input by the user is palindrome

n = int(input("Enter the number:"))
temp = n
rev = 0

while n != 0:
    r = n % 10
    rev = rev * 10 + r
    n //= 10
if rev == temp:
    print("The number is palindrome")
else:
    print("The number is not palindrome")
