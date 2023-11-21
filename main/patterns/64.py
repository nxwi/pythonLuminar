# Print the pattern
#     *
#   * *
# * * *
#   * *
#     *

for i in range(3):
    for j in range(3-i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()

for i in range(3):
    for j in range(i):
        print(" ", end=" ")
    for k in range(3-i):
        print("*", end=" ")
    print()
