# Ask user to enter age, sex (M or F ), marital status ( Y or N ) and then using following rules print their place of service.
# If employee is female, then she will work only in urban areas.
# If employee is a male and age is in between 20 and 40 then he may work in anywhere
# If employee is male and age is in between 40 t0 60 then he will work in urban areas only.
# And any other input of age should print "ERROR".

x = int(input("Enter the your age:"))
y = input("Enter your sex (M or F ):")
z = input("Enter your marital status ( Y or N ):")

if y == "F":
    if 20 <= x <= 60:
        print("You can work only in urban areas.")
    else:
        print("ERROR")
elif y == "M":
    if 20 <= x <= 40:
        print("You may work in anywhere")
    elif 40 < x <= 60:
        print("You can work only in urban areas.")
    else:
        print("ERROR")
else:
    print("Wrong sex input")
