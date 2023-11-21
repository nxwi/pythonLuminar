# Program to check whether a number is divisible by 2 and 3 both

def check(x):
    if (x % 2 == 0) and (x % 3 == 0):
        return "%d is divisible by 2 and 3 both" % x
    else:
        return "%d is not divisible by 2 and 3 both" % x


n = int(input("Enter the number:"))
print(check(n))
