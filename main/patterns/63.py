# Print the pattern
# * * * *
#  * * *
#   * *
#    *
#   * *
#  * * *
# * * * *

for i in range(4, 1, -1):
    for j in range(4-i):
        print(end=" ")
    for k in range(i):
        print("*", end=" ")
    print()

for i in range(4):
    for j in range(3-i):
        print(end=" ")
    for k in range(i+1):
        print("*", end=" ")
    print()
