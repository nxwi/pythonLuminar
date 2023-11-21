# Write a program to calculate the average of a list of numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

total = 0
for number in numbers:
    total += number
average = total / len(numbers)
print("The average of the list is:", average)
