"""
Create a function that takes a sentence and word and remove the word from the sentence
"""
def remove_word_from(sentence , word_to_remove):
    words = sentence.split()
    words_without_remove=[]
    for word in words:
        if word != word_to_remove :
            words_without_remove.append(word)
    result = ' '.join(words_without_remove)
    return result
sentence = (input("Enter the sentence :"))
word_to_remove = (input("Enter the word you want to remove :"))
new_sentence = remove_word_from(sentence,word_to_remove)
print (new_sentence)