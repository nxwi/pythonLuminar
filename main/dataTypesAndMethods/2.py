# program to find the product of numbers passing into a function using arbitrary arguments

def sm(*num):
    s = 1
    for i in num:
        s *= i
    print(s)


sm(1, 2, 3)
sm(1, 2, 3, 4, 5)
