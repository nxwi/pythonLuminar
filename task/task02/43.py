# Write a Python program to count the number of words in a paragraph.

paragraph = input("Enter a paragraph: ")
words = paragraph.split()
word_count = len(words)
print(word_count)
