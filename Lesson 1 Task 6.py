## List comprehensions
# Task 6 (Begin with a vowel)

def begin_with_vowel(words: list):
    return [word for word in words if word and word[0].lower() in 'aeiou']


word_list = ["automobile", "motorbike", "Animal", "cat", "Dog", "APPLE", "orange"]
for vowelled in begin_with_vowel(word_list):
    print(vowelled)
