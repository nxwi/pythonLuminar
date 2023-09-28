# Accept the percentage from the user and display the grade according to the following criteria:
# 81 to 100 -A+
# 71 to 80  -A
# 61 to 70  -B+
# 51 to 60  -B
# 41 to 50  -D+
# 31 to 40  -D
# 30 and below - fail

x = int(input("Enter the mark:"))

if x > 80:
    print("It's A+")
elif x > 70:
    print("It's A")
elif x > 60:
    print("It's B+")
elif x > 50:
    print("It's B")
elif x > 40:
    print("It's C")
elif x > 30:
    print("It's D")
else:
    print("Fail")
