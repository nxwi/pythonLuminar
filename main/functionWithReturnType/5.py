# A company decided to give bonus to employee according to following criteria:
# Time period of Service      Bonus
# More than 10 years          10%
# >=6 and <=10                8%
# Less than 6 years           5%

def bonus(x, y):
    if y > 10:
        return "You will get bonus %d" % (x * 0.1)
    elif (y > 6) and (y < 10):
        return "You will get bonus %d" % (x * 0.08)
    else:
        return "You will get bonus %d" % (x * 0.05)


a = int(input("Enter your Salary:"))
b = int(input("Enter your Time period of service:"))
print(bonus(a, b))
