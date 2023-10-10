# Print reverse pyramid

for i in range(3, 0, -1):
    for j in range(3-i):
        print(end=" ")
    for k in range(i):
        print("*", end=" ")
    print()
