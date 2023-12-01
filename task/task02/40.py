# Create a program to check if a string is a valid g-mail address.

email = input("Enter an email address: ")

if email.endswith("@gmail.com"):
  print(f"{email}: Valid Gmail address.")
else:
  print(f"{email}: Invalid Gmail address.")
