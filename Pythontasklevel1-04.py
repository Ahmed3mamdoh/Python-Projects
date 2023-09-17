"""
Create a function that takes a sentence and prints the sentence without duplicated words
"""
def no_duplicated_words(sentence):
    words = sentence.split()
    unique_words=[]
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    results = ' ' .join(unique_words)
    return results
sentence = (input("Enter the Sentence :"))
result = no_duplicated_words(sentence)
print (result)