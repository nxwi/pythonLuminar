# program to find the smallest of numbers passing into a function using arbitrary arguments

def sm(*num):
    smallest = num[0]
    for i in num:
        if i < smallest:
            smallest = i
    print(smallest)


sm(1, 2, 3)
sm(1, 2, 3, 4, 5)
