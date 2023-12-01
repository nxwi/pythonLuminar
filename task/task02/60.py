# Create a program that checks if a given string is a pangram (contains all alphabets).

text = input("Enter some text: ")

alphabet = set("abcdefghijklmnopqrstuvwxyz")
text_lower = text.lower()

is_pangram = True
for letter in alphabet:
    if letter not in text_lower:
        is_pangram = False
        break

if is_pangram:
    print("The text is a pangram.")
else:
    print("The text is not a pangram.")
