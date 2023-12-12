import re

text = input("Input: ")

x = re.sub('\s', "\t", text)

print(x)
