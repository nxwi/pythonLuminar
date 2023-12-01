# Create a program to check if a given number is a palindrome.

num = int(input("Enter a number: "))
num_str = str(num)
reversed_num_str = num_str[::-1]
if num_str == reversed_num_str:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")
