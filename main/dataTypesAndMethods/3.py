# program to find the largest of numbers passing into a function using arbitrary arguments

def sm(*num):
    largest = num[0]
    for i in num:
        if i > largest:
            largest = i
    print(largest)


sm(1, 2, 3)
sm(1, 2, 3, 4, 5)
