# Write a program to reverse the order of words in a sentence.

sentence = input("Enter a sentence: ")

reversed_sentence = " ".join(sentence.split()[::-1])

print("Reversed sentence:", reversed_sentence)
