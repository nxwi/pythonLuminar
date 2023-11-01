# Simple Calculater

def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mult(x, y):
    return x * y
def div(x, y):
    return x / y

print(
    "SIMPLE CALCULATER\n=================\nSelect an operation:\n"
      "\t1:Addition\n\t2:Subtraction\n\t3:Multiplication\n\t4:Division"
)
i = int(input("Input:"))

if i == 1:
    print(add(a, b))
elif i == 2:
    print(sub(a, b))
elif i == 3:
    print(mult(a, b))
elif i == 4:
    print(div(a, b))
else:
    print("Select a valid input")
    exit()

a = int(input("Enter the first value:"))
b = int(input("Enter the second value:"))
