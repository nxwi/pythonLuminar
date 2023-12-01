# Write a Python program to find and replace a word in a string.

text = input("Enter some text: ")
old_word = input("Enter the word to be replaced: ")
new_word = input("Enter the replacement word: ")

modified_text = text.replace(old_word, new_word)

print("Original text:", text)
print("Modified text:", modified_text)
