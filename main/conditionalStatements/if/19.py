# A company decided to give bonus to employee according to following criteria:
# Time period of Service      Bonus
# More than 10 years          10%
# >=6 and <=10                8%
# Less than 6 years           5%

x = int(input("Enter your Salary:"))
y = int(input("Enter your Time period of service:"))

if y > 10:
    print("You will get 10% bonus that is", x, "+", x * 0.1)
elif (y > 6) and (y < 10):
    print("You will get 8% bonus that is", x, "+", x * 0.08)
else:
    print("You will get 5% bonus that is", x, "+", x * 0.05)
