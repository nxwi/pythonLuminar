# Print the pattern
#     *
#   * *
# * * *

for i in range(3):
    for j in range(2-i):
        print(" ", end=" ")
    for k in range(i+1):
        print("*", end=" ")
    print()
