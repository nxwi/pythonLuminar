# Create a program that counts the number of words in a sentence.

sentence = input("Enter the sentence: ")

words = sentence.split()
word_count = len(words)

print("The number of words in the sentence is:", word_count)
