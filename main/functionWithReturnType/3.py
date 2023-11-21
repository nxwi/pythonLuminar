# Program to accept the cost price of a bike and display the road tax to be paid according to the following criteria

# Cost price (in Rs)        Tax
# > 100000                  15%
# > 50000 and <= 100000     10%
# <= 50000                  5%

def tax(x):
    if x > 100000:
        return "You have to pay %d" % (x * 0.15)
    elif x > 50000:
        return "You have to pay %d" % (x * 0.10)
    else:
        return "You have to pay %d" % (x * 0.05)


print(tax(50000))
