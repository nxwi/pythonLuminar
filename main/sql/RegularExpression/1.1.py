# Registration: username, email, phone, password, confirm password -> Reg Success || Reg Failed
# Login Page: username, password -> Login Success || Login Failed

import re

print("Registration\n------------")

username = input("Enter the username: ")
rule = "\w{5,255}"
match = re.fullmatch(rule, username)
if not match:
    print("Not valid")
    exit()

email = input("Enter the email: ")
rule = "[^_.]([a-zA-Z0-9_]*[.]?[a-zA-Z0-9_]+[^_]){2}@{1}[a-z0-9]+[.]{1}(([a-z]{2,3})|([a-z]{2,3}[.]{1}[a-z]{2,3}))"
match = re.fullmatch(rule, email)
if not match:
    print("Not valid")
    exit()

phone = input("Enter the phone: ")
rule = "[6-9][0-9]{9}"
match = re.fullmatch(rule, phone)
if not match:
    print("Not valid")
    exit()

password = input("Enter the password: ")
rule = "([a-zA-Z0-9@*#]{8,15})"
match = re.fullmatch(rule, password)
if not match:
    print("Not valid")
    exit()

confirm_password = input("Enter the password again: ")
if password != confirm_password:
    print("Not valid")
    exit()

print("Registration Success")

print("\nLogin Page\n----------")

lUser = input("Enter the username: ")
lPass = input("Enter the password: ")
if lUser == username and lPass == password:
    print("Login Success")
else:
    print("Login Failed")
