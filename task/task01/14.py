# Create a program that finds the largest number in a list.

numbers = [1, 2, 3, 4, 5]
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print("The largest number in the list is:", largest)
