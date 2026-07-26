## More comprehensions
# Task 4 (Lengths of strings)

def lengths(strings):
    return {word : len(word) for word in strings}

word_list = ["once", "upon" , "a", "time", "in"]

word_lengths = lengths(word_list)
print(word_lengths)
