# Write a program to check if a list is sorted in ascending order.

list1 = input("Enter a list of integers separated by spaces: ").split()
is_sorted = True
for i in range(len(list1) - 1):
    if list1[i] > list1[i + 1]:
        is_sorted = False
        break

if is_sorted:
    print(list1, "is sorted in ascending order")
else:
    print(list1, "is not sorted in ascending order")
