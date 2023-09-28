# Program to accept the cost price of a bike and display the road tax to be paid according to the following criteria

# Cost price (in Rs)        Tax
# > 100000                  15 %
# > 50000 and <= 100000     10%
# <= 50000                  5%

x = int(input("Enter the cost price:"))

if x > 100000:
    print("You have to pay 15% tax that is", x * 0.15)
elif x > 50000:
    print("You have to pay 10% tax that is", x * 0.1)
else:
    print("You have to pay 5% tax that is", x * 0.05)
