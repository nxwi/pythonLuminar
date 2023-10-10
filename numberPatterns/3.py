# Print the pattern

# 4
# 3 3
# 2 2 2
# 1 1 1 1

n = 4

for i in range(1, n+1):
    for j in range(i):
        print(n+1-i, end=" ")
    print()
