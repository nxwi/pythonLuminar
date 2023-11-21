# Write a Python program to find the sum of all even numbers from 1 to 100.

total_sum = 0
for number in range(2, 101, 2):
    total_sum += number

print("The sum of all even numbers from 1 to 100 is:", total_sum)
