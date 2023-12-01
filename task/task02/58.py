# Create a program to check if a list contains duplicate elements.

numbers = [int(x) for x in input("Enter a list of numbers: ").split()]

duplicate_found = False
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            duplicate_found = True
            break

if duplicate_found:
    print("The list contains duplicate elements.")
else:
    print("The list does not contain duplicate elements.")
