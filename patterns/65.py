# Print the pattern
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
# * * * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *

for i in range(6):
    for j in range(5-i):
        print(end=" ")
    for k in range(i+1):
        print("*", end=" ")
    print()

for i in range(5, 0, -1):
    for j in range(6-i):
        print(end=" ")
    for k in range(i):
        print("*", end=" ")
    print()
