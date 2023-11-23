# try:
#     a = int(input("enter the number: "))
#     b = int(input("enter 2nd number: "))
#     print("answer=", a / b)
# except ZeroDivisionError:
#     print("zero division error occurred")
# except ValueError:
#     print("value error occurred")

try:
    a = int(input("enter the number: "))
    b = int(input("enter 2nd number: "))
    print("answer=", a / b)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)

