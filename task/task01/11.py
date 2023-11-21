# Write a Python program to check if a number is prime.

n = int(input("Enter the number: "))

if n == 1:
    print(n, "is not a prime number")
elif n > 1:
    for i in range(2, n):
        if n % i == 0:
            print(n, "is not a prime number")
            exit()
    print(n, "is a prime number")
