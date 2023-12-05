import re

word = input("Input: ")

# Only letters
''' rule = "^[a-zA-Z]+" '''

# letters with space
''' rule = "^[a-zA-Z\s]+" '''

# start with capital letter and followed by small letters
''' rule = "^[A-Z][a-z]+" '''

# start with capital letter and followed by small letters then total limit of the name is 8 to 10
''' rule = "^[A-Z][a-z]{7,9}" '''

# phone number validation
''' rule = "^[0-9]{10}" '''

# phone number validation start with 9,8,7,6
''' rule = "^[6-9][0-9]{9}" '''

# phone number validation start with country code +91 followed by 9,8,7,6
rule = "^[+][9][1][6-9][0-9]{9}"

match = re.fullmatch(rule, word)

if match:
    print("Valid Input")
else:
    print("Not valid")
