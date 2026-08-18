## More comprehensions
# Task 1 (Filter forbidden)

def filter_forbidden(string: str, forbidden: str):
    new_str = ''.join([char for char in string if char not in forbidden])
    return new_str


sentence = "Once! upon, a time: there was a python!??!?!"
filtered = filter_forbidden(sentence, "!?:,.")
print(filtered)

