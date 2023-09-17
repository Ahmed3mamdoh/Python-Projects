"""
Create a function takes a sentence and a word and prints how many time the word used in the sentence
"""
def how_many_times_word_used(sentence , target_word):
    words = sentence.split()
    count = 0
    for word in words :
        if word == target_word:
            count += 1
    return count
    
sentence = (input("Enter the sentence : "))
target_word = (input("Enter the word you want to check how many times it is being used : "))
result = how_many_times_word_used(sentence , target_word)
print (f"The word {target_word} appears {result} times in the sentence. ")