# Print the pattern
# *
# *  *
# *  *  *
# *  *  *  *
# *  *  *
# *  *
# *


for i in range(4):
    for j in range(i+1):
        print("*", end="  ")
    print()

for i in range(3, 0, -1):
    for j in range(i):
        print("*", end="  ")
    print()
