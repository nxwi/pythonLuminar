# Accept the age, sex ('M', 'F'), number of days and display the wages accordingly

x = int(input("Enter the your age:"))
y = input("Enter your sex:")
z = int(input("Enter the number of days you worked:"))

if 18 <= x < 30:
    if y == "M":
        print("Your wage=", z * 700)
    elif y == "F":
        print("Your wage=", z * 750)
    else:
        print("Wrong sex input")
elif 30 <= x <= 40:
    if y == "M":
        print("Your wage=", z * 800)
    elif y == "F":
        print("Your wage=", z * 850)
    else:
        print("Wrong sex input")
else:
    print("Wrong age input")
