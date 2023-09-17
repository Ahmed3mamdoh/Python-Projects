"""
Create a function that takes a sentence and prints how many words in the sentence (do not count the
spaces)
"""
def how_many_words(sentence):
    words = sentence.split()
    words_count = len(words)
    return words_count
sentence = (input("Enter the sentence :"))
words_count = how_many_words(sentence)
print("Number of Words :",words_count)