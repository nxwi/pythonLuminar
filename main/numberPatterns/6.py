# Print the pattern
#   1
#  2 2
# 3 3 3
#  2 2
#   1

n = 3

for i in range(n):
    for j in range(n-1-i):
        print(end=" ")
    for k in range(i+1):
        print(i+1, end=" ")
    print()

for i in range(n-1):
    for j in range(i+1):
        print(end=" ")
    for k in range(n-1-i):
        print(n-1-i, end=" ")
    print()
